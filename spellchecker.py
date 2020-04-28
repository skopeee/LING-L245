import sys


freq = {}


fd = open('wiki.txt', 'r')

for line in fd.readlines():
    form = line.strip('\n')

    if form not in dict:
        freq[form] = 0
        freq[form] = freq[form] + 1
            
text = sys.stdin.read()
words = text.split(' ')

for word in words:
        if word in freq:
                print(word)
        else:
                print('*' + word)

