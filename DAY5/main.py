import re
import string
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def clean_text(text):
    text=text.lower()
    text=re.sub(r'\d+',' ',text)
    text=text.translate(str.maketrans('','',string.punctuation))

    stop_words=set(stopwords.words('english'))
    words=text.split()
    clean_words=[word for word in words if word not in stop_words]

    return" ".join(clean_words)


texts=[]
n=int(input("how many texts you want to enter:"))

for i in range(n):
    t=input(f"enter the noisy text {i+1}:")
    texts.append(t)

cleaned_texts=[]
for t in texts:
    clean=clean_text(t)
    cleaned_texts.append(clean)

for i,t in enumerate(cleaned_texts,1):
    print(f"the required clean text {i}:{t}")