import streamlit as st

def volatility_trading():
    st.header("Case Study: Volatility Trading")
    st.write("""
    **Volatility Trading** involves strategies that capitalize on changes in the volatility of an 
    underlying asset rather than its price direction.

    ### Why Trade Volatility?
    Volatility traders seek to:
    - Profit from large price movements in either direction.
    - Hedge against unexpected market events.
    """)

    st.subheader("Example: Straddle Strategy")
    st.write("""
    A **straddle** involves buying both a call and a put option with the same strike price and expiration date.

    #### Scenario:
    - **Stock Price**: $100
    - **Strike Price**: $100
    - **Premiums**: $5 for call, $5 for put
    - **Total Cost**: $10 per straddle

    ### Payoff Scenarios:
    1. **Stock Price Falls to $80**:
       - Gain on put: $20 - $10 (total premium) = $10.
       - Call expires worthless.
       - **Net Profit**: $10.
    2. **Stock Price Rises to $120**:
       - Gain on call: $20 - $10 (total premium) = $10.
       - Put expires worthless.
       - **Net Profit**: $10.
    3. **Stock Price Remains at $100**:
       - Both options expire worthless.
       - **Net Loss**: $10 (total premium).

    ### Pros and Cons
    **Pros**:
    - Profits from significant price movements in either direction.
    - Limited downside risk (loss is limited to the total premium).

    **Cons**:
    - Requires large price movements to be profitable.
    - High cost due to purchasing two options.
    """)
