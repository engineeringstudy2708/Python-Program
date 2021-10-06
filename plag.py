import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

original_file = [doc for doc in os.listdir() if doc.endswith('.txt')]
converted_file = [open(_file, encoding='utf-8').read()
                 for _file in original_file]

def check_plagiarism():
    
    global s_vectors
    
    for original_a, text_vector_a in s_vectors:
    
        new_vectors = s_vectors.copy()
    
        current_index = new_vectors.index((original_a, text_vector_a))
    
        del new_vectors[current_index]
    
        for original_b, text_vector_b in new_vectors:
    
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
    
            student_pair = sorted((original_a, original_b))
    
            score = (student_pair[0], student_pair[1], sim_score)
    
            plagiarism_results.add(score)
    
    return plagiarism_results

def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

vectors = vectorize(converted_file)

s_vectors = list(zip(original_file, vectors))

plagiarism_results = set()

for data in check_plagiarism():

    print(data)