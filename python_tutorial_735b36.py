###############################################################################
# Learning Objective:
# This tutorial demonstrates how to simulate a simplified N-body solar system
# using Python's Pygame for visualization and NumPy for efficient gravitational
# calculations. We will focus on understanding and implementing Newton's
# Law of Universal Gravitation to simulate the motion of celestial bodies.
# This will introduce concepts of vector physics, numerical integration,
# and game development basics for visual feedback.
###############################################################################

import pygame
import numpy as np

# --- Constants ---
# These are physical constants, scaled for our simulation.
# Real-world values are often too extreme for a simple visual simulation.
GRAVITATIONAL_CONSTANT = 1000  # Scaled gravitational constant (adjust for speed)
TIME_STEP = 0.1               # How much time passes in each simulation step
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# --- Helper Functions ---

def calculate_distance(pos1, pos2):
    """
    Calculates the Euclidean distance between two points (positions).
    Args:
        pos1 (np.ndarray): A NumPy array representing the first position [x, y].
        pos2 (np.ndarray): A NumPy array representing the second position [x, y].
    Returns:
        float: The distance between the two positions.
    """
    return np.linalg.norm(pos1 - pos2)

def calculate_gravitational_force(m1, pos1, m2, pos2):
    """
    Calculates the gravitational force exerted by body 2 on body 1.
    Uses Newton's Law of Universal Gravitation: F = G * (m1 * m2) / r^2.
    The force is a vector pointing from body 1 towards body 2.
    Args:
        m1 (float): Mass of the first body.
        pos1 (np.ndarray): Position of the first body [x, y].
        m2 (float): Mass of the second body.
        pos2 (np.ndarray): Position of the second body [x, y].
    Returns:
        np.ndarray: A NumPy array representing the gravitational force vector [Fx, Fy].
    """
    # Calculate the vector pointing from body 1 to body 2.
    direction_vector = pos2 - pos1
    # Calculate the distance between the two bodies.
    distance = calculate_distance(pos1, pos2)

    # Avoid division by zero if bodies are at the exact same position.
    if distance == 0:
        return np.array([0.0, 0.0])

    # Calculate the magnitude of the gravitational force.
    force_magnitude = GRAVITATIONAL_CONSTANT * (m1 * m2) / (distance ** 2)

    # Normalize the direction vector to get a unit vector (magnitude 1).
    direction_unit_vector = direction_vector / distance

    # The force vector is the magnitude multiplied by the unit direction vector.
    # This force pulls body 1 towards body 2.
    force_vector = force_magnitude * direction_unit_vector
    return force_vector

# --- Celestial Body Class ---

class CelestialBody:
    """
    Represents a celestial body (planet, star) in the solar system simulation.
    Stores its mass, position, velocity, and color for visualization.
    """
    def __init__(self, mass, position, velocity, color, radius=5):
        """
        Initializes a CelestialBody.
        Args:
            mass (float): The mass of the body.
            position (list or tuple or np.ndarray): Initial [x, y] coordinates.
            velocity (list or tuple or np.ndarray): Initial [vx, vy] velocity.
            color (tuple): RGB color tuple for drawing.
            radius (int): The visual radius of the body on the screen.
        """
        self.mass = mass
        # Ensure position and velocity are NumPy arrays for easier math operations.
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.color = color
        self.radius = radius

    def update_position(self):
        """
        Updates the body's position based on its current velocity.
        This is a simple Euler integration step.
        """
        self.position += self.velocity * TIME_STEP

    def draw(self, screen):
        """
        Draws the celestial body onto the Pygame screen.
        Args:
            screen (pygame.Surface): The Pygame surface to draw on.
        """
        # Convert float positions to integers for Pygame drawing.
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

# --- Simulation Setup ---

def run_simulation():
    """
    Initializes Pygame, sets up the screen, creates celestial bodies,
    and runs the main simulation loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simplified N-Body Solar System")
    clock = pygame.time.Clock()

    # --- Create Celestial Bodies ---
    # We'll create a sun and a planet for a simple demonstration.
    # Mass, initial position [x, y], initial velocity [vx, vy], color, radius
    sun = CelestialBody(mass=10000, position=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], velocity=[0, 0], color=YELLOW, radius=15)
    planet = CelestialBody(mass=10, position=[SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2], velocity=[0, 10], color=BLUE, radius=5)
    # Another planet to show interactions
    another_planet = CelestialBody(mass=5, position=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150], velocity=[-8, 0], color=RED, radius=4)

    # A list to hold all bodies in the simulation.
    bodies = [sun, planet, another_planet]

    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Simulation Logic (Physics) ---
        # Calculate forces for all pairs of bodies.
        # For each body, we want to calculate the total force acting on it.
        # The net force is the vector sum of all forces from other bodies.
        for i, body1 in enumerate(bodies):
            total_force_on_body1 = np.array([0.0, 0.0])
            for j, body2 in enumerate(bodies):
                # A body doesn't exert a gravitational force on itself.
                if i == j:
                    continue

                # Calculate the force exerted by body2 on body1.
                force = calculate_gravitational_force(body1.mass, body1.position, body2.mass, body2.position)
                # Add this force to the total force acting on body1.
                total_force_on_body1 += force

            # --- Update Velocity and Position (Numerical Integration) ---
            # Newton's Second Law: F = ma, so a = F/m.
            # Acceleration is the force divided by the body's mass.
            acceleration = total_force_on_body1 / body1.mass

            # Update the body's velocity: v_new = v_old + a * dt
            body1.velocity += acceleration * TIME_STEP

            # Update the body's position: p_new = p_old + v_new * dt
            body1.update_position() # Uses the already updated velocity

        # --- Drawing ---
        screen.fill((0, 0, 0))  # Clear screen with black background

        # Draw all celestial bodies.
        for body in bodies:
            body.draw(screen)

        pygame.display.flip()  # Update the full screen to show what's been drawn
        clock.tick(60)         # Limit frame rate to 60 FPS

    pygame.quit()

# --- Example Usage ---
if __name__ == "__main__":
    run_simulation()