import unittest
from TestUtils import TestChecker
from AST import *



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
        expect = ""
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