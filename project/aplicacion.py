from flask import Flask,request,jsonify
from werkzeug.utils import secure_filename
from tasks import resize_image
from tasks import blur_image
import os
app =Flask(__name__)
UPLOAD_FOLDER='/home/ernesto/distribuida/proyecto/imagenes/entrada/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if'file' not in request.files:
        return jsonify({'error':'No file apart'}),400
    file=request.files['file']
    opcion=request.form.get('opcion')
    print(opcion)
    if file.filename=="":
        return jsonify({'error':'No selected file'}),400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(filepath)
        if opcion=='resize':
            resize_image.delay(filepath,'/home/ernesto/distribuida/proyecto/imagenes/salida/'+filename,(250,250))
        if (opcion=='blur'):
            blur_image.delay(filepath,'/home/ernesto/distribuida/proyecto/imagenes/salida/'+filename)
        return jsonify({'meissage':'File uploaded and processing started.'}),202
