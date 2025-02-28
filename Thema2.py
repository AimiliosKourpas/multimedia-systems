import cv2
import numpy as np

def split_frame_to_macroblocks(frame, window_width=64, window_height=64): #the function that splits the frame into macroblocks
    previous_height, previous_width = frame.shape[:2] #get the height and width of the frame
    height = fit_the_size(previous_height, window_height) + 64 #fit the height to the window size
    width = fit_the_size(previous_width, window_width) + 64 #fit the width to the window size

    height_pad = (64, height - previous_height) #pad the height
    width_pad = (0, width - previous_width) #pad the width
    depth_pad = (0, 0) #pad the depth
    padding = (height_pad, width_pad, depth_pad) #pad the frame
    padded_frame = np.pad(frame, padding, mode='constant') #pad the frame

    macroblocks = [] #create an empty list
     
    for h in range(0, height - window_height + 1, window_height): #for loop for the height
        row = [] #create an empty list 
        for w in range(0, width - window_width + 1, window_width): #for loop for the width
            macroblock = padded_frame[h:h + window_height, w:w + window_width] #get the macroblock
            row.append(macroblock) #append the macroblock to the row
        macroblocks.append(row) #append the row to the macroblocks
    return macroblocks #return the macroblocks

def split_macroblocks_to_frame(macroblocks): #the function that creates the frame from the macroblocks
    rows = [] #create an empty list 
    for row in macroblocks: #for loop for the rows
        rows.append(np.concatenate(row, axis=1)) #append the row to the rows

    frame = np.concatenate(rows, axis=0) #create the frame from the rows
    return frame #return the frame

def fit_the_size(x, window=64): #the function that fits the size of the frame to the window size
    return x + (window - (x % window)) % window #return the fitted size

video = cv2.VideoCapture('videoThema2.mp4') #get the video

previous = False #set the previous to false
mb_prev = None #set the mb_prev to None

while video.isOpened():     
    success, frame = video.read() #read the video

    if not success: #if the video is not read
        break

    mb = split_frame_to_macroblocks(frame, window_width=64, window_height=64) #get the macroblocks
 
    if not previous:
        previous = True #set the previous to true
        mb_prev = mb   
        continue

    for i in range(3, 11):
        if i < len(mb_prev): 
            mb[i] = mb_prev[i]

    mb_frame = split_macroblocks_to_frame(mb)

    cv2.imshow('Original', frame) #show the original video
    cv2.imshow('Object-removal', mb_frame) #show the object removal video

    mb_prev = mb 

    cv2.waitKey(30) #wait 30ms

video.release() #release the video
cv2.destroyAllWindows() #destroy all the windows 
