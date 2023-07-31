import nltk
from nltk.parse import chart, parse_cfg
from nltk.grammar import CFG

# Define the CFG rules
cfg_rules = """
    S -> NP VP
    NP -> Det Noun | Noun
    VP -> Verb NP | Verb NP PP
    PP -> Prep NP
    Det -> 'a' | 'an' | 'the' | 'these' | 'some'
    Noun -> 'flight' | 'flights' | 'reservation' | 'reservations'
    Verb -> 'book' | 'reserve' | 'cancel'
    Prep -> 'from' | 'to' | 'on' | 'at'
"""

# Define the DCG rules
dcg_rules = """
    s(S) --> np(NP), vp(VP).
    np(NP) --> det(Det), noun(Noun).
    np(NP) --> noun(Noun).
    vp(VP) --> verb(Verb), np(NP).
    vp(VP) --> verb(Verb), np(NP), pp(PP).
    pp(PP) --> prep(Prep), np(NP).
    det(Det) --> ['a'] | ['an'] | ['the'] | ['these'] | ['some'].
    noun(Noun) --> ['flight'] | ['flights'] | ['reservation'] | ['reservations'].
    verb(Verb) --> ['book'] | ['reserve'] | ['cancel'].
    prep(Prep) --> ['from'] | ['to'] | ['on'] | ['at'].
"""

# Create the CFG and DCG parsers
cfg_parser = nltk.ChartParser(nltk.CFG.fromstring(cfg_rules))
dcg_parser = nltk.ChartParser(nltk.DCG.fromstring(dcg_rules))

# Read the tokenized sentences from ATIS_list.txt file
tokenized_sentences = []
with open('ATIS_list.txt', 'r') as file:
    for line in file:
        tokens = nltk.word_tokenize(line.strip()[1:-1])
        tokenized_sentences.append(tokens)

# Parse the tokenized sentences using CFG
print("CFG Parsing:")
for sentence in tokenized_sentences:
    for tree in cfg_parser.parse(sentence):
        print(tree)

# Parse the tokenized sentences using DCG
print("DCG Parsing:")
for sentence in tokenized_sentences:
    for tree in dcg_parser.parse(sentence):
        print(tree)
