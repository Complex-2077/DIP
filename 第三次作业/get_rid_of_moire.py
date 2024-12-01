import cv2
import numpy as np

import matplotlib.pyplot as plt

def read_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image

def apply_fourier_transform(image):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    return fshift, magnitude_spectrum

def notch_filter(shape, notch_center, notch_radius):
    rows, cols = shape
    mask = np.ones((rows, cols), np.uint8)
    center_row, center_col = rows // 2, cols // 2
    for r in range(rows):
        for c in range(cols):
            if np.sqrt((r - center_row - notch_center[0])**2 + (c - center_col - notch_center[1])**2) < notch_radius:
                mask[r, c] = 0
            if np.sqrt((r - center_row + notch_center[0])**2 + (c - center_col + notch_center[1])**2) < notch_radius:
                mask[r, c] = 0
            if np.sqrt((r - center_row - notch_center[0])**2 + (c - center_col + notch_center[1])**2) < notch_radius:
                mask[r, c] = 0
            if np.sqrt((r - center_row + notch_center[0])**2 + (c - center_col - notch_center[1])**2) < notch_radius:
                mask[r, c] = 0
    return mask

def apply_notch_filter(fshift, notch_center, notch_radius):
    mask = notch_filter(fshift.shape, notch_center, notch_radius)
    fshift_filtered = fshift * mask
    return fshift_filtered, mask

def inverse_fourier_transform(fshift_filtered):
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def main():
    image_path = './car-moire-pattern.tif'
    image = read_image(image_path)
    
    fshift, magnitude_spectrum = apply_fourier_transform(image)
    
    notch_center = (30, 30)  
    notch_radius = 19  
    fshift_filtered, mask = apply_notch_filter(fshift, notch_center, notch_radius)
    
    img_back = inverse_fourier_transform(fshift_filtered)
    
    plt.subplot(221), plt.imshow(image, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(np.log(np.abs(fshift)), cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(np.log(np.abs(fshift)) * mask, cmap='gray')
    plt.title('Magnitude Spectrum after Filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img_back, cmap='gray')
    plt.title('Image after Notch Filter'), plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imsave('input_image.png', image, cmap='gray')
    plt.imsave('magnitude_spectrum.png', np.log(np.abs(fshift)), cmap='gray')
    plt.imsave('magnitude_spectrum_after_filter.png', np.log(np.abs(fshift)) * mask, cmap='gray')
    plt.imsave('image_after_notch_filter.png', img_back, cmap='gray')

if __name__ == "__main__":
    main()