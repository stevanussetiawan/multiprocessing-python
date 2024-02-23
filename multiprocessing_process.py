from PIL import Image, ImageEnhance
import multiprocessing

def rotate_image(input_image_path, angle, rotate_res):
    image = Image.open(input_image_path)
    rotated_image = image.rotate(angle, expand=True)
    rotate_res.append(rotated_image)

def adjust_brightness(input_image_path, factor, brightness_res):
    image = Image.open(input_image_path)
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(factor)
    brightness_res.append(enhanced_image)

if __name__ == '__main__':
    ANGLE = 90
    FACTOR = 0.3
    nama_file = "data\Mona_Lisa.jpg"
    
    manager = multiprocessing.Manager()

    rotate_res = manager.list()
    brightness_res = manager.list()
    
    process_rotate = multiprocessing.Process(target=rotate_image, args=(nama_file, ANGLE, rotate_res, ))
    process_brightness = multiprocessing.Process(target=adjust_brightness, args=(nama_file, FACTOR, brightness_res, ))
    
    processes = [process_brightness, process_rotate]
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
        
    rotate_res_pil = rotate_res[0]
    brightness_res_pil = brightness_res[0]

    rotate_res_pil.save(f"result\Mona_list_rotat_{ANGLE}.jpg")        
    brightness_res_pil.save(f"result\Mona_list_brighness_{FACTOR}.jpg")        
    
    


