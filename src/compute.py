
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation
import string
import gensim
from gensim import corpora
from process import clean

# Sample documents
S1 = ["While the tf–idf normalization is often very useful, there might be cases where the binary occurrence markers might offer better features. This can be achieved by using the binary parameter of CountVectorizer. In particular, some estimators such as Bernoulli Naive Bayes explicitly model discrete boolean random variables. Also, very short texts are likely to have noisy tf–idf values while the binary occurrence info is more stable."]
S2 = ["This world is an amazing and beautiful place"]
doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

# Compiling sample documents
doc_complete = [doc1, doc2, doc3, doc4, doc5]

def tf_idf():
    # Calculates TF-IDF of corpus
    vectorizer = TfidfVectorizer()
    response1 = vectorizer.fit_transform(S1)    #TF-IDF Sparse matrix of document S1
    response2 = vectorizer.fit_transform(S2)    #TF-IDF Sparse matrix of document S2
    score = cosine_similarity(response1, response2)
    return score

def lda():
    # Models topics in the documents using LDA
    doc_clean = [clean(doc).split() for doc in doc_complete]
    dictionary = corpora.Dictionary(doc_clean)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    Lda = gensim.models.ldamodel.LdaModel
    myTopicModel = Lda(doc_term_matrix, id2word = dictionary, passes=50)
    numberOfModelTopics = len(myTopicModel.get_document_topics(doc_term_matrix))
    return numberOfModelTopics

def intelligence_score():

    intelligence = w1*rootTerms*L1 + w2*L2 + w3*L3 - w4*L4
