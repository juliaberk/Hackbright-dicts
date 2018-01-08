# put your code here.
def word_count(filename):
    with open(filename) as f:
        
        word_count = {}

        for line in f:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) +1

        for item in word_count.items():
            print item[0], item[1]
