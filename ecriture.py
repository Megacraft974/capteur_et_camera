from sense_hat import SenseHat
from time import sleep
from PIL import Image

sense=SenseHat()

background_color = [0,0,0]

def character_list():
    global text_dict
    img = Image.open('sense_hat_text.png').convert('RGB')
    pixel_list = list(map(list, img.getdata()))

    with open('sense_hat_text.txt', 'r') as f:
        loaded_text = f.read()
    text_dict = {}
    for index, s in enumerate(loaded_text):
        start = index * 40
        end = start + 40
        char = pixel_list[start:end]
        text_dict[s] = char

character_list()

count = 0
for i in text_dict:
    toShow = []
    print(background_color*int(64-len(text_dict[i])/2))
    toShow.append(background_color*int(64-len(text_dict[i])/2))
    toShow.append(text_dict[i])
    toShow.append(background_color*int(64-len(text_dict[i])/2))
    print(len(toShow))
    print(toShow)
    while not "" in toShow:
        toShow.replace("'","")
    print(len(toShow))
    print(toShow)
    sense.set_pixels(toShow)
    count += 1
