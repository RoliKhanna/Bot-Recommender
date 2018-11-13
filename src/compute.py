
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
S1 = ["While the tf–idf normalization is often very useful, there might be cases where the binary occurrence markers might offer better features. This can be achieved by using the binary parameter of CountVectorizer. In particular, some estimators such as Bernoulli Naive Bayes explicitly model discrete boolean random variables. Also, very short texts are likely to have noisy tf–idf values while the binary occurrence info is more stable."]
S2 = ["This world is an amazing and beautiful place"]

def tf_idf():
    # Calculates TF-IDF of corpus
    vectorizer = TfidfVectorizer()
    response1 = vectorizer.fit_transform(S1)    #TF-IDF Sparse matrix of document S1
    response2 = vectorizer.fit_transform(S2)    #TF-IDF Sparse matrix of document S2
    score = cosine_similarity(response1, response2)
    print("Cosine similarity between two corpi: ", score)

def intelligenceScore():

    intelligence = w1*rootTerms*L1 + w2*L2 + w3*L3 - w4*L4

tf_idf()
