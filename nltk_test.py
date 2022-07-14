from nltk.book import *
import nltk
text="Don't hesitate to ask questions. Be positive." 
from nltk.tokenize import sent_tokenize 
print(sent_tokenize(text))

tokenizer=nltk.data.load('tokenizers/punkt/english.pickle') 
print(tokenizer.tokenize(text))

words=nltk.word_tokenize(text) 
print(words)

from nltk.tokenize import WordPunctTokenizer 
tokenizer=WordPunctTokenizer()
words = tokenizer.tokenize(text) 
print(words)


from nltk.stem import PorterStemmer 
stemmerporter = PorterStemmer() 
print(stemmerporter.stem('happiness'))


from nltk.stem import LancasterStemmer 
stemmerlan=LancasterStemmer() 
print(stemmerlan.stem('happiness'))


text1=nltk.word_tokenize("It is a pleasant day today") 
print(nltk.pos_tag(text1))


print(text.lower()) 
print(text.upper())

from nltk.corpus import stopwords 
stops=set(stopwords.words('english'))
words = [word for word in words if word.lower() not in stops] 
print(words)












