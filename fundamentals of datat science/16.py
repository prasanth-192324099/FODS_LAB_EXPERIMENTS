from collections import Counter
import re

reviews = [
    "This product is excellent and easy to use.",
    "Easy to use and very effective.",
    "Not satisfied. Poor quality.",
    "Excellent quality and value for money!"
]

all_text = " ".join(reviews).lower()
words = re.findall(r'\b\w+\b', all_text)
word_freq = Counter(words)

print("Word Frequency in Reviews:")
print(word_freq.most_common(10))