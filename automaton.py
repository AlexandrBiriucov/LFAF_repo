


class Automaton:
    def __init__(self,states,alphabet,start,final,transitions):
        # self.states=['S','R','L','FINAL']
        # self.alphabet=['a','b','c','d','e','f']
        # self.start='S'
        # self.final=["FINAL"]
        # self.transitions={
        #         ('S','a'): 'S',
        #         ('S','b'): 'S',
        #         ('S','c'): 'R',
        #         ('S','d'): 'L',
        #         ('R','d'): 'L',
        #         ('R','e'): 'FINAL',
        #         ('L','f'): 'L',
        #         ('L','e'): 'L',
        #         ('L','d'): 'FINAL'
        #     }
        self.states=states
        self.alphabet=alphabet
        self.start=start
        self.final=final
        self.transitions=transitions

        # self.transitions=transitions

# alphabet,start,final,transitions

    


    def stringBelongToLanguage(self,input_string : str):
        current_state=self.start
        for letter in input_string:
             key = (current_state, letter)
             if key in self.transitions:
                 current_state=self.transitions[key]   
             else :
                 return False
        
        return current_state in self.final
    





