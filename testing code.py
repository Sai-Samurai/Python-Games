import pygame, sys
from pygame import Rect

#General setup
pygame.init()
clock = pygame.time.Clock()

YELLOW = (255, 255, 0) #Horrific yellow for debugging rectangles
playerX, playerY = (241, 400)
block_size = 50
block_size2 = 50
min_y = 400  #Value according the game's ground level

#Making anything dissapear
transapency = (0, 0, 0, 0)

#Background image
background = pygame.image.load("Final_background.png")
background_width, background_height = background.get_size()

#Blurred background image
blur_background = pygame.image.load("Blur_final_background.png")

#Dungeon image
dungeon = pygame.image.load("Final_dungeon_background.png")
dungeon_width, dungeon_height = dungeon.get_size()

#Screen appearance
screen_width = background_width
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TM Game')
bg_color = pygame.Color('black')

#New screen appearance
#Note: Need some esthetic changes, looks... could be worse
dngn_screen_width = dungeon_width
dngn_screen_height = dungeon_height
dungeon_screen = pygame.Surface((dngn_screen_width, dngn_screen_height))
dungeon_screen.blit(dungeon, (0, 0))

#Game Text Font For Level
game_font = pygame.font.Font("freesansbold.ttf", 25)
other_text = pygame.font.Font("Retro_Gaming.ttf", 35)

#Player image
p_image = pygame.image.load("Final_player.png").convert_alpha()
player_image = pygame.transform.scale(p_image, (p_image.get_width() / 5, p_image.get_height() / 6.5))
player_rect = player_image.get_rect()

#Block image
b_image = pygame.image.load("Brick_texture.png").convert_alpha()
block_image = pygame.transform.smoothscale(b_image, (b_image.get_width() / 3.3, b_image.get_height() / 3.3))
block_rect = block_image.get_rect()

#Door image
d_image = pygame.image.load("door.png").convert_alpha()
door_image = pygame.transform.scale(d_image, (d_image.get_width() / 1.5, d_image.get_height() / 1.5))
door_rect = door_image.get_rect()

#Coin image
c_image = pygame.image.load("coin.png").convert_alpha()
coin_image = pygame.transform.scale(c_image, (c_image.get_width(), c_image.get_height()))
coin_rect = coin_image.get_rect()

###################################################################################################################################

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
		self.facing_right = True

	def appear(self, screen):
		pygame.draw.rect(screen, YELLOW, self)
		if self.facing_right:
			screen.blit(player_image, player_rect)
		else:
			screen.blit(pygame.transform.flip(player_image, True, False), player_rect) #Flpis the player horizontally when moving left

	def move_right(self):
		self.x += speed_x
		self.rect.x = self.x
		self.facing_right = True

	def move_left(self):
		self.x -= speed_x
		self.rect.x = self.x
		self.facing_right = False

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

#Death items, like lava, spikes, ...
class Death_Items(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		#self.d_item = d_item
		self.rect = pygame.Rect(x, y, width, height)

	def appear(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), self.rect)




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
		self.other_text = pygame.font.Font("Retro_Gaming.ttf", 15)
		self.current_dialogue = ""

	def appear(self, screen):
		pygame.draw.rect(screen, narcolor, self.rect)


#Coins
class Coins(pygame.sprite.Sprite):
	def __init__(self, x, y, length, height, image):
		super().__init__()
		self.x = x
		self.y = y
		self.length = length
		self.height = height
		self.rect = pygame.Rect(x, y, length, height)
		self.image = image
		#coin_sprite.add(self)

	def appear(self, screen):
		pygame.draw.rect(screen, YELLOW, self.rect)
		if self.rect.colliderect(player.rect):
			coin_sprite.remove(self)
		screen.blit(coin_image, self.rect)




#Exit
color = (100, 150, 200)
exitlength = 80
exitheight = 113
class Exit(pygame.sprite.Sprite):
	def __init__(self, x3, y3, exitlength, exitheight, exit_image):
		super().__init__()
		self.x3 = x3
		self.y3 = y3
		self.exitlength = exitlength
		self.exitheight = exitheight
		#self.color = color
		self.exit_image = exit_image
		self.rect = pygame.Rect(x3, y3, exitlength, exitheight)
		#exit_sprite.add(self)

	def appear(self, screen):
		pygame.draw.rect(screen, (135, 206, 235), self.rect)
		screen.blit(door_image, self.rect)



###################################################################################################################################

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
player = Player(playerX, playerY, 60, 95, player_rect)
player_sprite = pygame.sprite.Group(player)

#Lives
lives = 3

#Coin score
coin_score = 0




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


#Wrapping text
#Function being able to seprate the text by counting number of words and length they have
def wrap_text(text, font, max_width):
    words = text.split()
    wrapped_lines = []
    current_line = ""

    for word in words:
        if font.size(current_line + word)[0] <= max_width:
            current_line += word + " "
        else:
            wrapped_lines.append(current_line)
            current_line = word + " "

    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines



#NARRATOR ATTRIBUTES

#Attributes
narcolor = ('purple')
narrator = Narrator(100, 100, 170, 70)
#bubble = pygame.Rect(bubbleX, bubbleY, 215, 80)
text_font = pygame.font.Font("Retro_Gaming.ttf", 10)

#Speech and speech bubble
def text0():
	bubbleX, bubbleY = narrator.rect.x + 150, narrator.rect.y - 65
	pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 250, 100))

	text = "Welcome explorer from the wilderness... I see you have stumbled into this world... But rest assured, I am of no harm... I am a friend to you, not a foe... Let me help you and get you back to your world by getting you through this door I have here..."

	wrapped_lines = wrap_text(text, text_font, 240)

	for i, line in enumerate(wrapped_lines):
		screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))


def text1():
	bubbleX, bubbleY = narrator.rect.x + 150, narrator.rect.y - 35
	pygame.draw.rect(screen, 'white', pygame.Rect(bubbleX, bubbleY, 200, 60))

	text = "Hahahaha... You've been trapped!!! I'll let you die here unless you can escape my dungeon!!!"

	wrapped_lines = wrap_text(text, text_font, 180)

	for i, line in enumerate(wrapped_lines):
		screen.blit(text_font.render(line, True, 'black', None), (bubbleX + 10, bubbleY + 10 + i * 10))




#EXIT ATTRIBUTES
#Levels
level = -1

#Exit Method
door0 = Exit(800, 380, exitlength, exitheight, color)
door1 = Exit(400, 250, exitlength, exitheight, color)
door2 = Exit(100, 400, exitlength, exitheight, color)

exit_sprite = pygame.sprite.Group(door0)


#MAIN SCREEN ATTRIBUTES (Introduction)

#It will have: level = -1, blur background, play button (initialize with key pressing)
# Optional: how to play button

#Start button
#outer rectangle
start_outer = pygame.Rect(screen_width / 2 - 125, screen_height / 2  - 50, 250, 100)

#inner rectangle
start_inner = pygame.Rect(screen_width / 2 - 75, screen_height / 2 - 25, 150, 50)

#text
start_text = other_text.render("START", False, (0, 0, 0))
starting_text = start_text.get_rect(center = (screen_width / 2, screen_height / 2))
start_text2 = pygame.font.Font("Retro_Gaming.ttf", 15).render("Press ENTER/RETURN to start the game", False, (0, 0, 0))
starting_text2 = start_text2.get_rect(center = (screen_width / 2, screen_height / 2 + 65))


#LOADING SCREEN ATTRIBUTES

loading_screen_x, loading_screen_y = 0, 0
loading_screen = pygame.Rect(loading_screen_x, loading_screen_y, screen_width, screen_height)
loading_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("Loading...", False, (255, 255, 255))

def loading():
	pygame.draw.rect(screen, (0, 0, 0), loading_screen)
	loading_text_rect = loading_text.get_rect(center = (screen_width / 2, screen_height / 2))
	screen.blit(loading_text, loading_text_rect)
	pygame.display.flip() # We forcefully update the screen in order to display the loading screen
	pygame.time.delay(2500) # 2500 represents 2500 miliseconds --> 2 seconds and a half of displaying the loading screen


#DEATH ITEMS ATTRIBUTES

#Lava
lava = Death_Items(600, 486, 350, 70)
lava_group = pygame.sprite.Group()
lava_contact = 0

#GAME OVER 
over_game = pygame.Rect(0, 0, screen_width, screen_height)
over_game_text = pygame.font.Font("Retro_Gaming.ttf", 45).render("GAME OVER", False, (255, 255, 255))
over_game_text_rect = over_game_text.get_rect(center = (screen_width / 2, screen_height / 2))

def game_over():
	pygame.draw.rect(screen, (0, 0, 0), over_game)
	screen.blit(over_game_text, over_game_text_rect)
	pygame.display.flip()
	pygame.time.delay(3000)
	

#COINS ATTRIBUTES

coin1 = Coins(600, 430, 19, 22, coin_image)
coin_sprite = pygame.sprite.Group()

#Multiply the number of coins and add in the group
#for i in range(0, 8):
#	coin_sprite.add(Coins(300 + i * 100, 430, 19, 22, coin_image))



########################################################## GAME LOOP ##################################################################

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
				player.y = min(player.y, 400)
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

	#COLLISIONS


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


	#Lava collision
	lava_collision = pygame.sprite.spritecollideany(player, lava_group) is not (None)

	if lava_collision:
		if pygame.sprite.spritecollide(player, lava_group, False):
			player.jumping = True

			#Increase lava_contact for every collision
			lava_contact += 1
			#For every 3 contacts, the remainder (%) of the division is == 0
			if lava_contact % 6 == 0:
				lives -= 1


	#Coin collisions
	coin_collision = pygame.sprite.spritecollideany(player, coin_sprite) is not (None)

	if coin_collision:
		if pygame.sprite.spritecollide(player, coin_sprite, True):
			coin_score += 1



	#Main menu (Level -1)
	if level == -1:
		screen.blit(blur_background, (0, 0))

		#Start button
		pygame.draw.rect(screen, (200, 150, 120), start_outer, border_radius = 10) #Can decide on color later
		pygame.draw.rect(screen, 'red', start_inner, border_radius = 10) #Same here for the color
		screen.blit(start_text, starting_text)
		screen.blit(start_text2, starting_text2)


		#for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				loading()
				level = level + 1

		player.x, player.y = 241, 400
		print(level)
		print(coin_score)



	#Level 0
	elif level == 0:
		blocks_sprite = pygame.sprite.Group()
		screen.blit(background, (0, 0))
		for sprite in player_sprite:
			sprite.appear(screen)
		for sprite in blocks_sprite:
			sprite.appear(screen)
		for sprite in exit_sprite:
			sprite.appear(screen)
		
		narrator.appear(screen)
		text0()

		level_text = other_text.render( "Level "f"{level}", True, (0, 0, 0))
		print(level)
		screen.blit(level_text, (750, 20))

		#Switch level back
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_TAB:
				level = level - 1

		print(lives)
		print(coin_score)

		


	#Level 1
	elif level == 1:
		#Setting the screen
		screen.fill(bg_color)
		screen.blit(dungeon_screen, (0, 0))

		#Updating manually the sprite groups
		pygame.sprite.Sprite.add(door1, exit_sprite)
		blocks_sprite.add(block4, block6)
		pygame.sprite.Sprite.add(coin1, coin_sprite)


		for sprite in player_sprite:
			sprite.appear(screen)
		for sprite in blocks_sprite:
			sprite.appear(screen)
		for sprite in exit_sprite:
			sprite.appear(screen)
		for sprite in coin_sprite:
			sprite.appear(screen)

		#Transitioning the narrator and its text
		if narrator.rect.x < 600:
			narrator.rect.x += 5
		else:	
			narrator.rect.x == 600
		narrator.appear(screen)
		text1()

		level_text = other_text.render( "Level "f"{level}", False, (255, 255, 255))
		print(level)
		screen.blit(level_text, (750, 20))

		score_text = other_text.render("Score : "f"{coin_score}", False, (255, 255, 255))
		print(coin_score)
		screen.blit(score_text, (200, 20))

		print(lives)





	#Level 2
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
		lava_group.add(lava)

		
		lava.appear(screen)

		for sprite in player_sprite:
			sprite.appear(screen)
		for sprite in blocks_sprite:
			sprite.appear(screen)
		for sprite in exit_sprite:
			sprite.appear(screen)

		level_text = other_text.render( "Level "f"{level}", False, (255, 255, 255))
		print(level)
		screen.blit(level_text, (750, 20))

		lives_text = other_text.render("Lives : "f"{lives}", False, (255, 255, 255))
		print(lives)
		screen.blit(lives_text, (200, 20))

		#Game over screen displaying if the player lives count turn 0
		if lives == 0:
			game_over()
			player.rect.x = 241
			player.rect.y = 400
			player.rect.x = player.x
			player.rect.y = player.y
			lava_group.remove(lava)
			player.stop_jumping()

		print(coin_score)





	elif level > 2: 								#Or we can manually say: if level != 0 and level != 1 and level != 2
		screen.fill(bg_color)
		screen.blit(dungeon_screen, (0, 0))						
		player.x, player.y = 500, 200
		for sprite in player_sprite:
			sprite.appear(screen)

		level_text = other_text.render( "Level "f"{level}", True, (250, 250, 250))
		print(level)
		screen.blit(level_text, (750, 20))





				














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
	The player only realizes that he is under the ground (y level above 400)
	only after 20 pixels before coming back to the ground.
	'''
	print(player.x, player.y)

	if player.y >= 400:
		player.y = 400
	else:
		print("Player going down!!!")
		print(screen_width, screen_height)



	#Updating the window
	pygame.display.flip()
	clock.tick(60)
