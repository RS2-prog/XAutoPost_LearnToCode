from post import postToX
from contents import getContents
from contents import moveContents
import os

base_path = os.path.dirname(__file__)
folder_path = os.path.join(base_path, 'contents')

image_path, text_path = getContents(folder_path)
#print("Image Path:", image_path)
#print("Text Path:", text_path)

with open(text_path, 'r', encoding='utf-8') as file:
    tweet_text = file.read()
    
#print(tweet_text)

postToX(tweet_text, image_path)

moveContents(text_path)
moveContents(image_path)