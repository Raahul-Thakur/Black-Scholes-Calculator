import numpy as np
from scipy.stats import norm

def heston_model(S, K, T, r, v0, kappa, theta, sigma, rho, option_type='call', n_simulations=10000):
    """
    Heston Model for option pricing using Monte Carlo simulation.

    Parameters:
    - S (float): Initial stock price
    - K (float): Strike price
    - T (float): Time to maturity (in years)
    - r (float): Risk-free interest rate
    - v0 (float): Initial variance of the stock
    - kappa (float): Rate at which variance reverts to its long-term mean
    - theta (float): Long-term mean variance
    - sigma (float): Volatility of volatility (how variance fluctuates)
    - rho (float): Correlation between the stock price and its variance
    - option_type (str): 'call' or 'put'
    - n_simulations (int): Number of Monte Carlo simulations

    Returns:
    - float: Estimated option price
    """
    dt = T / 252  # Daily time step
    n_steps = int(T * 252)
    prices = np.zeros(n_simulations)

    for i in range(n_simulations):
        # Initialize stock price and variance
        St = S
        vt = v0

        for _ in range(n_steps):
            # Generate correlated Brownian motions
            dW1 = np.random.normal(0, np.sqrt(dt))
            dW2 = rho * dW1 + np.sqrt(1 - rho**2) * np.random.normal(0, np.sqrt(dt))

            # Update variance using the CIR process
            vt = max(vt + kappa * (theta - vt) * dt + sigma * np.sqrt(max(vt, 0)) * dW2, 0)

            # Update stock price
            St *= np.exp((r - 0.5 * vt) * dt + np.sqrt(vt) * dW1)

        # Calculate payoff
        if option_type == 'call':
            prices[i] = max(St - K, 0)
        elif option_type == 'put':
            prices[i] = max(K - St, 0)

    # Discount the average payoff to present value
    return np.exp(-r * T) * np.mean(prices)


def sabr_model(S, K, T, alpha, beta, rho, nu, option_type='call'):
    """
    SABR Model for implied volatility calculation.

    Parameters:
    - S (float): Underlying asset price
    - K (float): Strike price
    - T (float): Time to maturity (in years)
    - alpha (float): Volatility of volatility
    - beta (float): Elasticity parameter (0 for log-normal, 1 for normal)
    - rho (float): Correlation between the underlying asset and its volatility
    - nu (float): Volatility of the volatility
    - option_type (str): 'call' or 'put'

    Returns:
    - float: Estimated option price using SABR implied volatility
    """
    F = S  # Forward price
    if F == K:
        sigma = alpha / (F ** (1 - beta))  # ATM case
    else:
        z = (nu / alpha) * (F ** (1 - beta) - K ** (1 - beta)) / (1 - beta)
        x_z = np.log((np.sqrt(1 - 2 * rho * z + z**2) + z - rho) / (1 - rho))
        sigma = alpha * z / x_z / (F ** (1 - beta))

    # Black-Scholes formula for final pricing
    d1 = (np.log(S / K) + (0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-0.5 * T) * norm.cdf(d2)
    else:
        return K * np.exp(-0.5 * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


# Example usage
if __name__ == "__main__":
    # Heston Model Example
    heston_price = heston_model(
        S=100, K=100, T=1, r=0.05, v0=0.04, kappa=2.0,
        theta=0.04, sigma=0.2, rho=-0.7, option_type='call'
    )
    print(f"Heston Model Option Price: {heston_price:.2f}")

    # SABR Model Example
    sabr_price = sabr_model(
        S=100, K=100, T=1, alpha=0.2, beta=0.5, rho=-0.3, nu=0.4, option_type='call'
    )
    print(f"SABR Model Option Price: {sabr_price:.2f}")
