import pygame
import pygame.camera
from pygame.locals import *
 
class CameraCapture(object):
	def get_frame(self):
		#pygame.init()
		pygame.camera.init()
		cam = pygame.camera.Camera("/dev/video0",(640,480))
		cam.start()
		while True:
			if cam.query_image():
				return pygame.image.tostring(cam.get_image(),'RGB')
		#pygame.image.save(image,"/share/flaskweb/image.jpg")
		#cam.stop()
		
if __name__ == '__main__':
    CameraCapture().get_frame()