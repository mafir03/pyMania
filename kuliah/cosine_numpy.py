import numpy as np
from numpy.linalg import norm
def hitung_kemiripan(kal1,kal2):
    X_Y_set = set(kal1).union(set(kal2)) 
    if len(X_Y_set) >= 1:
        li_1 = []
        li_2 = []
        arr = np.array(kal1)
        arr2 = np.array(kal2)
        for i in X_Y_set:
            count = np.count_nonzero(arr == i)
            li_1.append(count)
            count2 = np.count_nonzero(arr2 == i)
            li_2.append(count2)
        A = np.array(li_1)
        B = np.array(li_2)
        nilai_cosine = np.dot(A,B)/(norm(A)*norm(B)) # cosine_similarity_formula
    else:
        nilai_cosine = 0
    return nilai_cosine

teks1 = ['Julie', 'loves', 'me', 'more', 'than', 'Linda', 'loves', 'me']
teks2 = ['Jane', 'likes', 'me', 'more', 'than', 'Julie', 'loves', 'me']
print(hitung_kemiripan(teks1,teks2))

