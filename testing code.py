import pygame, sys

#General setup
pygame.init()
clock = pygame.time.Clock()

YELLOW = (255, 255, 0) #Horrific yellow for debugging rectangles
playerX, playerY = (241, 425)
block_size = 50
block_size2 = 50
min_y = 425  #Value according the game's ground level

#Making anything dissapear
transapency = (0, 0, 0, 0)

#Background image
background= pygame.image.load("Bkgrnd_game1.jpg")
bg= background.get_rect()
background_width, background_height = background.get_size()

#Dungeon image
dungeon= pygame.image.load("bg2.png")
dungeon_width, dungeon_height = dungeon.get_size()

#Screen appearance
screen_width = backgroung_width
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TM Game')
bg_color = pygame.Color('light grey')

#New screen appearance
dngn_screen_width = dungeon_width * 2 - 55
dngn_screen_height = dungeon_height * 3 - 75

#Game Text Font
game_font = pygame.font.Font("freesansbold.ttf", 32)

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

		'''
		There seem to STILL be a problem with the player's hitbox, whether it is a 
		collision with a block or a collision with the door. 
		The issue is the following:
		The collisions with the door seem to be off because the levels that getting 
		printed only appear with the left of the player's hitbox, where it originally was
		before having it moved.
		The same is for the collisions with the blocks. The collisions with the blocks are
		not complete, so it is hard to tell whether it actually is broken or not.
		'''

	def appear(self, screen):
		pygame.draw.rect(screen, YELLOW, self)
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

	#def handle_collision(self, block):

		'''
		if self.rect.bottom > block.rect.top and self.rect.top < block.rect.top:
			self.rect.bottom = block.rect.top
			self.y = max(self.y, min_y)
			self.y = self.rect.y
			self.stop_jumping()
			y_velocity = 0
			on_ground = True
			print('bottom')

		elif self.rect.top < block.rect.bottom and self.rect.y > block.rect.y:
			self.rect.top = block.rect.bottom
			self.rect.bottom = min(self.y, min_y)
			self.y = self.rect.y
			self.y_velocity = 0
			print("top")

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
		'''


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
player = Player(playerX, playerY, 80, 93, player_rect)
player_sprite = pygame.sprite.Group(player)




#BLOCK'S ATTRIBUTES VALUES

#Blocks
blocks_sprite = pygame.sprite.Group()

#block1 = Blocks(400, 350, block_size, block_size2, block_rect)
#block2 = Blocks(550, 350, block_size, block_size2, block_rect)
#block3 = Blocks(250, 350, block_size, block_size2, block_rect)
block4 = Blocks(10, 350, block_size, block_size2, block_rect)
#block5 = Blocks(340, 310, block_size, block_size2, block_rect)
block6 = Blocks(460, 475, block_size, block_size2, block_rect)

blocks_sprite.add(block4, block6)#, block2, block3, block1, block5)


for block in blocks_sprite:
	block.rect.x = block.x2
	block.rect.y = block.y2



#EXIT ATTRIBUTES
#Levels
level = 0 

#Exit Method

door0 = Exit(500, 250, exitlength, exitheight, color)
door1 = Exit(650, 400, exitlength, exitheight, color)
door2 = Exit(100, 400, exitlength, exitheight, color)

exit_sprite = pygame.sprite.Group(door0)


game_running = True
#Game loop
while game_running:

	pygame.display.flip()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				game_running = False


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

	#Commenting these collisions in order to fix it in the Player class
	
	#player.handle_collision(block)

	'''
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
	'''
	if pygame.sprite.spritecollideany(player, blocks_sprite) is not (None):
		if pygame.sprite.spritecollide(player, blocks_sprite, False):			
			if player.rect.bottom > block.rect.top :
				player.rect.bottom = block.rect.top
				player.y = player.rect.y
				player.y_velocity = 0
				player.y = min(player.y, 425)
				print("bottom")
			elif player.rect.top < block.rect.bottom :
				player.rect.top = block.rect.bottom
				player.y = player.rect.y
				y_velocity = - y_gravity
				jumping = False
				print("top")
			elif player.rect.right > block.rect.left and player.rect.left < block.rect.left:
				player.rect.right = block.rect.left
				player.x = player.rect.x
				print("right")
			elif player.rect.left < block.rect.right and player.rect.right > block.rect.right:
				player.rect.left = block.rect.right
				player.x = player.rect.x
				print("left")


	player.animate()

	#Visuals
	screen.blit(background, (0, 0))

	#Exit collisions
	exit_collisions = pygame.sprite.spritecollideany(player, exit_sprite) is not (None)

	if exit_collisions:
		dngn_screen = pygame.display.set_mode((dngn_screen_width, dngn_screen_height))
		bg.background.fill(transapency)
		if pygame.sprite.spritecollide(player, exit_sprite, True):
			screen.blit(dungeon, (0, 0))
			level = level +1

			if level == 1:
				player.x, player.y = 241, 425
				pygame.sprite.Sprite.add(door1, exit_sprite)
				level_text = game_font.render( "Level "f"{level}", True, (0, 0, 0))

				for sprite in player_sprite:
					sprite.appear(dngn_screen)
				for sprite in blocks_sprite:
					sprite.appear(dngn_screen)
				for sprite in exit_sprite:
					sprite.appear(dngn_screen)

	
	














	'''if exit_collisions:
						screen.blit(dungeon, (0, 0))
						level = level +1
						player.x, player.y = 241, 430
						level_text = game_font.render( "Level "f"{level}", True, (0, 0, 0))
						
						for sprite in player_sprite:
							sprite.appear(screen)
			
						for sprite in blocks_sprite:
							sprite.appear(screen)
			
			
						if level == 1:
							screen.blit(level_text, ((screen_width * 9/10) - 100, screen_height - 500))
			
			
							for sprite in exit_sprite:
								sprite.appear(screen)
			
						if level == 2:
							screen.blit(level_text, ((screen_width * 9/10) - 100, screen_height - 500))
			
							for sprite in exit_sprite:
								sprite.appear(screen)'''


	#Debugging the player's y coordinate
	'''
	The player only realizes that he is under the ground (y level above 425)
	only after 20 pixels before coming back to the ground.
	'''
	print(player.x, player.y)

	if player.y >= 425:
		player.y = 425
	else:
		print("Player going down!!!")
		print(screen_width, screen_height)
	

	for sprite in player_sprite:
		sprite.appear(screen)

	for sprite in blocks_sprite:
		sprite.appear(screen)

	for sprite in exit_sprite:
		sprite.appear(screen)


	#Updating the window
	pygame.display.flip()
	clock.tick(60)
