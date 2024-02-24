import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f'ServiceAccountToken.json'

FILE_PATH = f'C://Users//ameya//OneDrive//Desktop//2023-04-28//ret.jpeg'
with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()


image= vision.Image(content-content)
response= client.document_text_detection(image=image)
docText = response.full_text_annotation.text
print(docText)
