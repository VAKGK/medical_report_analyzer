import numpy as np

def preprocess_image(image):
    """
    Just converts the image to a format OpenCV understands.
    No thresholding, no blurring. Just raw image.
    """
    # Convert to numpy array (OpenCV format)
    return np.array(image)