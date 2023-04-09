import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    
    statistic, pvalue = ks_2samp(x, y)
    return pvalue < alpha
