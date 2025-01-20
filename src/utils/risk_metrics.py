import numpy as np
from scipy.stats import norm
from .black_scholes import calculate_black_scholes

def calculate_var(S, K, T, r, sigma, option_type, confidence_level, n_simulations):
    """
    Calculate Value at Risk (VaR) using Monte Carlo simulation
    """
    np.random.seed(42)
    dt = T / 252
    n_steps = int(T * 252)

    if n_simulations <= 0 or S <= 0 or sigma <= 0 or T <= 0:
        return None  # Invalid inputs

    try:
        Z = np.random.standard_normal((n_simulations, n_steps))
        S_paths = S * np.exp(np.cumsum((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z, axis=1))
        final_values = [calculate_black_scholes(s, K, T, r, sigma, option_type) for s in S_paths[:, -1]]
        return np.percentile(final_values, (1 - confidence_level) * 100)
    except Exception as e:
        return None

def calculate_expected_shortfall(S, K, T, r, sigma, option_type, confidence_level, n_simulations):
    """
    Calculate Expected Shortfall (Conditional VaR) using Monte Carlo simulation
    """
    np.random.seed(42)
    dt = T / 252
    n_steps = int(T * 252)

    if n_simulations <= 0 or S <= 0 or sigma <= 0 or T <= 0:
        return None  # Invalid inputs

    try:
        Z = np.random.standard_normal((n_simulations, n_steps))
        S_paths = S * np.exp(np.cumsum((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z, axis=1))
        final_values = [calculate_black_scholes(s, K, T, r, sigma, option_type) for s in S_paths[:, -1]]
        var = np.percentile(final_values, (1 - confidence_level) * 100)
        return np.mean([v for v in final_values if v <= var])
    except Exception as e:
        return None
