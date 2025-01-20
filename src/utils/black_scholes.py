import numpy as np
from scipy.stats import norm

def calculate_black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate Black-Scholes option price
    """
    epsilon = 1e-10  # Small value to prevent division by zero
    S = max(S, epsilon)
    K = max(K, epsilon)
    T = max(T, epsilon)
    sigma = max(sigma, epsilon)

    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return option_price
