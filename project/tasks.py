from celery import Celery
from PIL import Image
from PIL import ImageFilter

app=Celery('tasks',broker='amqp://ernesto:120100@148.228.16.6/vernesto')

@app.task
def resize_image(image_path,output_path,size):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(output_path)
@app.task
def blur_image(image_path,output_path):
    with Image.open(image_path) as img:
        im1= img.filter(ImageFilter.BoxBlur(4))
        im1.save(output_path)
