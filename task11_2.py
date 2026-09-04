import math

# 1. Input data
points_camera = [
    [2.0, 0.0, -0.2],
    [3.5, 1.0, -0.3],
    [1.5, -0.8, -0.1]
]

# Translation offset (camera position relative to base_link)
tx, ty, tz = 0.5, 0.0, 0.2

# Rotation angle (pitch around Y-axis) in degrees
theta_deg = -15.0
theta = math.radians(theta_deg)  # Convert to radians

# 2. Rotation matrix coefficients (around Y-axis)
cos_a = math.cos(theta)
sin_a = math.sin(theta)

# 3. Transform each point
print("Transformed Obstacles (Base Frame):")
for i, point in enumerate(points_camera):
    x_c, y_c, z_c = point  # Unpack camera coordinates

    # Apply rotation (R_y * point)
    x_rot = cos_a * x_c + sin_a * z_c
    y_rot = y_c
    z_rot = -sin_a * x_c + cos_a * z_c

    # Apply translation (add camera offset)
    x_base = x_rot + tx
    y_base = y_rot + ty
    z_base = z_rot + tz

    # Print result rounded to 2 decimal places
    print(f"Obstacle {i+1}: [{x_base:.2f}, {y_base:.2f}, {z_base:.2f}]")
