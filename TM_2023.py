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
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TM Game')
bg_color = pygame.Color('light grey')

#Player image
p_image = pygame.image.load("player.png").convert_alpha()
pl_image = pygame.transform.smoothscale(p_image, (p_image.get_width() / 3.5, p_image.get_height() / 3.5))
player_image = pl_image.get_rect()

#Background image
background= pygame.image.load("Bkgrnd_game1.jpg")


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
		self.image = image
		self.velocity = pygame.math.Vector2(0, 0)
		self.acceleration = pygame.math.Vector2(0, 0.5)
		self.jump_power = -15
		




	def appear(self, screen):
		pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.length, self.height))
		# screen.blit(self.image, (self.x, self.y))

	def move_right(self):
		self.x += speed_x

	def move_left(self):
		self.x -= speed_x


	#def stop_jumping(self):
	#	self.jumping = False
	#	self.y_velocity = jump_height


	def update(self, blocks_sprite):
		super().update()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.velocity.x = -7.5
		elif keys[pygame.K_RIGHT]:
			self.velocity.x = 7.5
		else:
			self.velocity.x = 0
        
		if keys[pygame.K_SPACE]:
			self.velocity.y = self.jump_power
        
		self.velocity += self.acceleration
		self.rect.move_ip(self.velocity.x, self.velocity.y)
		self.checkcollisions(blocks_sprite)

	def checkcollisions(self, blocks_sprite):
		for block in blocks_sprite:
			if self.rect.colliderect(block.rect):
				if self.velocity.x > 0:
					self.rect.right = block.rect.left
					self.velocity.x = 0
				elif self.velocity.x < 0:
					self.rect.left = block.rect.right
					self.velocity.x = 0
				elif self.velocity.y > 0:
					self.rect.bottom = block.rect.top
					self.velocity.y = 0
				elif self.velocity.y < 0:
					self.rect.top = block.rect.bottom
					self.velocity.y = 0


	def animate(self):
		if self.moving_left:
			self.move_left()
		if self.moving_right:
			self.move_right()
'''
		if self.jumping:
			self.y -= self.y_velocity
			self.y_velocity -= y_gravity    
			if self.y_velocity <- jump_height:
				self.stop_jumping()
'''


#Blocks
class Blocks(pygame.sprite.Sprite):
	def __init__(self, x2, y2, block_size, block_size2):
		super().__init__()
		self.x2 = x2
		self.y2 = y2
		self.block_size = block_size
		self.block_size2 = block_size2
		blocks_sprite.add(self)

	def appear(self, screen):
		pygame.draw.rect(screen, (0, 0, 0), (self.x2, self.y2, self.block_size, self.block_size2))



#Enemies
class Enemy():
	def __init__(self):
		pass






#PLAYER'S ATTRIBUTES VALUES

#Jumping
y_gravity = 1
jump_height= 20
y_velocity = jump_height 


#Moving
move_right= False
move_left= False
move_up= False

speed_x = 7.5

#Player
player = Player(playerX, playerY, 10, 80, player_image)

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

#block_sprites = [block1, block2, block3, block4]
blocks_sprite.add(block1, block2, block3, block4, block5)

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

		#if Player.topleft == blocks_sprite.bottom or player_sprite.midtop == blocks.bottom or player_sprite.topright == blocks.bottom:
			#print ('Step 1')
			#jumping == False



	player.update(blocks_sprite)
	player.checkcollisions()
	player.animate()

	#Visuals
	screen.blit(background, (0, 50))
	screen.blit(pl_image, player_image)

	for sprite in player_sprite:
		sprite.appear(screen)

	for sprite in blocks_sprite:
		sprite.appear(screen)



    #Updating the window
	pygame.display.flip()
	clock.tick(60)