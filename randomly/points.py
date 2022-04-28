"""
random x,y point
"""
import numpy as np
from scipy.stats import poisson, uniform
from typing import Tuple


def generate_poisson_points(
    bounds: Tuple[float, float, float, float], rate: float
) -> np.ndarray:
    """Generate poisson distribution of points between a lower and upper bound.

    Args:
        bounds: [dx_lower, dy_lower, dx_upper, dy_upper]
        rate: float

    Returns: Array containing

    """
    dx = bounds[2] - bounds[0]
    dy = bounds[3] - bounds[1]

    N = poisson(rate * dx * dy).rvs()
    xs = uniform.rvs(0, dx, ((N, 1))) + bounds[0]
    ys = uniform.rvs(0, dy, ((N, 1))) + bounds[1]

    return np.hstack((xs, ys))
