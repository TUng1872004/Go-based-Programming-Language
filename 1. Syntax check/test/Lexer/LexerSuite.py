
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_vutung","_vutung,<EOF>", inspect.stack()[0].function))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.test("0x11","0x11,<EOF>", inspect.stack()[0].function))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "vutung \\r" ""","\"vutung \\r\",<EOF>", inspect.stack()[0].function))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("// vutung","<EOF>", inspect.stack()[0].function))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "vutung\n" ""","Unclosed string: \"vutung", inspect.stack()[0].function))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "vutung\\f" ""","Illegal escape in string: \"vutung\\f", inspect.stack()[0].function))
        
    def test_014(self):
        """Binary"""
        self.assertTrue(TestLexer.test("0b1001","0b1001,<EOF>", inspect.stack()[0].function))

    def test_015(self):
        """Octal"""
        self.assertTrue(TestLexer.test("0o107","0o107,<EOF>", inspect.stack()[0].function))
    def test_016(self):
        """More Binary"""
        self.assertTrue(TestLexer.test("0b00","0b00,<EOF>", inspect.stack()[0].function))    
    def test_017(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VuTUng\\f" ""","Illegal escape in string: \"VuTUng\\f", inspect.stack()[0].function))
    def test_018(self):
            """skip"""
            self.assertTrue(TestLexer.test(""" /*
            /* a */ /* b */ 
            // 321231
            */ if  /* */ /* */""", "if,<EOF>", inspect.stack()[0].function))
    def test_019(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "\\z" """, "Illegal escape in string: \"\\z", inspect.stack()[0].function))
    
    def test_020(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "123
        " """, "Unclosed string: \"123", inspect.stack()[0].function))
    
    def test_021(self):
        """NEWLINE WITH COMMENTS"""
        self.assertTrue(TestLexer.test(""" 
        /* a    * */
        """, "<EOF>", inspect.stack()[0].function))
    def test_022(self):
        """Esq"""
        self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))
    def test_023(self):
        """Error Octal_LIT"""
        self.assertTrue(TestLexer.test("0o0", "0o0,<EOF>", inspect.stack()[0].function))
    def test_024(self):
        """auto semi for nil"""
        self.assertTrue(TestLexer.test("""
            nil
""", "nil,;,<EOF>", inspect.stack()[0].function))
    def test_025(self):
        """skip"""
        self.assertTrue(TestLexer.test("""  /*
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", inspect.stack()[0].function))
    def test_026(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "\\" \\\\ \\q" """, "Illegal escape in string: \"\\\" \\\\ \\q", inspect.stack()[0].function))
    def test_027(self):
        """negative"""
        self.assertTrue(TestLexer.test("-1", "-,1,<EOF>", inspect.stack()[0].function))
    def test_028(self):
        """COMMENT"""
        self.assertTrue(TestLexer.test("""
                /* test
                */ a /* */
        """, "a,;,<EOF>", inspect.stack()[0].function))
    def test_029(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",inspect.stack()[0].function))
    
    def test_030(self):
        self.assertTrue(TestLexer.test("ab?sVN","ab,ErrorToken ?",inspect.stack()[0].function))

    def test_031(self):
        """test keyword var"""
        self.assertTrue(TestLexer.test("var abc int ;","var,abc,int,;,<EOF>",inspect.stack()[0].function))

    def test_032(self):
        """test keyword func"""
        self.assertTrue(TestLexer.test("""func abc ( ) ""","""func,abc,(,),<EOF>""",inspect.stack()[0].function))
    def test_033(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0452.", "0452.,<EOF>", inspect.stack()[0].function))
    def test_034(self):
        self.assertTrue(TestLexer.test("""
        if (a)
        {
        a:=  "Hello, " + p.name
        }  
""","if,(,a,),{,a,:=,\"Hello, \",+,p,.,name,;,},;,<EOF>", inspect.stack()[0].function))
    def test_035(self):
        """unclose string with backslash double quote"""
        self.assertTrue(TestLexer.test("\"string with backslash double quote", "Unclosed string: \"string with backslash double quote", inspect.stack()[0].function))
    def test_036(self):
        """1 or 2"""
        self.assertTrue(TestLexer.test("+=-=", "+=,-=,<EOF>", inspect.stack()[0].function))
    def test_037(self):
        """More 1 or 2"""
        self.assertTrue(TestLexer.test("*=/=%=:==", "*=,/=,%=,:=,=,<EOF>", inspect.stack()[0].function))
    def test_038(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("2.0e+0+10", "2.0e+0,+,10,<EOF>", inspect.stack()[0].function))

    def test_039(self):
        """new one"""
        self.assertTrue(TestLexer.test("0.", "0.,<EOF>", inspect.stack()[0].function))
    def test_040(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if else for func return", "if,else,for,func,return,<EOF>", inspect.stack()[0].function))

    def test_041(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("variableName anotherVar _privateVar", "variableName,anotherVar,_privateVar,<EOF>", inspect.stack()[0].function))

    def test_042(self):
        """Integer Literals"""
        self.assertTrue(TestLexer.test("012345678", "0,12345678,<EOF>", inspect.stack()[0].function))

    def test_043(self):
        """Float Literals"""
        self.assertTrue(TestLexer.test("0.5 3.14159 10.0", "0.5,3.14159,10.0,<EOF>", inspect.stack()[0].function))

    def test_044(self):
        """String Literals"""
        self.assertTrue(TestLexer.test('"hello" "world"', '\"hello\",\"world\",<EOF>', inspect.stack()[0].function))

    def test_045(self):
        """Boolean Literals"""
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", inspect.stack()[0].function))
    def test_046(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.test("""
            if
            }
            ]
            )
""", "if,},;,],;,),;,<EOF>", inspect.stack()[0].function))

    
    def test_047(self):
        """Delimiters"""
        self.assertTrue(TestLexer.test("( ) { } [ ] , ;", "(,),{,},[,],,,;,<EOF>", inspect.stack()[0].function))

    def test_048(self):
        """Illegal Character"""
        self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))
    def test_049(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test("\"Edge case \\t why", "Unclosed string: \"Edge case \\t why", inspect.stack()[0].function))
    def test_050(self):
        """3 or 2"""
        self.assertTrue(TestLexer.test("+ = -=", "+,=,-=,<EOF>", inspect.stack()[0].function))
    def test_051(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test("\"Invalid newline\n\"", "Unclosed string: \"Invalid newline", inspect.stack()[0].function))
    def test_052(self):
        """Binary or ID or wrong"""
        self.assertTrue(TestLexer.test("0y1010b1", "0,y1010b1,<EOF>", inspect.stack()[0].function))
    def test_053(self):
        """Unterminated String"""
        self.assertTrue(TestLexer.test('"unterminated string', "Unclosed string: \"unterminated string", inspect.stack()[0].function))
    def test_054(self):
        """If"""
        self.assertTrue(TestLexer.test('"unterminated string\'', "Unclosed string: \"unterminated string\'", inspect.stack()[0].function))    
    def test_055(self):
        """Binary Literal"""
        self.assertTrue(TestLexer.test("0b1010b1", "0b1010,b1,<EOF>", inspect.stack()[0].function))
    def test_056(self):
        """Weird Float"""
        self.assertTrue(TestLexer.test("1.23e-10 4.5E+6", "1.23e-10,4.5E+6,<EOF>", inspect.stack()[0].function))
    def test_057(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+ - * / % = == !=", "+,-,*,/,%,=,==,!=,<EOF>", inspect.stack()[0].function))

    def test_058(self):
        """INTEGER_LITERAL"""
        self.assertTrue(TestLexer.test("0x_1A", "0x_1A,<EOF>", inspect.stack()[0].function))  

    def test_059(self):
        """INTEGER_LITERAL"""
        self.assertTrue(TestLexer.test("0b102", "0b10,2,<EOF>", inspect.stack()[0].function)) 

    def test_060(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("1..2", "1.,.,2,<EOF>", inspect.stack()[0].function))  

    def test_061(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("1e", "1,e,<EOF>", inspect.stack()[0].function))  

    def test_062(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("2.0e+", "2.0,e,+,<EOF>", inspect.stack()[0].function))  

    def test_063(self):
        """Id not bool"""
        self.assertTrue(TestLexer.test("ID := False", "ID,:=,False,<EOF>", inspect.stack()[0].function))  

    def test_064(self):
        """NIL_LITERAL with typo"""
        self.assertTrue(TestLexer.test("nill", "nill,<EOF>", inspect.stack()[0].function)) 

    def test_065(self):
        """STRING_LITERAL with special escape"""
        self.assertTrue(TestLexer.test("\"Hello\\nWorld\"", "\"Hello\\nWorld\",<EOF>", inspect.stack()[0].function))
    def test_066(self):
        """SUPER LONG ONE-LINER TEST CASE"""
        self.assertTrue(TestLexer.test(
            """
            varXvarY123"Hello"truefalse"HEX:"0b1013.14e-10_Identifier_42;if(for)return/*comment*/:=+=-*/&&||
            """,
            "varXvarY123,\"Hello\",truefalse,\"HEX:\",0b101,3.14e-10,_Identifier_42,;,if,(,for,),return,:=,+=,-,*,/,&&,||,<EOF>", 
            inspect.stack()[0].function
        ))

    def test_067(self):
        """STRING_LITERAL with multiple escapes"""
        self.assertTrue(TestLexer.test("\"Tab\\tNewline\\nQuote\\\"\"", "\"Tab\\tNewline\\nQuote\\\"\",<EOF>", inspect.stack()[0].function))

    def test_068(self):
        """UNCLOSE_STRING with newlines"""
        self.assertTrue(TestLexer.test("\"Unclosed\nstring\"", "Unclosed string: \"Unclosed", inspect.stack()[0].function))

    def test_069(self):
        """STRING_LITERAL"""
        self.assertTrue(TestLexer.test("\"Backslash: \\\\\"", "\"Backslash: \\\\\",<EOF>", inspect.stack()[0].function))

    def test_070(self):
        """MIXED_LITERALS"""
        self.assertTrue(TestLexer.test("123 0xA 3.14 true false nil \"MiniGo Test\"", 
            "123,0xA,3.14,true,false,nil,\"MiniGo Test\",<EOF>", inspect.stack()[0].function))
    def test_071(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test("\"Will this catch this->", "Unclosed string: \"Will this catch this->", inspect.stack()[0].function))

    def test_072(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test("\"Illegal escape \\y\"", "Illegal escape in string: \"Illegal escape \\y", inspect.stack()[0].function))

    def test_073(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test("\"Unknown escape \\7\"", "Illegal escape in string: \"Unknown escape \\7", inspect.stack()[0].function))

    def test_074(self):
        """INTEGER_LITERAL"""
        self.assertTrue(TestLexer.test("0123", "0,123,<EOF>", inspect.stack()[0].function)) 

    def test_075(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("1.2.3", "1.2,.,3,<EOF>", inspect.stack()[0].function))  

    def test_076(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("3.14e-2", "3.14e-2,<EOF>", inspect.stack()[0].function))

    def test_077(self):
        """FLOAT_LITERAL"""
        self.assertTrue(TestLexer.test("1.e010", "1.e010,<EOF>", inspect.stack()[0].function))

    def test_078(self):
        """INVALID_HEX"""
        self.assertTrue(TestLexer.test("0xG123", "0,xG123,<EOF>", inspect.stack()[0].function))  # Invalid hex digit

    def test_079(self):
        """BOOLEAN_LITERAL"""
        self.assertTrue(TestLexer.test("TRUE", "TRUE,<EOF>", inspect.stack()[0].function))  # Should be lowercase

    def test_080(self):
        """BOOLEAN_LITERAL"""
        self.assertTrue(TestLexer.test("False", "False,<EOF>", inspect.stack()[0].function))  # Should be lowercase

    def test_081(self):
        """IDENTIFIER"""
        self.assertTrue(TestLexer.test("_validIdentifier123", "_validIdentifier123,<EOF>", inspect.stack()[0].function))

    def test_082(self):
        """INVALID_IDENTIFIER"""
        self.assertTrue(TestLexer.test("123abc", "123,abc,<EOF>", inspect.stack()[0].function))  # Identifiers can't start with a digit

    def test_083(self):
        """KEYWORD"""
        self.assertTrue(TestLexer.test("func", "func,<EOF>", inspect.stack()[0].function))

    def test_084(self):
        """KEYWORD"""
        self.assertTrue(TestLexer.test("return", "return,<EOF>", inspect.stack()[0].function))

    def test_085(self):
        """KEYWORD"""
        self.assertTrue(TestLexer.test("for", "for,<EOF>", inspect.stack()[0].function))

    def test_086(self):
        """KEYWORD"""
        self.assertTrue(TestLexer.test("if else", "if,else,<EOF>", inspect.stack()[0].function))

    def test_087(self):
        """KEYWORD"""
        self.assertTrue(TestLexer.test("break continue", "break,continue,<EOF>", inspect.stack()[0].function))

    def test_088(self):
        """MIXED"""
        self.assertTrue(TestLexer.test("var x = 10;", "var,x,=,10,;,<EOF>", inspect.stack()[0].function))

    def test_089(self):
        """MIXED"""
        self.assertTrue(TestLexer.test("type Person struct {}", "type,Person,struct,{,},<EOF>", inspect.stack()[0].function))

    def test_090(self):
        """MIXED"""
        self.assertTrue(TestLexer.test("arr := [3]int{1,2,3}", "arr,:=,[,3,],int,{,1,,,2,,,3,},<EOF>", inspect.stack()[0].function))

    def test_091(self):
        """MIXED"""
        self.assertTrue(TestLexer.test("x = 0b1101 + 0o77 * 0xA", "x,=,0b1101,+,0o77,*,0xA,<EOF>", inspect.stack()[0].function))
    def test_092(self):
        """WWeird FLOAT"""
        self.assertTrue(TestLexer.test("1.e12", "1.e12,<EOF>", inspect.stack()[0].function))

    def test_093(self):
        """EMPTY_STRING"""
        self.assertTrue(TestLexer.test("\"\"", "\"\",<EOF>", inspect.stack()[0].function))  

    def test_094(self):
        """MULTIPLE_SPACES"""
        self.assertTrue(TestLexer.test("      123     ", "123,<EOF>", inspect.stack()[0].function)) 

    def test_095(self):
        """NEWLINE_HANDLING"""
        self.assertTrue(TestLexer.test("x = 5\ny = 10", "x,=,5,;,y,=,10,<EOF>", inspect.stack()[0].function))  

    def test_096(self):
        """MULTIPLE_SPACES"""
        self.assertTrue(TestLexer.test("/*      123     ", "/,*,123,<EOF>", inspect.stack()[0].function)) 

    def test_097(self):
        """MULTILINE_STRING"""
        self.assertTrue(TestLexer.test("\"Unescaped newline in string\n\"", "Unclosed string: \"Unescaped newline in string", inspect.stack()[0].function))

    def test_098(self):
        """MULTILINE_COMMENT"""
        self.assertTrue(TestLexer.test("/* This is a \n multi-line \n comment */", "<EOF>", inspect.stack()[0].function))  

    def test_099(self):
        """INTEGER_LITERAL with invalid underscore placement"""
        self.assertTrue(TestLexer.test("1_000", "1,_000,<EOF>", inspect.stack()[0].function))  
    def test_100(self):
        """Error token in Comment"""
        self.assertTrue(TestLexer.test("/* @@@@@@ */ ", "<EOF>", inspect.stack()[0].function)) 
    def test_101(self):
            """Keywords"""
            self.assertTrue(TestLexer.test(""" 
            /* a * */
    """, "<EOF>", inspect.stack()[0].function))

    def test_102(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))
    def test_103(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", inspect.stack()[0].function))

    def test_104(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", inspect.stack()[0].function))

    def test_105(self):
        """Separators"""
        self.assertTrue(TestLexer.test("{}[](),;", "{,},[,],(,),,,;,<EOF>", inspect.stack()[0].function))

    def test_106(self):
        """skip"""
        self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

    def test_107(self):
        """skip"""
        self.assertTrue(TestLexer.test("// tesst //", "<EOF>", inspect.stack()[0].function))

    def test_108(self):
        """skip"""
        self.assertTrue(TestLexer.test("/**///", "<EOF>", inspect.stack()[0].function))

    def test_109(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("2_bA", "2,_bA,<EOF>", inspect.stack()[0].function))

    def test_110(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_", "_,<EOF>", inspect.stack()[0].function))

    def test_111(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("2b", "2,b,<EOF>", inspect.stack()[0].function))

    def test_112(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("-0120", "-,0,120,<EOF>", inspect.stack()[0].function))

    def test_113(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0b000", "0b000,<EOF>", inspect.stack()[0].function))

    def test_114(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0b1e", "0b1,e,<EOF>", inspect.stack()[0].function))

    def test_115(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("-0O72", "-,0O72,<EOF>", inspect.stack()[0].function))

    def test_116(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0xae2", "0xae2,<EOF>", inspect.stack()[0].function))

    def test_117(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))

    def test_118(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("1.2Ee2", "1.2,Ee2,<EOF>", inspect.stack()[0].function))

    def test_119(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("00.1e2", "00.1e2,<EOF>", inspect.stack()[0].function))

    def test_120(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "vutung" """, "\"vutung\",<EOF>", inspect.stack()[0].function))

    def test_121(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "\\r" """, "\"\\r\",<EOF>", inspect.stack()[0].function))

    def test_122(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", inspect.stack()[0].function))
    def test_123(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "&\\&" """, "Illegal escape in string: \"&\\&", inspect.stack()[0].function))
    
    def test_124(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.test("""
            true
""", "true,;,<EOF>", inspect.stack()[0].function))