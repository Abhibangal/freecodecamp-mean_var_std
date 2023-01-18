import numpy as np


def calculate(a):
        if len(a) == 9:
            b = np.array(a).reshape((3, 3))
            f = b.flatten(order='C')
            calculations = {
                'mean': [list(np.mean(b, axis=0)), list(np.mean(b, axis=1)), f.mean()],
                'variance': [list(np.var(b, axis=0)), list(np.var(b, axis=1)), f.var()],
                'standard deviation': [list(np.std(b, axis=0)), list(np.std(b, axis=1)), f.std()],
                'max': [list(np.max(b, axis=0)), list(np.max(b, axis=1)), f.max()],
                'min': [list(np.min(b, axis=0)), list(np.min(b, axis=1)), f.min()],
                'sum': [list(np.sum(b, axis=0)), list(np.sum(b, axis=1)), f.sum()]
            }
            return calculations

        else:
            raise ValueError('List must contain nine numbers.')






print(calculate([0, 1, 2, 3, 4, 5, 6, 7, ]))
