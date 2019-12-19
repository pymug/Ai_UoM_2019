"""
Loads and displays a video with canny edge detection
"""

# Importing OpenCV
import cv2
import numpy as np

# Create a VideoCapture object and read from input file 
# enter 0 to use webcam as input
cap = cv2.VideoCapture('challenge.mp4') 

if (cap.isOpened()== False):
  print("Error opening video stream or file")
  
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# Read the video
while(cap.isOpened()):
  # Capture frame-by-frame

  ret, frame = cap.read()
  if ret == True:
    frame75 = rescale_frame(frame, percent=50)
    # Converting the image to grayscale.
    gray = cv2.cvtColor(frame75, cv2.COLOR_BGR2GRAY)


    # Using the Canny filter to get contours
    edges = cv2.Canny(gray, 20, 30)
    # Using the Canny filter with different parameters
    edges_high_thresh = cv2.Canny(gray, 60, 120)
    # Stacking the images to print them together
    # For comparison
    images = np.hstack((gray, edges, edges_high_thresh))

    # Display the resulting frame
    cv2.imshow('Frame', images)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
