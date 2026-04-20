import cv2

# Load image
img = cv2.imread("sample_image.jpg")
# Print shape
print("Image Shape:", img.shape)

# Print pixel value at (0,0)
print("Pixel value at (0,0):", img[0][0])

# Print number of channels
print("Number of Channels:", img.shape[2])