import numpy as np
from utils import mean_center

def fn(A, op, n) -> float:
    """
    Maximizing polarization only: \\bar{z}^T \\bar{z}
    """
    op_mean = mean_center(op, n)
    z_mean = np.dot(A, op_mean)
    return np.dot(np.transpose(z_mean), z_mean)[0, 0]
