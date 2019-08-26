import numpy as np
import cv2
def remove_alpha_channel(source, background_color):
    source_img = cv2.cvtColor(source[:,:,:3], cv2.COLOR_BGR2GRAY)
    source_mask = source[:,:,3] * (1 / 255.0)
    bg_part = (255 * (1 / 255.0)) * (1.0 - source_mask)
    weight = (source_img * (1 / 255.0)) * (source_mask)
    dest = np.uint8(cv2.addWeighted(bg_part, 255.0, weight, 255.0, 0.0))
    return dest

orig_img = cv2.imread('2.jpg', cv2.IMREAD_UNCHANGED)
dest_img = remove_alpha_channel(orig_img)
cv2.imwrite('I:/2.png', dest_img, [cv2.IMWRITE_PNG_COMPRESSION])