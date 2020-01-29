from PIL import Image
import sys
 

class StenoDecode:
	""" parameter: image path, X-coordinate range, Y-coordinate range (this can be found in the powershell script)"""
	def __init__(self, path, x_coordinate, y_coordinate):
		self.image_path = path
		self.y_coordinate = y_coordinate
		self.x_coordinate = x_coordinate

	def decode(self):
		image = Image.open(self.image_path)
		pixel = image.load()
		payload = bytearray()
		for y in range(self.y_coordinate):
			for x in range(self.x_coordinate):
				red_channel,green_channel,blue_channel = pixel[x,y]
				payload.append((blue_channel & 15) * 16 | green_channel & 15)
		return payload

if __name__ == '__main__':
	s = StenoDecode('image003.png',2679,2)
	print(s.decode())
