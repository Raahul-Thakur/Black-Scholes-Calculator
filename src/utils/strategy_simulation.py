import numpy as np
import plotly.graph_objects as go

def simulate_strategy(strategy, S_range, K, call_price, put_price):
    """
    Simulate common option strategies (e.g., straddle, strangle).
    """
    if strategy == 'straddle':
        pnl = np.maximum(S_range - K, 0) - call_price + np.maximum(K - S_range, 0) - put_price
    elif strategy == 'strangle':
        pnl = (np.maximum(S_range - K + 10, 0) - call_price
               + np.maximum(K - 10 - S_range, 0) - put_price)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=pnl, mode='lines', name=strategy))
    return fig
