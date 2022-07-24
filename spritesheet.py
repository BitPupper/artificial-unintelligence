import pygame

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour, mirrorx=False, mirrory=False):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		if(mirrorx):
			image = pygame.transform.flip(image, True, False)
		if(mirrory):
			image = pygame.transform.flip(image, False, True)
		
		image.set_colorkey(colour)
		return image