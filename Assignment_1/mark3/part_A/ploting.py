import plotly.graph_objects as go

def plot_results(results, title, text_lengths, adjust_dimensions=False):
    fig = go.Figure()

    if adjust_dimensions:
        x_label = 'Text Length (thousands of characters)'
        y_label = 'Running Time (microseconds)'
        for name, times in results.items():
            results[name] = [t*10**6 for t in times]
    else:
        text_lengths = [length / 10_000 for length in text_lengths]
        x_label = 'Text Length (10 000 characters)'
        y_label = 'Running Time (seconds)'

    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        plot_bgcolor='black',
        paper_bgcolor='black',
        legend=dict(font=dict(color='white'))
    )
    fig.update_xaxes(titlefont=dict(color='white'), tickfont=dict(color='white'), gridcolor='rgba(255, 255, 255, 0.2)')
    fig.update_yaxes(titlefont=dict(color='white'), tickfont=dict(color='white'), gridcolor='rgba(255, 255, 255, 0.2)')

    # Add a line along the y-axis
    fig.update_layout(
        shapes=[
            dict(
                type="line",
                xref="x",
                yref="paper",
                x0=0,
                y0=0,
                x1=0,
                y1=1,
                line=dict(color="white", width=2),
            )
        ]
    )

    for name, times in results.items():
        fig.add_trace(go.Scatter(x=text_lengths, y=times, mode='lines', name=name))

    fig.show()
