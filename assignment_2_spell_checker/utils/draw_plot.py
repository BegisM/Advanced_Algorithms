from plotly import graph_objects as go


def plot_results(results: list):
    descriptions, times = zip(*results)
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray']

    fig = go.Figure(data=[
        go.Bar(
            name=descriptions[i],
            x=['Load Time', 'Spell Check Time'],
            y=[times[i * 2], times[i * 2 + 1]], marker_color=colors[i]
        )
        for i in range(len(descriptions) // 2)
    ])

    fig.update_layout(
        title="Comparison of Dictionary Loading and Spell Checking Times",
        xaxis_title="Operation",
        yaxis_title="Time (seconds)",
        barmode='group'
    )

    fig.show()
