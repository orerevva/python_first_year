import numpy as np
from scipy.linalg import inv, det
from scipy.stats import multivariate_normal
import time

def log_multivariate_normal_pdf(X, m, C):
    D = m.shape[0]  
    N = X.shape[0]  
    
    diff = X - m 
    inv_C = inv(C) 
    det_C = det(C)
    
    log_const = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C))
    
    quad_form = np.sum((diff @ inv_C) * diff, axis=1) 
    
    log_pdf = log_const - 0.5 * quad_form
    
    return log_pdf

def compare_with_scipy():
    np.random.seed(42)
    D = 3  
    N = 10000 
    m = np.random.randn(D)
    C = np.random.randn(D, D)
    C = C @ C.T + np.eye(D) * 0.1
    
    X = np.random.randn(N, D)
    
    start = time.time()
    our_logpdf = log_multivariate_normal_pdf(X, m, C)
    our_time = time.time() - start
    
    start = time.time()
    scipy_logpdf = multivariate_normal(mean=m, cov=C).logpdf(X)
    scipy_time = time.time() - start
    
    max_diff = np.max(np.abs(our_logpdf - scipy_logpdf))
    mean_diff = np.mean(np.abs(our_logpdf - scipy_logpdf))
    
    print(our_time)
    print(scipy_time)
    print(max_diff)
    print(mean_diff)

if __name__ == "__main__":
    compare_with_scipy()