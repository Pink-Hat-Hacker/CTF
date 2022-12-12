from LSBSteg import *

#decoding
im = cv2.imread("lelystad.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())