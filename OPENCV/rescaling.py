import cv2

# Rescaling
def rescaling(content, scale):  # Content -> contain binary data | scale -> contain value between 0 and 1
    width = int(content.shape[0] * scale)       # Rescaling from width
    height = int(content.shape[1] * scale)      # Rescaling from height
    dimension = (width, height)                 # Setting dimension
    rescaled_content = cv2.resize(content, dimension, interpolation=cv2.INTER_AREA)
    '''
    To shrink image = cv2.INTER_AREA
    To enlarge image = cv2.INTER_CUBIC or cv2.INTER_LINEAR
    '''
    return rescaled_content

# Rescaling Image
'''
img = cv2.imread('demo.jpg')
img = rescaling(img, 0.85)
cv2.imshow('Rescaled Image', img)
'''

#Rescaling Video
'''
cap = cv2.VideoCapture(0)
while True:
    isT, vid = cap.read()
    cv2.imshow('Rescaled Video', rescaling(vid, 0.25))
    if cv2.waitKey(1) == ord('d'):
        cap.release()
        break
'''

# Change resolution of window and video
'''
capt = cv2.VideoCapture(0)
# capt.set(property_id, value)
width, height = 500, 500
capt.set(3, width)
capt.set(4, height)
while True:
    isT, vid = capt.read()
    cv2.imshow('Change Resolution', vid)
    if cv2.waitKey(1) == ord('d'):
        capt.release()
        break
'''
