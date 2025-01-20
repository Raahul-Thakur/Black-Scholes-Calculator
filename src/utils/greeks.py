import numpy as np
from scipy.stats import norm

def calculate_greeks(S, K, T, r, sigma):
    """
    Calculate option Greeks (Delta, Gamma, Theta, Vega, Rho).

    Parameters:
    S: Stock price
    K: Strike price
    T: Time to maturity (in years)
    r: Risk-free interest rate
    sigma: Volatility

    Returns:
    Dictionary of Greeks.
    """
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    return {
        'delta': norm.cdf(d1),
        'gamma': norm.pdf(d1) / (S * sigma * np.sqrt(T)),
        'theta': (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                  - r * K * np.exp(-r * T) * norm.cdf(d2)),
        'vega': S * np.sqrt(T) * norm.pdf(d1),
        'rho': K * T * np.exp(-r * T) * norm.cdf(d2)
    }
