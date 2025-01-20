import streamlit as st

def add_tutorials():
    """
    Add detailed interactive tutorials using Streamlit expander.
    """

    with st.expander("What are Options?"):
        st.write("""
        Options are financial derivatives that provide the **right, but not the obligation**, 
        to buy (call) or sell (put) an underlying asset at a specified price (strike price) 
        within a certain time period.

        ### Key Terminologies:
        - **Underlying Asset**: The stock, index, or commodity the option is based on.
        - **Call Option**: Gives the buyer the right to buy the asset.
        - **Put Option**: Gives the buyer the right to sell the asset.
        - **Strike Price**: The predetermined price at which the asset can be bought (call) or sold (put).
        - **Expiration Date**: The date after which the option becomes invalid.

        ### Real-World Example:
        Imagine you pay $10 for the right to buy a stock at $100 (strike price) within a month. 
        If the stock rises to $120, you can exercise your option and profit from the $20 gain, minus the $10 premium.
        """)

    with st.expander("How to Use the Tool?"):
        st.write("""
        This application is designed to make options analysis intuitive and insightful. Here's how to get started:

        1. **Input Parameters**:
           - Enter stock price, strike price, time to maturity, risk-free rate, and volatility in the sidebar.
           - Select the option type: **Call** or **Put**.

        2. **Explore Tabs**:
           - **Option Prices**: Calculate call and put prices and analyze P&L.
           - **Greeks Analysis**: Understand Delta, Gamma, Theta, Vega, and Rho.
           - **Risk Metrics**: Assess Value at Risk (VaR) and Conditional Value at Risk (CVaR).
           - **Strategy Simulations**: Visualize common trading strategies.

        3. **Interactive Charts**:
           - Use sliders and draggable elements to dynamically adjust parameters.
           - Observe how changes affect pricing, sensitivities, and profitability.
        """)

    with st.expander("Understanding Greeks"):
        st.write("""
        Greeks measure the sensitivity of an option's price to various factors. Here's a breakdown:

        ### Key Greeks:
        - **Delta**: Measures the change in option price for a $1 change in the underlying asset price.
          - Example: A Delta of 0.5 means the option price will increase by $0.50 if the stock price rises by $1.
        - **Gamma**: Measures the rate of change of Delta with respect to the underlying price.
          - Importance: Higher Gamma indicates greater sensitivity of Delta, often seen in at-the-money options.
        - **Theta**: Measures time decay, or the rate at which the option loses value as expiration approaches.
          - Example: A Theta of -0.05 means the option loses $0.05 per day.
        - **Vega**: Measures sensitivity to changes in volatility.
          - Example: A Vega of 0.2 means the option price increases by $0.20 for a 1% increase in volatility.
        - **Rho**: Measures sensitivity to changes in interest rates.
          - Importance: Useful for long-term options where interest rate changes can have a significant impact.

        ### Visualization:
        Use the **Greeks Analysis** tab to observe how these values vary with changes in stock price, time to maturity, and volatility.
        """)

    with st.expander("What is Implied Volatility?"):
        st.write("""
        Implied Volatility (IV) reflects the market's expectation of future volatility for the underlying asset.

        ### Why is it Important?
        - **High IV**: Indicates greater uncertainty, leading to higher option prices.
        - **Low IV**: Suggests stability, leading to lower option prices.

        ### Visualization:
        Use the **Volatility Surface** feature to explore how implied volatility changes across different strike prices and maturities.
        """)

    with st.expander("Option Strategies Explained"):
        st.write("""
        Options can be used to implement various trading strategies. Here are some common ones:

        ### **1. Straddle**:
        - Buy a call and a put with the same strike price and expiration.
        - **Goal**: Profit from large price movements, regardless of direction.

        ### **2. Strangle**:
        - Buy a call and a put with different strike prices.
        - **Goal**: Similar to a straddle but cheaper, requiring larger price movements to be profitable.

        ### **3. Butterfly Spread**:
        - Combines multiple options to profit from low volatility.
        - **Goal**: Maximize profit if the stock price remains close to the middle strike price.

        ### **4. Protective Put**:
        - Buy a put to hedge against potential losses in a stock position.
        - **Goal**: Limit downside risk while maintaining upside potential.

        Use the **Strategy Simulations** tab to visualize P&L for these strategies dynamically.
        """)

    with st.expander("Risk Metrics: VaR and CVaR"):
        st.write("""
        Risk metrics help quantify and manage potential losses in a portfolio.

        ### **Value at Risk (VaR)**:
        - Measures the maximum loss expected over a specified time period with a given confidence level.
        - **Example**: A daily VaR of $1,000 at 95% confidence means there is a 5% chance of losing more than $1,000 in a day.

        ### **Conditional Value at Risk (CVaR)**:
        - Calculates the average loss in scenarios where losses exceed the VaR threshold.
        - **Use Case**: Provides a more comprehensive view of tail risks.

        ### Stress Testing:
        Use the **Risk Metrics** tab to simulate extreme market conditions and assess potential impacts on your portfolio.
        """)
