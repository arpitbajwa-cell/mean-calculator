import numpy as np


def calculate(lst):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    
    m = np.array(lst).reshape(3, 3)
    
    return {
        'mean': [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), m.mean()],
        'variance': [m.var(axis=0).tolist(), m.var(axis=1).tolist(), m.var()],
        'standard deviation': [m.std(axis=0).tolist(), m.std(axis=1).tolist(), m.std()],
        'max': [m.max(axis=0).tolist(), m.max(axis=1).tolist(), m.max()],
        'min': [m.min(axis=0).tolist(), m.min(axis=1).tolist(), m.min()],
        'sum': [m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), m.sum()]
    }
