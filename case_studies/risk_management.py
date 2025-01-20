import streamlit as st

def risk_management():
    st.header("Case Study: Risk Management")
    st.write("""
    **Risk Management** focuses on identifying, analyzing, and mitigating financial risks 
    associated with market exposure.

    ### Key Metrics in Risk Management
    - **Value at Risk (VaR)**: Measures the maximum potential loss over a specific time horizon 
      with a given confidence level.
    - **Conditional Value at Risk (CVaR)**: Provides the average loss beyond the VaR threshold.
    """)

    st.subheader("Example: Using VaR and CVaR")
    st.write("""
    Suppose you manage a $1 million portfolio and calculate daily VaR and CVaR at a 95% confidence level:
    
    - **VaR**: $20,000 (5% chance of losing $20,000 or more in a day).
    - **CVaR**: $25,000 (average loss if losses exceed $20,000).
    
    ### Stress Testing
    To prepare for extreme events, consider:
    - Simulating market crashes (e.g., 2008 financial crisis).
    - Testing portfolio performance under high-volatility scenarios.
    """)

    st.subheader("Hedging as a Risk Management Tool")
    st.write("""
    Hedging strategies, such as buying options or diversifying investments, help reduce portfolio risk:
    - **Options**: Protect against downside risk or lock in potential gains.
    - **Diversification**: Spread investments across sectors to reduce exposure to a single asset class.
    """)
