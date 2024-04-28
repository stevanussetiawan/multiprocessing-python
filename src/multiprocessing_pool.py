# Import necessary libraries
import numpy as np
import cv2
import multiprocessing
import matplotlib.pyplot as plt
from functools import partial

# Define a function to rotate an image by a given angle
def rotate_im(image, angle):
    # Get dimensions of the image
    (h, w) = image.shape[:2]
    # Calculate the center of the image
    (cX, cY) = (w // 2, h // 2)
    
    # Calculate the rotation matrix for the given angle
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    
    # Compute new dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    
    # Adjust the rotation matrix to account for translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    
    # Perform the rotation
    image = cv2.warpAffine(image, M, (nW, nH), flags=cv2.INTER_LINEAR)
    return image

# Main execution block
if __name__ == '__main__':
    # Load an image from file
    file_path = "data\\Mona_Lisa.jpg"
    img = cv2.imread(file_path)
    
    # Determine number of processes to use based on available CPUs
    num_processes = multiprocessing.cpu_count()
    
    # Create a pool of processes
    pool = multiprocessing.Pool(processes=num_processes)
    
    # List of angles to rotate the image
    angles = [90, 180, 270]
    
    # Create a partial function that locks the image argument but varies the angle
    freeze_rotate_img = partial(rotate_im, img)
    
    # Apply rotation to each angle in the angles list in parallel
    rotated_images = pool.map(freeze_rotate_img, angles)
    
    # Close and join the pool to clean up
    pool.close()
    pool.join()
    
    # Display each rotated image using matplotlib
    for rotated_img in rotated_images:
        plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
        plt.show()
