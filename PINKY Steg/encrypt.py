from LSBSteg import *

#encoding
steg = LSBSteg(cv2.imread("lelystad.JPG"))
img_encoded = steg.encode_text("PINKY{cr0uch_iN_Cont3mpl@t!oN}")
cv2.imwrite("lelystad.png", img_encoded)