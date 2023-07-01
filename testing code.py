import pygame, sys

#General setup
pygame.init()
clock = pygame.time.Clock()

YELLOW = (255, 255, 0) #Horrific yellow for debugging rectangles
playerX, playerY = (241, 420)
block_size = 50
block_size2 = 50
min_y = 420  #Value according the game's ground level

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

#Block image
b_image = pygame.image.load("Brick_texture.png").convert_alpha()
block_image = pygame.transform.smoothscale(b_image, (b_image.get_width() / 3.3, b_image.get_height() / 3.3))
block_rect = block_image.get_rect()



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

	def hitbox(self, new_length, new_height):
		self.length = new_length
		self.height = new_height
		self.rect.width = new_length
		self.rect.height = new_height

	def appear(self, screen):
		pygame.draw.rect(screen, YELLOW, (self.rect.x + 58, self.rect.y + 27, self.length, self.height))
		screen.blit(player_image, player_rect)

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

		player_rect.x = self.x
		player_rect.y = self.y

	def updateplayer(x, y):
		player.x
		player.y

	def handle_collision(self, block):
		if self.rect.bottom > block.rect.top and self.rect.top < block.rect.top:
			self.rect.bottom = block.rect.top
			self.y = max(self.y, min_y)
			self.y = self.rect.y
			self.stop_jumping()
			y_velocity = 0
			on_ground = True
			print('bottom')

		elif self.rect.top < block.rect.bottom and self.rect.bottom > block.rect.bottom:
			self.rect.top = block.rect.bottom
			self.y = self.rect.y
			y_velocity = 0
			self.y += y_gravity
			print('top')

		if self.rect.right > block.rect.left and self.rect.left < block.rect.left:
			self.rect.right = block.rect.left
			self.x = self.rect.x
			if self.rect.bottom > block.rect.top and self.rect.top < block.rect.bottom:
				self.rect.bottom = block.rect.top
				self.y = self.rect.y
				self.stop_jumping()
				y_velocity = 0
			elif self.rect.top < block.rect.bottom and self.rect.bottom > block.rect.bottom:
				self.rect.top = block.rect.bottom
				self.y = self.rect.y
				y_velocity = 0
			print('right')

		elif self.rect.left < block.rect.right and self.rect.right > block.rect.right:
			self.rect.left = block.rect.right
			self.x = self.rect.x
			if self.rect.bottom > block.rect.top and self.rect.top < block.rect.bottom:
				self.rect.bottom = block.rect.top
				self.y = self.rect.y
				self.stop_jumping()
				y_velocity = 0
			elif self.rect.top < block.rect.bottom and self.rect.bottom > block.rect.bottom:
				self.rect.top = block.rect.bottom
				self.y = self.rect.y
				y_velocity = 0
			print('left')





#Blocks
class Blocks(pygame.sprite.Sprite):
	def __init__(self, x2, y2, block_size, block_size2, texture):
		super().__init__()
		self.x2 = x2
		self.y2 = y2
		self.block_size = block_size
		self.block_size2 = block_size2
		self.rect = pygame.Rect(x2, y2, block_size, block_size2)
		blocks_sprite.add(self)
		self.texture = texture

	def appear(self, screen):
		pygame.draw.rect(screen, YELLOW, self.rect)
		screen.blit(block_image, self.rect)
		# pygame.draw.rect(screen, (0, 0, 0), (self.x2, self.y2, self.block_size, self.block_size2))

	def updateblocks(self, x2, y2):
		self.x2
		self.y2


#Enemies
class Enemy():
	def __init__(self):
		pass


#Exit
color = (100, 150, 200)
exitlength = 50
exitheight = 100
class Exit(pygame.sprite.Sprite):
	def __init__(self, x3, y3, exitlength, exitheight, color):
		super().__init__()
		self.x3 = x3
		self.y3 = y3
		self.exitlength = exitlength
		self.exitheight = exitheight
		self.color = color
		self.rect = pygame.Rect(x3, y3, exitlength, exitheight)
		#exit_sprite.add(self)

	def appear(self, screen):
		pygame.draw.rect(screen, color, self.rect)





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
player_sprite = pygame.sprite.Group(player)

#Hitbox
new_length = 80
new_height = 93
player.hitbox(new_length, new_height)



#BLOCK'S ATTRIBUTES VALUES

#Blocks
blocks_sprite = pygame.sprite.Group()

block1 = Blocks(400, 350, block_size, block_size2, block_rect)
block2 = Blocks(550, 350, block_size, block_size2, block_rect)
block3 = Blocks(250, 350, block_size, block_size2, block_rect)
block4 = Blocks(10, 350, block_size, block_size2, block_rect)
block5 = Blocks(340, 310, block_size, block_size2, block_rect)
block6 = Blocks(460, 475, block_size, block_size2, block_rect)

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


#Levels
level = 0 

#Exit Method

door = Exit(500, 250, exitlength, exitheight, color)
exit_sprite = pygame.sprite.Group(door)

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
	print(collisions)
	if collisions:
		for block in collisions:
			print(block)
			if player.rect.colliderect(block.rect): #isn't this always true?!
				player.handle_collision(block)
			else:
				raise Exception("weird!!!")

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

	# print(player.x, player.y)

	#Exit collisions
	exit_collisions = pygame.sprite.spritecollide(player, exit_sprite, False)
	
	if exit_collisions:
		print("exit")
		level += 1
		print("Level ", level)

	player.animate()

	#Visuals
	screen.blit(background, (0, 50))

	for sprite in player_sprite:
		sprite.appear(screen)

	for sprite in blocks_sprite:
		sprite.appear(screen)

	for sprite in exit_sprite:
		sprite.appear(screen)

    #Updating the window
	pygame.display.flip()
	clock.tick(60)
