# main.py
from automaton_variant2 import Automaton

# NDFA definition (Variant 2)
states = ['q0','q1','q2','q3','q4']
alphabet = ['a','b','c']
start = 'q0'
final = ['q4']
transitions = {
    ('q0','a'): 'q1',
    ('q1','b'): ['q2','q3'],  # non-deterministic
    ('q2','c'): 'q3',
    ('q3','a'): 'q3',
    ('q3','b'): 'q4'
}

ndfa = Automaton(states, alphabet, start, final, transitions)

# a) Convert to regular grammar
grammar = ndfa.automaton_to_grammar()
print("Regular Grammar:", grammar)

# b) Check determinism
print("Is DFA?", ndfa.is_deterministic())

# c) Convert NDFA → DFA
dfa_states, dfa_transitions, dfa_start, dfa_final = ndfa.convert_to_dfa()
print("DFA States:", dfa_states)
print("DFA Transitions:")
for k,v in dfa_transitions.items():
    print(k, "->", v)
print("DFA Start:", dfa_start)
print("DFA Final:", dfa_final)