# put your code here.
from sys import argv
from string import punctuation

def word_count(filename):
    with open(filename) as f:
        
        word_count = {}

        for line in f:
            words = line.split()

            for word in words:
                format_word = word.strip(punctuation).lower()
                word_count[format_word] = word_count.get(format_word, 0) +1

        for item in word_count.items():
            print item[0], item[1]


for filename in argv[1:]:
    word_count(filename)
