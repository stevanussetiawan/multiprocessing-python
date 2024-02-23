import numpy as np
import cv2
import multiprocessing
import matplotlib.pyplot as plt
from functools import partial

def rotate_im(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    image = cv2.warpAffine(image, M, (nW, nH), flags=cv2.INTER_LINEAR)
    return image

if __name__ == '__main__':
    nama_file = "data\Mona_Lisa.jpg"
    img = cv2.imread(nama_file)
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    angle = [90, 180, 270]
    freeze_rotate_img = partial(rotate_im, img)
    rotate_imgs = pool.map(freeze_rotate_img, angle)
    pool.close()
    pool.join()
    
    for rotate_img in rotate_imgs:
        plt.imshow(rotate_img)
        plt.show()


