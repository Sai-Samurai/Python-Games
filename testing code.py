import pygame, sys

#General setup
pygame.init()
clock = pygame.time.Clock()

playerX, playerY = (241, 445)
block_size = 50
block_size2 = 50
min_y = 525  # Adjust the value according to your game's ground level

#Background image
background= pygame.image.load("Bkgrnd_game1.jpg")
backgroung_width, background_height = background.get_size()
#Screen appearance
screen_width = backgroung_width
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TM Game')
bg_color = pygame.Color('light grey')

#Player image
p_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.smoothscale(p_image, (p_image.get_width() / 3.5, p_image.get_height() / 3.5))
player_rect = player_image.get_rect()




#Player
class Player(pygame.sprite.Sprite):

	def __init__(self, x, y, length, height, image):
		super().__init__()
		self.x = x
		self.y = y
		self.length = length
		self.height = height
		self.moving_right = False
		self.moving_left = False
		self.jumping = False
		self.y_velocity = jump_height
		self.image = image
		self.rect = pygame.Rect(x, y, length, height)

	def appear(self, screen):
		pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.length, self.height))
		# screen.blit(screen, self.image, (self.x, self.y))

	def move_right(self):
		self.x += speed_x

	def move_left(self):
		self.x -= speed_x

	def stop_jumping(self):
		self.jumping = False
		self.y_velocity = jump_height

	def animate(self):
		if self.moving_left:
			self.move_left()
		if self.moving_right:
			self.move_right()

		if self.jumping:
			self.y -= self.y_velocity
			self.y_velocity -= y_gravity    
			if self.y_velocity <- jump_height:
				self.stop_jumping()

	def updateplayer(x, y):
		player.x
		player.y



#Blocks
class Blocks(pygame.sprite.Sprite):
	def __init__(self, x2, y2, block_size, block_size2):
		super().__init__()
		self.x2 = x2
		self.y2 = y2
		self.block_size = block_size
		self.block_size2 = block_size2
		self.rect = pygame.Rect(x2, y2, block_size, block_size2)
		blocks_sprite.add(self)

	def appear(self, screen):
		pygame.draw.rect(screen, (0, 0, 0), (self.x2, self.y2, self.block_size, self.block_size2))

	def updateblocks(x2, y2):
		block1.x2
		block1.y2



#Enemies
class Enemy():
	def __init__(self):
		pass






#PLAYER'S ATTRIBUTES VALUES

#Jumping
y_gravity = 1
jump_height= 20
y_velocity = jump_height 
on_ground = True


#Moving
move_right= False
move_left= False
move_up= False

speed_x = 7.5

#Player
player = Player(playerX, playerY, 10, 80, player_rect)

#sprites = [player]
player_sprite = pygame.sprite.Group(player)


#BLOCK'S ATTRIBUTES VALUES

#Blocks
blocks_sprite = pygame.sprite.Group()

block1 = Blocks(400, 350, block_size, block_size2)
block2 = Blocks(550, 350, block_size, block_size2)
block3 = Blocks(250, 350, block_size, block_size2)
block4 = Blocks(10, 350, block_size, block_size2)
block5 = Blocks(340, 310, block_size, block_size2)
block6 = Blocks(460, 475, block_size, block_size2)

#block_sprites = [block1, block2, block3, block4]
blocks_sprite.add(block1, block2, block3, block4, block5)


for block in blocks_sprite:
	block.rect.x = block.x2
	block.rect.y = block.y2

'''
collisions = pygame.sprite.groupcollide(player_sprite, blocks_sprite, False, False)
if collisions:
	print("We've got a collision!!")
'''


#Game loop
while True:

	pygame.display.flip()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_RIGHT:
				player.moving_right = True

			if event.key == pygame.K_LEFT:
				player.moving_left = True

			if event.key == pygame.K_SPACE:
				player.jumping = True
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				player.moving_right = False
			if event.key == pygame.K_LEFT:
				player.moving_left = False




	player.rect.x = player.x
	player.rect.y = player.y


	collisions = pygame.sprite.spritecollide(player, blocks_sprite, False)
	if collisions:

		for block in collisions:

			if player.rect.colliderect(block.rect):

				if player.rect.bottom > block.rect.top and player.rect.top < block.rect.top:
					player.rect.bottom = block.rect.top
					player.y = max(player.y, min_y)
					player.y = player.rect.y
					player.stop_jumping()
					y_velocity = 0
					on_ground = True
					print('bottom')

				elif player.rect.top < block.rect.bottom and player.rect.bottom > block.rect.bottom:
					player.rect.top = block.rect.bottom
					player.y = player.rect.y
					y_velocity = 0
					player.y += y_gravity
					print('top')

				if player.rect.right > block.rect.left and player.rect.left < block.rect.left:
					player.rect.right = block.rect.left
					player.x = player.rect.x
					if player.rect.bottom > block.rect.top and player.rect.top < block.rect.bottom:
						player.rect.bottom = block.rect.top
						player.y = player.rect.y
						player.stop_jumping()
						y_velocity = 0
					elif player.rect.top < block.rect.bottom and player.rect.bottom > block.rect.bottom:
						player.rect.top = block.rect.bottom
						player.y = player.rect.y
						y_velocity = 0
					print('right')

				elif player.rect.left < block.rect.right and player.rect.right > block.rect.right:
					player.rect.left = block.rect.right
					player.x = player.rect.x
					if player.rect.bottom > block.rect.top and player.rect.top < block.rect.bottom:
						player.rect.bottom = block.rect.top
						player.y = player.rect.y
						player.stop_jumping()
						y_velocity = 0
					elif player.rect.top < block.rect.bottom and player.rect.bottom > block.rect.bottom:
						player.rect.top = block.rect.bottom
						player.y = player.rect.y
						y_velocity = 0
					print('left')

	if not collisions:
		on_ground = True

	if not on_ground:
		player.rect.y -= y_gravity
		y_velocity -= y_gravity
                    

				#if player.rect.right >= block.rect.left:
				#	player.rect.right = block.rect.left
				#	player.stop_jumping()
				#	print('right')
				#elif player.rect.left <= block.rect.right:
				#	player.rect.left = block.rect.right
				#	player.stop_jumping()
				#	print('left')

	print(player.x, player.y)



	player.animate()

	#Visuals
	screen.blit(background, (0, 50))
	screen.blit(player_image, player_rect)

	for sprite in player_sprite:
		sprite.appear(screen)

	for sprite in blocks_sprite:
		sprite.appear(screen)



    #Updating the window
	pygame.display.flip()
	clock.tick(60)
