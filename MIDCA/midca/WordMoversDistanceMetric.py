from nltk.corpus import stopwords
from nltk import download

download('stopwords')

sentence_1 = "Stack the red block on the green block."
sentence_2 = "Please put the red block on the green block."
# sentence_3 = "Get the red block and place it on the green block"
sentence_3 = "Hello I am sam, is there a way to california."
print("-------------------------------------------------------")
print(sentence_1)
print(sentence_2)
print(sentence_3)

stop_words = stopwords.words('english')

sentence_1 = [word for word in sentence_1.lower().split() if word not in stop_words]
sentence_2 = [word for word in sentence_2 .lower().split()if word not in stop_words]
sentence_3 = [word for word in sentence_3 .lower().split()if word not in stop_words]
print("-------------------------------------------------------")
print(sentence_1)
print(sentence_2)
print(sentence_3)

import gensim
# from gensim.models import Word2Vec

# Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary = True)

distance12 = model.wmdistance(sentence_1,sentence_2)
distance13 = model.wmdistance(sentence_1,sentence_3)
distance23 = model.wmdistance(sentence_2,sentence_3)
print("-------------------------------------------------------")
print(distance12-1.0)
print(distance13-1.0)
print(distance23-1.0)
print("---------------------------------------------------")
