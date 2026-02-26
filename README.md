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