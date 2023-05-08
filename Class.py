import pygame, sys

#General setup
pygame.init()
clock = pygame.time.Clock()

playerX, playerY = (241, 445)
block_size = 50
block_size2 = 50

#Screen appearance
screen_width=950
screen_height=650
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')
bg_color= pygame.Color('light grey')

#Background image
background= pygame.image.load("Bkgrnd_game1.jpg")

#Player
class Player():
	def __init__(self, x, y, length, height):
		self.x = x
		self.y = y
		self.length = length
		self.height = height

	def appear(self, screen):
		pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.length, self.height))


#Blocks
class Blocks():
	def __init__(self, x2, y2, block_size, block_size2):
		self.x2 = x2
		self.y2 = y2
		self.block_size = block_size
		self.block_size2 = block_size2

	def appeaar(self, screen):
		pygame.draw.rect(screen, (0, 0, 0), (self.x2, self.y2, self.block_size, self.block_size2))




jumping = False
y_gravity = 1
jump_height= 20
y_velocity = jump_height

move_right= False
move_left= False
move_up= False

speed_x = 7.5



#Game running
while True:

	player = Player(playerX, playerY, 10, 80)
	block1 = Blocks(400, 350, block_size, block_size2)
	block2 = Blocks(550, 350, block_size, block_size2)
	#player.appear(screen)
	#block1.appeaarr(screen)
	pygame.display.flip()



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_RIGHT:
				move_right = True
				player = Player(playerX, playerY, 10, 80)
				#player.appear(screen)
				pygame.display.flip()

			if event.key == pygame.K_LEFT:
				move_left = True
				player = Player(playerX, playerY, 10, 80)
				#player.appear(screen)
				pygame.display.flip()

			if event.key == pygame.K_SPACE:
				jumping = True
				player = Player(playerX, playerY, 10, 80)
				#player.appear(screen)
				pygame.display.flip()

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				move_right = False
			if event.key == pygame.K_LEFT:
				move_left = False
			if event.key == pygame.K_SPACE:
				jumping = True


	if move_right:
		playerX += speed_x
	if move_left:
		playerX -= speed_x
    
	if jumping:
		playerY -= y_velocity
		y_velocity -= y_gravity     
		if y_velocity <- jump_height:
			jumping= False
			y_velocity= jump_height



	#Visuals
	screen.blit(background, (0, 50))
	player.appear(screen)
	block1.appeaar(screen)
	block2.appeaar(screen)


    

    #Updating the window
	pygame.display.flip()
	clock.tick(60)