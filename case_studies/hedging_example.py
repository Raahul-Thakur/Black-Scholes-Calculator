import streamlit as st

def hedging_example():
    st.header("Case Study: Portfolio Hedging")
    st.write("""
    **Hedging** is a risk management strategy designed to offset potential losses in a portfolio 
    by taking an opposite position in a related asset. 

    ### Why Hedge?
    Portfolio managers and individual investors hedge to:
    - Protect against adverse market movements.
    - Minimize risk while maintaining exposure to potential upside.
    """)

    st.subheader("Example: Hedging with Put Options")
    st.write("""
    Suppose you own 100 shares of Company XYZ, currently trading at $100 per share. You're concerned 
    about potential downside risk over the next 3 months. To hedge, you purchase put options with:
    
    - **Strike Price**: $95
    - **Premium**: $5 per option
    - **Expiration**: 3 months
    
    ### Payoff Scenarios:
    1. **Stock Price Falls to $80**: 
       - Put option exercised at $95.
       - Loss on stock: $100 - $80 = $20 per share.
       - Gain on put: $95 - $80 - $5 (premium) = $10 per share.
       - Net Loss: $20 - $10 = $10 per share.
    2. **Stock Price Rises to $110**:
       - Put option expires worthless.
       - Gain on stock: $110 - $100 = $10 per share.
       - Loss on put: $5 (premium).
       - Net Gain: $10 - $5 = $5 per share.
    """)

    st.subheader("Benefits and Drawbacks of Hedging")
    st.write("""
    **Benefits**:
    - Reduces downside risk.
    - Provides portfolio stability in volatile markets.

    **Drawbacks**:
    - Reduces upside potential due to the cost of the hedge (e.g., option premiums).
    - May require constant adjustments based on market conditions.
    """)
