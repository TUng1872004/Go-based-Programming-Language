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
        self.assertTrue(TestChecker.test(input, "Redeclared Constant: VuTung", inspect.stack()[0].function))

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
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"a\",IntType(),FloatLiteral(1.2))", inspect.stack()[0].function))
    
    def test_020(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b", inspect.stack()[0].function))
    def test_021(self):
        """

        """
        input = Program([
            VarDecl("v", Id("TIEN"), None),
            StructType("TIEN", [("a", IntType())], []),
            InterfaceType("VO", [Prototype("foo", [], IntType())]),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))),
            MethodDecl("b", Id("TIEN"), FuncDecl("koo", [], VoidType(), Block([MethCall(Id("b"), "koo", [])]))),
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("x", Id("VO"), None),
                ConstDecl("b", None, MethCall(Id("x"), "foo", [])),
                MethCall(Id("x"), "koo", [])
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Success", inspect.stack()[0].function))

    def test_022(self):
        """
    var a = foo();
    func foo(): int {
    var a = koo();
    var c = getInt();
    putInt(c);
    putIntLn(c);
    return 1;
    }
    var d = foo();
    func koo(): int {
    var a = foo();
    return 1;
    }
        """
        input = Program([
            VarDecl("a", None, FuncCall("foo", [])),
            FuncDecl("foo", [], IntType(), Block([
                VarDecl("a", None, FuncCall("koo", [])),
                VarDecl("c", None, FuncCall("getInt", [])),
                FuncCall("putInt", [Id("c")]),
                FuncCall("putIntLn", [Id("c")]),
                Return(IntLiteral(1))
            ])),
            VarDecl("d", None, FuncCall("foo", [])),
            FuncDecl("koo", [], IntType(), Block([
                VarDecl("a", None, FuncCall("foo", [])),
                Return(IntLiteral(1))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Success", inspect.stack()[0].function))

    def test_023(self):
        """
    struct TIEN {
    int Votien;
    }
    func v.getInt(): void {
    const c = v.Votien;
    var d = v.tien;
    }
        """
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("getInt", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("v"), "Votien")),
                VarDecl("d", None, FieldAccess(Id("v"), "tien"))
            ])))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Field: tien", inspect.stack()[0].function))

    def test_024(self):
        """
    func foo(): void {
    const a = 1;
    foreach a in [3] : int in [1,2,3] {
        var b = 1;
    }
    }
        """
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("a", None, IntLiteral(1)),
                ForEach(Id("a"), Id("b"), ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Block([
                    VarDecl("b", None, IntLiteral(1))
                ]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Undeclared Identifier: b", inspect.stack()[0].function))

    def test_025(self):
        """
    struct TIEN {
    int Votien;
    }
    func v.foo(v: int): void {
    return;
    }
    func foo(): void {
    return;
    }
        """
        input = Program([
            StructType("TIEN", [("Votien", IntType())], []),
            MethodDecl("v", Id("TIEN"), FuncDecl("foo", [ParamDecl("v", IntType())], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [], VoidType(), Block([Return(None)]))
        ])
        self.assertTrue(TestChecker.test(input, "Success", inspect.stack()[0].function))
    def test_026(self):
        """
    var a: [2][3]int;
    var b = a[1];
    var c: [2]int = b;
    var d: [1]string = b;
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None),
            VarDecl("b", None, ArrayCell(Id("a"), [IntLiteral(1)])),
            VarDecl("c", ArrayType([IntLiteral(2)], IntType()), Id("b")),
            VarDecl("d", ArrayType([IntLiteral(1)], StringType()), Id("b"))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"c\",ArrayType([IntLiteral(2)],IntType()),Id(\"b\"))", inspect.stack()[0].function))

    def test_027(self):
        """
    var a: int = 1 % 2;
    var b: int = 1 % 2.0;
        """
        input = Program([
            VarDecl("a", IntType(), BinaryOp("%", IntLiteral(1), IntLiteral(2))),
            VarDecl("b", IntType(), BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(\"%\", IntLiteral(1), FloatLiteral(2.0))", inspect.stack()[0].function))

    def test_028(self):
        """
    func foo(): int {
        return 1;
    }
    func votien(): int {
        return votien();
        foo();
    }
        """
        input = Program([
            FuncDecl("foo", [], IntType(), Block([
                Return(IntLiteral(1))
            ])),
            FuncDecl("votien", [], IntType(), Block([
                Return(FuncCall("votien", [])),
                FuncCall("foo", [])
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(\"foo\",[])", inspect.stack()[0].function))

    def test_029(self):
        """
    struct TIEN {
        v: int;
    }
    var v: TIEN;
    func foo(): void {
        for 1 {
            var a: int = 1.2;
        }
    }
        """
        input = Program([
            StructType("TIEN", [("v", IntType())], []),
            VarDecl("v", Id("TIEN"), None),
            FuncDecl("foo", [], VoidType(), Block([
                ForBasic(IntLiteral(1), Block([
                    VarDecl("a", IntType(), FloatLiteral(1.2))
                ]))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"a\",IntType(),FloatLiteral(1.2))", inspect.stack()[0].function))
    def test_030(self):
        input =  """
const v = 3;
const a = v + v;
var b [a * 2 + a] int;
var c [18] int = b;
        """
        input = Program([ConstDecl("v",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("v"), Id("v"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        self.assertTrue(TestChecker.test(input, """Success""", inspect.stack()[0].function)) 

    def test_031(self):
        input =  """
func foo(a [2] float) {
    foo([2] float {1.0,2.0})
    foo([2] int {1,2})
}
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        self.assertTrue(TestChecker.test(input, """Type Mismatch: FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])""", inspect.stack()[0].function)) 
    def test_032(self):
        input =  """
    type A interface {foo();}
    const A = 2;
        """
        input = Program([InterfaceType("A",[Prototype("foo",[],VoidType())]),ConstDecl("A",None,IntLiteral(2))])
        self.assertTrue(TestChecker.test(input, """Redeclared Constant: A""", inspect.stack()[0].function)) 
    def test_033(self):
        """
func foo() {
    a := 1;
    var a = 1;
}
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),IntLiteral(1)),VarDecl("a", None,IntLiteral(1))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: a""", inspect.stack()[0].function)) 
    def test_034(self):
        """
func Votien (b int) {
    for var a = 1; c < 1; a += c {
        const c = 2;
    }
}
        """
        input = Program([FuncDecl("Votien",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Identifier: c""", inspect.stack()[0].function)) 
    def test_035(self):
        """
var v TIEN;
func (v TIEN) foo (v int) int {
    return v;
}

type TIEN struct {
    Votien int;
}
        """
        input = Program([VarDecl("v",Id("TIEN"), None),MethodDecl("v",Id("TIEN"),FuncDecl("foo",[ParamDecl("v",IntType())],IntType(),Block([Return(Id("v"))]))),StructType("TIEN",[("Votien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, "Success", inspect.stack()[0].function))
    def test_036(self):
        """
        var a = 1.0;
        var b = a + "string";
        """
        input = Program([
            VarDecl("a", None, FloatLiteral(1.0)),
            VarDecl("b", None, BinaryOp("+", Id("a"), StringLiteral("string")))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(\"+\", Id(\"a\"), StringLiteral(\"string\"))", inspect.stack()[0].function))

    def test_037(self):
        """
        const a = 1;
        func main(): void {
            a = 2;
        }
        """
        input = Program([
            ConstDecl("a", None, IntLiteral(1)),
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), IntLiteral(2))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Assign(Id(\"a\"),IntLiteral(2))", inspect.stack()[0].function))


    def test_038(self):
        """
        func foo(): int {
            return "string";
        }
        """
        input = Program([
            FuncDecl("foo", [], IntType(), Block([Return(StringLiteral("string"))]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(StringLiteral(\"string\"))", inspect.stack()[0].function))

    def test_039(self):
        """
        var a: [2]float;
        var b: [2]int = a;
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2)], FloatType()), None),
            VarDecl("b", ArrayType([IntLiteral(2)], IntType()), Id("a"))
        ])
        self.assertTrue(TestChecker.test(input, "Success", inspect.stack()[0].function))

    def test_040(self):
        """
        func foo(a: [2]int): void {}
        func bar(): void {
            foo([3]int{1, 2, 3});
        }
        """
        input = Program([
            FuncDecl("foo", [ParamDecl("a", ArrayType([IntLiteral(2)], IntType()))], VoidType(), Block([])),
            FuncDecl("bar", [], VoidType(), Block([FuncCall("foo", [ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])])]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: FuncCall(\"foo\",[ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])", inspect.stack()[0].function))
    def test_041(self):
        """
        var x = 5;
        func test(): void {
            var x = true;
            x = x + 1;
        }
        """
        input = Program([
            VarDecl("x", None, IntLiteral(5)),
            FuncDecl("test", [], VoidType(), Block([
                VarDecl("x", None, BooleanLiteral(True)),
                Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: BinaryOp(\"+\", Id(\"x\"), IntLiteral(1))", inspect.stack()[0].function))

    def test_042(self):
        """
        func foo(): int {
            return;
        }
        """
        input = Program([
            FuncDecl("foo", [], IntType(), Block([
                Return(None)
            ]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: Return(None)", inspect.stack()[0].function))

    def test_043(self):
        """
        var a: [3]int = [1, 2];
        """
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(3)], IntType()), ArrayLiteral([IntLiteral(1)], IntType(),[IntLiteral(1), IntLiteral(2)]))
        ])
        self.assertTrue(TestChecker.test(input, "Type Mismatch: VarDecl(\"a\",ArrayType([IntLiteral(3)],IntType()),ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1),IntLiteral(2)]))", inspect.stack()[0].function))

    
    def test_044(self):
        """
func (v TIEN) VO () {return ;}
func (v TIEN) Tien () {return ;}
type TIEN struct {
    Votien int;
    Tien int;
}
        """
        input = Program([MethodDecl("v",Id("TIEN"),FuncDecl("VO",[],VoidType(),Block([Return(None)]))),MethodDecl("v",Id("TIEN"),FuncDecl("Tien",[],VoidType(),Block([Return(None)]))),StructType("TIEN",[("Votien",IntType()),("Tien",IntType())],[])])
        self.assertTrue(TestChecker.test(input, """Redeclared Method: Tien""", inspect.stack()[0].function))
    def test_045(self):
        input = """
func foo() int {
    const foo = 1;
    return foo()
}
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        self.assertTrue(TestChecker.test(input, """Undeclared Function: foo""", inspect.stack()[0].function))


    def test_046(self):
        input = Program([
        FuncDecl("a", [], VoidType(), Block([ ])),
        ConstDecl("a",IntType(),None),
        ])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(
        input,
        expect,
        inspect.stack()[0].function
        ))

    def test_047(self):
        input = Program([
        ConstDecl("a",IntType(),None),
        FuncDecl("a", [], VoidType(), Block([ ])),
        ])
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(
        input,
        expect,inspect.stack()[0].function
        ))

    def test_048(self):
        input = Program([
        MethodDecl(
            "a",
            StructType("A", [], []),
            FuncDecl("Foo", [
            ParamDecl("a", IntType()),
            ], VoidType(), Block([ ])),
        ),
        StructType("A", [], [])
        ])
        expect = "Success"
        self.assertTrue(TestChecker.test(
        input,
        expect,
        inspect.stack()[0].function
        ))
    def test_builtin_functions_bad(self):
        input = Program([
        VarDecl(
            "a",
            IntType(),
            FuncCall("getInt", [])
        ),
        VarDecl(
            "b",
            None,
            FuncCall("putInt", [IntLiteral(5)])
        ),
        VarDecl(
            "c",
            VoidType(),
            FuncCall("putIntLn", [IntLiteral(5)])
        ),
        VarDecl(
            "d",
            FloatType(),
            FuncCall("getFloat", [])
        ),
        VarDecl(
            "e",
            VoidType(),
            FuncCall("putFloat", [FloatLiteral(5.5)])
        ),
        VarDecl(
            "f",
            VoidType(),
            FuncCall("putFloatLn", [FloatLiteral(5.5)])
        ),
        VarDecl(
            "g",
            BoolType(),
            FuncCall("getBool", [])
        ),
        VarDecl(
            "h",
            VoidType(),
            FuncCall("putBool", [BooleanLiteral(True)])
        ),
        VarDecl(
            "j",
            VoidType(),
            FuncCall("putBoolLn", [BooleanLiteral(True)])
        ),
        VarDecl(
            "k",
            StringType(),
            FuncCall("getString", [])
        ),
        VarDecl(
            "l",
            VoidType(),
            FuncCall("putString", [StringLiteral("hi")])
        ),
        VarDecl(
            "m",
            VoidType(),
            FuncCall("putStringLn", [StringLiteral("hi")])
        ),
        VarDecl(
            "n",
            VoidType(),
            FuncCall("putLn", [])
        ),
        ])
        expect = "Type Mismatch: FuncCall(\"putInt\",[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(
        input,
        expect,
        inspect.stack()[0].function
        ))

    def test_100(self):
        """var a int; var b int; var a int; """
        input = Program([VarDecl("a", IntType(), None), VarDecl("b", IntType(), None), VarDecl("a", IntType(), None)])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))

    def test_101(self):
        """var a int = 1.2;"""
        input = Program([VarDecl("a", IntType(), FloatLiteral(1.2))])
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))

    def test_102(self):
        """var a int = b;"""
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))
        
    def test_103(self):
        """
            var a int; 
            const a = 1;
        """
        input = Program([VarDecl("a", IntType(), None), ConstDecl("a", None, IntLiteral(1))])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_101(self):
        """
            func main() {
                a();
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("a", [])]))])
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_105(self):
        """
            var a = 2.1;
            func main() {
                var c = a.b;
            }
        """
        input = Program([VarDecl("a", None, FloatLiteral(2.1)), FuncDecl("main", [], VoidType(), Block([VarDecl("c", None, FieldAccess(Id("a"), "b"))]))])
        expect = "Type Mismatch: FieldAccess(Id(a),b)"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_106(self):
        """
            func main() {
                var c = a.b();
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("c", None, MethCall(Id("a"), "b", []))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_107(self):
        """
            var getInt = 1;
        """
        input = Program([VarDecl("getInt", None, IntLiteral(1))])
        expect = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_108(self):
        """
            var a = 1;
            var b = a;
            var c = d;
        """
        input = Program([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, Id("a")), VarDecl("c", None, Id("d"))])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_109(self):
        """
            func main() {
                const b = 10;
            }
            func main(a int) int {
                return a;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ConstDecl("b", None, IntLiteral(10))])), FuncDecl("main", [ParamDecl("a", IntType())], IntType(), Block([Return(Id("a"))]))])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_110(self):
        """
            const a = 2;
            func foo () {
                const a = 1;
                for var a = 1; a < 1; b := 2 {
                    const b = 1;
                }
            }
        """
        input = Program([ConstDecl("a",None,IntLiteral(2)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,IntLiteral(1)),ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Block([ConstDecl("b",None,IntLiteral(1))]))]))])
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_111(self):
        """
            var a = [2] float {1, 2}
            var c [3] int = a
        """
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],FloatType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_112(self):
        """
            type S1 struct {asdf int; x S1;}
            var b S1;
            var c = b.x.asdf;
            var d = c.x;
        """
        input = Program([StructType("S1",[("asdf",IntType()),("x",Id("S1"))],[]),VarDecl("b",Id("S1"), None),VarDecl("c", None,FieldAccess(FieldAccess(Id("b"),"x"),"asdf")),VarDecl("d", None,FieldAccess(Id("c"),"x"))])
        expect = "Type Mismatch: FieldAccess(Id(c),x)"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_113(self):
        """
            func main() {
                a += 1
                var a int;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))), VarDecl("a", IntType(), None)]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_114(self):
        """
            var a boolean = 1 > 2;
            var b boolean = 1.0 < 2.0;
            var c boolean = "1" == "2";
            var d boolean = 1 > 2.0;
        """
        input = Program([VarDecl("a",BoolType(),BinaryOp(">", IntLiteral(1), IntLiteral(2))),VarDecl("b",BoolType(),BinaryOp("<", FloatLiteral(1.0), FloatLiteral(2.0))),VarDecl("c",BoolType(),BinaryOp("==", StringLiteral("1"), StringLiteral("2"))),VarDecl("d",BoolType(),BinaryOp(">", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),>,FloatLiteral(2.0))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_115(self):
        """
            var a int = 1;
            var b int = 2;
            var c int = a + b;
            var d int = a + b + 1.0;
        """
        input = Program([VarDecl("a", IntType(), IntLiteral(1)), VarDecl("b", IntType(), IntLiteral(2)), VarDecl("c", IntType(), BinaryOp("+", Id("a"), Id("b"))), VarDecl("d", IntType(), BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), FloatLiteral(1.0)))])
        expect = "Type Mismatch: VarDecl(d,IntType,BinaryOp(BinaryOp(Id(a),+,Id(b)),+,FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_116(self):
        """
            func foo(){
                for var i int = 1; i < 10; i := 1.0 {
                    return;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([ForStep(VarDecl("i",IntType(),IntLiteral(1)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),FloatLiteral(1.0)),Block([Return(None)]))]))])
        expect = "Type Mismatch: Assign(Id(i),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_117(self):
        """
            func foo(){
                var arr [2][3] int;
                for a, b := range arr {
                    var c int = a;
                    var d [3]int = b;
                    var e [2]string = a;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_118(self):
        """
            func foo(a int) int {return 1;}

            var a int = foo(1 + 1);
            var b = foo(1.0);
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))])),VarDecl("a",IntType(),FuncCall("foo",[BinaryOp("+", IntLiteral(1), IntLiteral(1))])),VarDecl("b", None,FuncCall("foo",[FloatLiteral(1.0)]))])
        expect = "Type Mismatch: FuncCall(\"foo\",[FloatLiteral(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_119(self):
        """
            func foo() [2] float {
                return [2] float {1.0, 2.0};
                return [2] int {1, 2};
            }
        """
        input = Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],FloatType()),Block([Return(ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])),Return(ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_120(self):
        """
            type Shape interface {
                calculate ();
                calculate (a int);
            }
        """
        input = Program([InterfaceType("Shape", [Prototype("calculate", [], VoidType()), Prototype("calculate", [("a", IntType())], VoidType())])])
        expect = "Redeclared Prototype: calculate"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_121(self):
        """
            func Haha (a, a int) {return;}
        """
        input = Program([FuncDecl("Haha", [ParamDecl("a", IntType()), ParamDecl("a", IntType())], VoidType(), Block([]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_122(self):
        """
            func Foo () int {return 1;}

            func foo () {
                var b = Foo();
                foo_foo();
                return;
            }
        """
        input = Program([FuncDecl("Foo", [], IntType(), Block([Return(IntLiteral(1))])), FuncDecl("foo", [], VoidType(), Block([VarDecl("b", None, FuncCall("Foo", [])), FuncCall("foo_foo", []), Return(None)]))])
        expect = "Undeclared Function: foo_foo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_123(self):
        """
            type DUMMY struct {
                time int;
            }

            func (asdf DUMMY) getInt () {
                const c = asdf.time;
                var d = asdf.size;
            }
        """
        input = Program([StructType("DUMMY", [("time", IntType())], []), MethodDecl("asdf", Id("DUMMY"), FuncDecl("getInt", [], VoidType(), Block([ConstDecl("c", None, FieldAccess(Id("asdf"), "time")), VarDecl("d", None, FieldAccess(Id("asdf"), "size"))])))])
        expect = "Undeclared Field: size"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_121(self):
        """
            type A struct {x int;}
            type B struct {x int;}
            var a A;
            var b B = a;
        """
        input = Program([
            StructType("A", [("x", IntType())], []),
            StructType("B", [("x", IntType())], []),
            VarDecl("a", Id("A"), None),
            VarDecl("b", Id("B"), Id("a"))
        ])
        expect = "Type Mismatch: VarDecl(b,Id(B),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_125(self):
        """
            func test() int {
                return true;
            }
        """
        input = Program([
            FuncDecl("test", [], IntType(), Block([
                Return(BooleanLiteral(True))
            ]))
        ])
        expect = "Type Mismatch: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_126(self):
        """
            type X struct {
                a int;
                a float;
            }
        """
        input = Program([
            StructType("X", [("a", IntType()), ("a", FloatType())], [])
        ])
        expect = "Redeclared Field: a"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_127(self):
        """
            func main() {
                var a = 1;
                a := "string";
            }
        """
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                VarDecl("a", None, IntLiteral(1)),
                Assign(Id("a"), StringLiteral("string"))
            ]))
        ])
        expect = "Success""Type Mismatch: Assign(Id(a),StringLiteral(string))"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_128(self):
        """
            func main() {
                a := 1.0;
                var a float;
            }
        """
        input = Program([
            FuncDecl("main", [], VoidType(), Block([
                Assign(Id("a"), FloatLiteral(1.0)),
                VarDecl("a", FloatType(), None)
            ]))
        ])
        expect = "Success""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_129(self):
        """
            func foo() int {
                const foo = 1;
                return foo()
            }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([ConstDecl("foo",None,IntLiteral(1)),Return(FuncCall("foo",[]))]))])
        expect = "Redeclared Constant: foo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_130(self):
        """
            var a int = 1 % 2;
            var b int = 1 % 2.0;
        """
        input = Program([VarDecl("a",IntType(),BinaryOp("%", IntLiteral(1), IntLiteral(2))),VarDecl("b",IntType(),BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_131(self):
        """
            var a [2][3] int;
            var b = a[1];
            var c [3] int = b;
            var d [3] string = b;
        """
        input = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("d",ArrayType([IntLiteral(3)],StringType()),Id("b"))])
        expect = "Type Mismatch: VarDecl(d,ArrayType(StringType,[IntLiteral(3)]),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_132(self):
        """
            var A = 1;
            type A struct {a int;}
        """
        input = Program([VarDecl("A", None,IntLiteral(1)),StructType("A",[("a",IntType())],[])])
        expect = "Redeclared Type: A"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_133(self):
        """
            type SMTH struct {a [2]int;} 

            func foo() SMTH {
                return nil
            }
        """
        input = Program([StructType("SMTH",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),FuncDecl("foo",[],Id("SMTH"),Block([Return(NilLiteral())]))])
        expect = "Type Mismatch: Return(Nil)"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_131(self):
        """
            func foo(a [2] float) {
                foo([2] float {1.0,2.0})
                foo([2] int {1,2})
            }
        """
        input = Program([FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],FloatType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)])]),FuncCall("foo",[ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])])]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_135(self):
        """
            func foo() {
                var a int = 1;
                var b float = a;
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(1)),VarDecl("b",FloatType(),Id("a"))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_136(self):
        """
            type Person struct {
                name string ;
                age int ;
            }

            func  lms()  {
                var person = Person{name: "Alice", age: 30}
                person.name := "John";
                person.age := 30;
                putStringLn(person.name)
                putStringLn(person.Greet())
            }

            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),FuncDecl("lms",[],VoidType(),Block([VarDecl("person", None,StructLiteral("Person",[("name",StringLiteral("Alice")),("age",IntLiteral(30))])),Assign(FieldAccess(Id("person"),"name"),StringLiteral("John")),Assign(FieldAccess(Id("person"),"age"),IntLiteral(30)),FuncCall("putStringLn",[FieldAccess(Id("person"),"name")]),FuncCall("putStringLn",[MethCall(Id("person"),"Greet",[])])])),MethodDecl("p",Id("Person"),FuncDecl("Greet",[],StringType(),Block([Return(BinaryOp("+", StringLiteral("Hello, "), FieldAccess(Id("p"),"name")))])))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_137(self):
        """
            type S1 struct {lms int;}
            type S2 struct {lms int;}
            type I1 interface {lms(e, e int) S1;}
            type I2 interface {lms(a int, b float) S1;}

            func (s S1) lms(a, b int) S1 {return s;}

            var a S1;
            var c I1 = a;
            var d I2 = a;
        """
        input = Program([StructType("S1",[("lms",IntType())],[]),StructType("S2",[("lms",IntType())],[]),InterfaceType("I1",[Prototype("lms",[IntType(),IntType()],Id("S1"))]),InterfaceType("I2",[Prototype("lms",[IntType(),FloatType()],Id("S1"))]),MethodDecl("s",Id("S1"),FuncDecl("lms",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],Id("S1"),Block([Return(Id("s"))]))),VarDecl("a",Id("S1"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("a"))])
        expect = "Redeclared Method: lms"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_138(self):
        """
            type WHAT struct {a [2]int;} 
            type WHY interface {foo() int;}

            func (asdf WHAT) foo() int {return 1;}

            func foo() {
                var b = WHAT{a: [2]int{1, 2}};
                var a int = b.a[1]
            }
        """
        input = Program([StructType("WHAT",[("a",ArrayType([IntLiteral(2)],IntType()))],[]),InterfaceType("WHY",[Prototype("foo",[],IntType())]),MethodDecl("asdf",Id("WHAT"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,StructLiteral("WHAT",[("a",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]))])),VarDecl("a",IntType(),ArrayCell(FieldAccess(Id("b"),"a"),[IntLiteral(1)]))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_139(self):
        """
            func foo() int {
                var a = 1;
                if (a < 3) {
                    var a = 1;
                } else if(a > 2) {
                    var a = 2;
                }
                return a;
            }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1)),If(BinaryOp("<", Id("a"), IntLiteral(3)), Block([VarDecl("a", None,IntLiteral(1))]), If(BinaryOp(">", Id("a"), IntLiteral(2)), Block([VarDecl("a", None,IntLiteral(2))]), None)),Return(Id("a"))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_140(self):
        """
            func foo() {
                var a [5][6] int;
                var b [2] float;
                b[2] := a[2][3]
                a[2][3] := b[2] + 1;
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(6)],IntType()), None),VarDecl("b",ArrayType([IntLiteral(2)],FloatType()), None),Assign(ArrayCell(Id("b"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+", ArrayCell(Id("b"),[IntLiteral(2)]), IntLiteral(1)))]))])
        expect = "Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(2),IntLiteral(3)]),BinaryOp(ArrayCell(Id(b),[IntLiteral(2)]),+,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_141(self):
        """
            type Person struct {
                name string;
                age  int;
            };
            func (p Person) getAge() int {
                p := Person{name: "Alice", age: 30}
                var q = Person{}
                return p.age
            };
        """
        input = Program([StructType("Person",[("name",StringType()),("age",IntType())],[]),MethodDecl("p",Id("Person"),FuncDecl("getAge",[],IntType(),Block([Assign(Id("p"),StructLiteral("Person",[("name",StringLiteral("Alice")),("age",IntLiteral(30))])),VarDecl("q", None,StructLiteral("Person",[])),Return(FieldAccess(Id("p"),"age"))])))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_142(self):
        """
            var a = 1;
            func foo () {
                const b = 1;
                for a, c := range [3]int{1, 2, 3} {
                    var d = c;
                }
                var d = a;
                var a = 1;
            }
            var d = b;
        """
        input = Program([VarDecl("a", None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(1)),ForEach(Id("a"),Id("c"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("d", None,Id("c"))])),VarDecl("d", None,Id("a")),VarDecl("a", None,IntLiteral(1))])),VarDecl("d", None,Id("b"))])
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_143(self):
        """
            const asdf = 3;
            const k = asdf + 1;
            func foo(a [1 + 2] int) {
                foo([k - 1] int {1,2,3})
            } 
        """
        input = Program([ConstDecl("asdf",None,IntLiteral(3)),ConstDecl("k",None,BinaryOp("+", Id("asdf"), IntLiteral(1))),FuncDecl("foo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([FuncCall("foo",[ArrayLiteral([BinaryOp("-", Id("k"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_144(self):
        """
            type K struct {a int;}
            func (k K) koo(a [1 + 2] int) {return;}
            type H interface {koo(a [1 + 2] int);}

            const c = 1;
            func foo() {
                var k H;
                k.koo([c - 1] int {1,2,3})
            } 
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],VoidType(),Block([Return(None)]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],VoidType())]),ConstDecl("c",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([VarDecl("k",Id("H"), None),MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_145(self):
        """
            type K struct {a int;}
            func (k K) koo(a [1 + 2] int) [1 + 2] int {return [3*1] int {1,2,3};}
            type H interface {koo(a [1 + 2] int) [1 + 2] int;}

            const c = 1;
            func foo() [1 + 2] int{
                return foo()
                var k K;
                return k.koo([c - 1] int {1,2,3})
                var h H;
                return h.koo([c - 1] int {1,2,3})
            }   
        """
        input = Program([StructType("K",[("a",IntType())],[]),MethodDecl("k",Id("K"),FuncDecl("koo",[ParamDecl("a",ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(ArrayLiteral([BinaryOp("*", IntLiteral(3), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))),InterfaceType("H",[Prototype("koo",[ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType())],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()))]),ConstDecl("c",None,IntLiteral(1)),FuncDecl("foo",[],ArrayType([BinaryOp("+", IntLiteral(1), IntLiteral(2))],IntType()),Block([Return(FuncCall("foo",[])),VarDecl("k",Id("K"), None),Return(MethCall(Id("k"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),VarDecl("h",Id("H"), None),Return(MethCall(Id("h"),"koo",[ArrayLiteral([BinaryOp("-", Id("c"), IntLiteral(1))],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_146(self):
        """
            const a = 3;
            const b = -a;
            const c = -b;
            var d [c] int = [3] int {1,2,3}
        """
        input = Program([ConstDecl("a",None,IntLiteral(3)),ConstDecl("b",None,UnaryOp("-",Id("a"))),ConstDecl("c",None,UnaryOp("-",Id("b"))),VarDecl("d",ArrayType([Id("c")],IntType()),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_147(self):
        """
            const a = 1;
            func foo() {
                a := 1.;
            }
        """
        input = Program([ConstDecl("a",None,IntLiteral(1)),FuncDecl("foo",[],VoidType(),Block([Assign(Id("a"),FloatLiteral(1.0))]))])
        expect = "Type Mismatch: Assign(Id(a),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_148(self):
        """
            func foo() {
                var a = 1.0 == 1
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,BinaryOp("==", FloatLiteral(1.0), IntLiteral(1)))]))])
        expect = "Type Mismatch: BinaryOp(FloatLiteral(1.0),==,IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_149(self):
        """
            func foo() {
                foo := 1;
                foo()
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([Assign(Id("foo"),IntLiteral(1)),FuncCall("foo",[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_150(self):
        """
            type Person stuct {
                name string;
                age int
            }
            func (p Person) Add(p int) {
                p.age := p.age + p
            }
        """
        input = Program([StructType("Person", [("name", StringType()), ("age", IntType())], []), MethodDecl("p", Id("Person"), FuncDecl("Add", [ParamDecl("p", IntType())], VoidType(), Block([Assign(FieldAccess(Id("p"), "age"), BinaryOp("+", FieldAccess(Id("p"), "age"), Id("p")))])))])
        expect = "Type Mismatch: FieldAccess(Id(\"p\"),\"age\")"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_151(self):
        """
            func foo () {
                var a = 1;
                var b = 1;
                for a, b := range [3]int {1, 2, 3} {
                    var b = 1;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,IntLiteral(1)),ForEach(Id("a"),Id("b"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),Block([VarDecl("b", None,IntLiteral(1))]))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_152(self):
        """
            func foo(){
                var arr [2][3] int;
                var a = 1;
                var b[3]int;
                for a, b := range arr {
                    var c int = a;
                    var d [3]int = b;
                    var e [2]string = a;
                }
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("arr",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("a", None,IntLiteral(1)),VarDecl("b",ArrayType([IntLiteral(3)],IntType()), None),ForEach(Id("a"),Id("b"),Id("arr"),Block([VarDecl("c",IntType(),Id("a")),VarDecl("d",ArrayType([IntLiteral(3)],IntType()),Id("b")),VarDecl("e",ArrayType([IntLiteral(2)],StringType()),Id("a"))]))]))])
        expect = "Type Mismatch: ForEach(Id(a),Id(b),Id(arr),Block([VarDecl(c,IntType,Id(a)),VarDecl(d,ArrayType(IntType,[IntLiteral(3)]),Id(b)),VarDecl(e,ArrayType(StringType,[IntLiteral(2)]),Id(a))]))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_153(self):
        """
            var asdf moo;      
            type moo struct {
                a int;
            } 
            type cow interface {
                fooA();
                fooB();
                fooC();
            }

            func (asdf moo) fooA() {return ;}
            func (foo moo) fooB() {
                foo()
                return ;
            }
            func (asdf moo) fooC()  {return ;}

            func foo() {
                var x cow = moo{a:1};  
            }
        """
        input = Program([VarDecl("asdf",Id("moo"), None),StructType("moo",[("a",IntType())],[]),InterfaceType("cow",[Prototype("fooA",[],VoidType()),Prototype("fooB",[],VoidType()),Prototype("fooC",[],VoidType())]),MethodDecl("asdf",Id("moo"),FuncDecl("fooA",[],VoidType(),Block([Return(None)]))),MethodDecl("foo",Id("moo"),FuncDecl("fooB",[],VoidType(),Block([FuncCall("foo",[]),Return(None)]))),MethodDecl("asdf",Id("moo"),FuncDecl("fooC",[],VoidType(),Block([Return(None)]))),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",Id("cow"),StructLiteral("moo",[("a",IntLiteral(1))]))]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_154(self):
        """
            func loop () {
                var array [2][3] int;
                var index int;
                var value [3] float;
                for index, value := range array {
                    return;
                }
            }
        """
        input = Program([FuncDecl("loop",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),VarDecl("index",IntType(), None),VarDecl("value",ArrayType([IntLiteral(3)],FloatType()), None),ForEach(Id("index"),Id("value"),Id("array"),Block([Return(None)]))]))])
        expect = "Type Mismatch: ForEach(Id(index),Id(value),Id(array),Block([Return()]))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_155(self):
        """
            var asdf ABC;
            const b = asdf.b;        
            type ABC struct {
                a int;
                b int;
                c int;
            }
            const a = asdf.a;
            const e = asdf.e;
        """
        input = Program([VarDecl("asdf",Id("ABC"), None),ConstDecl("b",None,FieldAccess(Id("asdf"),"b")),StructType("ABC",[("a",IntType()),("b",IntType()),("c",IntType())],[]),ConstDecl("a",None,FieldAccess(Id("asdf"),"a")),ConstDecl("e",None,FieldAccess(Id("asdf"),"e"))])
        expect = "Undeclared Field: e"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
    
    def test_156(self):
        """
            var asdf moo;       
            type moo struct {
                a int;
            } 
            func (asdf moo) foo() int {return 1;}
            func (b moo) koo() {b.koo();}
            func foo() {
                const b = asdf.foo(); 
                asdf.koo(); 
                const d = asdf.zoo();
            }
        """
        input = Program([VarDecl("asdf",Id("moo"), None),StructType("moo",[("a",IntType())],[]),MethodDecl("asdf",Id("moo"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))]))),MethodDecl("b",Id("moo"),FuncDecl("koo",[],VoidType(),Block([MethCall(Id("b"),"koo",[])]))),FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,MethCall(Id("asdf"),"foo",[])),MethCall(Id("asdf"),"koo",[]),ConstDecl("d",None,MethCall(Id("asdf"),"zoo",[]))]))])
        expect = "Undeclared Method: zoo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_157(self):
        """
            func foo() int {return 1;}
            func  lms() int {
                return lms();
                foo();
            }
        """
        input = Program([FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("lms",[],IntType(),Block([Return(FuncCall("lms",[])),FuncCall("foo",[])]))])
        expect = "Type Mismatch: FuncCall(foo,[])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_158(self):
        """
            type moo struct {asdf int;}
            var asdf moo;
            func foo(){
                for 1 {
                    var a int = 1.2;
                }
            }
        """
        input = Program([StructType("moo",[("asdf",IntType())],[]),VarDecl("asdf",Id("moo"), None),FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([VarDecl("a",IntType(),FloatLiteral(1.2))]))]))])
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_159(self):
        """
            const asdf = 3;
            const a = asdf + asdf;
            var b [a * -(-2) + a] int;
            var c [18] int = b;
        """
        input = Program([ConstDecl("asdf",None,IntLiteral(3)),ConstDecl("a",None,BinaryOp("+", Id("asdf"), Id("asdf"))),VarDecl("b",ArrayType([BinaryOp("+", BinaryOp("*", Id("a"), UnaryOp("-", UnaryOp("-", IntLiteral(2)))), Id("a"))],IntType()), None),VarDecl("c",ArrayType([IntLiteral(18)],IntType()),Id("b"))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_160(self):
        """
            func loop (b int) {
                for var a = 1; c < 1; a += c {
                    const c = 2;
                }
            }
        """
        input = Program([FuncDecl("loop",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("c"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), Id("c"))),Block([ConstDecl("c",None,IntLiteral(2))]))]))])
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_161(self):
        """
            func foo() {
                var a = foo
            }
        """
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,Id("foo"))]))])
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_162(self):
        """
            type A struct { h int }
            func (a A) print() { return; }

            func main() {
                var b int;
                b.print();
            }
        """
        input = Program([StructType("A", [("h", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("print", [], VoidType(), Block([Return(None)]))), FuncDecl("main", [], VoidType(), Block([VarDecl("b", IntType(), None), MethCall(Id("b"), "print", [])]))])
        expect = "Type Mismatch: MethCall(Id(b),print,[])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_163(self):
        """
            type Node struct {
                next Node;
            }
        """
        input = Program([StructType("Node", [("next", Id("Node"))], [])])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_164(self):
        """
            func main() {
                var x A;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", Id("A"), None)]))])
        expect = "Undeclared Type: A"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_165(self):
        """
            type A struct { h int }
            var a A = A{h:1};
        """
        input = Program([StructType("A", [("h", IntType())], []), VarDecl("a", Id("A"), StructLiteral("A", [("h", IntLiteral(1))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_166(self):
        """
            func main() A {
                return A{h:1};
            }
        """
        input = Program([FuncDecl("main", [], Id("A"), Block([Return(StructLiteral("A", [("h", IntLiteral(1))]))]))])
        expect = "Undeclared Type: A"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_167(self):
        """
            func printA() {
                return;
            }
            func main() {
                var a = printA();
            }
        """
        input = Program([FuncDecl("printA", [], VoidType(), Block([Return(None)])), FuncDecl("main", [], VoidType(), Block([VarDecl("a", None, FuncCall("printA", []))]))])
        expect = "Type Mismatch: FuncCall(printA,[])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_168(self):
        """
            type moo struct {
                fff int;
            }
            func (asdf moo) fff () {return ;}
        """
        input = Program([StructType("moo",[("fff",IntType())],[]), MethodDecl("asdf",Id("moo"),FuncDecl("fff",[],VoidType(),Block([Return(None)])))])
        expect = "Redeclared Method: fff"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_169(self):
        """
            func (asdf STRU) putIntLn () {return;}
            func (asdf STRU) getInt () {return;}
            func (asdf STRU) getInt () {return;}
            type STRU struct {
                num int;
            }
        """
        input = Program([MethodDecl("asdf", Id("STRU"), FuncDecl("putIntLn", [], VoidType(), Block([Return(None)]))), MethodDecl("asdf", Id("STRU"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))), MethodDecl("asdf", Id("STRU"), FuncDecl("getInt", [], VoidType(), Block([Return(None)]))), StructType("STRU", [("fff", IntType())], [])])
        expect = "Redeclared Method: getInt"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_170(self):
        """
            type S1 struct {lms int;}
            type S2 struct {lms int;}
            type I1 interface {lms();}
            type I2 interface {lms();}

            func (s S1) lms() {return;}

            var a S1;
            var b S2;
            var c I1 = a;
            var d I2 = b;
        """
        input = Program([StructType("S1",[("lms",IntType())],[]),StructType("S2",[("lms",IntType())],[]),InterfaceType("I1",[Prototype("lms",[],VoidType())]),InterfaceType("I2",[Prototype("lms",[],VoidType())]),MethodDecl("s",Id("S1"),FuncDecl("lms",[],VoidType(),Block([Return(None)]))),VarDecl("a",Id("S1"), None),VarDecl("b",Id("S2"), None),VarDecl("c",Id("I1"),Id("a")),VarDecl("d",Id("I2"),Id("b"))])
        expect = "Redeclared Method: lms"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_171(self):
        """
            type S1 struct {lms int;}
            type I1 interface {lms(a int) int;}
            func (s S1) lms( a int) int {return 1;}

            var s S1;
            var a int = s.lms(1);
            var b int = s.lms(1.0);
        """ 
        input = Program([StructType("S1",[("lms",IntType())],[]),InterfaceType("I1",[Prototype("lms",[IntType()],IntType())]),MethodDecl("s",Id("S1"),FuncDecl("lms",[ParamDecl("a",IntType())],IntType(),Block([Return(IntLiteral(1))]))),VarDecl("s",Id("S1"), None),VarDecl("a",IntType(),MethCall(Id("s"),"lms",[IntLiteral(1)])),VarDecl("b",IntType(),MethCall(Id("s"),"lms",[FloatLiteral(1.0)]))])
        expect = "Redeclared Method: lms"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_172(self):
        """
            func main() {
                var arr [3]int;
                arr[3] := 5;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(3)], IntType()), None),Assign(ArrayCell(Id("arr"), [IntLiteral(3)]), IntLiteral(5))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_173(self):
        """
            func main() {
                var arr [3]string;
                arr[1] = 100;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(3)], StringType()), None), Assign(ArrayCell(Id("arr"), [IntLiteral(1)]), IntLiteral(100))]))])
        expect = "Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(1)]),IntLiteral(100))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_171(self):
        """
            type A struct { x int; }
            func (a A) getX() int { return a.x; }
            func main() {
                var a A;
                var x int = a.getX(5);
            }
        """
        input = Program([StructType("A", [("x", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("getX", [], IntType(), Block([Return(FieldAccess(Id("a"), "x"))]))), FuncDecl("main", [], VoidType(), Block([VarDecl("a", Id("A"), None), VarDecl("x", IntType(), MethCall(Id("a"), "getX", [IntLiteral(5)]))]))])
        expect = "Type Mismatch: MethodCall(Id(a),getX,[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_175(self):
        """
            func main() {
                if true {
                    var x int = 5;
                }
                x := 10;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([If(BooleanLiteral(True), Block([VarDecl("x", IntType(), IntLiteral(5))]), None), Assign(Id("x"), IntLiteral(10))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_176(self):
        """
            func add(a int, b int) int {
                return a + b;
            }

            func main() {
                var result = add(1, 2.0);
            }
        """
        input = Program([FuncDecl("add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([Return(BinaryOp("+", Id("a"), Id("b")))])), FuncDecl("main", [], VoidType(), Block([VarDecl("result", None, FuncCall("add", [IntLiteral(1), FloatLiteral(2.0)]))]))])
        expect = "Type Mismatch: FuncCall(add,[IntLiteral(1),FloatLiteral(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_177(self):
        """
            func foo() {
                return;
            }

            func bar() {
                foo(1);
            }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([Return(None)])), FuncDecl("bar", [], VoidType(), Block([FuncCall("foo", [IntLiteral(1)])]))])
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_178(self):
        """
            type A struct { x int; }
            func main() {
                var a A;
                var y = a.y;
            }
        """
        input = Program([StructType("A", [("x", IntType())], []), FuncDecl("main", [], VoidType(), Block([VarDecl("a", Id("A"), None), VarDecl("y", None, FieldAccess(Id("a"), "y"))]))])
        expect = "Undeclared Field: y"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_179(self):
        """
            func foo() {
                var x = 1;
                x := 2.0;
            }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([VarDecl("x", None, IntLiteral(1)), Assign(Id("x"), FloatLiteral(2.0))]))])
        expect = "Type Mismatch: Assign(Id(x),FloatLiteral(2.0))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_180(self):
        """
            func foo() {
                const foo = 1;
                var x = foo();
            }
        """
        input = Program([FuncDecl("foo", [], VoidType(), Block([ConstDecl("foo", None, IntLiteral(1)), VarDecl("x", None, FuncCall("foo", []))]))])
        expect = "Redeclared Constant: foo"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_181(self):
        """
            func main() {
                var arr[5] int;
                var x = arr[true];
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None), VarDecl("x", None, ArrayCell(Id("arr"), [BooleanLiteral(True)]))]))])
        expect = "Type Mismatch: ArrayCell(Id(arr),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_182(self):
        """
            type A struct { x int; }
            func main() {
                var a A;
                var y = a.x.y;
            }
        """
        input = Program([StructType("A", [("x", IntType())], []), FuncDecl("main", [], VoidType(), Block([VarDecl("a", Id("A"), None), VarDecl("y", None, FieldAccess(FieldAccess(Id("a"), "x"), "y"))]))])
        expect = "Type Mismatch: FieldAccess(FieldAccess(Id(a),x),y)"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_183(self):
        """
            func foo(a int, b int) int {
                return a + b;
            }

            func main() {
                var x = foo(1);
            }
        """
        input = Program([FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], IntType(), Block([Return(BinaryOp("+", Id("a"), Id("b")))])), FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, FuncCall("foo", [IntLiteral(1)]))]))])
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_181(self):
        """
            type I interface { foo(); }
            type S struct { b int; }

            var a I = S;
        """
        input = Program([InterfaceType("I", [Prototype("foo", [], VoidType())]), StructType("S", [("b", IntType())], []), VarDecl("a", Id("I"), Id("S"))])
        expect = "Type Mismatch: VarDecl(a,Id(I),Id(S))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_185(self):
        """
            type I interface { foo(); }
            type S struct { b int }

            func (s S) foo() {}

            var a I = S{b:1};
        """
        input = Program([InterfaceType("I", [Prototype("foo", [], VoidType())]), StructType("S", [("b", IntType())], []), MethodDecl("s", Id("S"), FuncDecl("foo", [], VoidType(), Block([Return(None)]))), VarDecl("a", Id("I"), StructLiteral("S", [("b", IntLiteral(1))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_186(self):
        """
            func main() {
                var x = y + 1;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, BinaryOp("+", Id("y"), IntLiteral(1)))]))])
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_187(self):
        """
            func main() {
                for var i = 0; i < 10; i += 1 {
                    var i = 100;
                }
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ForStep(VarDecl("i", None, IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(10)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([VarDecl("i", None, IntLiteral(100))]))]))])
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_188(self):
        """
            func main() {
                var x = 1;
                var y = 2;
                var z = x + y;
                var t = x + y + z;
                var u = x + y + z + t;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, IntLiteral(1)), VarDecl("y", None, IntLiteral(2)), VarDecl("z", None, BinaryOp("+", Id("x"), Id("y"))), VarDecl("t", None, BinaryOp("+", BinaryOp("+", Id("x"), Id("y")), Id("z"))), VarDecl("u", None, BinaryOp("+", BinaryOp("+", BinaryOp("+", Id("x"), Id("y")), Id("z")), Id("t")))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_189(self):
        """
            func foo() int {
                return;
            }
        """
        input = Program([FuncDecl("foo", [], IntType(), Block([Return(None)]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_190(self):
        """
            func main() {
                for var i = 0; i < 5; i += 1 {
                    break;
                }
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([ForStep(VarDecl("i", None, IntLiteral(0)), BinaryOp("<", Id("i"), IntLiteral(5)), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([Break()]))]))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_191(self):
        """
            func main() {
                var x[3] int;
                var a = x[1.1];
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", ArrayType([IntLiteral(3)], IntType()), None), VarDecl("a", None, ArrayCell(Id("x"), [FloatLiteral(1.1)]))]))])
        expect = "Type Mismatch: ArrayCell(Id(x),[FloatLiteral(1.1)])"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_192(self):
        """
            const a = 1 + 2;
            const b = 3 * (1 - 1);
            const c = -5;
            const d = +10;
            const e = !(true && false);
            const f = "Hello" + " World";
            const g = 1.5 * 2.0;
            const h = true || false;
            const i = 10 / 2 + 3;
            const num1 = b - (-c);
        """
        input = Program([ConstDecl("a", None, BinaryOp("+", IntLiteral(1), IntLiteral(2))), ConstDecl("b", None, BinaryOp("*", IntLiteral(3), BinaryOp("-", IntLiteral(1), IntLiteral(1)))), ConstDecl("c", None, UnaryOp("-", IntLiteral(5))), ConstDecl("d", None, UnaryOp("+", IntLiteral(10))), ConstDecl("e", None, UnaryOp("!", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)))), ConstDecl("f", None, BinaryOp("+", StringLiteral("Hello"), StringLiteral(" World"))), ConstDecl("g", None, BinaryOp("*", FloatLiteral(1.5), FloatLiteral(2.0))), ConstDecl("h", None, BinaryOp("||", BooleanLiteral(True), BooleanLiteral(False))), ConstDecl("i", None, BinaryOp("+", BinaryOp("/", IntLiteral(10), IntLiteral(2)), IntLiteral(3))), ConstDecl("num1", None, BinaryOp("-", Id("b"), UnaryOp("-", Id("c"))))])
        expect = "Type Mismatch: UnaryOp(+,IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_193(self):
        """
            func main() {
                var a int = 1;
                var b float = 2.0;
                a := b;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", None, IntLiteral(1)), VarDecl("b", None, FloatLiteral(2.0)), Assign(Id("a"), Id("b"))]))])
        expect = "Type Mismatch: Assign(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_191(self):
        """
            func main() {
                var x = x;
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, Id("x"))]))])
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_195(self):
        """
            type A struct { x int; }
            func (a A) foo() int { return 1; }

            var x A;
            var y int = x.foo() + x.bar();
        """
        input = Program([StructType("A", [("x", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))), VarDecl("x", Id("A"), None), VarDecl("y", None, BinaryOp("+", MethCall(Id("x"), "foo", []), MethCall(Id("x"), "bar", [])))])
        expect = "Undeclared Method: bar"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_196(self):
        """
            type A struct { x int; }
            func (a A) foo() int { return 1; }
            func (a A) bar() boolean { return false; }

            var x A;
            var y int = x.foo() + x.bar();
        """
        input = Program([StructType("A", [("x", IntType())], []), MethodDecl("a", Id("A"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))), MethodDecl("a", Id("A"), FuncDecl("bar", [], BoolType(), Block([Return(BooleanLiteral(False))]))), VarDecl("x", Id("A"), None), VarDecl("y", None, BinaryOp("+", MethCall(Id("x"), "foo", []), MethCall(Id("x"), "bar", [])))])
        expect = "Type Mismatch: BinaryOp(MethodCall(Id(x),foo,[]),+,MethodCall(Id(x),bar,[]))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_197(self):
        """
            func lenString(string string) int {
                return 5;
            }
            
            var x int = lenString("Hello");
            var y = x && lenString("haha")
        """
        input = Program([FuncDecl("lenString", [ParamDecl("string", StringType())], IntType(), Block([Return(IntLiteral(5))])), VarDecl("x", None, FuncCall("lenString", [StringLiteral("Hello")])), VarDecl("y", None, BinaryOp("&&", Id("x"), FuncCall("lenString", [StringLiteral("haha")])))])
        expect = "Type Mismatch: BinaryOp(Id(x),&&,FuncCall(lenString,[StringLiteral(haha)]))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_198(self):
        """
            func main() {
                var x = 1 % "a";
            }
        """
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("x", None, BinaryOp("%", IntLiteral(1), StringLiteral("a")))]))])
        expect = "Type Mismatch: BinaryOp(%,IntLiteral(1),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))
        
    def test_199(self):
        """
            type A struct {}
            type B struct {}
            func (a A) foo() {}
            func (b B) foo() {}
        """
        input = Program([StructType("A", [], []), StructType("B", [], []), MethodDecl("a", Id("A"), FuncDecl("foo", [], VoidType(), Block([Return(None)]))), MethodDecl("b", Id("B"), FuncDecl("foo", [], VoidType(), Block([Return(None)])))])
        expect = "Success"
        self.assertTrue(TestChecker.test(input, expect, inspect.stack()[0].function))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,inspect.stack()[0].function))