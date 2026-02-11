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