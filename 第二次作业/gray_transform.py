import cv2
import numpy as np

def apply_log_transform(image):
    # Convert image to float32 for precision
    image = np.float32(image)
    # Apply log transform
    log_image = cv2.log(image + 1)
    # Normalize the image to the range [0, 255]
    log_image = cv2.normalize(log_image, None, 0, 255, cv2.NORM_MINMAX)
    # Convert back to uint8
    log_image = np.uint8(log_image)
    return log_image

# Load the image
image = cv2.imread('./result_image_视网膜.jpg', cv2.IMREAD_GRAYSCALE)

# Apply log transform
log_transformed_image = apply_log_transform(image)

# Save the result
cv2.imshow('simple_transform.jpg', log_transformed_image)
cv2.waitKey(0)
image2 = cv2.imread('log_transformed_image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image2', image2)
cv2.waitKey(0)