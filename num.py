import numpy as np
import cv2

black = np.zeros([600,600])
print(black)

cv2.inshow("preto", black)
cv2.waitKey(0)