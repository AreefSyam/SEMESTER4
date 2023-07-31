import re

# Read sentences from a file
with open("D:\VISUAL STUDIO CODE\PYTHON\CSC3600_AI\Lab7\ATIS.txt", "r") as file:
    sentences = file.readlines()

# Tokenizer function
def tokenize_sentence(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return words

# Tokenize each sentence and store the resulting lists
tokenized_sentences = [tokenize_sentence(sentence) for sentence in sentences]

# Write the lists into a file
with open("ATIS_list.txt", "w") as file:
    for sentence_tokens in tokenized_sentences:
        file.write(str(sentence_tokens) + '\n')
