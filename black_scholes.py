import numpy as np
from scipy.stats import norm

def calculate_black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

if __name__ == "__main__":
    print(calculate_black_scholes(100, 100, 1, 0.05, 0.2, 'call'))
    print(calculate_black_scholes(100, 100, 1, 0.05, 0.2, 'put'))
