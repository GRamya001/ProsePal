# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 23:23:22 2023

@author: chinn
"""


import requests
import json
import config

def get_image(query):
    access_key = 'qsX6c_tV5xsLx4k8uqqyrdd3EuXU-MfJEbzaTCZYsrQ'
    base_url = 'https://api.unsplash.com/'
    endpoint = 'search/photos'
    headers = {
        'Authorization': f'Client-ID {access_key}',
        'Accept-Version': 'v1'
    }

    params = {
        'query': query,
        'per_page': 1  # Number of images to retrieve
    }
    response = requests.get(f'{base_url}{endpoint}', headers=headers, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        if 'results' in data and len(data['results']) > 0:
            image_url = data['results'][0]['urls']['regular']
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open('image.jpg', 'wb') as file:
                    file.write(image_response.content)
                    print('Image saved successfully.')
            else:
                print('Error occurred while saving the image.')
        else:
            print('No images found.')
    else:
        print('Error occurred while retrieving images.')
    return image_url

write_up = write_up = """
Great things in life are often effortless. 
Best friendships you ever had best memories 
you ever made and best people you are with 
don't require a lot of questioning. and fighting 
with yourself to preserve. Everything just feels 
right with them. They just exist and you live with them.
Everything you do and spend your time with is is 
just you loving to do it from the bottom of your heart. 
So it never feels like an effort. The best things in 
life are often simple calm and close to heart.
"""
image_url = get_image(write_up)
get_image(write_up)

from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def add_text_to_image(image_path, text, output_path):
    image = Image.open(image_path)
    opacity = 0.3  # Opacity value between 0.0 (transparent) and 1.0 (opaque)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(opacity)

    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("font.otf", size=50)
    font_writer =  ImageFont.truetype("font.otf", size=50)
    image_width, image_height = image.size

    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
    writer_name = "@ramya0120"
    writer_width, writer_height = draw.textsize(writer_name, font=font_writer)
    writer_position = ((image_width - writer_width) // 2, (image_height + text_height - 10) // 2)

    text_color = (255, 255, 255) 
    
    draw.text(text_position, text, font=font, fill=text_color)
    draw.text(writer_position, writer_name, font=font_writer, fill=text_color)
    image.save(output_path)

image_path = 'image.jpg'
output_path = 'output.jpg'
text = write_up

add_text_to_image(image_path, text, output_path)


def get_hashtags(key_word):
    url = "https://hashtag5.p.rapidapi.com/api/v2.1/tag/predict"

    querystring = {"keyword": key_word}
    
    headers = {
     	"X-RapidAPI-Key": "a8f718383dmshe97932bf0ad9dd9p158b28jsned7aac5e0487",
     	"X-RapidAPI-Host": "hashtag5.p.rapidapi.com"
    }
    

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Extract relevant hashtags from the API response
        hashtags = []
        for tag in data["tags"]:
            hashtags.append('#'+tag)
        
        return hashtags
    except requests.exceptions.RequestException as e:
        print('Error occurred:', e)
        return None

key_word = input('Enter keyword for hash tags: ')
hashtags = get_hashtags(key_word)
if hashtags:
    print('Hashtags:')
    for hashtag in hashtags:
        print(hashtag)
hastag_value = ''.join(hashtags)

url = "https://image-caption-generator2.p.rapidapi.com/v2/captions"

querystring = {"imageUrl":str(image_url),"limit":"3"}

headers = {
 	"X-RapidAPI-Key": "a8f718383dmshe97932bf0ad9dd9p158b28jsned7aac5e0487",
 	"X-RapidAPI-Host": "image-caption-generator2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

caption = data['captions'][0]

print(data['captions'][0])


from instagrapi import Client

c = Client()
c.login(config.username, config.password)
media = c.photo_upload(
    path="output.jpg",caption = caption +' '+hastag_value)











