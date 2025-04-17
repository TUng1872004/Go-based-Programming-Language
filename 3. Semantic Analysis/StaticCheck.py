from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, param)

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ctx):
        self.ctx = ctx
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_func: List[FuncDecl] =  [
                FuncDecl("getInt", [], IntType(), Block([])),
                FuncDecl("putInt", [ParamDecl("a", IntType())], VoidType(), Block([])),
                FuncDecl("putIntLn", [ParamDecl("a", IntType())], VoidType(), Block([])),
                FuncDecl("getFloat", [], FloatType(), Block([])),
                FuncDecl("putFloat", [ParamDecl("a", FloatType())], VoidType(), Block([])),
                FuncDecl("putFloatLn", [ParamDecl("a", FloatType())], VoidType(), Block([])),
                FuncDecl("getBool", [], BoolType(), Block([])),
                FuncDecl("putBool", [ParamDecl("a", BoolType())], VoidType(), Block([])),
                FuncDecl("putBoolLn", [ParamDecl("a", BoolType())], VoidType(), Block([])),
                FuncDecl("getString", [], StringType(), Block([])),
                FuncDecl("putString", [ParamDecl("a", StringType())], VoidType(), Block([])),
                FuncDecl("putStringLn", [ParamDecl("a", StringType())], VoidType(), Block([])),
                FuncDecl("putLn", [], VoidType(), Block([]))
            ]
        self.curr_func: FuncDecl = None

    def check(self):
        self.visit(self.ctx, None)

    def visitProgram(self, ctx: Program,c : None):

        def visitMethodDecl(ctx: MethodDecl, c: StructType) -> MethodDecl:
            if self.lookup(ctx.fun.name, c.methods, lambda x: x.fun.name):
                raise Redeclared(Method(), ctx.fun.name)
            if self.lookup(ctx.fun.name, c.elements, lambda x: x[0]):
                raise Redeclared(Method(), ctx.fun.name)
            self.curr_func = FuncDecl(ctx.fun.name, ctx.fun.params, ctx.fun.retType, ctx.fun.body)
            c.methods.append(MethodDecl(ctx.receiver, c.name, self.curr_func))
            meth_env = []
            for param in ctx.fun.params:
                if self.lookup(param.parName, meth_env, lambda x: x.parName):
                    raise Redeclared(Parameter(), param.parName)
                meth_env.append(Symbol(param.parName, param.parType))
            
            meth_env.append(Symbol(ctx.receiver, c, None))

            self.visit(ctx.fun.body, [meth_env])
            
            return ctx

        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ctx.decl, [])
        self.list_func = self.list_func + list(filter(lambda item: isinstance(item, FuncDecl), ctx.decl))

        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name))  , 
             list(filter(lambda item: isinstance(item, MethodDecl), ctx.decl))
        ))
        
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            filter(lambda item: isinstance(item, Decl), ctx.decl), 
            [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                Symbol("getFloat", FuntionType()),
                Symbol("putFloat", FuntionType()),
                Symbol("putFloatLn", FuntionType()),
                Symbol("getBool", FuntionType()),
                Symbol("putBool", FuntionType()),
                Symbol("putBoolLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putString", FuntionType()),
                Symbol("putStringLn", FuntionType()),
                Symbol("putLn", FuntionType())
            ]]
        )

    def visitStructType(self, ctx: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        result = self.lookup(ctx.name, c, lambda x: x.name)
        if  result is not None:
            raise Redeclared(StaticErrorType(), ctx.name) 

        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            for name, _ in c:
                if element[0] == name:
                    raise Redeclared(Field(),name)
            return element

        ctx.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ctx.elements , [])
        return ctx

    def visitPrototype(self, ctx: Prototype, c: List[Prototype]) -> Prototype:
        result = self.lookup(ctx.name, c, lambda x: x.name)
        if not result is None:
            raise Redeclared(Prototype(), ctx.name) 
        return ctx

    def visitInterfaceType(self, ctx: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        result = self.lookup(ctx.name, c, lambda x: x.name)
        if not result is None:
            raise Redeclared(StaticErrorType(), ctx.name)  
        ctx.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ctx.methods , [])
        return ctx
    
    def visitFuncDecl(self, ctx: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        result = self.lookup(ctx.name, c[0], lambda x: x.name)
        if not result is None:
            raise Redeclared(Function(), ctx.name)
        self.curr_func = ctx
        self.visit(ctx.body, list(
            reduce(
                lambda acc, ele: [[self.visit(ele, acc)] + acc[0]] + acc[1:],
                ctx.params,
                [[]] + c
            )
        ))
        self.curr_func = None
        return Symbol(ctx.name, FuntionType())

    def visitParamDecl(self, ctx: ParamDecl, c: List[Symbol]) -> Symbol:
        result = self.lookup(ctx.parName, c[0], lambda x: x.name)
        if result is not None:
            raise Redeclared(Parameter(), ctx.parName)  
        return Symbol(ctx.parName, ctx.parType, None)

    def visitMethodDecl(self, ctx: MethodDecl, c : List[List[Symbol]]) -> None:
        if self.lookup(ctx.fun.name, c[0], lambda x: x.name):
                raise Redeclared(Method(), ctx.fun.name)
        
    def visitVarDecl(self, ctx: VarDecl, c : List[List[Symbol]]) -> Symbol:
        for i in range(len(c)):
            result = self.lookup(ctx.varName, c[i], lambda x: x.name)
            if result is not None:
                raise Redeclared(Variable(), ctx.varName) 
            
        result = self.lookup(ctx.varName, self.list_func, lambda x: x.name)
        if not result is None:
                raise Redeclared(Variable(), ctx.varName) 
        

        init= self.visit(ctx.varInit,c) if ctx.varInit else None

        if init:
            if isinstance(init, VoidType):
                raise TypeMismatch(ctx)
            if ctx.varType is None:
                ctx.varType = init
            if not self.checky(ctx.varType, init, []):
                raise TypeMismatch(ctx)
        return Symbol(ctx.varName, ctx.varType, None)

    def visitConstDecl(self, ctx: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        for i in range(len(c)):
            result = self.lookup(ctx.conName, c[i], lambda x: x.name)
            if not result is None:
                raise Redeclared(Constant(), ctx.conName) 
        result = self.lookup(ctx.conName, self.list_func, lambda x: x.name)
        if result is not None:
                raise Redeclared(Constant(), ctx.conName) 
        result = self.lookup(ctx.conName, self.list_type, lambda x: x.name)
        if result is not None:
                raise Redeclared(Constant(), ctx.conName) 
        
        if ctx.iniExpr is None:
            raise TypeMismatch(ctx)
        init= self.visit(ctx.iniExpr,c)
        if ctx.conType is None:
            ctx.conType = init
        if not self.checky(ctx.conType, init, []):
            raise TypeMismatch(ctx)
        return Symbol(ctx.conName, init, ctx.iniExpr)


    def visitBlock(self, ctx: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c 

        for ele in ctx.member:
            result = self.visit(ele, (acc, True)) if isinstance(ele, (FuncCall, MethCall)) else self.visit(ele, acc)
            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]

    def visitForBasic(self, ctx: ForBasic, c : List[List[Symbol]]) -> None: 
        cond_type = self.visit(ctx.cond, c)
        if not isinstance(cond_type, BoolType) and not isinstance(cond_type, IntType):
            raise TypeMismatch(ctx)
        self.visit(ctx.loop, c)

    def visitForStep(self, ctx: ForStep, c: List[List[Symbol]]) -> None: 
        symbol = self.visit(ctx.init, [[]] +  c)
        c[0].append(symbol)
        cond_type = self.visit(ctx.cond, c)
        if not isinstance(cond_type, BoolType) and not isinstance(cond_type, IntType):
            raise TypeMismatch(ctx)
        self.visit(Block( ctx.loop.member + [ctx.upda]), c)


    def checky(self, LHS: Type, RHS: Type, permission: List[Tuple[Type, Type]] = []) -> bool:
        if type(RHS) == StructType and RHS.name == "":
            return LHS == None
        LHS = self.lookup(LHS.name, self.list_type, lambda x: x.name) if isinstance(LHS, Id) else LHS
        RHS = self.lookup(RHS.name, self.list_type, lambda x: x.name) if isinstance(RHS, Id) else RHS
        if (type(LHS), type(RHS)) in permission:
            if isinstance(LHS, InterfaceType) and isinstance(RHS, StructType):
                for func_in_interface in LHS.methods:
                    found = False
                    for func_in_struct in RHS.methods:
                        if (func_in_interface.name == func_in_struct.name and 
                            func_in_interface.returnType == func_in_struct.returnType and 
                            len(func_in_interface.param) == len(func_in_struct.param) and
                            all(self.checky(p1.typ, p2.typ) for p1, p2 in zip(func_in_interface.param, func_in_struct.param))):
                            found = True
                            break
                    if not found:
                        return False
                return True
            return True

        if isinstance(LHS, (StructType, InterfaceType)) and isinstance(RHS, (StructType,InterfaceType)):
            return LHS.name == RHS.name

        if isinstance(LHS, ArrayType) and isinstance(RHS, ArrayType):
            if len(LHS.dimens) != len(RHS.dimens) or not all(d1 == d2 or isinstance(d2, BinaryOp) or isinstance(d1, BinaryOp)  for d1, d2 in zip(LHS.dimens, RHS.dimens)):
                return False
            return self.checky(LHS.eleType, RHS.eleType,[(FloatType, IntType),(IntType, FloatType)]) 
        return type(LHS) == type(RHS)
    
    def visitArrayType(self, ctx: ArrayType, c: List[List[Symbol]]):
        ctx.dimens = list(map(lambda item: self.visit(item, c), ctx.dimens))  
        ctx.eleType= self.visit(ctx.eleType, c) 
        return ctx
    
    def visitForEach(self, ctx: ForEach, c: List[List[Symbol]]) -> None: 
        type_array = self.visit(ctx.arr, c)
        if type(self.visit(ctx.arr, c)) != ArrayType:
            raise TypeMismatch(ctx)

        type_idx = self.visit(ctx.idx, c) 

        if not self.checky(type_idx, IntType(),[(None, IntType)]):
            raise TypeMismatch(ctx.idx)       
        type_value = self.visit(ctx.value, c)
        if not self.checky(type_value, type_array.eleType):
            raise TypeMismatch(ctx)          

        self.visit(Block(ctx.loop.member), c)


    def visitFuncCall(self, ctx: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c

        result = self.lookup(ctx.funName, self.list_func, lambda x: x.name)
        if result:
            if len(result.params) != len(ctx.args):
                raise TypeMismatch(ctx)

            for param, arg in zip(result.params, ctx.args):
                arg_type = self.visit(arg, c) if isinstance(c, tuple) else self.visit(arg, c[0])
                if not self.checky(arg_type, param.parType,[(FloatType(), IntType())]):
                    raise TypeMismatch(ctx)
            if is_stmt and not isinstance(result.retType, VoidType):
                raise TypeMismatch(ctx)
            if not is_stmt and isinstance(result.retType, VoidType):
                raise TypeMismatch(ctx)

            return result.retType

        raise Undeclared(Function(), ctx.funName)



    def visitFieldAccess(self, ctx: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ctx.receiver, c)
        result = None
        
        if isinstance(type_receiver, StructType) :
            result = self.lookup(ctx.field, type_receiver.elements, lambda x: x[0])  
        else: 
            raise TypeMismatch(ctx)    
        if result is None:
            raise Undeclared(Field(), ctx.field)
        return result[1]

    def visitMethCall(self, ctx: MethCall, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ctx.receiver, c)
        result = None
        if isinstance(type_receiver, StructType) :
            result = self.lookup(ctx.metName, type_receiver.methods, lambda x: x.fun.name)
        elif isinstance(type_receiver, InterfaceType): 
            result = self.lookup(ctx.metName, type_receiver.methods, lambda x: x.name)
        else:
            raise TypeMismatch(ctx)
        if result is None:
            raise Undeclared(Method(), ctx.metName)
        return result.fun.retType if isinstance(result, MethodDecl) else result.retType
        



    def visitIntType(self, ctx, c: List[List[Symbol]]) -> Type: return ctx
    def visitFloatType(self, ctx, c: List[List[Symbol]])-> Type: return ctx
    def visitBoolType(self, ctx, c: List[List[Symbol]])-> Type: return ctx
    def visitStringType(self, ctx, c: List[List[Symbol]]) -> Type: return ctx
    def visitVoidType(self, ctx, c: List[List[Symbol]]) -> Type: return ctx

    def visitAssign(self, ctx: Assign, c: List[List[Symbol]]) -> None:
        if not isinstance(ctx.lhs,ArrayCell) and not isinstance(ctx.lhs,FieldAccess):
            result = next(filter(None, (sym if isinstance(sym, Symbol) and sym.name == ctx.lhs.name else None for scope in c for sym in scope)), None)
            if result and result.value is not None:
                raise TypeMismatch(ctx)
        
        LHS = self.visit(ctx.lhs, c)
        RHS = self.visit(ctx.rhs, c)
        if not self.checky(LHS, RHS, [(FloatType, IntType), 
                                                   (InterfaceType, StructType)]):
            raise TypeMismatch(ctx)
        
    def visitIf(self, ctx: If, c: List[List[Symbol]]) -> None: 
        if not isinstance(self.visit(ctx.expr,c), BoolType ):
            raise TypeMismatch(ctx)
        self.visit(Block(ctx.thenStmt.member), c)
        if ctx.elseStmt:
            self.visit(Block(ctx.elseStmt.member), c)

    def visitContinue(self, ctx, c: List[List[Symbol]]) -> None: return None
    def visitBreak(self, ctx, c: List[List[Symbol]]) -> None: return None

    def visitReturn(self, ctx: Return, c: List[List[Symbol]]) -> None: 
        if not self.checky(self.visit(ctx.expr,c) if ctx.expr else VoidType(), self.curr_func.retType):
            raise TypeMismatch(ctx)
        return None
    
    def visitBinaryOp(self, ctx: BinaryOp, c: List[List[Symbol]]):
        LHS = self.visit(ctx.left, c)
        RHS = self.visit(ctx.right, c)

        if ctx.op in ['+', '-', '*', '/']:
            if self.checky(LHS, RHS, [(IntType, FloatType), (FloatType, IntType), (IntType, IntType), (FloatType, FloatType)]):
                if isinstance(LHS, StringType) or isinstance(RHS, StringType):
                    if ctx.op == '+':
                        return StringType()
                    else:
                        raise TypeMismatch(ctx)
                if isinstance(LHS, FloatType) or isinstance(RHS, FloatType):
                    return FloatType()
                return IntType()


        elif ctx.op == '%':
            if isinstance(LHS, IntType) and isinstance(RHS, IntType):
                return IntType()
            else:
                raise TypeMismatch(ctx)
        elif ctx.op in ['&&', '||']:
            if isinstance(LHS, BoolType) and isinstance(RHS, BoolType):
                return BoolType()
            raise TypeMismatch(ctx)
        elif ctx.op in ['==', '!=']:
            if type(LHS) == type(RHS):
                if isinstance(LHS, (IntType, BoolType)):
                    return BoolType()
            raise TypeMismatch(ctx)
        elif ctx.op in ['<', '<=', '>', '>=']:
            if self.checky(LHS, RHS, [(IntType, FloatType), (FloatType, IntType)]):
                if isinstance(LHS, (IntType, FloatType)):
                        return BoolType()
            raise TypeMismatch(ctx)
        
        raise TypeMismatch(ctx)
    


    def visitUnaryOp(self, ctx: UnaryOp, c: List[List[Symbol]]):
        unary_type = self.visit(ctx.body, c)

        if ctx.op == '-':
            if isinstance(unary_type, (IntType, FloatType)):
                return unary_type
            raise TypeMismatch(ctx)

        if ctx.op == '!':
            if isinstance(unary_type, BoolType):
                return BoolType()
            raise TypeMismatch(ctx)

        raise TypeMismatch(ctx)  

    
    def visitArrayCell(self, ctx: ArrayCell, c: List[List[Symbol]]):
        array = self.visit(ctx.arr,c )
        if not isinstance(array, ArrayType):
            raise TypeMismatch(ctx)
        if not all(map(lambda item: self.checky(self.visit(item, c),IntType() ), ctx.idx)):
            raise TypeMismatch(ctx)
        if len(array.dimens) == len(ctx.idx):
            return array.eleType
        elif len(array.dimens) > len(ctx.idx):
            type_return = ArrayType(array.dimens[len(ctx.idx):], array.eleType)
            return type_return
        raise TypeMismatch(ctx)

    def visitIntLiteral(self, ctx, c: List[List[Symbol]]) -> Type: return IntType()
    def visitFloatLiteral(self, ctx, c: List[List[Symbol]]) -> Type: return FloatType()
    def visitBooleanLiteral(self, ctx, c: List[List[Symbol]]) -> Type: return BoolType()
    def visitStringLiteral(self, ctx, c: List[List[Symbol]]) -> Type: return StringType()
    
    def visitArrayLiteral(self, ctx:ArrayLiteral , c: List[List[Symbol]]) -> Type:  
        stack = [ctx.value]
        while stack:
            current = stack.pop()
            if isinstance(current, list):
                stack.extend(reversed(current))  
            else:
                self.visit(current, c)
        return ArrayType(ctx.dimens, ctx.eleType)

    def visitStructLiteral(self, ctx:StructLiteral, c: List[List[Symbol]]) -> Type: 
        ele = list(map(lambda value: self.visit(value[1], c), ctx.elements))
        struct= self.lookup(ctx.name,self.list_type, lambda x: x.name)
        if struct is None:
            raise Undeclared(StaticErrorType(),ctx.name)
        return StructType(ctx.name,struct.methods,ele)

    def visitNilLiteral(self, ctx:NilLiteral, c: List[List[Symbol]]) -> Type: return StructType("", [], [])

    def visitId(self, ctx: Id, c: List[List[Symbol]]) -> Type:
        if isinstance(c, tuple):
            c, _ = c
        result = next(filter(None, (sym if isinstance(sym, Symbol) and sym.name == ctx.name else None for scope in c for sym in scope)), None)
        if result and not isinstance(result.mtype, FuntionType):
            if not isinstance(result.mtype, Id):
                return result.mtype  
            else:
                result= self.lookup(result.mtype.name, self.list_type, lambda x: x.name)
                if result is not None:
                    return result
        raise Undeclared(Identifier(), ctx.name)