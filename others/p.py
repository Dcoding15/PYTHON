#! /usr/bin/python3

'''

1. add no. using loop

n = int(input("enter range: "))
l = [i for i in range(1,n+1)]
s = 0
for i in l:
    s += i
print(s)

2. even / odd

n = int(input("enter no.: "))
print("EVEN" if n%2==0 else "ODD")

3. run length encoding (RLE)

msg = input('enter string: ')
new_msg = ""
count = 0
for i in range(len(msg) - 1):
    if msg[i] == msg[i+1]:
        count += 1
        if i == len(msg) - 2:
            count += 1
            new_msg += (msg[i+1] + str(count))
    elif msg[i] != msg[i+1]:
        count += 1
        new_msg += (msg[i] + str(count))
        count = 0

# If there is one different character at last position
if msg[len(msg)-2] != msg[len(msg)-1]:
    new_msg += msg[len(msg)-1] + "1"
print(new_msg)

4. LZW encoding

n = input('Enter string : ')
patrn = []
pri_index = []
index = []
distn = {'':0}
pri_count = 0

for i in n:
    if i not in patrn:
        patrn.append(i)
        pri_count += 1
        pri_index.append(pri_count)

i, j = 0, 1
while j < len(n):
    if n[i:j] not in patrn:
        patrn.append(n[i:j])
        pri_count += 1
        pri_index.append(pri_count)
        i += len(n[i:j])-1
        j += 1
    else:
        j += 1

for i in range(len(patrn)):
    distn[patrn[i]] = pri_index[i]

for i in patrn:
    index.append(distn[i[:len(i)-1]])

print('pattern      : ',end='')
for i in patrn:
    print(i,end=' ')
print()
print('primary index: ',end='')
for i in pri_index:
    print(i,end=' ')
print()
print('index        : ',end='')
for i in index:
    print(i,end=' ')

5. rgb to gray scale

from PIL import Image

def rgb_to_gray(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_image_path)

input_image_path = "path/to/your/input/image.jpg"
output_image_path = "path/to/your/output/grayscale_image.jpg"

rgb_to_gray(input_image_path, output_image_path)


6. increase pixel of an image

from PIL import Image

def increase_image_size(input_image_path, output_image_path, scale_factor):
    image = Image.open(input_image_path)
    original_width, original_height = image.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    resized_image = image.resize((new_width, new_height))
    resized_image.save(output_image_path)

input_image_path = "path/to/your/input/image.jpg"
output_image_path = "path/to/your/output/resized_image.jpg"
scale_factor = 2.0  # You can adjust this factor based on your needs

increase_image_size(input_image_path, output_image_path, scale_factor)

7. plot histogram of an image

import cv2
import matplotlib.pyplot as plt

def plot_histogram(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    plt.plot(hist)
    plt.title('Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

image_path = 'path/to/your/image.jpg'
plot_histogram(image_path)


8. to play audio, video file
FOR AUDIO: -
----------
from pydub import AudioSegment
from pydub.playback import play

wav_file = AudioSegment.from_file(file="D://Multimedia//file_example_WAV_1MG.wav", format="wav")
play(wav_file)

FOR VIDEO: -
---------
import vlc
import time

# creating vlc media player object
media_player = vlc.MediaPlayer()
 
# media object
media = vlc.Media("D:\Multimedia\Python_programs\sample-mp4-file.mp4")
 
# setting media to the media player
media_player.set_media(media)
 
# start playing video
media_player.play()
 
# wait so the video can be played for 15 seconds
# irrespective for length of video
time.sleep(15)
 
# getting media
value = media_player.get_media()
 
# printing media
print("Media : ")
print(value)

# getting the duration of the video  
video_duration = media_player.get_length()  
       
# printing the duration of the video  
print("Duration : " + str(video_duration))  
'''

