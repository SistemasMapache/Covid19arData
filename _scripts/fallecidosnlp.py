from bs4 import BeautifulSoup
import spacy
import pandas as pd

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

y = 0

df = pd.DataFrame( columns = ['id','sentence','text' , 'ent_type', 'lemma_', 'pos_', 'tag_', 'dep_', 'shape_', 'is_alpha', 'is_stop']) 

for sent in sentences:
    print('---')
    print (y) 
    print(sent)
    print('--')    
    for attr in sent:
        print(
        attr.i,
        attr.text, 
        attr.ent_type, 
        attr.lemma_, 
        attr.pos_, 
        attr.tag_, 
        attr.dep_, 
        attr.shape_, 
        attr.is_alpha, 
        attr.is_stop
        )
        df.loc[attr.i] = [attr.i, sent, attr.text, attr.ent_type, attr.lemma_, attr.pos_, attr.tag_, attr.dep_, attr.shape_, attr.is_alpha, attr.is_stop]
    y = y + 1
print(df)

