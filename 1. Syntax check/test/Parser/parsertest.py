"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
from antlr4 import *
import unittest
import inspect
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
from MiniGoParser import MiniGoParser
from MiniGoLexer import MiniGoLexer

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)

NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg

class TestParser:
    _DIR = './test/'
    @staticmethod
    def makeSource(inputStr, inputfile):
        file = open(inputfile, "w")
        file.write(inputStr)
        file.close()
        return FileStream(inputfile)


    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestParser.makeSource(input, TestParser._DIR + 'input/' + str(num) + ".txt")
        TestParser.check(TestParser._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestParser._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect
        
    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = MiniGoLexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = MiniGoParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()


        








class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Tung = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Tung = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Tung = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Tung = [1.]ID{1, 3};","Error on line 1 col 14: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Tung = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Tung = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Tung = 1[2] + test()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Tung = ca.test(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Tung = a.a.test();","successful", inspect.stack()[0].function))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = test() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const Tung = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func Tung(x int, y int) int {return;}
            func Tung1() [2][3] ID {return;};        
            func Tung2() {return;}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) Tung(x int) int {return;};  
            func (c Calculator) Tung() ID {return;}      
            func (c Calculator) Tung(x int, y [2]Tung) {return;}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type Tung struct {
                Tung string ;
                Tung [1][3]Tung ;                     
            }                                                                     
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Tung struct {}                                                                       
        ""","Error on line 2 col 30: }", inspect.stack()[0].function))
    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type Tung interface {}                                                                       
        ""","Error on line 11 col 33: }", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func Tung() {
                var x int = test() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const Tung = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func Tung() {
                x  := test() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""    
            func Tung() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))
    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func Tung() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""    
            func Tung() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                test(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
       
    def test_022(self):
        """False array lit"""
        self.assertTrue(TestParser.test("""    
            var z Tung = a[2, 3];                         
        ""","Error on line 2 col 28: ,", inspect.stack()[0].function))
    def test_023(self):
        """Var array element"""
        self.assertTrue(TestParser.test("""    
            var z Tung = a[x];                         
        ""","successful", inspect.stack()[0].function))
    def test_024(self):
        """Var array element"""
        self.assertTrue(TestParser.test("""    
            var z Tung = a[Person{name: \"Alice\", age: 30}];                         
        ""","Error on line 2 col 33: {", inspect.stack()[0].function))
    def test_025(self):
        """Var array element"""
        self.assertTrue(TestParser.test("""    
            var z  = 123();                         
        ""","Error on line 2 col 24: (", inspect.stack()[0].function))
        
    def test_026(self):
        """Assign with operation"""
        self.assertTrue(TestParser.test("""    
            z += ADD();                         
        ""","successful", inspect.stack()[0].function))
    def test_027(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Add() {
            const a = a[2].b
            var a = a[2].b; var a = "s";           
        };""","successful", inspect.stack()[0].function))
    def test_028(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        if (x.test().b[2])
                                        {
                                            if (){}
                                        } 
                                    }""","Error on line 5 col 48: )", inspect.stack()[0].function)) 
    def test_029(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Person struct{Tung str};  ""","Error on line 2 col 39: }", inspect.stack()[0].function))
        
    def test_030(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))
        
    def test_031(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a[2][3].test(2 + 3, a {a:2})
                                    };""","successful", inspect.stack()[0].function))
    def test_032(self):
        """statement with array"""
        self.assertTrue(TestParser.test("""    
            z.c.test()[1][x] := [3]int{1,2,3,4,5} ;                        
        ""","successful", inspect.stack()[0].function))
    def test_033(self):
        """Struct with newline"""
        self.assertTrue(TestParser.test("""    
            type Male struct
            {Tung int;};                         
        ""","successful", inspect.stack()[0].function)) 
    def test_034(self):
        """Negative"""
        self.assertTrue(TestParser.test("""    
            z := -1;                    
        ""","successful", inspect.stack()[0].function)) 
    def test_035(self):
        """Simple program: Vuid main() {} """
        input = """func main() {var anything int;};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,inspect.stack()[0].function))

    def test_036(self):
        """More complex program"""
        input = """func test () {var anything int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,inspect.stack()[0].function))
    
    def test_037(self):
        input = """var int;"""
        expect = "Error on line 1 col 4: int"
        self.assertTrue(TestParser.test(input,expect,inspect.stack()[0].function))
    def test_038(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", inspect.stack()[0].function))
        
    def test_039(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Add() {
                                        }
""","Error on line 3 col 40: }", inspect.stack()[0].function))
    def test_040(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func Greet() string {
                return "Hello, " + p.name
            }
            c c
            func Add(x, y int, b float) {return ;}  
            value int;                            
        }      
""","successful", inspect.stack()[0].function))
    def test_041(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func Greet() string {
                return "Hello, " + p.name
            }; c c;
            func Greet() string {
                return "Hello, " + p.name
            } c c;                                                    
        }      
""","Error on line 8 col 14: c", inspect.stack()[0].function))
    def test_042(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {return ;}
""","successful", inspect.stack()[0].function))
    def test_043(self):
        input='func Tung(){return ab}'
        expected = "Error on line 1 col 21: }"
        self.assertTrue(TestParser.test(input,expected , inspect.stack()[0].function))

    def test_044(self):
        """Cannot conclude type"""
        input="var a;"
        expected = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.test(input,expected , inspect.stack()[0].function))
    def test_045(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", inspect.stack()[0].function))
    def test_046(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{1+1}                    
""","Error on line 1 col 18: +", inspect.stack()[0].function))
        
    def test_047(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1} , ID{} , {{ID{}}}}                    
""","successful", inspect.stack()[0].function))
        
    def test_048(self):
        self.assertTrue(TestParser.test("""
        type Person struct 
            {
            func Greet() string 
                {
                    if (a);{
                    a := "Hello, " + p.name
                    }
                }                           
        }      
""","Error on line 6 col 26: ;", inspect.stack()[0].function))
    def test_049(self):
        self.assertTrue(TestParser.test("""
        if (a)
        {
        a:=  "Hello, " + p.name
        }  
""","successful", inspect.stack()[0].function))
    def test_050(self):
        self.assertTrue(TestParser.test("""
        a :=nil-
""","Error on line 3 col 0: <EOF>", inspect.stack()[0].function))
    def test_051(self):
        self.assertTrue(TestParser.test("""
        a :=nil-
a;""","successful", inspect.stack()[0].function))
    def test_052(self):
        """ASSIGNMENT_STATEMENT"""
        self.assertTrue(TestParser.test("x := 5;", "successful", inspect.stack()[0].function))

    def test_053(self):
        """ASSIGNMENT_STATEMENT with expression"""
        self.assertTrue(TestParser.test("x := a + 10 * (b - 3);", "successful", inspect.stack()[0].function))

    def test_054(self):
        """ASSIGNMENT_STATEMENT with multiple variables"""
        self.assertTrue(TestParser.test("a, b, c := 123;", "successful", inspect.stack()[0].function))

    def test_055(self):
        """IF_STATEMENT simple"""
        self.assertTrue(TestParser.test("if (x > 0) { y := x; };", "successful", inspect.stack()[0].function))

    def test_056(self):
        """IF_ELSE_STATEMENT"""
        self.assertTrue(TestParser.test("if (x > 0) { y := x; } else { y := -x; };", "successful", inspect.stack()[0].function))

    def test_057(self):
        """IF_ELSE_IF_STATEMENT"""
        self.assertTrue(TestParser.test("if (x > 0) { y := 1; } else if (x < 0) { y := -1; } else { y := 0; };", "successful", inspect.stack()[0].function))

    def test_058(self):
        """IF_STATEMENT missing braces"""
        self.assertTrue(TestParser.test("if x > 0 y := 5;", "Error on line 1 col 3: x", inspect.stack()[0].function))

    def test_059(self):
        """FOR_LOOP basic"""
        self.assertTrue(TestParser.test("for i := 0; i < 10; i += 1 { sum := sum + i; };", "successful", inspect.stack()[0].function))

    def test_060(self):
        """FOR_LOOP without initialization"""
        self.assertTrue(TestParser.test("for i :=1; i < 10; i += 1 { sum := sum + i; };", "successful", inspect.stack()[0].function))

    def test_061(self):
        """FOR_LOOP with range"""
        self.assertTrue(TestParser.test("for index, value := range arr { sum := sum + value; };", "successful", inspect.stack()[0].function))

    def test_062(self):
        """FOR_LOOP missing condition"""
        self.assertTrue(TestParser.test("for i := 0; i<0; i += 1 { sum := sum + i; };", "successful", inspect.stack()[0].function))

    def test_063(self):
        """BREAK_STATEMENT inside loop"""
        self.assertTrue(TestParser.test("for i := 0; i < 10; i += 1 { if (i == 5) { break; }; };", "successful", inspect.stack()[0].function))

    def test_064(self):
        """CONTINUE_STATEMENT inside loop"""
        self.assertTrue(TestParser.test("for i := 0; i < 10; i += 1 { if(i % 2 == 0) { continue; }; };", "successful", inspect.stack()[0].function))

    def test_065(self):
        """RETURN_STATEMENT in function"""
        self.assertTrue(TestParser.test("func add(x int, y int) int { return x + y; };", "successful", inspect.stack()[0].function))

    def test_066(self):
        """RETURN_STATEMENT without value"""
        self.assertTrue(TestParser.test("func doNothing() { return; };", "successful", inspect.stack()[0].function))

    def test_067(self):
        """CALL_STATEMENT standalone"""
        self.assertTrue(TestParser.test("print(x);", "successful", inspect.stack()[0].function))

    def test_068(self):
        """CALL_STATEMENT inside assignment"""
        self.assertTrue(TestParser.test("result := compute(x, y);", "successful", inspect.stack()[0].function))

    def test_069(self):
        """Let's see"""
        self.assertTrue(TestParser.test("true :=false;", "Error on line 1 col 5: :=", inspect.stack()[0].function))

    def test_070(self):
        """MISSING_SEMICOLON"""
        self.assertTrue(TestParser.test("x := 5 y := 10;", "Error on line 1 col 7: y", inspect.stack()[0].function))
    def test_071(self):
        """Let's see"""
        self.assertTrue(TestParser.test("True.False.test().c[2][3] :=3.14;", "successful", inspect.stack()[0].function))
    def test_072(self):
        """VARIABLE DECLARATION with initialization"""
        self.assertTrue(TestParser.test("var y float = 3.14;", "successful", inspect.stack()[0].function))

    def test_073(self):
        """MULTIPLE VARIABLE DECLARATIONS"""
        self.assertTrue(TestParser.test("var a, b, c int;", "successful", inspect.stack()[0].function))

    def test_074(self):
        """CONSTANT DECLARATION"""
        self.assertTrue(TestParser.test("const PI = 3.14159;", "successful", inspect.stack()[0].function))

    def test_075(self):
        """ASSIGNMENT STATEMENT"""
        self.assertTrue(TestParser.test("x := 42;", "successful", inspect.stack()[0].function))

    def test_076(self):
        """ASSIGNMENT WITH EXPRESSION"""
        self.assertTrue(TestParser.test("result *= a + b * c;", "successful", inspect.stack()[0].function))

    def test_077(self):
        """IF STATEMENT"""
        self.assertTrue(TestParser.test("if (x > 0) { y := x; };", "successful", inspect.stack()[0].function))

    def test_078(self):
        """IF-ELSE STATEMENT"""
        self.assertTrue(TestParser.test("if (x > 0) { y := x; } else { y := -x; };", "successful", inspect.stack()[0].function))

    def test_079(self):
        """IF-ELSE IF STATEMENT"""
        self.assertTrue(TestParser.test("if (x > 0) { y := 1; } else if (x < 0) { y := -1; } else { y := 0; };", "successful", inspect.stack()[0].function))

    def test_080(self):
        """FOR LOOP with initialization, condition, update"""
        self.assertTrue(TestParser.test("for i := 0; i < 10; i += 1 { sum := sum + i; };", "successful", inspect.stack()[0].function))

    def test_081(self):
        """FOR LOOP with range"""
        self.assertTrue(TestParser.test("for index, value := range arr { sum := sum + value; };", "successful", inspect.stack()[0].function))

    def test_082(self):
        """FOR LOOP condition"""
        self.assertTrue(TestParser.test("for i<6 { print(\"infinite loop\"); };", "successful", inspect.stack()[0].function))
    def test_083(self):
        """Dunno"""
        self.assertTrue(TestParser.test(" x := [3]int{1,2,3};  ;", "successful", inspect.stack()[0].function))
    def test_084(self):
        self.assertTrue(TestParser.test("var x int;", "successful", inspect.stack()[0].function))

    def test_085(self):
        self.assertTrue(TestParser.test("x := 10;", "successful", inspect.stack()[0].function))
    def test_086(self):
        """RETURN STATEMENT"""
        self.assertTrue(TestParser.test("func add(x int, y int) int { return x + y; };", "successful", inspect.stack()[0].function))

    def test_087(self):
        """RETURN WITHOUT VALUE"""
        self.assertTrue(TestParser.test("func doNothing() { return; };", "successful", inspect.stack()[0].function))


    def test_088(self):
        """FUNCTION CALL STATEMENT"""
        self.assertTrue(TestParser.test("print(\"Hello, MiniGo\");", "successful", inspect.stack()[0].function))

    def test_089(self):
        """FUNCTION CALL INSIDE EXPRESSION"""
        self.assertTrue(TestParser.test("result := compute(x, y) + 10;", "successful", inspect.stack()[0].function))

    def test_090(self):
        """STRUCT DECLARATION"""
        self.assertTrue(TestParser.test("type Person struct { name string; age int; };", "successful", inspect.stack()[0].function))

    def test_091(self):
        """STRUCT INITIALIZATION"""
        self.assertTrue(TestParser.test("p := Person{name: \"Alice\", age: 25};", "successful", inspect.stack()[0].function))

    def test_092(self):
        """ARRAY DECLARATION"""
        self.assertTrue(TestParser.test("var arr [5]int;", "successful", inspect.stack()[0].function))

    def test_093(self):
        """ARRAY ASSIGNMENT"""
        self.assertTrue(TestParser.test("arr[2] := 42;", "successful", inspect.stack()[0].function))

    def test_094(self):
        """INTERFACE DECLARATION"""
        self.assertTrue(TestParser.test("type Animal interface { Speak() string; };", "successful", inspect.stack()[0].function))

    def test_095(self):
        """METHOD DECLARATION INSIDE STRUCT"""
        self.assertTrue(TestParser.test("func (p Person) Greet() string { return \"Hello, \" + p.name; };", "successful", inspect.stack()[0].function))

    def test_096(self):
        """LOGICAL EXPRESSION IN IF"""
        self.assertTrue(TestParser.test("if (x > 0 && y < 100 || z == 50) { a := 10; };", "successful", inspect.stack()[0].function))

    def test_097(self):
        """NESTED IF-ELSE"""
        self.assertTrue(TestParser.test("if (x > 0) { if (y < 5) { z := 1; } else { z := 2; }; };", "successful", inspect.stack()[0].function))

    def test_098(self):
        """MULTIPLE STATEMENTS IN A ROW"""
        self.assertTrue(TestParser.test("a := 10; b := a * 2; c := b - 5; print(c);", "successful", inspect.stack()[0].function))

    def test_099(self):
        """UNEXPECTED SEMICOLON"""
        self.assertTrue(TestParser.test("x := 10;;", "successful", inspect.stack()[0].function)) 
 
    def test_100(self):
        """FUNCTION CALL String"""
        self.assertTrue(TestParser.test("print(\"Hello, MiniGo\");", "successful", inspect.stack()[0].function))
    def test_101(self):
        """STATEMENT RANGE FOR"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for index, value := range arrrr {
                                            print(value);
                                        }
                                    };""","successful", inspect.stack()[0].function))
    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
            func Add() {
                for var i [2] int = 0; test().a.b(); i[3] := 1 {
                    return;
                }
            };
            """, "Error on line 3 col 54: [", inspect.stack()[0].function))
    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        a.test() += 2;
                                    };""","Error on line 3 col 49: +=", inspect.stack()[0].function))
    def test_104(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {return ;}
""","successful", inspect.stack()[0].function))
    def test_105(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", inspect.stack()[0].function))
    def test_106(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a [0b10]int ={1,2}                   
""","successful", inspect.stack()[0].function))
    def test_107(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a [test()[2][2]]int ={1,2}                   
""","successful", inspect.stack()[0].function))
    def test_108(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = ID {};                         
        ""","successful", inspect.stack()[0].function))
    def test_109(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = 1[2];                         
        ""","successful", inspect.stack()[0].function))
    def test_110(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = [true]int{1};                         
        ""","Error on line 2 col 28: true", inspect.stack()[0].function))
    def test_111(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        ""","successful", inspect.stack()[0].function))
    def test_112(self):
        """And OR"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = 1 && 2 && 3 || 1 || 1;                         
        ""","successful", inspect.stack()[0].function))
    def test_113(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        ""","successful", inspect.stack()[0].function))
    def test_114(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = a.b.a.c.e.g;                         
        ""","successful", inspect.stack()[0].function))

    def test_115(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = a[2][3][a + 2];                         
        ""","successful", inspect.stack()[0].function))

    def test_116(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = a.a.a[2].foo(1);                         
        ""","successful", inspect.stack()[0].function))

    def test_117(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = foo().a[2].goo();                         
        ""","successful", inspect.stack()[0].function))

    def test_118(self):
        """Expressions"""
        self.assertTrue(TestParser.test("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        ""","successful", inspect.stack()[0].function))

    def test_119(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var c [2][3]ID
        ""","successful", inspect.stack()[0].function))

    def test_120(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            const a =;
        ""","Error on line 2 col 21: ;", inspect.stack()[0].function))

    def test_121(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add(x int, y [2]int) [2]id {return ;}
        ""","successful", inspect.stack()[0].function))

    def test_122(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            func Add() {return ;}
        ""","successful", inspect.stack()[0].function))

    def test_123(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
        ""","successful", inspect.stack()[0].function))

    def test_124(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator struct {
                a int = 2;       
            }
        ""","Error on line 3 col 22: =", inspect.stack()[0].function))

    def test_125(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = a[b.c.d.e.f]
        ""","successful", inspect.stack()[0].function))

    def test_126(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator interface {Reset()}
        ""","Error on line 2 col 46: }", inspect.stack()[0].function))

    def test_127(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            type Calculator {
                Add(x int,c,d ID)}
        ""","Error on line 2 col 28: {", inspect.stack()[0].function))
    def test_128(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = "hello".6
        ""","Error on line 2 col 34: .", inspect.stack()[0].function))
    def test_129(self):
        """Declared"""
        self.assertTrue(TestParser.test("""    
            var z Vutung = Tung.6
        ""","Error on line 2 col 32: 6", inspect.stack()[0].function))
