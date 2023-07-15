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
background = pygame.image.load("Bkgrnd_game1.jpg")
background_width, background_height = background.get_size()

#Dungeon image
dungeon = pygame.image.load("bg2.png")
dungeon_width, dungeon_height = dungeon.get_size()

#Screen appearance
screen_width = background_width
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TM Game')
bg_color = pygame.Color('black')

#New screen appearance
dngn_screen_width = dungeon_width - 535
dngn_screen_height = dungeon_height
dungeon_screen = pygame.Surface((dngn_screen_width, dngn_screen_height))
dungeon_screen.blit(dungeon, (0, 0))

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

	def appear(self, screen):
		pygame.draw.rect(screen, YELLOW, self)
		screen.blit(player_image, player_rect)

	def move_right(self):
		self.x += speed_x
		self.rect.x = self.x

	def move_left(self):
		self.x -= speed_x
		self.rect.x = self.x

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

	def updateplayer(self, x, y):
		self.x
		self.y

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


#Narrator / Main evil villain
class Narrator():
	def __init__(self, narX, narY, narlength, narheight):
		super().__init__()
		self.narX = narX
		self.narY = narY
		self.narlength = narlength
		self.narheight = narheight
		self.narcolor = narcolor
		self.rect = pygame.Rect(narX, narY, narlength, narheight)

	def appear(self, screen):
		pygame.draw.rect(screen, narcolor, self.rect)


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

block1 = Blocks(400, 350, block_size, block_size2, block_rect)
block2 = Blocks(550, 350, block_size, block_size2, block_rect)
block3 = Blocks(250, 350, block_size, block_size2, block_rect)
block4 = Blocks(10, 350, block_size, block_size2, block_rect)
block5 = Blocks(340, 310, block_size, block_size2, block_rect)
block6 = Blocks(460, 475, block_size, block_size2, block_rect)

#blocks_sprite.add(block4, block6)#, block2, block3, block1, block5)


for block in blocks_sprite:
	block.rect.x = block.x2
	block.rect.y = block.y2

#NARRATOR ATTRIBUTES
narcolor = ('purple')
narrator = Narrator(600, 200, 100, 50)

#EXIT ATTRIBUTES
#Levels
level = 0 

#Exit Method
door0 = Exit(800, 400, exitlength, exitheight, color)
door1 = Exit(500, 250, exitlength, exitheight, color)
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
	#screen.blit(background, (0, 0))

	#Exit collisions
	exit_collisions = pygame.sprite.spritecollideany(player, exit_sprite) is not (None)

	
	if exit_collisions:
		screen.blit(background, (- 80000, 0))
		
		if pygame.sprite.spritecollide(player, exit_sprite, True):
			#Every door is specific to its level and in resulting, by turning the value to True, every element of
			#the exit_sprite group is deleted from the group after every collision. By doing so,  we just need to
			#add every diffeent door to every specific level using the method .add(). 
			screen.blit(dungeon, (0, 0))
			level = level +1




	if level == 0:
		blocks_sprite = pygame.sprite.Group()
		screen.blit(background, (0, 0))
		for sprite in player_sprite:
			sprite.appear(screen)
		for sprite in blocks_sprite:
			sprite.appear(screen)
		for sprite in exit_sprite:
			sprite.appear(screen)
		narrator.appear(screen)

	elif level == 1:
		#Setting the screen
		screen.fill(bg_color)
		screen.blit(dungeon_screen, (0, 0))

		#Updating manually the sprite groups
		pygame.sprite.Sprite.add(door1, exit_sprite)
		blocks_sprite.add(block4, block6)

		#player.x = playerX #Reset the player's x value
		#player.y = playerY #Reset the player's y value
		#player.moving_right = False
		#player.moving_left = False
		#player.animate()
		#player.update(player.x, player.y) #This does nothing
		
		for sprite in player_sprite:
			sprite.appear(screen)
		for sprite in blocks_sprite:
			sprite.appear(screen)
		for sprite in exit_sprite:
			sprite.appear(screen)

	elif level == 2:
		#Setting the screen
		screen.fill(bg_color)
		screen.blit(dungeon_screen, (0, 0))

		#Updating manually the sprite groups
			#Removing everything from the block group
		blocks_sprite.remove(block4, block6)
			#Adding the elements for this level
		pygame.sprite.Sprite.add(door2, exit_sprite)
		blocks_sprite.add(block1, block3)
		
		for sprite in player_sprite:
			sprite.appear(screen)
		for sprite in blocks_sprite:
			sprite.appear(screen)
		for sprite in exit_sprite:
			sprite.appear(screen)




	elif level > 2: 								#Or we can manually say: if level != 0 and level != 1 and level != 2
		screen.fill(bg_color)
		screen.blit(dungeon_screen, (0, 0))						
		player.x, player.y = 500, 200
		for sprite in player_sprite:
			sprite.appear(screen)



				

	#Text not displaying
	level_text = game_font.render( "Level "f"{level}", True, (0, 0, 0))
	print(level)













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
	
	'''
	for sprite in player_sprite:
		sprite.appear(screen)

	for sprite in blocks_sprite:
		sprite.appear(screen)

	for sprite in exit_sprite:
		sprite.appear(screen)
	'''


	#Updating the window
	pygame.display.flip()
	clock.tick(60)
