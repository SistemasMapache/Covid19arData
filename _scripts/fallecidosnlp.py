from bs4 import BeautifulSoup
import spacy

#beautifulsoup
with open("fallecidos.txt") as f:
    soup = BeautifulSoup(f.read(),features="lxml")
text = soup.get_text(strip=True)

#text
text = text.replace('Ciudad de Buenos Aires','')
text = text.replace(' (CABA)','CABA')
text = text.replace('\n',' ')
text = text.replace('  ',' ')

print ('-')
print (text)
print ('-')

# spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp(text)
sentences = list(doc.sents)

y = 1
for sent in sentences:
    print('---')
    print (y) 
    print(sent)
    print('--')    
    for token in sent:
        print(token.text, token.ent_type, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)    
    y = y + 1
