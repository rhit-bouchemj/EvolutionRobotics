import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_multiple_datasets(num_lines):
    # Create a figure and an axes
    fig, ax = plt.subplots()
    
    # Initialize lists to hold datasets and line objects
    x_data = [[] for _ in range(num_lines)]
    y_data = [[] for _ in range(num_lines)]
    lines = [plt.plot([], [], animated=True)[0] for _ in range(num_lines)]
    
    # Generate a wider range of colors using the 'hsv' colormap
    colors = plt.cm.hsv(np.linspace(0, 1, num_lines))  # 'hsv' covers the full spectrum of hues

    # Assign colors to lines
    for line, color in zip(lines, colors):
        line.set_color(color)

    # Plot a dot at the origin that should appear on top of all lines
    origin_dot, = plt.plot(0, 0, 'ko', markersize=10)  # Dot at (0, 0)

    # Initialize the plot limits
    def init():
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.5, 1.5)
        return lines + [origin_dot]

    # Update function to extend all lines simultaneously
    def update(frame):
        for i in range(num_lines):
            x_data[i].append(frame)
            y_data[i].append(np.sin(frame + i * np.pi / num_lines))  # Different phase shifts for variety
            lines[i].set_data(x_data[i], y_data[i])
        return lines + [origin_dot]

    # Function to add a dot at (9, 1) after the animation finishes
    def add_dot_at_end():
        ax.plot(9, 1, 'ro', markersize=10)  # Plot a red dot at (9, 1)
        plt.draw()  # Redraw the plot to show the new dot

    # Callback to stop the animation and add the dot
    def on_animation_complete():
        ani.event_source.stop()  # Stop the animation
        add_dot_at_end()  # Add the dot after stopping the animation

    # Create an animation object
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), init_func=init, blit=True, repeat=False)

    # Set up a timer to call the function after the animation ends
    fig.canvas.mpl_connect('draw_event', lambda event: on_animation_complete() if not ani.event_source.is_running() else None)

    plt.show()  # Display the plot

# Call the function with a specified number of lines (e.g., 10 lines)
animate_multiple_datasets(10)
