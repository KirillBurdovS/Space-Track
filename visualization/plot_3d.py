import plotly.graph_objects as go
import numpy as np

def plot_3d_trajectory(sol):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=sol.y[0], y=sol.y[1], z=sol.y[2],
        mode='lines', name='Траектория'
    ))

    # Земля (сфера)
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 50)
    x = 6371 * np.outer(np.cos(theta),np.sin(phi)) # R=6371 км
    y = 6371 * np.outer(np.sin(theta),np.sin(phi))
    z = 6371 * np.outer(np.ones(100), np.cos(phi))

    fig.add_trace(go.Surface(x=x, y=y, z=z, opacity=0.3, name='Земля'))
    fig.show()
