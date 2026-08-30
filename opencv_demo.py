'''
OpenCV (cv2) — Step 1: Installation

Unlike Tkinter and winsound, OpenCV is not normally included with Python, so we need to install it.

Open CMD in your project folder and run:

py -m pip install opencv-python

After installation, verify it:

py -c "import cv2; print(cv2.__version__)"

'''




'''
Important interview point

You install:

pip install opencv-python

but import:

import cv2

Why?

Package name → opencv-python
Python module → cv2
'''


import cv2

img = cv2.imread('picture.jpg')   #Reads the image and stores it in img.  

resized = cv2.resize(img, (600, 400))

cv2.imshow("My Image", resized)   #Opens a window and displays the image.

cv2.waitKey(0)  #Waits for you to press a keyboard key.

cv2.destroyAllWindows()  #Closes the OpenCV window.







'''
mportant interview concept

cv2.imread() doesn't return a special "Image" object.

It returns the image as a NumPy array.

Conceptually:

photo.jpg
   ↓
cv2.imread()
   ↓
NumPy array
   ↓
pixel values

'''



'''
The flow is:

cv2.imshow()
      ↓
OpenCV creates/displays the window
      ↓
cv2.waitKey(0)
      ↓
Wait for a key press
      ↓
cv2.destroyAllWindows()
      ↓
Close the OpenCV window
'''



# Remember: OpenCV uses BGR by default, not RGB.