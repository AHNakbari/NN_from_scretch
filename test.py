import numpy as np

# Example input
N = 4  # Number of examples
d_1 = 3  # Dimension 1
d_2 = 5  # Dimension 2
x = np.random.rand(N, d_1, d_2)  # Randomly generated input of shape (4, 3, 5)

# Reshaping
x_reshaped = x.reshape(N, -1)

# Print shapes
print("Original shape of x:", x.shape)  # Expected: (4, 3, 5)
print("Shape of x_reshaped:", x_reshaped.shape)  # Expected: (4, 15)

