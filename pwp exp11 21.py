import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#Postlab A

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image using PIL
image = Image.open(r'C:\Users\user\Desktop\sem 3\b.tech sem-3\pwp\exp12.png')  # Replace with your image file path

# Convert image to NumPy array
image_array = np.array(image)

# Get image dimensions and shape
height, width = image_array.shape[:2]
shape = image_array.shape

# Get minimum pixel value at channel B (assuming image is in RGB format)
min_b = image_array[:, :, 2].min()

# Display the results
print("Image Dimensions (Height x Width):", height, "x", width)
print("Image Shape:", shape)
print("Minimum pixel value at channel B:", min_b)

# Show the image using matplotlib
plt.imshow(image)
plt.axis('off')  # Hide axis
plt.title("Image Display")
plt.show()

#postlab 2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image using PIL
image = Image.open(r'C:\Users\user\Desktop\sem 3\b.tech sem-3\pwp\exp12.png')  # Replace with your image file path

# Convert image to NumPy array
image_array = np.array(image)

# Define padding size (top, bottom, left, right)
pad_top = 50
pad_bottom = 50
pad_left = 50
pad_right = 50

# Add padding using NumPy, fill with 0 (black)
padded_array = np.pad(
    image_array,
    ((pad_top, pad_bottom), (pad_left, pad_right), (0, 0)),
    mode='constant',
    constant_values=0
)

# Convert padded array back to image
padded_image = Image.fromarray(padded_array)

# Display both images side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Original image
axes[0].imshow(image)
axes[0].axis('off')
axes[0].set_title('Original Image')

# Padded image
axes[1].imshow(padded_image)
axes[1].axis('off')
axes[1].set_title('Padded Image')

plt.tight_layout()
plt.show()

#postlab 3
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image using PIL
image = Image.open(r'C:\Users\user\Desktop\sem 3\b.tech sem-3\pwp\exp12.png')  # Replace with your image file path

# Convert image to NumPy array
image_array = np.array(image)

# Extract the R, G, B channels
R = image_array.copy()
G = image_array.copy()
B = image_array.copy()

# Set other channels to zero for visualization
R[:, :, 1] = 0  # Zero out G
R[:, :, 2] = 0  # Zero out B

G[:, :, 0] = 0  # Zero out R
G[:, :, 2] = 0  # Zero out B

B[:, :, 0] = 0  # Zero out R
B[:, :, 1] = 0  # Zero out G

# Create images from arrays
R_image = Image.fromarray(R)
G_image = Image.fromarray(G)
B_image = Image.fromarray(B)

# Display the original image and RGB channels
fig, axes = plt.subplots(1, 4, figsize=(16, 5))

# Original image
axes[0].imshow(image)
axes[0].axis('off')
axes[0].set_title('Original')

# Red channel
axes[1].imshow(R_image)
axes[1].axis('off')
axes[1].set_title('Red Channel')

# Green channel
axes[2].imshow(G_image)
axes[2].axis('off')
axes[2].set_title('Green Channel')

# Blue channel
axes[3].imshow(B_image)
axes[3].axis('off')
axes[3].set_title('Blue Channel')

plt.tight_layout()
plt.show()
