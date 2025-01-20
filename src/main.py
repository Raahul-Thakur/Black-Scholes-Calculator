import streamlit as st
import numpy as np
from utils.black_scholes import calculate_black_scholes, calculate_pnl
from utils.visualization import create_price_matrix, create_heatmap, create_pnl_chart

def main():
    st.set_page_config(page_title="Black-Scholes Option Calculator", layout="wide")
    st.title("Black-Scholes Option Calculator")

    # Input parameters
    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Stock Price ($)", min_value=0.0, value=100.0, step=1.0)
        K = st.number_input("Strike Price ($)", min_value=0.0, value=100.0, step=1.0)
        T = st.number_input("Time to Maturity (years)", min_value=0.0, value=1.0, step=0.1)

    with col2:
        r = st.number_input("Risk-free Rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
        sigma = st.number_input("Volatility (%)", min_value=0.0, value=20.0, step=1.0) / 100
        option_type = st.selectbox("Option Type", ['call', 'put'])

    # Calculate option prices
    call_price = calculate_black_scholes(S, K, T, r, sigma, 'call')
    put_price = calculate_black_scholes(S, K, T, r, sigma, 'put')

    # Display results
    st.header("Option Prices")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Call Option Price", f"${call_price:.2f}")
    with col2:
        st.metric("Put Option Price", f"${put_price:.2f}")

    # Create sensitivity analysis
    st.header("Price Sensitivity Analysis")
    S_range = np.linspace(max(0, S-50), S+50, 50)
    sigma_range = np.linspace(max(0.05, sigma-0.2), sigma+0.2, 50)
    
    prices = create_price_matrix(S_range, sigma_range, K, T, r, option_type)
    fig = create_heatmap(prices, S_range, sigma_range, option_type)
    st.plotly_chart(fig)

    # P&L analysis
    st.header("Profit/Loss Analysis")
    spot_prices = np.linspace(max(0, S-50), S+50, 100)
    current_price = call_price if option_type == 'call' else put_price
    pnl = calculate_pnl(spot_prices, K, current_price, option_type)
    
    fig_pnl = create_pnl_chart(spot_prices, pnl, option_type)
    st.plotly_chart(fig_pnl)

if __name__ == "__main__":
    main()