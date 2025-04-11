
import unittest
from TestUtils import TestAST
from AST import *
import inspect

class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        input = """const Tung = function( 1 ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[IntLiteral(1)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        input = """const Tung = function( 1.0,true,false,nil,\"Tung\" ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[FloatLiteral(1.0),BooleanLiteral(True),BooleanLiteral(False),NilLiteral(),StringLiteral("Tung")]))
		])
        
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        input = """const Tung = function( id ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[Id("id")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        input = """const Tung = function( 1+2-3&&5--1 ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[BinaryOp("&&", BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), BinaryOp("-", IntLiteral(5), UnaryOp("-",IntLiteral(1))))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        input = """const Tung = function( a > b <= c ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[BinaryOp("<=", BinaryOp(">", Id("a"), Id("b")), Id("c"))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        input = """const Tung = function( a[2][3] ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        input = """const Tung = function( a.b.c ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[FieldAccess(FieldAccess(Id("a"),"b"),"c")]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        input = """const Tung = function( a(),b.a(2, 3) ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[FuncCall("a",[]),MethCall(Id("b"),"a",[IntLiteral(2),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        input = """const Tung = function( a * (1+2) ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[BinaryOp("*", Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        input = """const Tung = function( Tung {}, Tung {a: 1} ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[StructLiteral("Tung",[]),StructLiteral("Tung",[("a",IntLiteral(1))])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        input = """const Tung = function( [1]int{1}, [1][1]int{2} ); """
        expect = Program([ConstDecl("Tung",None,FuncCall("function",[ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(1)],IntType(),[IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_012(self):
        input = """
            var Tung = 1;
            var Tung int;
            var Votine int = 1;
"""
        expect = Program([VarDecl("Tung", None,IntLiteral(1)),
			VarDecl("Tung",IntType(), None),
			VarDecl("Votine",IntType(),IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_013(self):
        input = """
            func function() int {return;}
            func function(a int, b int) {return;}
"""
        expect = Program([FuncDecl("function",[],IntType(),Block([Return(None)])),
			FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        input = """
            func (Tung v) function(Tung int) {return;}
"""
        expect = Program([MethodDecl("Tung",Id("v"),FuncDecl("function",[ParamDecl("Tung",IntType())],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_015(self):
        input = """
            type Tung struct {
                a int;
            }
"""
        expect = Program([StructType("Tung",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_016(self):
        input = """
            type Tung struct {
                a int;
            }
"""
        expect = Program([StructType("Tung",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_017(self):
        input = """
            func Tung() {
                var a int;
                const a = nil;
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([VarDecl("a",IntType(), None),ConstDecl("a",None,NilLiteral())]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        input = """
            func Tung() {
                a += 1;
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        input = """
            func Tung() {
                break;
                continue;
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        input = """
            func Tung() {
                function(1, 2);
                a[2].function(1,3);
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([FuncCall("function",[IntLiteral(1),IntLiteral(2)]),MethCall(ArrayCell(Id("a"),[IntLiteral(2)]),"function",[IntLiteral(1),IntLiteral(3)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        input = """
            func Tung() {
                if(1) {return;}
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([If(IntLiteral(1), Block([Return(None)]), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        input = """
            func Tung() {
                if(1) {
                    a := 1;
                } else {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), Block([Assign(Id("a"),IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_023(self):
        input = """
            func Tung() {
                if(1) { return;
                }else if(1) {
                    a := 1;
                }else if(2) {
                    a := 1;
                }
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Assign(Id("a"),IntLiteral(1))]), 
                    If(IntLiteral(2), Block([Assign(Id("a"),IntLiteral(1))]), None)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_024(self):
        input = """
            func Tung() {
                for i < 10 {return;}
                for var i = 0; i < 10; i += 1  {return;}
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([Return(None)])),ForStep(VarDecl("i", None,IntLiteral(0)),BinaryOp("<", Id("i"), IntLiteral(10)),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        input = """
            func Tung() {
                for index, value := range array[2] {return;}
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayCell(Id("array"),[IntLiteral(2)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_026(self):
        input = """
            const a = true + false - true;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_027(self):
        input = """
            const a = 1 && 2 || 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_028(self):
        input = """
            const a = 1 + 2 && 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_029(self):
        input = """
            const a = 1 - 2 % 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", IntLiteral(1), BinaryOp("%", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_030(self):
        input = """
            const a = 1 + -2 - 1;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(1), UnaryOp("-",IntLiteral(2))), IntLiteral(1)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_031(self):
        input = """
            const a = [1]ID{Tung{}};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1)],Id("ID"),[StructLiteral("Tung",[])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_032(self):
        input = """
            const a = [1][3]float{1.};
"""
        expect = Program([ConstDecl("a",None,ArrayLiteral([IntLiteral(1),IntLiteral(3)],FloatType(),[FloatLiteral(1.0)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_033(self):
        input = """
            const a = ID{a: 1, b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",IntLiteral(1)),("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_034(self):
        input = """
            const a = ID{a: [1]int{1}};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("a",ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_035(self):
        input = """
            const a = ID{b: true};
"""
        expect = Program([ConstDecl("a",None,StructLiteral("ID",[("b",BooleanLiteral(True))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_036(self):
        input = """
            const a = 0 && 1 && 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("&&", BinaryOp("&&", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_037(self):
        input = """
            const a = 0 || 1 || 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("||", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_038(self):
        input = """
            const a = 0 >= 1 <= 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("<=", BinaryOp(">=", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_039(self):
        input = """
            const a = 0 + 1 - 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("-", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_040(self):
        input = """
            const a = 0 * 1 / 2;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("/", BinaryOp("*", IntLiteral(0), IntLiteral(1)), IntLiteral(2)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_041(self):
        input = """
            const a = !-!2;
"""
        expect = Program([ConstDecl("a",None,UnaryOp("!",UnaryOp("-",UnaryOp("!",IntLiteral(2)))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_042(self):
        input = """
            const a = 1 && 2 || 3 >= 4 + 5 * -6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("||", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), BinaryOp(">=", IntLiteral(3), BinaryOp("+", IntLiteral(4), BinaryOp("*", IntLiteral(5), UnaryOp("-",IntLiteral(6)))))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_043(self):
        input = """
            const a = 1 > 2 < 3 >= 4 <=5 == 6;
"""
        expect = Program([ConstDecl("a",None,BinaryOp("==", BinaryOp("<=", BinaryOp(">=", BinaryOp("<", BinaryOp(">", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_044(self):
        input = """
            const a = 1 >= 2 + 3;
"""
        expect = Program([ConstDecl("a",None,BinaryOp(">=", IntLiteral(1), BinaryOp("+", IntLiteral(2), IntLiteral(3))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_045(self):
        input = """
            const a = a[1][2][3][4];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_046(self):
        input = """
            const a = a[1 + 2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_047(self):
        input = """
            const a = a.b.c.d.e;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_048(self):
        input = """
            const a = ID {}.a;
"""
        expect = Program([ConstDecl("a",None,FieldAccess(StructLiteral("ID",[]),"a"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_049(self):
        input = """
            const a = ID {}.a[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FieldAccess(StructLiteral("ID",[]),"a"),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_050(self):
        input = """
            const a = a.b().c().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(MethCall(MethCall(Id("a"),"b",[]),"c",[]),"d",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_051(self):
        input = """
            const a = a().d();
"""
        expect = Program([ConstDecl("a",None,MethCall(FuncCall("a",[]),"d",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_052(self):
        input = """
            const a = a[1].b.c()[2].d.e();
"""
        expect = Program([ConstDecl("a",None,MethCall(FieldAccess(ArrayCell(MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1)]),"b"),"c",[]),[IntLiteral(2)]),"d"),"e",[]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_053(self):
        input = """
            const a = a * (nil - "a");
"""
        expect = Program([ConstDecl("a",None,BinaryOp("*", Id("a"), BinaryOp("-", NilLiteral(), StringLiteral("a"))))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_054(self):
        input = """
            const a = f() + f(1 + 2, 3.);
"""
        expect = Program([ConstDecl("a",None,BinaryOp("+", FuncCall("f",[]), FuncCall("f",[BinaryOp("+", IntLiteral(1), IntLiteral(2)),FloatLiteral(3.0)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_055(self):
        input = """
            const a = function()[2];
"""
        expect = Program([ConstDecl("a",None,ArrayCell(FuncCall("function",[]),[IntLiteral(2)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_056(self):
        input = """
            const a = a;
"""
        expect = Program([ConstDecl("a",None,Id("a"))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_057(self):
        input = """
            var a Tung = 1.;
"""
        expect = Program([VarDecl("a",Id("Tung"),FloatLiteral(1.0))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_058(self):
        "thêm type array vào AST anh có thông bao trong nhóm task 3"
        input = """
            var a [2][3]int;
"""
        expect = Program([VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None)
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_059(self):
        input = """
            var a = 1;
"""
        expect = Program([VarDecl("a", None,IntLiteral(1))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_060(self):
        input = """
            type Tung struct {
                a int;
            }
"""
        expect = Program([StructType("Tung",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_061(self):
        input = """
            type Tung struct {
                a int;
            }
"""
        expect = Program([StructType("Tung",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_062(self):
        input = """
            type Tung struct {
                a  int;
                b  boolean;
                
            }
"""
        expect = Program([StructType("Tung",[("a",IntType()),("b",BoolType())],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_063(self):
        input = """
            type Tung struct {
                a  int;
                b  boolean;
                c  [2]Tung;
            }
"""
        expect = Program([StructType("Tung",[("a",IntType()),("b",BoolType()),("c",ArrayType([IntLiteral(2)],Id("Tung")))],[])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_064(self):
        input = """
            type Tung interface {
                Add() ;
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_065(self):
        input = """
            type Tung interface {
                Add(a int) ;
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_066(self):
        input = """
            type Tung interface {
                Add(a int, b int) ;
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_067(self):
        input = """
            type Tung interface {
                Add(a, c int, b int) ;
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[IntType(),IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_068(self):
        input = """
            type Tung interface {
                Add(a, c int, b int) [2]string;
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[IntType(),IntType(),IntType()],ArrayType([IntLiteral(2)],StringType()))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_069(self):
        input = """
            type Tung interface {
                Add() [2]string;
                Add() ID;
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[],ArrayType([IntLiteral(2)],StringType())),Prototype("Add",[],Id("ID"))])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_070(self):
        input = """
            type Tung interface {
                Add();
            }
"""
        expect = Program([InterfaceType("Tung",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_071(self):
        input = """
            func function() {return;}
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_072(self):
        input = """
            func function(a [2]ID) {return;}
"""
        expect = Program([FuncDecl("function",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_073(self):
        input = """
            func function(a int, b [1]int) {return;}
"""
        expect = Program([FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_074(self):
        input = """
            func function() [2]int {return;}
"""
        expect = Program([FuncDecl("function",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_075(self):
        input = """
            func (Cat c) function() {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("function",[],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_076(self):
        input = """
            func  (Cat c) function(a [2]ID) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("function",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_077(self):
        input = """
            func  (Cat c) function(a int, b [1]int) {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_078(self):
        input = """
            func  (Cat c) function() [2]int {return;}
"""
        expect = Program([MethodDecl("Cat",Id("c"),FuncDecl("function",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_079(self):
        input = """
            var a = 1;
            const b = 2;
            type a struct{a float;}
            type b interface {function();} 
            func function(){return;}
            func  (Cat c) function() [2]int {return;}
"""
        expect = Program([VarDecl("a", None,IntLiteral(1)),
			ConstDecl("b",None,IntLiteral(2)),
			StructType("a",[("a",FloatType())],[]),
			InterfaceType("b",[Prototype("function",[],VoidType())]),
			FuncDecl("function",[],VoidType(),Block([Return(None)])),
			MethodDecl("Cat",Id("c"),FuncDecl("function",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_080(self):
        input = """
            func function(a,b,c,d [ID][2][c] ID ){return;}
"""
        expect = Program([FuncDecl("function",[ParamDecl("a",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("b",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("c",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID"))),ParamDecl("d",ArrayType([Id("ID"),IntLiteral(2),Id("c")],Id("ID")))],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_081(self):
        input = """
            func function(){
                const a = 1.;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_082(self):
        input = """
            func function(){
                var a = 1.;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([VarDecl("a", None,FloatLiteral(1.0))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_083(self):
        input = """
            func function(){
                var a [1]int = 1;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([VarDecl("a",ArrayType([IntLiteral(1)],IntType()),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_084(self):
        input = """
            func function(){
                var a int;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([VarDecl("a",IntType(), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_085(self):
        input = """
            func function(){
                a += 1;
                a -= 1;
                a *= 1;
                a /= 1;
                a %= 1;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("*", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("/", Id("a"), IntLiteral(1))),Assign(Id("a"),BinaryOp("%", Id("a"), IntLiteral(1)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_086(self):
        input = """
            func function(){
                a[1 + 1] := 1;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(1))]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_087(self):
        input = """
            func function(){
                a[2].b.c[2] := 1;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"b"),"c"),[IntLiteral(2)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_088(self):
        input = """
            func function(){
                a["s"][function()] := a[2][2][3];
                a[2] := a[3][4];
                b.c.a[2] := b.c.a[2];
                b.c.a[2][3] := b.c.a[2][3];
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[StringLiteral("s"),FuncCall("function",[])]),ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2),IntLiteral(3)])),
            Assign(ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2)])),
            Assign(ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]),ArrayCell(FieldAccess(FieldAccess(Id("b"),"c"),"a"),[IntLiteral(2),IntLiteral(3)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_089(self):
        input = """
            func function(){
                a.b := 1;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Assign(FieldAccess(Id("a"),"b"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_090(self):
        input = """
            func function(){
                a.b[2].c := 1;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_091(self):
        input = """
            func function(){
                break;
                continue;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Break(),Continue()]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_092(self):
        input = """
            func function(){
                return;
                return function() + 2;
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Return(None),Return(BinaryOp("+", FuncCall("function",[]), IntLiteral(2)))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_093(self):
        input = """
            func function(){
                function();
                function(function(), 2);
                a.function();
                a[2].c.function(function(), 2);
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([FuncCall("function",[]),FuncCall("function",[FuncCall("function",[]),IntLiteral(2)]),MethCall(Id("a"),"function",[]),MethCall(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2)]),"c"),"function",[FuncCall("function",[]),IntLiteral(2)])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_094(self):
        input = """
            func function(){
                if(1) {return;}
                if(1 + 1) {
                    return 1;
                    return;
                }
            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), None),
            If(BinaryOp("+", IntLiteral(1), IntLiteral(1)), Block([Return(IntLiteral(1)),Return(None)]), None)]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_095(self):
        input = """
            func function(){
                if(1) { return;
                }else if(1) {
                    return 1;
                    return ;
                } else {return;}

                if(1) {return;
                }  else {
                    return 1;
                    return ;
                }

            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(None)]), 
                If(IntLiteral(1), Block([Return(IntLiteral(1)),Return(None)]), Block([Return(None)]))),
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(1)),Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_096(self):
        input = """
            func function(){
                if(1) {
                    return 1;
                }else if(2) {
                    return 2;
                } else if(3) {
                    return 3;
                } else if(4) {
                    return 4;
                } 

            } 
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            If(IntLiteral(1), Block([Return(IntLiteral(1))]), 
                If(IntLiteral(2), Block([Return(IntLiteral(2))]), 
                    If(IntLiteral(3), Block([Return(IntLiteral(3))]), 
                        If(IntLiteral(4), Block([Return(IntLiteral(4))]), None))))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_097(self):
        input = """
            func Tung() {
                for a.i[8] {
                    return;
                    return 1;
                }
                for i := 0; i[1] < 10; i *= 2+3  {
                    return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))])),ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", ArrayCell(Id("i"),[IntLiteral(1)]), IntLiteral(10)),Assign(Id("i"),BinaryOp("*", Id("i"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_098(self):
        input = """
            func Tung() {
                for index, value := range [2]int{1,2} {
                     return;
                    return 1;
                }
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_099(self):
        input = """
            func Tung() {
                a.b.c[2].d()
            }
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([MethCall(ArrayCell(FieldAccess(FieldAccess(Id("a"),"b"),"c"),[IntLiteral(2)]),"d",[])]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_100(self):
        input = """
            func Tung() {
                return [2] ID { {1}, {"2"}, {nil}, {struc{}} };
                return "THANKS YOU, PPL1 ";
            };
"""
        expect = Program([FuncDecl("Tung",[],VoidType(),Block([Return(ArrayLiteral([IntLiteral(2)],Id("ID"),[[IntLiteral(1)],[StringLiteral("2")],[NilLiteral()],[StructLiteral("struc",[])]])),Return(StringLiteral("THANKS YOU, PPL1 "))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_101(self):
        input = """const Tung = 1; """
        expect = Program([ConstDecl("Tung", None, IntLiteral(1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_102(self):
        """ chuyển đổi sang kiểu int hết """
        input = """const Tung = 0b11; """
        expect = Program([ConstDecl("Tung", None, IntLiteral(3))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_103(self):
        input = """const Tung = 0o70; """
        expect = Program([ConstDecl("Tung", None, IntLiteral(56))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_104(self):
        input = """const Tung = 0Xa1; """
        expect = Program([ConstDecl("Tung", None, IntLiteral(161))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_105(self):
        input = """const Tung = 01.e-1; """
        expect = Program([ConstDecl("Tung", None, FloatLiteral(0.1))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_106(self):
        """ đầu vào là giá trị True False chứ không phải string """
        input = """const Tung = true; """
        expect = Program([ConstDecl("Tung", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_107(self):
        input = """const Tung = false; """
        expect = Program([ConstDecl("Tung", None, BooleanLiteral(False))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_108(self):
        """ loại bỏ "" ở trước và sau string """
        input = """const Tung = "Tung"; """
        expect = Program([ConstDecl("Tung", None, StringLiteral("Tung"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_109(self):
        input = """const Tung = nil; """
        expect = Program([ConstDecl("Tung", None, NilLiteral())])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_110(self):
        input = """const Tung = STRUCT {}; """
        expect = Program([ConstDecl("Tung", None, StructLiteral("STRUCT",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_111(self):
        input = """const Tung = STRUCT {
            a : 1,
            b : false}; """
        expect = Program([ConstDecl("Tung", None, StructLiteral("STRUCT",[("a",IntLiteral(1)),("b",BooleanLiteral(False))]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_112(self):
        input = """const Tung = [ID] int {1}; """
        expect = Program([ConstDecl("Tung", None, ArrayLiteral([Id("ID")],IntType(),[IntLiteral(1)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_113(self):
        input = """const Tung = [1][2] int {1., STRUCT{}, nil}; """
        expect = Program([ConstDecl("Tung", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],IntType(),[FloatLiteral(1.0),StructLiteral("STRUCT",[]),NilLiteral()]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_114(self):
        input = """const Tung = [1][2] STRUCT {{1, {3}}, {2}}; """
        expect = Program([ConstDecl("Tung", None, ArrayLiteral([IntLiteral(1),IntLiteral(2)],Id("STRUCT"),[[IntLiteral(1), [IntLiteral(3)]],[IntLiteral(2)]]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_115(self):
        input = """const Tung = 1 || 2 || 3; """
        expect = Program([ConstDecl("Tung", None, BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_116(self):
        input = """const Tung = 1 && 2 && 3; """
        expect = Program([ConstDecl("Tung", None, BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_117(self):
        input = """const Tung = 1 >= 2 <= 3 > 4 < 5 == 6 != 7; """
        expect = Program([ConstDecl("Tung", None, BinaryOp("!=", BinaryOp("==", BinaryOp("<", BinaryOp(">", BinaryOp("<=", BinaryOp(">=", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
    
    def test_118(self):
        input = """const Tung = 1 + 2 - 3; """
        expect = Program([ConstDecl("Tung", None, BinaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_119(self):
        input = """const Tung = 1 * 2 / 3 % 4; """
        expect = Program([ConstDecl("Tung", None, BinaryOp("%", BinaryOp("/", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_120(self):
        input = """const Tung = ! - 1; """
        expect = Program([ConstDecl("Tung", None, UnaryOp("!",UnaryOp("-",IntLiteral(1))))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_121(self):
        input = """const Tung = a; """
        expect = Program([ConstDecl("Tung", None, Id("a"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_122(self):
        input = """const Tung = (1+2)*3; """
        expect = Program([ConstDecl("Tung", None, BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_123(self):
        input = """const Tung = function(); """
        expect = Program([ConstDecl("Tung", None, FuncCall("function",[]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_124(self):
        input = """const Tung = function(1, 2); """
        expect = Program([ConstDecl("Tung", None, FuncCall("function",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_125(self):
        input = """const Tung = a[2][3]; """
        expect = Program([ConstDecl("Tung",None,ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_126(self):
        input = """const Tung = a.b.c; """
        expect = Program([ConstDecl("Tung", None, FieldAccess(FieldAccess(Id("a"),"b"),"c"))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_127(self):
        input = """const Tung = a.b().c(1, 2); """
        expect = Program([ConstDecl("Tung", None, MethCall(MethCall(Id("a"),"b",[]),"c",[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_128(self):
        input = """const Tung = a.b[2].c.d(); """
        expect = Program([ConstDecl("Tung", None, MethCall(FieldAccess(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),"c"),"d",[]))])
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
    func function () {var a = 1;}
    func function () int {var a = 1;}
    func function () [2] ID {var a = 1;}
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("function",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("function",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_133(self):
        input = """
    func function (a int) {var a = 1;}
    func function (a int, b ID) {var a = 1;}
    func function (a, b int) {var a = 1;}
"""
        expect = Program([FuncDecl("function",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])),
			FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_133(self):
        input = """
    func (ID ID) function () {var a = 1;}
    func (ID ID) function () int {var a = 1;}
    func (ID ID) function () [2] ID {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("function",[],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("function",[],IntType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("function",[],ArrayType([IntLiteral(2)],Id("ID")),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_134(self):
        input = """
    func (ID ID) function (a int) {var a = 1;}
    func (ID ID) function (a int, b ID) {var a = 1;}
    func (ID ID) function (a, b int) {var a = 1;}
"""
        expect = Program([MethodDecl("ID",Id("ID"),FuncDecl("function",[ParamDecl("a",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",Id("ID"))],VoidType(),Block([VarDecl("a", None,IntLiteral(1))]))),
			MethodDecl("ID",Id("ID"),FuncDecl("function",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],VoidType(),Block([VarDecl("a", None,IntLiteral(1))])))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_135(self):
        input = """
        type INTERFACE interface {
            function();
            function() int;
            function() [2]ID;
            function(a int);
            function(a int, b int);
            function(a, b int);
        }
"""
        expect = Program([InterfaceType("INTERFACE",[
            Prototype("function",[],VoidType()),Prototype("function",[],IntType()),
            Prototype("function",[],ArrayType([IntLiteral(2)],Id("ID"))),
            Prototype("function",[IntType()],VoidType()),
            Prototype("function",[IntType(),IntType()],VoidType()),
            Prototype("function",[IntType(),IntType()],VoidType())])
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_136(self):
        input = """
    func function () {
        continue;
        break;
        return;
        return 1;
    }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Continue(),Break(),Return(None),Return(IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_137(self):
        input = """
    func function () {
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
        expect = Program([FuncDecl("function",[],VoidType(),Block([
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
    func function () {
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
        expect = Program([FuncDecl("function",[],VoidType(),Block([
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
    func function () {
        a := 1;
        a += 1;
        a -= 1;
        a *= 1;
        a /= 1;
        a %= 1;
    }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
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
    func function () {
        a[1] := 2;
        a[2][1+1] += 3;
        a.b -= 5;
        b.b[a + b].b.c[2] := 4;
    }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),IntLiteral(2)),
            Assign(ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]),BinaryOp("+", ArrayCell(Id("a"),[IntLiteral(2),BinaryOp("+", IntLiteral(1), IntLiteral(1))]), IntLiteral(3))),
            Assign(FieldAccess(Id("a"),"b"),BinaryOp("-", FieldAccess(Id("a"),"b"), IntLiteral(5))),
            Assign(ArrayCell(FieldAccess(FieldAccess(ArrayCell(FieldAccess(Id("b"),"b"),[BinaryOp("+", Id("a"), Id("b"))]),"b"),"c"),[IntLiteral(2)]),IntLiteral(4))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_141(self):
        input = """
    func function () {
        a();
        a(1, 2);
        a(1);
        b.a.a();
        b.a.a(1, 2);
        b.a.a(1);
    }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
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
        func function () {
            if (a) {return;}
            if (b) {return;} else {return;}
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            If(Id("a"),Block([Return(None)]), None),
            If(Id("b"),Block([Return(None)]),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_143(self):
        input = """
        func function () {
            for(1) {return;}
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([ForBasic(IntLiteral(1),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_144(self):
        input = """
        func function () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_145(self):
        input = """
        func function () {
            for a, b := range 2 {return;}
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([ForEach(Id("a"),Id("b"),IntLiteral(2),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_146(self):
        input = """
        func function () {
            for var a = 1; a < 10; a := 1 {return;}
            for a += 1; a < 10; a -= 1 {return;}
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),IntLiteral(1)),Block([Return(None)])),
            ForStep(Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),BinaryOp("<", Id("a"), IntLiteral(10)),Assign(Id("a"),BinaryOp("-", Id("a"), IntLiteral(1))),Block([Return(None)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_147(self):
        input = """
        func function () {
            if (1){return;} else if (2){return;} else if (3){return;} else {return;}
            if (1){return;} else if (2){return;} else if (3){return;}
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
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
        func function () {
            return a[2][3][4];
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([Return(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_149(self):
        input = """
        func function () {
            a.b[2][3][4] := 1;
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            Assign(ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),IntLiteral(1))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_150(self):
        input = """
        func function () {
            a[1*2][1+2] := a[1*2][1+2];
            a[1+2] := a[1+2];
        }
"""
        expect = Program([FuncDecl("function",[],VoidType(),Block([
            Assign(ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("*", IntLiteral(1), IntLiteral(2)),BinaryOp("+", IntLiteral(1), IntLiteral(2))])),
            Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]),ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))
		])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))