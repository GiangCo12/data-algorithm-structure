import cv2

# Load pre-trained Haar Cascade Classifier for upper body detection
upper_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

# Load input image
image = cv2.imread('input_image.jpg')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect upper bodies in the image
upper_bodies = upper_body_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected upper bodies
for (x, y, w, h) in upper_bodies:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Detected Upper Bodies', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
