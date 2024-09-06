'''for permission'''
import requests

URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
response = requests.get(URL, timeout=10)
with open("imagenet_classes.txt", "w", encoding='utf-8') as f:
    f.write(response.text)
