import serial
from PIL import Image
import time

# Open serial connection to Arduino
ser = serial.Serial('COM3', 9600)

# Load image
image = Image.open("image_4.png")
pixels = image.load()

# Get image dimensions
width, height = image.size

# Create empty matrix to hold all pixel values
pixel_data = []
#while True:
# Loop through each pixel and add its RGB values to the matrix
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        #led_index = y * width + x
        #data = (r, g, b)
        #print(data)
        # color_string = " ".join(str(value) for value in data)
        # send_string = "[" + color_string + "]"
        #print(send_string)
        # pixel_data.append(x)
        # pixel_data.append(y)
        pixel_data.append(r)
        pixel_data.append(g)
        pixel_data.append(b)
        color_string = str(pixel_data).replace(',', '')

        # Send pixel data to Arduino
    ser.write((color_string.encode()))
    time.sleep(1.5)
    ser.write((color_string.encode()))
    print(color_string)
    # wait for a short time before sending the next set of RGB values
    #time.sleep(1.2)
    #pixel_data = []