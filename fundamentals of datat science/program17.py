
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("data.csv")
text = " ".join(df["feedback"].astype(str)).lower()

# Preprocess text
text = re.sub(r'[^\w\s]', '', text)
words = text.split()
filtered_words = [word for word in words if word not in stopwords.words('english')]

# Frequency distribution
word_freq = Counter(filtered_words)
top_n = 10
most_common = word_freq.most_common(top_n)

# Display
print("Top words:")
for word, freq in most_common:
    print(f"{word}: {freq}")

# Bar chart
words, freqs = zip(*most_common)
plt.bar(words, freqs)
plt.title("Top N Frequent Words")
plt.xticks(rotation=45)
plt.show()
