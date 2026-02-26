# Variant 2:
# VN={S, R, L}, 
# VT={a, b, c, d, e, f},
# P={ 
#     S → aS
#     S → bS
#     S → cR
#     S → dL
#     R → dL
#     R → e
#     L → fLZ
#     L → eL
#     L → d
# }

import random
from automaton import Automaton
class Grammar:
    def __init__(self):
        self.VN=['S','R','L']
        self.VT=['a','b','c','d','e','f']
        self.Rules = {
        'S': ['aS', 'bS', 'cR', 'dL'],
        'R': ['dL', 'e'],
        'L': ['fL', 'eL', 'd']
                            }

        self.start='S'



    

    def generate_string(self):
        current=self.start

        # while any(character in self.VN for character in current):
            # print(random.choice(self.VN))
        # print(random.choice(self.VN))
        
        while any(character in self.VN for character in current):
            for i, ch in enumerate(current):
                if ch in self.VN:
                    replacement= random.choice(self.Rules[ch])
                    current=current[:i]+replacement+current[i+1:]
                    break

        
        print(current)




    def grammar_to_automaton(self):
        # autmaton=Automaton()
        automaton_states=[]
        automaton_aplhabet=[]
        # automaton_transitions={}
        for ch in self.VN:
            automaton_states.append(ch)
        
        automaton_states+=["FINAL"]
        

        for ch in self.VT:
            automaton_aplhabet.append(ch)


        automaton_start=self.start
        automaton_final=['FINAL']

        transitions = {}
        for VN,rules in self.Rules.items():
            for rule in rules:
                terminal=rule[0]
                if len(rule)==1:
                    next_state='FINAL'
                else:
                    next_state=rule[1]

                transitions[(VN,terminal)]=next_state

            

        automaton=Automaton(automaton_states,automaton_aplhabet,automaton_start,automaton_final,transitions)

        return(automaton)


        # print(automaton.states,automaton.alphabet,automaton.start,automaton.final,automaton.transitions)

    def classify_grammar(self):
        for lhs, rules in self.Rules.items():
            # check if LHS is more than 1 symbol → not Type 2/3
            if len(lhs) != 1:
                return "Type 0 or 1 (not regular)"
            for rule in rules:
                # rule can be 1 or 2 symbols max for Type 3
                if len(rule) > 2:
                    return "Type 2 (Context-Free)"
                # check if first character is a terminal
                if rule[0] not in self.VT:
                    return "Type 2 (Context-Free)"
        return "Type 3 (Regular)"



# g1=Grammar()


# g1.generate_string()


        
    
        

         

         
        








