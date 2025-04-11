"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import unittest
from TestUtils import TestAST
from AST import *
import inspect


##! continue update
class ASTGenSuite(unittest.TestCase):
    def test_101(self):
        input = """const VoTien = 1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_102(self):
        """ chuyển đổi sang kiểu int hết """
        input = """const VoTien = 0b11; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(3))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_103(self):
        input = """const VoTien = 0o70; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(56))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_104(self):
        input = """const VoTien = 0Xa1; """
        expect = Program([ConstDecl("VoTien", None, IntLiteral(161))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_105(self):
        input = """const VoTien = 01.e-1; """
        expect = Program([ConstDecl("VoTien", None, FloatLiteral(0.1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_106(self):
        """ đầu vào là giá trị True False chứ không phải string """
        input = """const VoTien = true; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_107(self):
        input = """const VoTien = false; """
        expect = Program([ConstDecl("VoTien", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_108(self):
        """ loại bỏ "" ở trước và sau string """
        input = """const VoTien = "votien"; """
        expect = Program([ConstDecl("VoTien", None, StringLiteral("votien"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_109(self):
        input = """const VoTien = nil; """
        expect = Program([ConstDecl("VoTien", None, NilLiteral())])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_110(self):
        input = """const VoTien = STRUCT {}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_111(self):
        input = """const VoTien = STRUCT {
            a : 1,
            b : false}; """
        expect = Program([ConstDecl("VoTien", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_112(self):
        input = """const VoTien = [ID] int {1}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_113(self):
        input = """const VoTien = [1][2] int {1., STRUCT{}, nil}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_114(self):
        input = """const VoTien = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = Program([ConstDecl("VoTien", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_115(self):
        input = """const VoTien = 1 || 2 || 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_116(self):
        input = """const VoTien = 1 && 2 && 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_117(self):
        input = """const VoTien = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_118(self):
        input = """const VoTien = 1 + 2 - 3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_119(self):
        input = """const VoTien = 1 * 2 / 3 % 4; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_120(self):
        input = """const VoTien = ! - 1; """
        expect = Program([ConstDecl("VoTien", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_121(self):
        input = """const VoTien = a; """
        expect = Program([ConstDecl("VoTien", None, Id("a"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_122(self):
        input = """const VoTien = (1+2)*3; """
        expect = Program([ConstDecl("VoTien", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_123(self):
        input = """const VoTien = foo(); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_124(self):
        input = """const VoTien = foo(1, 2); """
        expect = Program([ConstDecl("VoTien", None, FuncCall("foo",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_125(self):
        input = """const VoTien = a[2][3]; """
        expect = Program([ConstDecl("VoTien",None,ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_126(self):
        input = """const VoTien = a.b.c; """
        expect = Program([ConstDecl("VoTien", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_127(self):
        input = """const VoTien = a.b().c(1, 2); """
        expect = Program([ConstDecl("VoTien", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_128(self):
        input = """const VoTien = a.b[2].c.d(); """
        expect = Program([ConstDecl("VoTien", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_129(self):
        input = """
    var a int = 1;
    var a float = 1;
    var a boolean;
    var a string = 1;
    var a = 1;
    var a ID = 1;
    var a [ID][1] int = 1;
"""
        expect = Program([VarDecl("a",IntType(),IntLiteral(1)),
			VarDecl("a",FloatType(),IntLiteral(1)),
			VarDecl("a",BoolType(), None),
			VarDecl("a",StringType(),IntLiteral(1)),
			VarDecl("a", None,IntLiteral(1)),
			VarDecl("a",Id("ID"),IntLiteral(1)),
			VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_130(self):
        input = """
    const a = 1;
"""
        expect = Program([ConstDecl("a",None,IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_131(self):
        input = """
    type ID struct {
        a int;
        b ID;
        c [2]int;
    }
"""
        expect = Program([StructType("ID",[("a",IntType()),("b",Id("ID")),("c",ArrayType([IntLiteral(2)],IntType()))],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_132(self):
        input = """
    func foo () {var a = 1;}
    func foo () int {var a = 1;}
    func foo () [2] ID {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_133(self):
        input = """
    func foo (a int) {var a = 1;}
    func foo (a int, b ID) {var a = 1;}
    func foo (a, b int) {var a = 1;}
"""
        expect = Program([FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_133(self):
        input = """
    func (ID ID) foo () {var a = 1;}
    func (ID ID) foo () int {var a = 1;}
    func (ID ID) foo () [2] ID {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_134(self):
        input = """
    func (ID ID) foo (a int) {var a = 1;}
    func (ID ID) foo (a int, b ID) {var a = 1;}
    func (ID ID) foo (a, b int) {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_135(self):
        input = """
        type INTERFACE interface {
            foo();
            foo() int;
            foo() [2]ID;
            foo(a int);
            foo(a int, b int);
            foo(a, b int);
        }
"""
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("foo",[],VoidType()),Prototype("foo",[],IntType()),
            Prototype("foo",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("foo",[IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType()),
            Prototype("foo",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_136(self):
        input = """
    func foo () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_137(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_138(self):
        input = """
    func foo () {
        var a int = 1;
        var a float = 1;
        var a boolean;
        var a string = 1;
        var a = 1;
        var a ID = 1;
        var a [ID][1] int = 1;
        const a = 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            VarDecl("a",IntType(),IntLiteral(1)),
            VarDecl("a",FloatType(),IntLiteral(1)),
            VarDecl("a",BoolType(), None),
            VarDecl("a",StringType(),IntLiteral(1)),
            VarDecl("a", None,IntLiteral(1)),
            VarDecl("a",Id("ID"),IntLiteral(1)),
            VarDecl("a",ArrayType([Id("ID"),IntLiteral(1)],IntType()),IntLiteral(1)),
            ConstDecl("a",None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_139(self):
        input = """
    func foo () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),
            Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_140(self):
        input = """
    func foo () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_141(self):
        input = """
    func foo () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            FuncCall("a",[]),
            FuncCall("a",[IntLiteral(1),IntLiteral(2)]),
            FuncCall("a",[IntLiteral(1)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1),IntLiteral(2)]),
            MethCall(FieldAccess(Id("b"),"a"),"a",[IntLiteral(1)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_142(self):
        input = """
        func foo () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_143(self):
        input = """
        func foo () {
            for(1) {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_144(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_145(self):
        input = """
        func foo () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_146(self):
        input = """
        func foo () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),
            ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_147(self):
        input = """
        func foo () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
            If(IntLiteral(1), Block([Return(None)]), 
               If(IntLiteral(2), Block([Return(None)]), 
                  If(IntLiteral(3), Block([Return(None)]), None)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_148(self):
        input = """
        func foo () {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_149(self):
        input = """
        func foo () {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_150(self):
        input = """
        func foo () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = Program([FuncDecl("foo",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))