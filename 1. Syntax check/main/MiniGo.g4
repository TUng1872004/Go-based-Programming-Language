grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
from antlr4.Token import Token
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

def insertSemicolon(self):
    prev = self.preType
    #if(prev!=None):
        #print(self.symbolicNames[prev])
    if(prev==None):
        self.skip()
    elif(prev in [
            self.INT_LIT, self.ID, self.FLOAT_LIT, self.OCT_LIT, self.HEX_LIT,
            self.BI_LIT, self.STRING_LIT, self.RETURN, self.CONTINUE, self.BREAK,
            self.TRUE,self.FALSE, self.RCB, self.RP, self.RSB, self.NIL
        ]):
        self.text = ';'
    else:
        self.skip()

}



options{
	language = Python3;
}


//! ---------------- Parser ----------------------- */
program: stmtend? list_declared EOF;
declared_statement:
	(variables_declared
    | constants_declared
    | struct_declared
    | array_declared
	| function_declared
	| interface_declared
	| method_declared) ;
declared: declared_statement stmtend;
list_declared: declared list_declared | declared;

literal: primitive_literal | array_literal | struct_literal ;
primitive_literal: INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT | HEX_LIT | OCT_LIT | BI_LIT | NIL ;

array_literal: array_type LCB array RCB;
array: array_list CM array | array_list;
array_list: literal | LCB array RCB ;
array_type: array_dimension types_specifier;
struct_literal: ID CO expression stmtend? (CM struct_literal)? | ID LCB struct_literal? RCB ;

array_declared: (CONST | VAR) ID array_dimension types_specifier (ASSIGNINIT array_literal)?;
array_dimension: LSB expression  RSB array_dimension?;

number: INT_LIT | HEX_LIT | OCT_LIT | BI_LIT;
func_literal: ID LP para_list? RP;

variables_init: ASSIGNINIT expression;
variables_declared: VAR ID (types_specifier | variables_init | types_specifier variables_init) ;
constants_declared: CONST ID (types_specifier)? variables_init ;

struct_declared: TYPE ID STRUCT ignore? LCB stmtend? struct_field RCB;
struct_field: (ID types_specifier | struct_declared | function_declared | interface_declared) stmtend struct_field?;

interface_declared: TYPE ID INTERFACE ignore? LCB stmtend? interface_method RCB;
interface_method: ID LP para_declare? RP types_specifier? stmtend interface_method? ;

function_declared: FUNC ID LP (para_declare)? RP (types_specifier)? ignore? block_statement;
para_declare: list_identifiers types_specifier (CM para_declare)?;
para_list: expression6 types_specifier? (CM para_list)?;

method_declared: FUNC LP ID ID RP ID LP (para_declare)? RP (types_specifier)? ignore? block_statement;

list_identifiers: ID CM list_identifiers | ID;
types_specifier: basic_type | array_type | ID ;
basic_type: INT | BOOLEAN | FLOAT | STRING ;
list_statement: statement list_statement | statement;
statement:
	(
		declared_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	) stmtend;
assign_statement: nolit assign expression ;
return_statement: RETURN expression? ;
block_statement: LCB stmtend? list_statement? RCB;
if_statement: IF LP expression RP ignore? block_statement else_if  (ELSE ignore? block_statement)? ;
else_if: ELSE IF LP expression RP ignore? block_statement else_if |;
for_statement: (range_for | index_for); 
range_for: FOR ID CM ID ASSIGN RANGE expression6 ignore? block_statement ;
index_for: FOR (expression | (assign_statement |VAR ID types_specifier? ASSIGNINIT expression)  stmtend expression stmtend ID assign expression)  block_statement ;
break_statement: BREAK ;
continue_statement: CONTINUE ;
call_statement: expression6 LP list_expression? RP ;


list_expression: expression CM list_expression | expression;
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2:
    expression2 (EQ | NEQ | LT | LTE | GT | GTE) expression3
    | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4:
    expression4 (MUL | DIV | MOD) expression5
    | expression5;
expression5: (NOT | SUB) expression5 | expression6;
expression6:
    expression6 LCB expression? RCB
    |expression6 DOT ID
    | expression6 DOT funtion_call
    |expression6 array_dimension
    | expression7;
expression7:
    ID
    | literal
    | funtion_call
    | LP expression RP
    ;
funtion_call: ID LP list_expression? RP;

var_check: ID | funtion_call ;
nolit: nolit DOT var_check | nolit array_dimension| var_check;

assign: ASSIGN | E_DIV | E_MOD | E_ADD | E_SUB | E_MUL ;
stmtend: (NEWLINE|  SC) stmtend?;
ignore: NEWLINE ignore? ;
// ! ---------------- LEXER----------------------- */

//TODO Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string'  | 'str';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//TODO Operators 3.3.3 pdf
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
ASSIGNINIT: '=';
EXP:'**';
DOT:'.';
ASSIGN: ':=';

E_DIV: '/=';
E_MOD: '%=';
E_ADD: '+=';
E_SUB: '-=';
E_MUL: '*=';
NOT:'!';
OR:'||';
AND:'&&';


//TODO Separators 3.3.4 pdf
LSB: '[';
RSB: ']';
LP: '(';
RP: ')';
CM: ',';
LCB: '{';    
RCB: '}'; 
SC: ';'; 
CO:':';

//TODO Literals 3.3.5 pdf
INT_LIT: Int;
fragment Int: '0' | [1-9][0-9]*;
FLOAT_LIT: [0-9]+('.'[0-9]*)( [Ee] [+-]? [0-9]+) ?;
HEX_LIT: '0' [xX] ('_'? [0-9a-fA-F])+;
BI_LIT: '0' [Bb] ('_'? [0-1])+;
OCT_LIT: '0' [oO] ('_'? [0-7])+;
BOOL_LIT: (TRUE | FALSE);


ID: [a-zA-Z_][a-zA-Z0-9_]*;

STRING_LIT: '"' STR_CHAR* '"' 
//{    self.text = self.text[1:-1] } 
;
fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [rnt\\] | '\\"';
fragment ESC_ILLEGAL: [\r] | '\\' ~[rnt'\\];


COMMENT_LINE: '//' ~[\n]* -> skip;
 COMMENT : '/*' (COMMENT|.)*? '*/' -> skip;
    

//  AUTO_SEMI: '\r'? '\n'{self.text = ';' } ;
 NEWLINE: '\r'? '\n'
 {self.insertSemicolon()}
;

WS: [ \t\r\f\b]+ -> skip;

// COMMENT_LINE: '/*' ('/'*? COMMENT | ('/'* | '*'*) ~[/*])*? '*'*? '*/' -> skip;
// COMMENT: '/*' ( '/*' .*? '*/' | ~[*/] | '//' .*? NEWLINE)* '*/' -> skip;

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' (~[\n\\"] | '\\' [bfrnt"\\] )* (EOF | '\n') {
    if (len(self.text) >= 3 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[0:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};

ILLEGAL_ESCAPE
    : '"'STR_CHAR* ESC_ILLEGAL { raise IllegalEscape(self.text); }
    ;