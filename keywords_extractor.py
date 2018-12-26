import nltk
import re

from nltk.corpus import inaugural, names, words, stopwords
from nltk import FreqDist
from nltk import WordNetLemmatizer
def get_keywords(input_file):
    new_tokenized_text = []
    tokenized_text = inaugural.words(input_file)
    for word in tokenized_text:
        if word not in '.?-!:;/,' and word not in names.words():
            new_tokenized_text.append(word)
    lemmatized = []
    for token in new_tokenized_text:
        if WordNetLemmatizer().lemmatize(token) not in stopwords.words('english') and WordNetLemmatizer().lemmatize(token) in words.words('en'):
            lemmatized.append(WordNetLemmatizer().lemmatize(token))
    fd = FreqDist(lemmatized)
    return fd.most_common(20)
print(inaugural.fileids())
obama = get_keywords('2009-Obama.txt')
print(obama)



