import re
import string
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

text=input("enter the noisy text: \n")
text=text.lower()
text=re.sub(r'\d+',' ',text)
text=text.translate(str.maketrans('','',string.punctuation))
stop_words= set(stopwords.words('english'))
words=text.split()
clean_words=[word for word in words if word not in stop_words]
clean_text=" ".join(clean_words)

print("required clean text :",clean_text)