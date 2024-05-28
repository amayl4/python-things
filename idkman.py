import tkinter as tk
from manim import *

# Function to submit parameters and run Manim simulation
def submit():
    mass = float(mass_entry.get())
    velocity = float(velocity_entry.get())
    force = float(force_entry.get())
    friction = float(friction_entry.get())
    time = float(time_entry.get())

    class MechanicsSimulation(Scene):
        def __init__(self, mass, velocity, force, friction, time, **kwargs):
            super().__init__(**kwargs)
            self.mass = mass
            self.velocity = velocity
            self.force = force
            self.friction = friction
            self.time = time

        def construct(self):
            # Example: Simulate a moving object under the given parameters
            object = Dot().shift(LEFT * 3)
            self.add(object)
            
            # Calculate the acceleration (F = ma, a = F/m)
            acceleration = self.force / self.mass

            # Calculate final position using s = ut + 0.5at^2
            displacement = self.velocity * self.time + 0.5 * acceleration * self.time**2
            
            # Animate the movement
            self.play(object.animate.shift(RIGHT * displacement))

    # Configuration for Manim rendering
    config.background_color = "#333333"  # Set background color if needed
    config.pixel_height = 480
    config.pixel_width = 854
    config.frame_rate = 30

    scene = MechanicsSimulation(mass, velocity, force, friction, time)
    scene.render()

# Create the main window
root = tk.Tk()
root.title("Mechanics Simulator")

# Create and place labels and entries
tk.Label(root, text="Mass:").grid(row=0)
mass_entry = tk.Entry(root)
mass_entry.grid(row=0, column=1)

tk.Label(root, text="Initial Velocity:").grid(row=1)
velocity_entry = tk.Entry(root)
velocity_entry.grid(row=1, column=1)

tk.Label(root, text="Force:").grid(row=2)
force_entry = tk.Entry(root)
force_entry.grid(row=2, column=1)

tk.Label(root, text="Friction:").grid(row=3)
friction_entry = tk.Entry(root)
friction_entry.grid(row=3, column=1)

tk.Label(root, text="Time:").grid(row=4)
time_entry = tk.Entry(root)
time_entry.grid(row=4, column=1)

# Submit button
submit_button = tk.Button(root, text="Simulate", command=submit)
submit_button.grid(row=5, columnspan=2)

root.mainloop()
