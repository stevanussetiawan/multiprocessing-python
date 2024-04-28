# Import necessary libraries from PIL for image manipulation and brightness enhancement
from PIL import Image, ImageEnhance
# Import multiprocessing for concurrent execution
import multiprocessing

# Define a function to rotate an image
def rotate_image(input_image_path, angle, rotate_res):
    # Open an image from the given path
    image = Image.open(input_image_path)
    # Rotate the image by the specified angle, 'expand=True' allows the image to enlarge to fit the rotated image
    rotated_image = image.rotate(angle, expand=True)
    # Append the rotated image to the shared list
    rotate_res.append(rotated_image)

# Define a function to adjust the brightness of an image
def adjust_brightness(input_image_path, factor, brightness_res):
    # Open an image from the given path
    image = Image.open(input_image_path)
    # Create a brightness enhancer
    enhancer = ImageEnhance.Brightness(image)
    # Enhance the image brightness by a specified factor
    enhanced_image = enhancer.enhance(factor)
    # Append the enhanced image to the shared list
    brightness_res.append(enhanced_image)

# Main execution block, runs only if the script is the main program
if __name__ == '__main__':
    # Constants for the angle of rotation and the brightness factor
    ANGLE = 90
    FACTOR = 0.3
    # File path for the input image
    nama_file = "data\Mona_Lisa.jpg"
    
    # Create a multiprocessing manager to handle shared data
    manager = multiprocessing.Manager()

    # Create shared lists for storing results
    rotate_res = manager.list()
    brightness_res = manager.list()
    
    # Setup multiprocessing processes for each image transformation task
    process_rotate = multiprocessing.Process(target=rotate_image, args=(nama_file, ANGLE, rotate_res, ))
    process_brightness = multiprocessing.Process(target=adjust_brightness, args=(nama_file, FACTOR, brightness_res, ))
    
    # List of all processes
    processes = [process_brightness, process_rotate]
    
    # Start all processes
    for p in processes:
        p.start()
        
    # Wait for all processes to complete
    for p in processes:
        p.join()
        
    # Retrieve the results from shared lists
    rotate_res_pil = rotate_res[0]
    brightness_res_pil = brightness_res[0]

    # Save the processed images to files
    rotate_res_pil.save(f"result\Mona_list_rotat_{ANGLE}.jpg")        
    brightness_res_pil.save(f"result\Mona_list_brighness_{FACTOR}.jpg")        
