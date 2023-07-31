import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
from nltk import CFG

# Read the text file
text_file = "D:\VISUAL STUDIO CODE\PYTHON\CSC3600_AI\Lab7\ATIS.txt"
with open(text_file, 'r') as file:
    text = file.read()

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

# Initialize CFG and DCG rules
cfg_rules = []
dcg_rules = []

# Iterate over each sentence
for sentence in sentences:
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Perform part-of-speech (POS) tagging
    tagged_words = nltk.pos_tag(words)

    # Convert the POS tags to simplified form (e.g., Noun, Verb, Adjective)
    simplified_tags = [(word, nltk.map_tag('en-ptb', 'universal', tag)) for word, tag in tagged_words]

    # Extract constituents and grammatical relations based on the simplified tags
    constituents = [tag for word, tag in simplified_tags]
    relations = [(constituents[i], constituents[i + 1]) for i in range(len(constituents) - 1)]

    # Build CFG rules
    cfg_rules.extend([(constituents[i], (constituents[i + 1],)) for i in range(len(constituents) - 1)])

    # Build DCG rules
    dcg_rules.extend([(constituents[i], (constituents[i + 1],)) for i in range(len(constituents) - 1)])

# Remove duplicate rules
cfg_rules = list(set(cfg_rules))
dcg_rules = list(set(dcg_rules))

# Print CFG rules
print("Context-Free Grammar (CFG) Rules:")
for rule in cfg_rules:
    print(f"{rule[0]} -> {' '.join(rule[1])}")

# Print DCG rules
print("\nDefinite Clause Grammar (DCG) Rules:")
for rule in dcg_rules:
    print(f"{rule[0]} --> {' '.join(rule[1])}")