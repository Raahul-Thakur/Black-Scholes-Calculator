import plotly.graph_objects as go

def create_heatmap(prices, S_range, sigma_range, title="Heatmap"):
    """
    Create a heatmap visualization.
    """
    fig = go.Figure(data=go.Heatmap(
        z=prices,
        x=S_range,
        y=sigma_range,
        colorscale='Viridis',
        colorbar=dict(title="Price")
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Stock Price ($)",
        yaxis_title="Volatility (%)"
    )
    return fig

def create_pnl_chart(S_range, pnl, strategy_name="P&L Chart"):
    """
    Create a P&L chart visualization.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=pnl, mode='lines', name=strategy_name))
    fig.update_layout(
        title=f"{strategy_name} P&L",
        xaxis_title="Stock Price at Expiry ($)",
        yaxis_title="Profit/Loss ($)"
    )
    return fig
