import re
from enum import Enum, auto

# =========================
# TOKEN TYPES
# =========================

class TokenType(Enum):
    NUMBER = auto()
    IDENTIFIER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    LPAREN = auto()
    RPAREN = auto()
    EOF = auto()


# =========================
# TOKEN CLASS
# =========================

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


# =========================
# LEXER
# =========================

class Lexer:
    token_specification = [
        ('NUMBER', r'\d+'),
        ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('MULTIPLY', r'\*'),
        ('DIVIDE', r'/'),
        ('ASSIGN', r'='),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []

        regex = '|'.join(f'(?P<{name}>{pattern})'
                         for name, pattern in self.token_specification)

        for match in re.finditer(regex, self.text):
            kind = match.lastgroup
            value = match.group()

            if kind == 'NUMBER':
                tokens.append(Token(TokenType.NUMBER, int(value)))

            elif kind == 'IDENTIFIER':
                tokens.append(Token(TokenType.IDENTIFIER, value))

            elif kind == 'PLUS':
                tokens.append(Token(TokenType.PLUS, value))

            elif kind == 'MINUS':
                tokens.append(Token(TokenType.MINUS, value))

            elif kind == 'MULTIPLY':
                tokens.append(Token(TokenType.MULTIPLY, value))

            elif kind == 'DIVIDE':
                tokens.append(Token(TokenType.DIVIDE, value))

            elif kind == 'ASSIGN':
                tokens.append(Token(TokenType.ASSIGN, value))

            elif kind == 'LPAREN':
                tokens.append(Token(TokenType.LPAREN, value))

            elif kind == 'RPAREN':
                tokens.append(Token(TokenType.RPAREN, value))

            elif kind == 'SKIP':
                continue

            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected character: {value}')

        tokens.append(Token(TokenType.EOF, None))
        return tokens


# =========================
# AST NODES
# =========================

class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"


class BinaryOperationNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.operator.value} {self.right})"


class AssignmentNode(ASTNode):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        return f"Assign({self.identifier} = {self.expression})"


# =========================
# PARSER
# =========================

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.position += 1

            if self.position < len(self.tokens):
                self.current_token = self.tokens[self.position]
        else:
            raise Exception(
                f"Expected {token_type}, got {self.current_token.type}"
            )

    # assignment -> IDENTIFIER = expression
    def parse(self):
        if self.current_token.type == TokenType.IDENTIFIER:
            identifier = IdentifierNode(self.current_token.value)
            self.eat(TokenType.IDENTIFIER)

            self.eat(TokenType.ASSIGN)

            expr = self.expression()

            return AssignmentNode(identifier, expr)

        else:
            return self.expression()

    # expression -> term ((+|-) term)*
    def expression(self):
        node = self.term()

        while self.current_token.type in (
                TokenType.PLUS,
                TokenType.MINUS):

            operator = self.current_token

            if operator.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)

            elif operator.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinaryOperationNode(node, operator, self.term())

        return node

    # term -> factor ((*|/) factor)*
    def term(self):
        node = self.factor()

        while self.current_token.type in (
                TokenType.MULTIPLY,
                TokenType.DIVIDE):

            operator = self.current_token

            if operator.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)

            elif operator.type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)

            node = BinaryOperationNode(node, operator, self.factor())

        return node

    # factor -> NUMBER | IDENTIFIER | (expression)
    def factor(self):
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumberNode(token.value)

        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return IdentifierNode(token.value)

        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)

            node = self.expression()

            self.eat(TokenType.RPAREN)

            return node

        else:
            raise Exception("Invalid syntax")


# =========================
# MAIN PROGRAM
# =========================

text = input("Enter expression: ")

lexer = Lexer(text)
tokens = lexer.tokenize()

print("\nTOKENS:")
for token in tokens:
    print(token)

parser = Parser(tokens)
ast = parser.parse()

print("\nABSTRACT SYNTAX TREE:")
print(ast)