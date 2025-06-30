from collections import Counter
import re

with open("sample_text.txt", "r") as file:
    text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)
    word_freq = Counter(words)

print("Top 10 common words:")
print(word_freq.most_common(10))
