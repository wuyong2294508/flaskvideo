from flask import Flask, render_template, Response
from camera_opencv import CameraCapture

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
	
def gen(camera):
	while True:
		frame = camera.frames()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
	
@app.route('/video_feed')
def video_feed():
	return Response(gen(CameraCapture()), mimetype = 'multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888, debug=True, threaded=True)