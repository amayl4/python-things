from manim import Scene, Dot, LEFT, RIGHT, config

class MechanicsSimulation(Scene):
    def __init__(self, mass, velocity, force, friction, time, **kwargs):
        super().__init__(**kwargs)
        self.mass = mass
        self.velocity = velocity
        self.force = force
        self.friction = friction
        self.time = time

    def construct(self):
        object = Dot().shift(LEFT * 3)
        self.add(object)
        
        acceleration = self.force / self.mass
        displacement = self.velocity * self.time + 0.5 * acceleration * self.time**2
        self.play(object.animate.shift(RIGHT * displacement))

def run_simulation(mass, velocity, force, friction, time):
    config.background_color = "#333333"
    config.pixel_height = 480
    config.pixel_width = 854
    config.frame_rate = 30

    scene = MechanicsSimulation(mass, velocity, force, friction, time)
    scene.render()
