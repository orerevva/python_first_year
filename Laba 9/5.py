import numpy as np
from scipy.linalg import inv, det
from scipy.stats import multivariate_normal
import time

def log_multivariate_normal_pdf(X, m, C):
    D = m.shape[0]  # Размерность пространства
    N = X.shape[0]  # Количество точек
    
    # 1. Вычисляем разницу X - m
    diff = X - m  # shape (N, D)
    
    # 2. Вычисляем обратную матрицу ковариации и её определитель
    inv_C = inv(C)  # shape (D, D)
    det_C = det(C)
    
    # 3. Вычисляем константу нормализации
    log_const = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C))
    
    # 4. Вычисляем квадратичную форму: (X-m)^T @ C^{-1} @ (X-m)
    # Эффективное вычисление через (diff @ inv_C) * diff
    quad_form = np.sum((diff @ inv_C) * diff, axis=1)  # shape (N,)
    
    # 5. Вычисляем итоговый логарифм плотности
    log_pdf = log_const - 0.5 * quad_form
    
    return log_pdf

def compare_with_scipy():
    # Генерируем тестовые данные
    np.random.seed(42)
    D = 3  # Размерность
    N = 10000  # Количество точек
    m = np.random.randn(D)
    
    # Генерируем положительно определённую матрицу ковариации
    C = np.random.randn(D, D)
    C = C @ C.T + np.eye(D) * 0.1  # Добавляем диагональную нагрузку
    
    X = np.random.randn(N, D)
    
    # Наша реализация
    start = time.time()
    our_logpdf = log_multivariate_normal_pdf(X, m, C)
    our_time = time.time() - start
    
    # Реализация SciPy
    start = time.time()
    scipy_logpdf = multivariate_normal(mean=m, cov=C).logpdf(X)
    scipy_time = time.time() - start
    
    # Сравнение результатов
    max_diff = np.max(np.abs(our_logpdf - scipy_logpdf))
    mean_diff = np.mean(np.abs(our_logpdf - scipy_logpdf))
    
    print(our_time)
    print(scipy_time)
    print(max_diff)
    print(mean_diff)

if __name__ == "__main__":
    compare_with_scipy()