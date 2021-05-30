import argparse
import re
from collections import Counter
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='target file containing lyrics to be counted', type=str, required=True)
parser.add_argument('-n', '--num', help='show only the n most frequent words (default: show all words)', type=int, default=None, required=False)

args = parser.parse_args()

lyrics = []

with open(args.file, 'r') as f:
    for line in f:
        for word in line.split():
            word = word.strip() # remove leading and trailing whitespaces
            word = re.sub('[\W_]+', '', word) # remove punctuation
            lyrics.append(word)

counts = Counter(lyrics)
counts_list = counts.most_common(args.num)

keys = [entry[0] for entry in counts_list]
values = [entry[1] for entry in counts_list]

fig = plt.figure()
plt.title('Most common words')
plt.bar(keys, values)
plt.grid(color='#a5a5a5', linestyle='--', linewidth=1, axis='y', alpha=0.7)
plt.show()