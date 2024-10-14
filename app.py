import glob
from flask import Flask, render_template, request, Response, redirect, url_for
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os
from model import runModels
import cv2
import datetime


global capture
capture=0

load_dotenv()

app =Flask(__name__, template_folder = 'templates', static_folder='static',static_url_path='/')

@app.route('/')
def index():
    return render_template('about.html', active='index')

@app.route('/milestone1', methods=['GET','POST'])
def interaction_1():
    if request.method =='POST':
        f = request.files["imgFile"]
        file_name = secure_filename(f.filename)
        cwd = os.getcwd()
        upld_path = cwd+'/static/imgs/' + file_name
        f.save(upld_path)
        img_path = 'imgs/'+file_name
        (caption, story) = runModels(upld_path)
        return render_template('milestone1.html', active='interaction_1',imgPath = img_path, story=story,caption=caption)
    else:
        return render_template('milestone1.html', active='interaction_1')

@app.route('/camera', methods=['GET','POST'])
def interaction_2():
    global camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture=1
        elif request.form.get('delete') == 'Delete All':
            delete_all_images()
    images = update_image_folder()
    return render_template('camera.html', images=images)

def delete_all_images():
    image_folder = 'static/imgs/shots'
    # Use glob to match all image files in the directory
    files = glob.glob(os.path.join(image_folder, '*'))
    for f in files:
        try:
            os.remove(f)  # Delete each file
        except Exception as e:
            print(f"Error deleting file {f}: {e}")


#make shots directory to save pics
try:
    os.mkdir('./static/imgs/shots')
except OSError as error:
    pass

camera = cv2.VideoCapture(0) #0 is computer, 1 is connected phone

def update_image_folder():
     # Define the folder where images are stored
    image_folder = 'static/imgs/shots'
    # List all image filenames in the folder
    images = os.listdir(image_folder)
    return images

def gen_frames():  # generate frame by frame from camera
    global capture
    while True:
        success, frame = camera.read() 
        
        if success:
            if(capture):
                capture=0
                now = datetime.datetime.now()
                p = os.path.sep.join(['static/imgs/shots', "shot_{}.png".format(str(now).replace(":",'_'))])
                p = p.replace(" ","_")
                cv2.imwrite(p, frame)
                images = update_image_folder()
                return render_template('camera.html', images=images)
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
        else:
            pass
    

    
    
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0')