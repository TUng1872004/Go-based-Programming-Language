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
    def __init__(self,ast):
        self.ast = ast
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
        self.visit(self.ast, None)

    def visitProgram(self, ast: Program,c : None):

        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            print("Actual:",c)
            if c is None:
                raise Undeclared(Type(),"")
            if self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name):
                raise Redeclared(Method(), ast.fun.name)
            
            self.curr_func = FuncDecl(ast.fun.name, ast.fun.params, ast.fun.retType, ast.fun.body)
            
            meth_env = []
            for param in ast.fun.params:
                if self.lookup(param.parName, meth_env, lambda x: x.parName):
                    raise Redeclared(Parameter(), param.parName)
                meth_env.append(Symbol(param.parName, param.parType))
            
            meth_env.append(Symbol(ast.receiver, c, None))

            self.visit(ast.fun.body, [meth_env])
            
            return ast

        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        self.list_func = self.list_func + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name))  , 
             list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))
        
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            filter(lambda item: isinstance(item, Decl), ast.decl), 
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

    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        result = self.lookup(ast.name, c, lambda x: x.name)
        if  result is not None:
            raise Redeclared(StaticErrorType(), ast.name) 

        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            for name, _ in c:
                if element[0] == name:
                    raise Redeclared(Field(),name)
            return element

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        result = self.lookup(ast.name, c, lambda x: x.name)
        if not result is None:
            raise Redeclared(Prototype(), ast.name) 
        return ast

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        result = self.lookup(ast.name, c, lambda x: x.name)
        if not result is None:
            raise Redeclared(StaticErrorType(), ast.name)  
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        result = self.lookup(ast.name, c[0], lambda x: x.name)
        if not result is None:
            raise Redeclared(Function(), ast.name)
        self.curr_func = ast
        self.visit(ast.body, list(
                                    reduce(
                                        lambda acc, ele: [[self.visit(ele, acc)] + acc[0]] + acc[1:],
                                        ast.params,
                                        [[]] + c
                                    )
                                ))
        self.curr_func = None
        return Symbol(ast.name, FuntionType())

    def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) -> Symbol:
        
        result = self.lookup(ast.parName, c[1], lambda x: x.name)
        if result is not None:
            raise Redeclared(Parameter(), ast.parName)  
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        if self.lookup(ast.fun.name, c[0], lambda x: x.name):
                raise Redeclared(Method(), ast.fun.name)
        
    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]]) -> Symbol:
        result = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not result is None:
            raise Redeclared(Variable(), ast.varName) 
        return Symbol(ast.varName, self.visit(ast.varInit, c) if ast.varInit else ast.varType, None)

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        result = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not result is None:
            raise Redeclared(Constant(), ast.conName) 
        if ast.iniExpr is None:
            raise TypeMismatch(ast.iniExpr)
        return Symbol(ast.conName, self.visit(ast.iniExpr, c) )


    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        reduce(
            lambda acc, ele: [
                ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
            ] + acc[1:], 
            ast.member, 
            [[]] + c
        )

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None: 
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None: 
        self.visit(Block([ast.init] + ast.loop.member + [ast.upda]), c)
    
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None: 
          self.visit(Block([VarDecl(ast.idx.name, None, None), VarDecl(ast.value.name, None, None)] + ast.loop.member), c)


    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        result = self.lookup(ast.funName, self.list_func, lambda x: x.name)
        if result:
            return result.retType
        raise Undeclared(Function(), ast.funName)
    


    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        result = self.lookup(ast.field, type_receiver.elements, lambda x: x[0]) if isinstance(type_receiver, StructType) else TypeMismatch(type_receiver)
        if result is None:
            raise Undeclared(Field(), ast.field)
        elif isinstance(result,TypeMismatch):
            raise result
        return result[1]

    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        #result = # TODO: Implement if isinstance(type_receiver, StructType) else # TODO: Implement
        result = self.lookup(ast.metName, type_receiver.methods, lambda x: x.fun.name) if isinstance(type_receiver, StructType) else TypeMismatch(type_receiver)
        if result is None:
            raise Undeclared(Method(), ast.metName)
        elif not isinstance(result,MethodDecl):
            raise result
        return result.recType


    def visitIntType(self, ast, param): return IntType()
    def visitFloatType(self, ast, param): return FloatType()
    def visitBoolType(self, ast, param): return BoolType()
    def visitStringType(self, ast, param): return StringType()
    def visitVoidType(self, ast, param): return VoidType()
    def visitArrayType(self, ast, param): return ArrayType()
    def visitAssign(self, ast, param): return None
    def visitIf(self, ast, param): return None
    def visitContinue(self, ast, param): return None
    def visitBreak(self, ast, param): return None
    def visitReturn(self, ast, param): return None
    def visitBinaryOp(self, ast, param): return None
    def visitUnaryOp(self, ast, param): return None
    def visitArrayCell(self, ast, param): return None
    def visitIntLiteral(self, ast, param): return None
    def visitFloatLiteral(self, ast, param): return None
    def visitBooleanLiteral(self, ast, param): return None
    def visitStringLiteral(self, ast, param): return None
    def visitArrayLiteral(self, ast, param): return None
    def visitStructLiteral(self, ast, param): return None
    def visitNilLiteral(self, ast, param): return None

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        #result = next(filter(None, # TODO: Implement), None)
        result = next(filter(None, (sym if sym.name == ast.name else None for scope in c for sym in scope)), None)
        if result and not isinstance(result.mtype, Function):
            return result.mtype if not isinstance(result.mtype, Id) else self.visit(result.mtype, c)
        raise Undeclared(Identifier(), ast.name)