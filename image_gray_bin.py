import cv2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

img_gray = cv2.imread("/content/download.png", cv2.IMREAD_GRAYSCALE)

plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)

threshold = 127
img_BINARY = (img_gray > threshold).astype(np.uint8) * 255  # Converter para 0 e 255

plt.imshow(img_BINARY, cmap='gray', vmin=0, vmax=255)
