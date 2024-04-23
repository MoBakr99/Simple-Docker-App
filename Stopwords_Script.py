# Importing the required libraries
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Installing the necessary NLTK data (stop words) if not exist
try:
    nltk.data.find('corpora/stopwords.zip')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
# nltk.download('punkt')
# if not nltk.data.find('corpora/stopwords.zip') or not nltk.data.find('tokenizers/punkt'):
#     nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Reading the file
with open(r"D:\\01 STUDY\\Visual Studio Code\\Python_Projects\\Assignments\\Docker cloud Ass\\random_paragraphs.txt", 'r') as file:
    text = file.read().lower()

words = nltk.word_tokenize(text)

# Removing unnecessary characters
filtered = [word for word in words if not word in ["(", ")", "[", "]", "{", "}", ",", ".", "\"","\'", "/", "\\"]]

# Removing the stop words
filtered_words = [word for word in filtered if word.isalnum() and word not in stop_words]

# Counting the frequency of each word
word_freq = Counter(filtered_words)

for word, count in word_freq.items():
    print(f'{word} : {count}')