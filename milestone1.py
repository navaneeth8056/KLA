import numpy as np
import matplotlib.pyplot as plt

def generate_equally_spaced_points(diameter_mm, num_points, angle_deg):
    angle_rad = np.radians(angle_deg)
    # Calculate radius based on the diameter
    radius = diameter_mm / 2.0
    # Generate equally spaced distances along the line at the specified angle
    distances = np.linspace(-radius, radius, num_points)
    # Calculate x and y coordinates for each point
    x_coords = distances * np.cos(angle_rad)
    y_coords = distances * np.sin(angle_rad)

    return x_coords, y_coords

wafer_diameter_mm = 200  # Replace with your wafer diameter
num_points = 31         # Replace with the desired number of points
angle_degrees = 150       # Replace with the desired angle in degrees

x, y = generate_equally_spaced_points(wafer_diameter_mm, num_points, angle_degrees)

# Plotting the points
plt.scatter(x, y, color='red', marker='o')
plt.title('Equally Spaced Points on Wafer Line')
plt.xlabel('X-coordinate (mm)')
plt.ylabel('Y-coordinate (mm)')
plt.grid(True)
plt.show()


# Write coordinates to a text file
output_file_path = "equally_spaced_points.txt"

with open(output_file_path, 'w') as file:
    for i in range(num_points):
        file.write(f"({x[i]:.4f}, {y[i]:.4f})\n")

print(f"Coordinates written to: {output_file_path}")

