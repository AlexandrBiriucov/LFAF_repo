# automaton_variant2.py
from itertools import chain, combinations

class Automaton:
    def __init__(self, states, alphabet, start, final, transitions):
        self.states = states          # list of states
        self.alphabet = alphabet      # list of symbols
        self.start = start            # start state
        self.final = final            # list of final states
        self.transitions = transitions  # dict: (state, symbol) -> list of next states

    # ---------------- a) NDFA → Regular Grammar ----------------
    def automaton_to_grammar(self):
        grammar_rules = {}
        for (state, symbol), next_states in self.transitions.items():
            if not isinstance(next_states, list):
                next_states = [next_states]  # make sure it's a list
            for next_state in next_states:
                # If next_state is final, we can generate just the symbol
                rhs = symbol if next_state in self.final else symbol + next_state
                grammar_rules.setdefault(state, []).append(rhs)
        return grammar_rules

    # ---------------- b) Check determinism ----------------
    def is_deterministic(self):
        for (state, symbol), next_states in self.transitions.items():
            if isinstance(next_states, list) and len(next_states) > 1:
                return False
        return True

    # ---------------- c) NDFA → DFA ----------------
    def convert_to_dfa(self):
        start_set = frozenset([self.start])
        dfa_states = {start_set}
        unprocessed = [start_set]
        dfa_transitions = {}
        dfa_final = []

        while unprocessed:
            current_set = unprocessed.pop()
            for symbol in self.alphabet:
                next_set = set()
                for state in current_set:
                    # get NDFA transitions
                    next_states = self.transitions.get((state, symbol), [])
                    if not isinstance(next_states, list):
                        next_states = [next_states]
                    next_set.update(next_states)
                if next_set:
                    next_fset = frozenset(next_set)
                    dfa_transitions[(current_set, symbol)] = next_fset
                    if next_fset not in dfa_states:
                        dfa_states.add(next_fset)
                        unprocessed.append(next_fset)

        # determine DFA final states
        for state_set in dfa_states:
            if any(s in self.final for s in state_set):
                dfa_final.append(state_set)

        return dfa_states, dfa_transitions, start_set, dfa_final