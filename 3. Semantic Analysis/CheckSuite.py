import unittest
from TestUtils import TestChecker
from AST import *
import inspect

class CheckSuite(unittest.TestCase):
    def test_001(self):
        """
var VuTung = 1; 
var VuTung = 2;
        """
        input = Program([VarDecl("VuTung", None, IntLiteral(1)), VarDecl("VuTung", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VuTung", inspect.stack()[0].function))

    def test_002(self):
        """
var VuTung = 1;
const VuTung = 2;
        """
        input = Program([VarDecl("VuTung", None, IntLiteral(1)), ConstDecl("VuTung", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: VuTung", inspect.stack()[0].function))

    def test_003(self):
        """
const VuTung = 1;
var VuTung = 2;
        """
        input = Program([ConstDecl("VuTung", None, IntLiteral(1)), VarDecl("VuTung", None, IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VuTung", inspect.stack()[0].function))

    def test_004(self):
        """
const VuTung = 1;
func VuTung(): void {}
        """
        input = Program([ConstDecl("VuTung", None, IntLiteral(1)), FuncDecl("VuTung", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Function: VuTung", inspect.stack()[0].function))

    def test_005(self):
        """
func VuTung(): void {}
var VuTung = 1;
        """
        input = Program([FuncDecl("VuTung", [], VoidType(), Block([Return(None)])), VarDecl("VuTung", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: VuTung", inspect.stack()[0].function))

    def test_006(self):
        """
var getInt = 1;
        """
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: getInt", inspect.stack()[0].function))

    def test_007(self):
        """
struct tung { tung: int }
struct TUNG { tung: string, TUNG: int, TUNG: float }
        """
        input = Program([
            StructType("tung", [("tung", IntType())], []),
            StructType("TUNG", [("tung", StringType()), ("TUNG", IntType()), ("TUNG", FloatType())], [])
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Field: TUNG", inspect.stack()[0].function))

    def test_008(self):
        """
class TUNG {
  method putIntLn() {}
  method getInt() {}
  method getInt() {}
}
struct TUNG { tung: int }
        """
        input = Program([
            MethodDecl("v", Id("TUNG"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TUNG"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            MethodDecl("v", Id("TUNG"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))),
            StructType("TUNG", [("tung", IntType())], [])
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Method: getInt", inspect.stack()[0].function))

    def test_009(self):
        """
interface VuTung {
  VuTung(): void;
  VuTung(int): void;
}
        """
        input = Program([InterfaceType("VuTung", [Prototype("VuTung", [], VoidType()), Prototype("VuTung", [IntType()], VoidType())])])
        self.assertTrue(TestChecker.test(input, "Redeclared Prototype: VuTung", inspect.stack()[0].function))

    def test_010(self):
        """
func tung(a: int, a: int): void {}
        """
        input = Program([FuncDecl("tung", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Parameter: a", inspect.stack()[0].function))

    def test_011(self):
        """
func tung(b: int): void {
  var b = 1;
  var a = 1;
  const a = 1;
}
        """
        input = Program([FuncDecl("tung", [ParamDecl("b", IntType())], VoidType(), Block([
            VarDecl("b", None, IntLiteral(1)),
            VarDecl("a", None, IntLiteral(1)),
            ConstDecl("a", None, IntLiteral(1))
        ]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: b", inspect.stack()[0].function))

    def test_012(self):
        """
func tung(b: int): void {
  for var a = 1; a < 1; a = a + 1 {
    const a = 2;
  }
}
        """
        input = Program([FuncDecl("tung", [ParamDecl("b", IntType())], VoidType(), Block([
            ForStep(
                VarDecl("a", None, IntLiteral(1)),
                BinaryOp("<", Id("a"), IntLiteral(1)),
                Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                Block([ConstDecl("a", None, IntLiteral(2))])
            )
        ]))])
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: a", inspect.stack()[0].function))

    def test_013(self):
        """
var a = 1;
var b = a;
var c = d;
        """
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            VarDecl("b", None, Id("a")),
            VarDecl("c", None, Id("d"))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: d", inspect.stack()[0].function))

    def test_014(self):
        """
func tung(): int { return 1; }
func foo(): void {
  var b = tung();
  foo_votine();
  return;
}
        """
        input = Program([
            FuncDecl("tung", [], IntType(), Block([Return(IntLiteral(1))])),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("b", None, FuncCall("tung", [])),
                FuncCall("foo_votine", []),
                Return(None)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Function: foo_votine", inspect.stack()[0].function))

    def test_015(self):
        """
struct TUNG { tung: int }
method getInt(): void {
  const c = this.tung;
  var d = this.Kophaitung;
}
        """
        input = Program([
            StructType("TUNG", [("tung", IntType())], []),
            MethodDecl("v", Id("TUNG"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "tung")),
                VarDecl("d", None, FieldAccess(Id("v"), "Kophaitung"))
            ])))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: Kophaitung", inspect.stack()[0].function))

    def test_016(self):
        """
struct TUNG { tung: int }
method getInt(): void {
  this.getInt();
  this.putInt();
}
        """
        input = Program([
            StructType("TUNG", [("tung", IntType())], []),
            MethodDecl("v", Id("TUNG"), FuncDecl("getInt", [], VoidType(), Block([
                MethCall(Id("v"), "getInt", []),
                MethCall(Id("v"), "putInt", [])
            ])))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Method: putInt", inspect.stack()[0].function))

    def test_017(self):
        """
struct TUNG { tung: int }
struct TUNG { v: int }
        """
        input = Program([
            StructType("TUNG", [("tung", IntType())], []),
            StructType("TUNG", [("v", IntType())], [])
        ])
        self.assertTrue(TestChecker.test(input, "Redeclared Type: TUNG", inspect.stack()[0].function))
    
    def test_018(self):
        input = Program([VarDecl("a",IntType(),None),VarDecl("b",FloatType(),None),VarDecl("a",IntType(),None)])
        self.assertTrue(TestChecker.test(input, "Redeclared Variable: a", inspect.stack()[0].function))

    def test_019(self):
        input = Program([VarDecl("a",IntType(),FloatLiteral(1.2))])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))", inspect.stack()[0].function))
    
    def test_020(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b", inspect.stack()[0].function))
    

    	

