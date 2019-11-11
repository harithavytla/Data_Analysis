def mysvd(A):
    S_points = np.dot(A, A.T)
    A_c = A-np.mean(A, axis= 0)
    S_attributes = np.dot(A_c.T, A_c)/(A.shape[0])
   
    ## U and delta
    w, U = np.linalg.eigh(S_points)
    w_id = w.argsort()[::-1]  
    w = w[w_id]
    U = U[:, w_id]
    diagonal = np.nonzero(w)
    w_diagonal = w[diagonal].copy()
    w_diagonal=np.diag(w_diagonal)
    print w_diagonal.shape
    S = np.zeros_like(A).astype(np.float64)
    print S.shape
    S[:w_diagonal.shape[0],:w_diagonal.shape[1]] = w_diagonal[:A.shape[0], :A.shape[1]]
   
    ## V
    W, V = np.linalg.eigh(S_attributes)
    W_id = W.argsort()[::-1]  
    W = W[W_id]
    V = V[:,W_id]
   
    return U, S, V