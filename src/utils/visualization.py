import plotly.graph_objects as go
from .black_scholes import calculate_black_scholes
import numpy as np

def create_interactive_heatmap(S_range, sigma_range, K, T, r, option_type):
    """
    Create an interactive heatmap for option prices.
    """
    prices = np.array([
        [calculate_black_scholes(s, K, T, r, sigma, option_type) for s in S_range]
        for sigma in sigma_range
    ])
    fig = go.Figure(data=go.Heatmap(
        z=prices,
        x=S_range,
        y=sigma_range * 100,
        colorscale='Viridis',
        colorbar=dict(title="Option Price ($)")
    ))
    return fig

def create_draggable_pnl_chart(S_range, K, current_price, option_type):
    """
    Create a P&L chart with draggable lines.
    """
    pnl = np.maximum(S_range - K, 0) - current_price if option_type == 'call' else np.maximum(K - S_range, 0) - current_price
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=pnl, mode='lines', name='P&L'))
    fig.update_layout(
        title=f"P&L Analysis for {option_type.capitalize()} Option",
        xaxis_title="Stock Price at Expiry ($)",
        yaxis_title="Profit/Loss ($)",
        dragmode="pan",
    )
    return fig
