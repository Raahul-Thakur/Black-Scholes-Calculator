import streamlit as st

def add_tooltips():
    """
    Add detailed tooltips for financial terms to help users understand key concepts.
    """
    st.sidebar.markdown("## Tooltips: Financial Terms")
    
    st.sidebar.markdown("""
    ### **Option Pricing Terms**
    - **Call Option**: A financial contract that gives the buyer the right, but not the obligation, to buy an underlying asset at a specified price (strike price) within a certain time period.
    - **Put Option**: A financial contract that gives the buyer the right, but not the obligation, to sell an underlying asset at a specified price (strike price) within a certain time period.
    - **Strike Price**: The price at which the buyer of the option can exercise their right to buy (call) or sell (put) the underlying asset.
    - **Expiration**: The date on which the option contract expires.
    - **Premium**: The cost of purchasing an option, paid by the buyer to the seller.

    ### **Greeks: Sensitivities of Option Prices**
    - **Delta**: Measures how much the price of an option changes when the price of the underlying asset changes. 
      - **Interpretation**: A Delta of 0.5 means the option price will change by $0.50 for every $1 change in the underlying asset.
    - **Gamma**: Measures the rate of change of Delta with respect to the price of the underlying asset. 
      - **Interpretation**: Gamma is important for assessing the stability of Delta and the responsiveness of the option to price changes.
    - **Theta**: Measures the sensitivity of the option price to the passage of time, also known as "time decay."
      - **Interpretation**: Negative Theta indicates the option loses value as time passes.
    - **Vega**: Measures the sensitivity of the option price to changes in volatility of the underlying asset.
      - **Interpretation**: A Vega of 0.2 means the option price will change by $0.20 for every 1% change in volatility.
    - **Rho**: Measures the sensitivity of the option price to changes in interest rates.
      - **Interpretation**: A Rho of 0.1 means the option price will change by $0.10 for every 1% change in the risk-free rate.

    ### **Risk Metrics**
    - **Value at Risk (VaR)**: The maximum loss expected over a given time period with a specified confidence level.
      - **Example**: A daily VaR of $1,000 at 95% confidence means there is a 5% chance of losing more than $1,000 in a day.
    - **Conditional Value at Risk (CVaR)**: The average loss in scenarios where the loss exceeds the VaR threshold.
      - **Use Case**: Provides a more comprehensive risk assessment by focusing on extreme losses.

    ### **Volatility**
    - **Implied Volatility**: The market's expectation of the future volatility of the underlying asset, derived from the option price.
    - **Historical Volatility**: The actual observed volatility of the underlying asset over a past period.
    - **Volatility Smile**: A graphical representation of implied volatility across strike prices, showing a "smile" shape.

    ### **Common Option Strategies**
    - **Straddle**: A strategy involving the purchase of both a call and a put option at the same strike price and expiration, used to profit from large price movements.
    - **Strangle**: Similar to a straddle but involves options with different strike prices, typically cheaper than a straddle.
    - **Butterfly Spread**: A neutral strategy combining multiple options to profit from low volatility.
    - **Collar**: A hedging strategy combining a long position in the underlying asset, a protective put, and a short call.

    ### **Key Financial Terms**
    - **Risk-Free Rate**: The theoretical return on an investment with zero risk, typically associated with government bonds.
    - **Time to Maturity**: The remaining time until the option expires.
    - **Underlying Asset**: The asset (e.g., stock, index) on which the option is based.

    ### **Advanced Topics**
    - **Delta Hedging**: A strategy that involves buying or selling the underlying asset to offset the Delta risk of an options position.
    - **Stochastic Volatility Models**: Models (e.g., Heston) that account for changing volatility over time, providing more realistic pricing for certain options.
    - **Monte Carlo Simulation**: A method of simulating a range of possible outcomes by repeatedly randomizing inputs to a pricing model.
    """)

    st.sidebar.info("Hover over or click on these terms in the app for detailed explanations!")
