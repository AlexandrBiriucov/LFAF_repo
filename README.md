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
**Author:** Alexander Biriucov
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





