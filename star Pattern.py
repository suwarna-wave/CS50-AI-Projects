import random
import matplotlib.pyplot as plt
import math

# Set the seed for reproducibility
random.seed(42)

# Define the world boundaries and the number of stars
world_min = -110000
world_max = 110000
num_stars = 500
min_distance = 5000

# Function to check if a new star is at least min_distance away from existing stars
def is_valid_position(new_star, stars, min_distance):
    for star in stars:
        distance = math.sqrt((new_star[0] - star[0]) ** 2 + (new_star[1] - star[1]) ** 2)
        if distance < min_distance:
            return False
    return True

# Generate star positions
stars = []
while len(stars) < num_stars:
    new_star = (random.randint(world_min, world_max), random.randint(world_min, world_max))
    if is_valid_position(new_star, stars, min_distance):
        stars.append(new_star)

# Extract x and y coordinates for plotting
x_coords = [star[0] for star in stars]
y_coords = [star[1] for star in stars]

# Plot the stars
plt.figure(figsize=(10, 10))
plt.scatter(x_coords, y_coords, color='white')
plt.gca().set_facecolor('black')
plt.title('Random Starfield Simulation')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()