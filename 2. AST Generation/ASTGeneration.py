from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce


class ASTGeneration(MiniGoVisitor):
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        # print(dir(ctx))  # Lists available attributes/methods of ctx
        # print(list(i.getText() for i in ctx.getChildren()))  # Gets text of all children
        # print(ctx.parser.ruleNames[ctx.getChild(0).getRuleIndex()])  # Gets rule name
        r=Program(self.visit(ctx.list_declared()))
        return r


    '''declared_statement:
	(variables_declared
    | constants_declared
    | struct_declared
    | array_declared
	| function_declared
	| interface_declared
	| method_declared) ;'''
    def visitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
            if ctx.variables_declared():
                return self.visit(ctx.variables_declared())
            elif ctx.constants_declared():
                r = self.visit(ctx.constants_declared())
                return r
            elif ctx.struct_declared():
                return self.visit(ctx.struct_declared())
            elif ctx.array_declared():
                return self.visit(ctx.array_declared())
            elif ctx.function_declared():
                return self.visit(ctx.function_declared())
            elif ctx.interface_declared():
                return self.visit(ctx.interface_declared())
            elif ctx.method_declared():
                return self.visit(ctx.method_declared())


    # declared: declared_statement stmtend;
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
            result = self.visit(ctx.declared_statement())
            return result

    # list_declared: declared list_declared | declared;
    def visitList_declared(self, ctx:MiniGoParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        result = [self.visit(ctx.declared())]
        return result

    # literal: primitive_literal | array_literal |struct_literal
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.primitive_literal():
            return self.visit(ctx.primitive_literal())
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())

    # primitive_literal: INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT | HEX_LIT | OCT_LIT | BI_LIT | NIL ;
    def visitPrimitive_literal(self, ctx:MiniGoParser.Primitive_literalContext):

        if ctx.INT_LIT():
            r= IntLiteral(int(ctx.INT_LIT().getText()))
            return r
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.HEX_LIT():
            return IntLiteral(int(ctx.HEX_LIT().getText(), 16))
        elif ctx.OCT_LIT():
            return IntLiteral(int(ctx.OCT_LIT().getText(), 8))
        elif ctx.BI_LIT():
            return IntLiteral(int(ctx.BI_LIT().getText(), 2))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()

    '''
    array_literal: array_type LCB array RCB;
    array_type: array_dimension types_specifier;
    '''
    def visitArray_literal(self, ctx: MiniGoParser.Array_literalContext):

        # Extract array type components
        eleType = self.visit(ctx.array_type().types_specifier())  
        dimens = self.visit(ctx.array_type().array_dimension())  

        value = self.visit(ctx.array()) 
        return ArrayLiteral(dimens, eleType, value)

    # array: array_list CM array | array_list;
    def visitArray(self, ctx: MiniGoParser.ArrayContext):
        if ctx.array(): 
            return [self.visit(ctx.array_list())] + self.visit(ctx.array())   
        else:  
            return [self.visit(ctx.array_list())]



    # array_list: literal | LCB array RCB ;
    def visitArray_list(self, ctx: MiniGoParser.Array_listContext):
        if ctx.literal():  
            return self.visit(ctx.literal())
        elif ctx.LCB():  
            return self.visit(ctx.array())  

    # array_type: array_dimension types_specifier;
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        dimens = self.visit(ctx.array_dimension())
        eleTyp = self.visit(ctx.types_specifier())
        return ArrayType(dimens,eleTyp)

    # struct_literal: ID CO expression stmtend? (CM struct_literal)? | ID LCB struct_literal? RCB ;
    def visitStruct_literal(self, ctx: MiniGoParser.Struct_literalContext):
        if ctx.LCB():
            return StructLiteral(ctx.ID().getText(),self.visit(ctx.struct_literal()) if ctx.struct_literal() else [])
        field_name = ctx.ID().getText()
        field_value = self.visit(ctx.expression())  

        if ctx.struct_literal():
            return [(field_name,field_value)]+ self.visit(ctx.struct_literal())
        return [(field_name,field_value)]



    # Visit a parse tree produced by MiniGoParser#array_declared.
    def visitArray_declared(self, ctx:MiniGoParser.Array_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_dimension.
    def visitArray_dimension(self, ctx:MiniGoParser.Array_dimensionContext):
        if(ctx.array_dimension()):
            return [self.visit(ctx.expression())] + self.visit(ctx.array_dimension())
        return [self.visit(ctx.expression())]


    # Visit a parse tree produced by MiniGoParser#number.
    def visitNumber(self, ctx:MiniGoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variables_init.
    def visitVariables_init(self, ctx:MiniGoParser.Variables_initContext):
        return self.visit(ctx.expression())


    # VAR ID (types_specifier | variables_init | types_specifier variables_init) ;
    def visitVariables_declared(self, ctx:MiniGoParser.Variables_declaredContext):
        Vtype = self.visit(ctx.types_specifier()) if ctx.types_specifier() else None
        varInit = self.visit(ctx.variables_init()) if ctx.variables_init() else None
        return VarDecl(ctx.ID().getText(),Vtype, varInit)

    # Visit a parse tree produced by MiniGoParser#list_identifier.

    # Visit a parse tree produced by MiniGoParser#constants_declared.
    def visitConstants_declared(self, ctx:MiniGoParser.Constants_declaredContext):
        expression = self.visit(ctx.variables_init())
        ID = ctx.ID().getText()
        type = self.visit(ctx.types_specifier()) if ctx.types_specifier() else None
        return ConstDecl(str(ID), type, expression) 


    # TYPE ID STRUCT ignore? LCB stmtend? struct_field RCB;
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        elements, methods = self.visit(ctx.struct_field())
        return StructType(ctx.ID().getText(),elements,methods)

    # struct_field: (ID types_specifier | struct_declared | function_declared | interface_declared) stmtend struct_field?;
    def visitStruct_field(self, ctx: MiniGoParser.Struct_fieldContext):
        elements = []
        methods = []


        if ctx.ID() and ctx.types_specifier():  
            field_name = ctx.ID().getText()
            field_type = self.visit(ctx.types_specifier())
            elements.append((field_name, field_type))

        elif ctx.function_declared():  
            methods.append(self.visit(ctx.function_declared()))

        elif ctx.struct_declared(): 
            self.visit(ctx.struct_declared())  

        if ctx.struct_field():
            next_elements, next_methods = self.visit(ctx.struct_field())
            elements.extend(next_elements)
            methods.extend(next_methods)

        return elements, methods  



    # interface_declared: TYPE ID INTERFACE ignore? LCB stmtend? interface_method RCB;
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        method  = self.visit(ctx.interface_method())
        return InterfaceType(ctx.ID().getText(),method)

    # func_literal: ID LP para_list? RP;
    def visitFunc_literal(self, ctx:MiniGoParser.Func_literalContext):
        name = ctx.ID().getText()
        para = self.visit(ctx.para_list()) if ctx.para_list() else []
        
        return (name, para)
    
    # interface_method: ID LP para_declare? RP types_specifier? stmtend interface_method? ;
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        name= ctx.ID().getText()
        para = self.visit(ctx.para_declare()) if ctx.para_declare() else []
        para = [param.parType for param in para]
        retType = self.visit(ctx.types_specifier()) if ctx.types_specifier() else VoidType()
        if ctx.interface_method():
            return [Prototype(name,para,retType)] + self.visit(ctx.interface_method())
        return [Prototype(name,para,retType)]


    # function_declared: FUNC ID LP (para_declare)? RP (types_specifier)? ignore? block_statement;
    def visitFunction_declared(self, ctx:MiniGoParser.Function_declaredContext):
        para = self.visit(ctx.para_declare()) if ctx.para_declare() else []
        retType = self.visit(ctx.types_specifier()) if ctx.types_specifier() else VoidType()
        block = self.visit(ctx.block_statement())
        return FuncDecl(ctx.ID().getText(),para,retType,block)


    # list_identifiers: ID CM list_identifiers | ID;
    def visitList_identifiers(self, ctx:MiniGoParser.List_identifiersContext):
        if ctx.list_identifiers():
            return [ctx.ID().getText()] + self.visit(ctx.list_identifiers())
        return [ctx.ID().getText()]
        

    # para_declare: list_identifiers types_specifier (CM para_declare)?;   Weird P_declare
    def visitPara_declare(self, ctx:MiniGoParser.Para_declareContext):
        # print("tada:", ctx.list_identifiers().getText()) if ctx.list_identifiers() else print("Fuck")
        if ctx.para_declare():
            return [ParamDecl(id,self.visit(ctx.types_specifier())) for id in self.visit(ctx.list_identifiers())] + self.visit(ctx.para_declare())
        return [ParamDecl(id,self.visit(ctx.types_specifier())) for id in self.visit(ctx.list_identifiers())]


    # para_list: expression6 types_specifier? (CM para_list)?;
    def visitPara_list(self, ctx:MiniGoParser.Para_listContext):
        if ctx.para_list():
            return [ParamDecl(ctx.expression6().getText(),self.visit(ctx.types_specifier()) if ctx.types_specifier() else VoidType())] + self.visit(ctx.para_list())
        return [ParamDecl(ctx.expression6().getText(),self.visit(ctx.types_specifier()))]



    # method_declared: FUNC LP ID ID RP ID LP (para_declare)? RP (types_specifier)? ignore? block_statement;
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        rec = ctx.ID(0).getText()
        T = Id(ctx.ID(1).getText())
        funname = ctx.ID(2).getText()
        reTyp = self.visit(ctx.types_specifier()) if ctx.types_specifier() else VoidType()
        block = self.visit(ctx.block_statement())
        para = self.visit(ctx.para_declare()) if ctx.para_declare() else []
        return MethodDecl(rec,T,FuncDecl(funname,para,reTyp,block))


    # list_expression: expression CM list_expression | expression;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())
        return [self.visit(ctx.expression())]


    # Visit a parse tree produced by MiniGoParser#types_specifier.
    def visitTypes_specifier(self, ctx:MiniGoParser.Types_specifierContext):
        if ctx.basic_type():
            return self.visit(ctx.basic_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        elif ctx.ID():
            return Id(ctx.ID().getText())


    # basic_type: INT | BOOLEAN | FLOAT | STRING ;
    def visitBasic_type(self, ctx:MiniGoParser.Basic_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()

    # list_statement: statement list_statement | statement;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        return [self.visit(ctx.statement())]


    '''statement:
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
    '''
    def visitStatement(self, ctx: MiniGoParser.StatementContext):
        if ctx.declared_statement():
            return self.visit(ctx.declared_statement())  
        elif ctx.assign_statement():
            return self.visit(ctx.assign_statement()) 
        elif ctx.if_statement():
            return self.visit(ctx.if_statement()) 
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())  
        elif ctx.break_statement():
            return self.visit(ctx.break_statement()) 
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())  
        elif ctx.call_statement():
            return self.visit(ctx.call_statement()) 
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())  
        else:
            raise Exception(f"What on Earth is this? {ctx.getText()}")  # Debugging



    # assign_statement: nolit assign expression ;
    def visitAssign_statement(self, ctx: MiniGoParser.Assign_statementContext):

        lhs = self.visit(ctx.nolit())
        if isinstance(lhs, str):
            lhs = Id(lhs) 
        rhs = self.visit(ctx.expression())

        assign_op = ctx.assign().getText() if ctx.assign() else "="

        if assign_op in ["+=", "-=", "*=", "/=", "%="]:
            op = assign_op[0]
            rhs = BinaryOp(op, lhs, rhs)

        return Assign(lhs, rhs)


    # return_statement: RETURN expression? ;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)


    # block_statement: LCB stmtend? list_statement RCB;
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        statements =  self.visit(ctx.list_statement())
        return Block(statements)


    # if_statement: IF LP expression RP ignore? block_statement else_if  (ELSE ignore? block_statement)? ;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        condition = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.block_statement(0))
        elseStmt = self.visit(ctx.else_if())
        if ctx.ELSE():
            Else = self.visit(ctx.block_statement(1))
            if elseStmt:
                current = elseStmt
                while current.elseStmt: 
                    current = current.elseStmt
                current.elseStmt = Else  
            else:
                elseStmt = Else  
        return If(condition,thenStmt,elseStmt)


    # else_if: ELSE IF LP expression RP ignore? block_statement else_if |;
    def visitElse_if(self, ctx:MiniGoParser.Else_ifContext):
        if ctx is None or ctx.getChildCount() == 0:
            # print("OK")
            return None
        condition = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.block_statement())
        elseStmt = None
        if ctx.else_if():
            elseStmt = self.visit(ctx.else_if())
        return If(condition,thenStmt,elseStmt)


    '''for_statement: (range_for | index_for); 
    '''
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visit(ctx.range_for()) if ctx.range_for() else self.visit(ctx.index_for())


    # range_for: FOR ID CM ID ASSIGN RANGE expression6 ignore? block_statement ; = ForEach
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        idx =Id(ctx.ID(0).getText())
        value = Id(ctx.ID(1).getText())
        arr = self.visit(ctx.expression6())
        loop = self.visit(ctx.block_statement())
        return ForEach(idx,value,arr,loop)


    # index_for: FOR (expression | (assign_statement |VAR ID types_specifier? ASSIGNINIT expression)  
    # stmtend expression stmtend ID assign expression)  block_statement ;= ForStep | ForBasic
    def visitIndex_for(self, ctx:MiniGoParser.Index_forContext):
        loop = self.visit(ctx.block_statement())
        if ctx.stmtend():
            cond = None
            init = None
            lhs = None
            rhs = None

            if ctx.assign_statement(): 
                init = self.visit(ctx.assign_statement()) 
                cond = self.visit(ctx.expression(0))
                rhs = self.visit(ctx.expression(1))
                lhs = Id(ctx.ID(0).getText()) 
            else:
                init = VarDecl(ctx.ID(0).getText(),self.visit(ctx.types_specifier()) if ctx.types_specifier() else None,self.visit(ctx.expression(0)))
                cond = self.visit(ctx.expression(1))
                lhs = Id(ctx.ID(1).getText()) 
                rhs = self.visit(ctx.expression(2))

            assign_op = ctx.assign().getText()

            if assign_op in ["+=", "-=", "*=", "/=", "%="]:
                    op = assign_op[0]
                    rhs = BinaryOp(op, lhs, rhs) 
            update = Assign(lhs,rhs)
            
            return ForStep(init, cond, update,loop)
        cond = self.visit(ctx.expression(0))
        return ForBasic(cond,loop)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # call_statement: expression6 LP list_expression? RP ;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        exp = self.visit(ctx.expression6())
        args = self.visit(ctx.list_expression()) if ctx.list_expression() else []

        if isinstance(exp, Id):
            return FuncCall(exp.name, args)
        elif isinstance(exp, FieldAccess):
            return MethCall(exp.receiver, exp.field, args)

        return self.visitChildren(ctx)


    def visitExpression(self, ctx: MiniGoParser.ExpressionContext):
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        return self.visit(ctx.expression1())
    
    def visitExpression1(self, ctx: MiniGoParser.Expression1Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))
        return self.visit(ctx.expression2())
    
    def visitExpression2(self, ctx: MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        return self.visit(ctx.expression3())
    
    def visitExpression3(self, ctx: MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        return self.visit(ctx.expression4())
    
    def visitExpression4(self, ctx: MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
        return self.visit(ctx.expression5())
    
    def visitExpression5(self, ctx: MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression5()))
        return self.visit(ctx.expression6())
    '''
    expression6:
    expression6 LCB expression? RCB
    |expression6 DOT ID
    | expression6 DOT funtion_call
    |expression6 array_dimension
    | expression7;
    '''

    '''array_literal: array_type LCB array RCB;
    array: array_list CM array | array_list;
    array_list: primitive_literal | LCB array RCB ;
    array_type: array_dimension types_specifier;
    struct_literal: ID CO expression stmtend? (CM struct_literal)? ;
    '''
    def visitExpression6(self, ctx: MiniGoParser.Expression6Context):
            
        if ctx.LCB():
            expr6 = self.visit(ctx.expression6())  # Visit expression6
            if isinstance(expr6, Id):
                name = expr6.name
                field = self.visit(ctx.expression()) if ctx.expression() else []
                return StructLiteral(name, field)
            return ArrayLiteral(self.visit(ctx.expression6()), self.visit(ctx.expression()))
        
        elif ctx.array_dimension():
            arr = self.visit(ctx.expression6())
            if isinstance(arr,str):
                arr = Id(arr)
            return ArrayCell(arr, self.visit(ctx.array_dimension()))
        elif ctx.DOT():
            STRUCT = self.visit(ctx.expression6())
            if ctx.funtion_call():
                var = self.visit(ctx.funtion_call())
                return MethCall(STRUCT, var.funName, var.args)
            return FieldAccess(STRUCT, ctx.ID().getText())
        return self.visit(ctx.expression7())
    '''
    expression7:
    ID
    | literal
    | funtion_call
    | LP expression RP
    '''
    def visitExpression7(self, ctx: MiniGoParser.Expression7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.funtion_call():
            return self.visit(ctx.funtion_call())
        elif ctx.LP():
            return self.visit(ctx.expression())
    
    # funtion_call: ID LP list_expression? RP;
    def visitFuntion_call(self, ctx:MiniGoParser.Funtion_callContext):
        funcname = ctx.ID().getText()
        para = self.visit(ctx.list_expression()) if ctx.list_expression() else []
        return FuncCall(funcname,para)
    
    # nolit: nolit DOT var_check | nolit array_dimension| var_check;
    def visitNolit(self, ctx: MiniGoParser.NolitContext):
        if ctx.DOT():
            receiver = self.visit(ctx.nolit())
            if isinstance(receiver,str):
                receiver = Id(receiver)
            return FieldAccess(receiver, self.visit(ctx.var_check()))
        elif ctx.array_dimension():
            arr = self.visit(ctx.nolit())
            if isinstance(arr,str):
                arr = Id(arr)
            # print(arr)
            return ArrayCell(arr, self.visit(ctx.array_dimension()))
        return self.visit(ctx.var_check())
    
    def visitVar_check(self, ctx: MiniGoParser.Var_checkContext):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.funtion_call():
            return self.visit(ctx.funtion_call())
        elif ctx.array_dimension():
            return ArrayCell(self.visit(ctx.var_check()), self.visit(ctx.array_dimension()))



    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmtend.
    def visitStmtend(self, ctx:MiniGoParser.StmtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ignore.
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniGoParser#number.
    def visitNumber(self, ctx:MiniGoParser.NumberContext):
        if ctx.INT_LIT():
            r= IntLiteral(int(ctx.INT_LIT().getText()))
            return r
        elif ctx.HEX_LIT():
            return IntLiteral(int(ctx.HEX_LIT().getText(), 16))
        elif ctx.OCT_LIT():
            return IntLiteral(int(ctx.OCT_LIT().getText(), 8))
        elif ctx.BI_LIT():
            return IntLiteral(int(ctx.BI_LIT().getText(), 2))
