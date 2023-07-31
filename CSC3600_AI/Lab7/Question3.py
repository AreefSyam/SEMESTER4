import nltk
from nltk.parse import chart, parse_cfg
from nltk.grammar import CFG

# Define your DCG rules
dcg_rules = """
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'chased' | 'ate'
"""

# Create a CFG object from your DCG rules
cfg = CFG.fromstring(dcg_rules)

# Create a parser object that can parse sentences using your DCG rules
parser = chart.ChartParser(cfg)

# Parse a sentence using your parser object
sentence = ['the', 'cat', 'chased', 'the', 'dog']
parse_trees = parser.parse(sentence)

# Print the parse trees
for tree in parse_trees:
    print(tree)