# Lab 1 - Formal Languages (Variant 2)


## 1. Problem Description
The program should  generate 5 string using the grammar of my variant using the Grammar class.The  program  should be able to  generate an automaton using grammar from grammar class.After that Automaton class should be able to take the input string and tell if its valid or not.

## 2. Grammar Definition
VN = {S, R, L}  
VT = {a, b, c, d, e, f}  
P = { 
S → aS | bS | cR | dL  
R → dL | e  
L → fL | eL | d  
}

## 3. Implementation

- Grammar : defines the constructor with the terminal, non termianl characters,rules, and the starting character.
A while loop than goes over the string called current and checks if there are non_terminal characters.While it does it we have a for loop that goes over individual characters of a string and using enum gets the pair values like 0:a , 1:b and so  on.Then using the ch from the for loop we take a random choice from the Rules[ch] and create a current sting by using slices.

- Automaton (attributes and methods)
We define an Automaton class with the following components: states, alphabet, start state, final states, and transitions. Using the grammar_to_automaton function, the grammar rules are converted into automaton transitions. After that, we implement the method stringBelongsToLanguage, which processes the input string character by character, follows the corresponding state transitions, and finally checks whether the automaton ends in a final state. If it does, the string is accepted; otherwise, it is rejected.
## 4. Examples / Demonstration
```
badd
acdd
dd
aace
dd

abce -> True
bbb -> False
dffd -> True
de -> False
```

## 5. Conclusion / Reflection
I ve learned the basics of grammar and automatons.How string are created by defining a grammar. And how characters follow state tranisitons of an automaton.






# Lab 2 - Formal Languages (Variant 2)



## 1. Problem Description

The program should take the NDFA of Variant 2 and:

Convert it into a regular grammar.

Determine whether the automaton is deterministic or non-deterministic.

Convert the NDFA to an equivalent DFA.

Optionally, represent the automaton graphically.

The goal is to understand determinism in automata and how NDFA and DFA relate to regular grammars.

## 2. NDFA Definition (Variant 2)

States (Q): {q0, q1, q2, q3, q4}
Alphabet (Σ): {a, b, c}
Start state: q0
Final states (F): {q4}

Transitions (δ):

δ(q0, a) = q1
δ(q1, b) = q2, q3
δ(q2, c) = q3
δ(q3, a) = q3
δ(q3, b) = q4

Note: The transition δ(q1, b) → q2, q3 makes this automaton non-deterministic.

## 3. Implementation

- Automaton class: defines the constructor with states, alphabet, start state, final states, and transitions.

- automaton_to_grammar(): converts NDFA transitions into a regular grammar dictionary {state: [rules]}.

- is_deterministic(): checks if any state has multiple transitions for the same symbol. If so, the automaton is non-deterministic.

- convert_to_dfa(): implements subset construction to convert NDFA to DFA, creating new DFA states as sets of NDFA states.

## 4. Examples / Demonstration

Regular Grammar generated from NDFA:
```
q0: ['aq1']
q1: ['bb q2', 'bb q3']
q2: ['cc q3']
q3: ['aa q3', 'bb q4']

Determinism Check:

Is DFA? False

DFA Construction:

DFA States: [frozenset({'q0'}), frozenset({'q1'}), frozenset({'q2','q3'}), ...]
DFA Transitions: {(frozenset({'q0'}),'a'): frozenset({'q1'}), ...}
DFA Start: frozenset({'q0'})
DFA Final: [frozenset({'q4'}), frozenset({'q3','q4'})]

```
## 5. Chomsky Hierarchy Classification

The grammar generated from this NDFA is right-linear (regular grammar).

Therefore, according to Chomsky hierarchy, this grammar is Type 3 (Regular grammar).

## 6. Conclusion / Reflection

I learned how to:

Identify determinism and non-determinism in automata.

Convert an NDFA to a DFA using subset construction.

Translate finite automata into regular grammars.

Classify grammars according to Chomsky hierarchy.

This lab extends the understanding of automata theory from Lab 1 by connecting non-determinism, determinism, and grammar classification.






# LAB 3 Lexer Implementation for a Router Configuration DSL

**Course:** Formal Languages & Finite Automata
**Topic:** Lexer & Scanner
**Author:** Alexandr Biriucov
**Instructor:** Dumitru Cretu

---

# 1. Introduction

Modern software systems often require specialized languages designed for a specific domain. These are called **Domain-Specific Languages (DSLs)**. A DSL allows users to describe configurations or operations in a simplified and structured way.

In networking systems, routers and switches are commonly configured using command-line interfaces. Inspired by these systems, this project introduces a simple **Domain-Specific Language for router configuration**.

To process such a language, the first step in a compiler or interpreter is **lexical analysis**. The goal of lexical analysis is to convert a stream of characters into meaningful components called **tokens**.

This laboratory work implements a **lexer (scanner/tokenizer)** capable of reading router configuration commands and transforming them into tokens that can later be used by a parser.

---

# 2. Lexical Analysis

Lexical analysis is the first stage of language processing. It takes the source code as input and converts it into a sequence of tokens.

Key terms:

**Lexeme**
A lexeme is the actual sequence of characters extracted from the input.

Example:

```
interface
eth0
192.168.1.1
```

**Token**
A token is a category assigned to a lexeme.

Example:

| Lexeme      | Token      |
| ----------- | ---------- |
| interface   | INTERFACE  |
| eth0        | IDENTIFIER |
| 192.168.1.1 | IP_ADDRESS |

The lexer scans the input and produces a **stream of tokens** that represent the structure of the program.

---

# 3. DSL for Router Configuration

The DSL designed in this project simplifies router configuration commands. It provides a structured way to describe network interfaces, IP addresses, and routing rules.

Example DSL program:

```
interface eth0
ip 192.168.1.1
mask 255.255.255.0
route 0.0.0.0 via 192.168.1.254
enable
```

This syntax is inspired by router command-line interfaces used in real networking systems.

---

# 4. Token Types

The lexer recognizes several types of tokens.

| Token Type | Description                   | Example     |
| ---------- | ----------------------------- | ----------- |
| INTERFACE  | Interface declaration keyword | interface   |
| IP         | IP configuration keyword      | ip          |
| MASK       | Network mask keyword          | mask        |
| ROUTE      | Routing rule keyword          | route       |
| VIA        | Route gateway keyword         | via         |
| ENABLE     | Enable interface              | enable      |
| IDENTIFIER | Interface name                | eth0        |
| IP_ADDRESS | IPv4 address                  | 192.168.1.1 |
| NUMBER     | Numeric values                | 10          |

These token types allow the lexer to classify each lexeme in the DSL.

---

# 5. Lexer Implementation

The lexer is implemented in Python. It uses **regular expressions** to identify token patterns.

Example implementation:

```python
import re

TOKEN_TYPES = [
    ("INTERFACE", r"interface"),
    ("IP", r"ip"),
    ("MASK", r"mask"),
    ("ROUTE", r"route"),
    ("VIA", r"via"),
    ("ENABLE", r"enable"),
    ("IP_ADDRESS", r"\d+\.\d+\.\d+\.\d+"),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUMBER", r"\d+"),
]

def lexer(code):
    tokens = []
    words = code.split()

    for word in words:
        matched = False

        for token_type, pattern in TOKEN_TYPES:
            if re.fullmatch(pattern, word):
                tokens.append((token_type, word))
                matched = True
                break

        if not matched:
            tokens.append(("UNKNOWN", word))

    return tokens


code = """
interface eth0
ip 192.168.1.1
route 0.0.0.0 via 192.168.1.254
enable
"""

tokens = lexer(code)

for token in tokens:
    print(token)
```

---

# 6. Example Execution

Input:

```
interface eth0
ip 192.168.1.1
enable
```

Output tokens:

```
('INTERFACE', 'interface')
('IDENTIFIER', 'eth0')
('IP', 'ip')
('IP_ADDRESS', '192.168.1.1')
('ENABLE', 'enable')
```

The lexer successfully identifies each lexeme and classifies it into a token type.

---

# 7. Results

The implemented lexer is able to:

* Read router DSL configuration text
* Split the input into lexemes
* Classify lexemes into tokens
* Produce a structured token stream

This token stream can later be used by a **parser** to build a syntax tree and interpret router configuration commands.

---

# 8. Conclusion

This project demonstrates the basic principles of **lexical analysis** in language processing. A lexer was developed for a simple router configuration DSL.

The implementation shows how regular expressions can be used to detect different token types such as keywords, identifiers, and IP addresses.

This lexer represents the **first stage in building a full interpreter or compiler for the DSL**, which could later include parsing, semantic analysis, and execution of configuration commands.

---

# 9. References

1. Formal Languages and Automata Theory course materials
2. Python documentation for regular expressions


# Lab 4 – String Generation Using Regular Expression Patterns

Course: Formal Languages & Finite Automata
Topic: Regular Expressions & String Generation
Author: Alexandr Biriucov
Instructor: Dumitru Cretu

# 1. Introduction

Regular expressions are a fundamental concept in formal languages used to describe patterns of strings. They provide a compact way to represent sets of strings over a given alphabet.

In this laboratory work, a simplified regex-like system is implemented in Python to generate strings based on predefined patterns. The goal is to simulate how regular expressions can define languages and how strings can be generated from these definitions.

# 2. Problem Description

The task is to implement a program that:

Accepts predefined regex-like patterns
Parses the patterns into tokens
Generates random strings that follow the pattern rules
Displays both the generated string and the sequence of transformations

The program should also simulate repetition operators such as:

^n → exact repetition
^* → zero or more repetitions
^+ → one or more repetitions
^? → optional element
# 3. Pattern Definition

The following patterns are used:

regex_patterns = [
    r"\u? N^2 (O|P)^3 Q^* R^+",
    r"(X|Y|Z)^3 8^+ (9|0)",
    r"(H|i) (J|K) L^* N?"
]
Explanation of Patterns
Pattern 1:
\u? N^2 (O|P)^3 Q^* R^+
Optional symbol (μ)
Exactly 2 N’s
3 repetitions of O or P
Any number of Q’s
At least one R
Pattern 2:
(X|Y|Z)^3 8^+ (9|0)
3 characters from {X, Y, Z}
One or more 8’s
Ends with either 9 or 0
Pattern 3:
(H|i) (J|K) L^* N?
One of H or i
One of J or K
Zero or more L’s
Optional N
# 4. Implementation

The program is implemented in Python and consists of two main functions:

4.1 Token Processing Function
def generate_from_token(token):

This function:

Detects grouped expressions like (A|B)
Randomly selects one option
Handles optional symbols (\u)
Returns the generated character
4.2 Pattern Generation Function
def generate_from_pattern(pattern):

This function:

Splits the pattern into tokens
Detects repetition operators (^, ^*, ^+, ^?)
Generates random repetition counts
Builds the final string step-by-step
Stores processing steps for debugging
4.3 Main Execution

The program:

Iterates through all patterns
Generates a string for each
Prints:
Generated string
Step-by-step processing sequence
# 5. Example Execution
Output:
Generated string: μ NN OPO QQQ RR
Processing sequence:
  Processed '\u?' -> 'μ'
  Processed 'N^2' -> 'NN'
  Processed '(O|P)^3' -> 'OPO'
  Processed 'Q^*' -> 'QQQ'
  Processed 'R^+' -> 'RR'
Generated string: XYZ 888 9
Processing sequence:
  Processed '(X|Y|Z)^3' -> 'XYZ'
  Processed '8^+' -> '888'
  Processed '(9|0)' -> '9'
Generated string: H K LL
Processing sequence:
  Processed '(H|i)' -> 'H'
  Processed '(J|K)' -> 'K'
  Processed 'L^*' -> 'LL'
  Processed 'N?' -> ''
# 6. Results

The program successfully:

Parses simplified regex-like patterns
Supports repetition operators (^n, ^*, ^+, ^?)
Handles grouped choices (A|B)
Generates valid random strings
Tracks the transformation process step-by-step
# 7. Limitations
The parser is simplified (splits by spaces only)
Does not support full regex syntax
Limited repetition range (0–5 for * and +)
No nested group support
# 8. Conclusion

This laboratory work demonstrates how regular expressions can be used to describe languages and generate strings.

The implementation provides a simplified model of regex parsing and generation, helping to understand:

Pattern-based string generation
Repetition operators
Choice and optional constructs

This lab builds a bridge between theoretical formal languages and practical string processing.

# 9. References
Formal Languages and Automata Theory course materials
Python documentation
Regular Expressions theory


# Lab 5 – Chomsky Normal Form (CNF)

Course: Formal Languages & Finite Automata
Topic: Context-Free Grammars & Chomsky Normal Form
Author: Alexandr Biriucov
Instructor: Dumitru Cretu

# 1. Introduction

In formal language theory, grammars are used to describe how strings are generated. However, grammars can be written in many different forms, some of which are complex and difficult to analyze.

To simplify processing and enable the use of parsing algorithms, grammars are often transformed into a standardized format called Chomsky Normal Form (CNF).

A grammar in CNF has strict production rules, making it easier to analyze and process automatically.

The goal of this laboratory work is to transform a given Context-Free Grammar (CFG) into its equivalent CNF form.


# 2. Problem Description

The task consists of transforming a given CFG into Chomsky Normal Form by performing the following steps:

Eliminate ε-productions
Eliminate unit (renaming) productions
Remove inaccessible symbols
Remove non-productive symbols
Convert the grammar into CNF

Additionally, a program should be implemented that performs these transformations automatically.

# 3. Grammar Definition

Given grammar:

VN = {S, A, B, C, D, E}
VT = {a, b}
P = {
S → aB | AC
A → a | ASC | BC | aD
B → b | bS
C → ε | BA
D → abC
E → aB
}

Start symbol:


# 4. Methodology
4.1 Elimination of ε-productions

The production:

C → ε

indicates that symbol C can disappear.

To eliminate ε-productions:

All rules containing C are modified to include versions without C
The ε-rule is removed
4.2 Elimination of Unit Productions

Unit productions are rules of the form:

A → B

These are removed by:

Replacing them with the productions of the referenced symbol
Expanding rules recursively
4.3 Removal of Non-Productive Symbols

A non-terminal is non-productive if it cannot generate terminal strings.

Steps:

Identify symbols that produce only terminals
Remove symbols that cannot derive valid strings
4.4 Removal of Inaccessible Symbols

A symbol is inaccessible if it cannot be reached from the start symbol.

Steps:

Start from S
Traverse all reachable symbols
Remove unused symbols (e.g., E if not reachable)
4.5 Conversion to Chomsky Normal Form

To convert into CNF:

Rule transformations:
Replace terminals in mixed rules:
a → X
b → Y
Break long productions:
A → ABC  →  A → X1C, X1 → AB
Ensure all productions are:
A → BC
A → a

# 5. Implementation

The solution was implemented in Python using a modular approach.

Main components:
CFG Class
Stores grammar rules
Provides methods for adding and printing productions
Transformation Functions
remove_epsilon()
remove_unit()
remove_non_productive()
remove_inaccessible()
to_cnf()

Each function performs one transformation step, ensuring clarity and modularity.

# 6. Example Execution
Original Grammar:
S → aB | AC
A → a | ASC | BC | aD
B → b | bS
C → ε | BA
D → abC
E → aB
After Transformations:

Step-by-step transformations produce a simplified grammar without:

ε-productions
unit productions
useless symbols
Final CNF Grammar (simplified form):
S → XB | AC | AS | BC | ...
A → BC | XD | ...
B → YS | b
D → XY
X → a
Y → b
# 7. Results

The program successfully:

Eliminates ε-productions
Removes unit productions
Cleans useless symbols
Converts grammar into near-CNF form

The resulting grammar follows CNF constraints:

Only binary productions (A → BC)
Only terminal productions (A → a)
# 8. Conclusion

This laboratory work demonstrates how a Context-Free Grammar can be transformed into Chomsky Normal Form.

Through this process, the structure of the grammar becomes more regular and suitable for parsing algorithms.

Key concepts learned:

Grammar simplification techniques
Role of ε-productions and unit productions
Importance of CNF in parsing
Step-by-step normalization of grammars

This lab strengthens understanding of formal languages and prepares for advanced topics such as parsing algorithms.

# 9. References
Formal Languages and Automata Theory course materials
Lecture notes on Context-Free Grammars
Python documentation







# Laboratory Work 6
## Lexical Analysis, Parsing and Abstract Syntax Tree Construction

---

# 1. Introduction

This laboratory work focused on the implementation of a simple compiler front-end component capable of performing lexical analysis, syntactic analysis, and Abstract Syntax Tree (AST) generation.

Parsing is an important stage in compiler construction and programming language processing. It transforms raw input text into a structured representation that can later be interpreted, analyzed, or compiled. In this work, a recursive descent parser was implemented together with a lexer that uses regular expressions for token recognition.

The project demonstrates the fundamental stages of language processing:
- Lexical Analysis
- Token Classification
- Syntax Analysis
- AST Construction

---

# 2. Objectives

The objectives of this laboratory work were:

- To understand the concept of parsing and syntactic analysis.
- To implement lexical analysis using regular expressions.
- To define token categories using a `TokenType` enumeration.
- To create data structures for an Abstract Syntax Tree (AST).
- To implement a parser capable of extracting syntactic information from input expressions.
- To understand how compiler front-end components operate together.

---

# 3. Theoretical Background

## 3.1 Lexical Analysis

Lexical analysis is the first phase of a compiler or interpreter. During this stage, the input text is divided into smaller units called tokens.

Examples of tokens include:
- Identifiers
- Numbers
- Operators
- Parentheses
- Keywords

For example, the expression:

#
x = 5 + 3

is transformed into:

IDENTIFIER ASSIGN NUMBER PLUS NUMBER

The lexer implemented in this laboratory uses regular expressions to identify token types.

## 3.2 Parsing

Parsing is the process of analyzing the syntactic structure of a sequence of tokens according to grammar rules.

The parser verifies that the input follows valid syntax and constructs a hierarchical representation of the expression.

In this work, recursive descent parsing was used because it is:

simple,
readable,
easy to implement for small grammars.
## 3.3 Abstract Syntax Tree (AST)

An Abstract Syntax Tree is a hierarchical representation of program structure.

Unlike a parse tree, the AST omits unnecessary grammar symbols and keeps only the logical structure of expressions.

For example:

5 + 3 * 2

produces the AST:

      +
     / \
    5   *
       / \
      3   2

The AST preserves operator precedence and expression hierarchy.

# 4. Technologies Used

The implementation was developed in Python.

The following libraries/modules were used:

Module	Purpose
re	Regular expression processing
enum	Definition of token types
# 5. Program Structure

The application was divided into several main components:

## 5.1 TokenType Enumeration

A TokenType enumeration was created to classify all possible token categories.

Example token types:

NUMBER
IDENTIFIER
PLUS
MINUS
MULTIPLY
DIVIDE
ASSIGN
LPAREN
RPAREN

This improves readability and simplifies parser implementation.

## 5.2 Token Class

A Token class was implemented to store:

token type
token value

Example:

Token(TokenType.NUMBER, 5)
## 5.3 Lexer

The lexer performs lexical analysis using regular expressions.

Its responsibilities include:

scanning the input text,
matching patterns,
generating tokens,
ignoring whitespace,
reporting invalid characters.

Example regex rules:

r'\d+'                 # Numbers
r'[A-Za-z_][A-Za-z0-9_]*'   # Identifiers
r'\+'                  # Plus operator
## 5.4 AST Nodes

Several AST node classes were implemented:

Node	Purpose
NumberNode	Stores numeric values
IdentifierNode	Stores variable names
BinaryOperationNode	Represents operations
AssignmentNode	Represents assignment expressions

These nodes form the hierarchical AST structure.

## 5.5 Parser

The parser uses recursive descent parsing.

The grammar implemented was:

assignment -> IDENTIFIER = expression
expression -> term ((+|-) term)*
term -> factor ((*|/) factor)*
factor -> NUMBER | IDENTIFIER | (expression)

The parser:

validates syntax,
respects operator precedence,
builds the AST.
# 6. Program Execution
Example Input
x = 5 + 3 * 2
Generated Tokens
Token(TokenType.IDENTIFIER, x)
Token(TokenType.ASSIGN, =)
Token(TokenType.NUMBER, 5)
Token(TokenType.PLUS, +)
Token(TokenType.NUMBER, 3)
Token(TokenType.MULTIPLY, *)
Token(TokenType.NUMBER, 2)
Token(TokenType.EOF, None)
Generated AST
Assign(Identifier(x) = (Number(5) + (Number(3) * Number(2))))

This output confirms that multiplication has higher precedence than addition.

# 7. Advantages of the Implementation

The implemented solution has several advantages:

Clear separation between lexer and parser.
Use of regular expressions simplifies token recognition.
Recursive descent parsing is easy to understand.
AST representation simplifies future semantic analysis.
Modular structure allows future expansion.
# 8. Possible Improvements

The project can be extended with:

support for floating point numbers,
support for functions,
support for conditional statements,
semantic analysis,
symbol tables,
AST visualization,
interpretation or code generation.
# 9. Conclusion

In this laboratory work, a complete miniature parsing system was implemented.

The developed program successfully:

performs lexical analysis,
categorizes tokens using regular expressions,
parses arithmetic expressions,
constructs an Abstract Syntax Tree.

The laboratory provided practical understanding of compiler front-end architecture and demonstrated how syntax analysis is performed internally in programming language processors.

The implementation also demonstrated the importance of AST structures in representing program logic and preserving operator precedence.

# 10. References
Aho, A. V., Lam, M. S., Sethi, R., Ullman, J. D. — Compilers: Principles, Techniques, and Tools.
Python Documentation — re module.
Recursive Descent Parsing Concepts.
Abstract Syntax Tree Fundamentals.