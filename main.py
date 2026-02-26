from grammar import Grammar




g1=Grammar()

for i in range(5):
    g1.generate_string()

# g1.generate_string()

print(g1.classify_grammar())

automaton=g1.grammar_to_automaton()

# print(automaton.states,automaton.alphabet,automaton.start,automaton.final,automaton.transitions)



test_words = ["abce", "bbb", "dffd", "de"]
for word in test_words:
    print(word, "->", automaton.stringBelongToLanguage(word))



