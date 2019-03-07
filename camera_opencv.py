import cv2

class CameraCapture():
	def __init__(self):
		self.camera = cv2.VideoCapture(0)
		if not self.camera.isOpened():
			raise RuntimeError('Could not start camera.')

		
	def __del__(self):
		self.camera.release
		
	def frames(self):
		# read current frame
		_, img = self.camera.read()
		# encode as a jpeg image and return it
		return cv2.imencode('.jpg', img)[1].tobytes()