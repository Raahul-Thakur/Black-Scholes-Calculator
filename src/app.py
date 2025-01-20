import streamlit as st
import numpy as np
from src.utils.black_scholes import calculate_black_scholes
from src.utils.advanced_models import heston_model, sabr_model
from src.utils.visualization import create_interactive_heatmap, create_draggable_pnl_chart
from src.utils.greeks import calculate_greeks
from src.utils.risk_metrics import calculate_var, calculate_expected_shortfall
from src.utils.historical_data import fetch_historical_data
from src.components.tooltips import add_tooltips
import datetime
assert isinstance(datetime.date(2020, 1, 1), datetime.date)


def render_application():
    """
    Render the main application with a polished UI in permanent dark mode, including improved Greeks Analysis.
    """
    # Apply dark mode CSS
    with open("src/themes/dark_mode.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Header
    st.title("📈 Black-Scholes Calculator")
    st.markdown("""
    Welcome to the advanced Black-Scholes calculator! Use this tool to price options, analyze sensitivities, evaluate risk metrics, and compare models.
    """)

    # FAQs Section
    st.header("❓ FAQs")
    with st.expander("What are Options?"):
        st.write("""
        Options are financial derivatives that provide the right, but not the obligation, 
        to buy (call) or sell (put) an underlying asset at a specified price (strike price) on or before a certain date.
        """)

    with st.expander("What is the Black-Scholes Model?"):
        st.write("""
        The Black-Scholes model is a mathematical framework for pricing European-style options. 
        It calculates the theoretical price of options based on the stock price, strike price, volatility, time to maturity, and risk-free rate.
        """)

    with st.expander("How do I use this tool?"):
        st.write("""
        1. Enter the stock price, strike price, time to maturity, and other required parameters in the sidebar.
        2. Choose the option type (Call/Put) and select the pricing model (Black-Scholes, Heston, or SABR).
        3. Navigate through the tabs to view:
           - **Option Pricing**: Calculate the option's price.
           - **Greeks Analysis**: Analyze sensitivities like Delta, Gamma, and more.
           - **Risk Metrics**: Assess metrics like Value at Risk (VaR) and Conditional VaR (CVaR).
           - **Model Comparison**: Compare results from different pricing models.
           - **Historical Data**: Fetch and analyze historical stock data.
        """)

    # Sidebar for inputs
    with st.sidebar:
        st.header("⚙️ Parameters")
        S = st.slider("Stock Price ($)", min_value=10.0, max_value=500.0, value=100.0, step=1.0)
        K = st.slider("Strike Price ($)", min_value=10.0, max_value=500.0, value=100.0, step=1.0)
        T = st.slider("Time to Maturity (years)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        r = st.slider("Risk-Free Rate (%)", min_value=0.0, max_value=10.0, value=5.0, step=0.1) / 100
        sigma = st.slider("Volatility (%)", min_value=1.0, max_value=200.0, value=20.0, step=1.0) / 100
        option_type = st.radio("Option Type", ["Call", "Put"])
        confidence_level = st.slider("Confidence Level for Risk Metrics", 0.9, 0.99, 0.95, step=0.01)
        n_simulations = st.number_input("Monte Carlo Simulations", min_value=1000, max_value=100000, value=10000, step=1000)
        model = st.radio("Pricing Model", ["Black-Scholes", "Heston", "SABR"])
        st.markdown("---")

    if T <= 0 or sigma <= 0 or S <= 0:
        st.error("Invalid input: Ensure T, S, and sigma are greater than zero!")

    # Main Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Option Pricing", "Greeks Analysis", "Risk Metrics", "Model Comparison", "Historical Data", "Case Studies"]
    )

    # Tab 1: Option Pricing
    with tab1:
        st.subheader("📊 Option Pricing")
        if model == "Black-Scholes":
            price = calculate_black_scholes(S, K, T, r, sigma, option_type.lower())
        elif model == "Heston":
            price = heston_model(S, K, T, r, v0=0.04, kappa=2.0, theta=0.04, sigma=0.2, rho=-0.7, option_type=option_type.lower())
        elif model == "SABR":
            price = sabr_model(S, K, T, alpha=0.2, beta=0.5, rho=-0.3, nu=0.4, option_type=option_type.lower())
        
        st.metric(f"{model} {option_type} Option Price", f"${price:.2f}")

        st.markdown("### Sensitivity Heatmap")
        S_range = np.linspace(max(10, S - 50), S + 50, 50)
        sigma_range = np.linspace(max(0.05, sigma - 0.2), sigma + 0.2, 50)
        heatmap = create_interactive_heatmap(S_range, sigma_range, K, T, r, option_type.lower())
        st.plotly_chart(heatmap, use_container_width=True)

    # Tab 2: Greeks Analysis
    with tab2:
        st.subheader("📉 Greeks Analysis")
        st.markdown("Analyze the sensitivities of the option price to various factors:")

        greeks = calculate_greeks(S, K, T, r, sigma)

        # Create styled cards for each Greek
        greek_names = ["Delta", "Gamma", "Theta", "Vega", "Rho"]
        greek_values = [
            f"{greeks['delta']:.4f}",
            f"{greeks['gamma']:.4f}",
            f"{greeks['theta']:.4f}",
            f"{greeks['vega']:.4f}",
            f"{greeks['rho']:.4f}",
        ]
        greek_descriptions = [
            "Sensitivity to the stock price.",
            "Rate of change of Delta.",
            "Time decay of the option price.",
            "Sensitivity to volatility.",
            "Sensitivity to interest rates.",
        ]

        # Use columns to display metrics in a visually appealing manner
        cols = st.columns(len(greek_names))
        for col, name, value, description in zip(cols, greek_names, greek_values, greek_descriptions):
            with col:
                st.markdown(f"<h4 style='text-align: center; color: #76c7c0;'>{name}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; font-size: 18px; color: #ffffff;'><b>{value}</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; color: #aaaaaa;'>{description}</p>", unsafe_allow_html=True)

    # Tab 3: Risk Metrics
    with tab3:
        st.subheader("📊 Risk Metrics")
        var = calculate_var(S, K, T, r, sigma, option_type.lower(), confidence_level, n_simulations)
        es = calculate_expected_shortfall(S, K, T, r, sigma, option_type.lower(), confidence_level, n_simulations)
        col1, col2 = st.columns(2)
        col1.metric("Value at Risk (VaR)", f"${abs(var):.2f}")
        col2.metric("Conditional VaR (CVaR)", f"${abs(es):.2f}")

    # Tab 4: Model Comparison
    with tab4:
        st.subheader("📚 Model Comparison")
        bs_price = calculate_black_scholes(S, K, T, r, sigma, option_type.lower())
        heston_price = heston_model(S, K, T, r, v0=0.04, kappa=2.0, theta=0.04, sigma=0.2, rho=-0.7, option_type=option_type.lower())
        sabr_price = sabr_model(S, K, T, alpha=0.2, beta=0.5, rho=-0.3, nu=0.4, option_type=option_type.lower())

        col1, col2, col3 = st.columns(3)
        col1.metric("Black-Scholes Price", f"${bs_price:.2f}")
        col2.metric("Heston Price", f"${heston_price:.2f}")
        col3.metric("SABR Price", f"${sabr_price:.2f}")

    # Tab 5: Historical Data
    with tab5:
        st.subheader("🔍 Historical Data")
        ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", value="AAPL")
        start_date = st.date_input("Start Date", value=datetime.date(2020, 1, 1))
        end_date = st.date_input("End Date", value=datetime.date(2023, 1, 1))

        if st.button("Fetch Data"):
            historical_data = fetch_historical_data(ticker, start_date, end_date)
            st.write(historical_data)

     # Tab 6: Case Studies
    with tab6:
        st.subheader("📚 Case Studies")
        st.markdown("""
        Explore real-world applications of options analytics with the following case studies:
        """)
        case_study_options = ["Portfolio Hedging", "Volatility Trading", "Risk Management"]
        selected_case_study = st.selectbox("Choose a Case Study", case_study_options)

        if selected_case_study == "Portfolio Hedging":
            from case_studies.hedging_example import hedging_example
            hedging_example()
        elif selected_case_study == "Volatility Trading":
            from case_studies.volatility_trading import volatility_trading
            volatility_trading()
        elif selected_case_study == "Risk Management":
            from case_studies.risk_management import risk_management
            risk_management()

    # Add tooltips for guidance
    add_tooltips()
