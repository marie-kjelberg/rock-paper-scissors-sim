import pygame 
import random
import numpy as np # should use this to speed up things later
images = {
   "rock": "./img/rock.png",
   "paper": "./img/paper.png",
   "scissors": "./img/scissors.png"
}
win_map = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
img_dimensions = (32, 32)
(width, height) = (720, 600)
amounts = 5
spawn_range = 100
speed = 50*10
class Sprite:
    '''
        Types: "rock", "paper", "scissors"

        Make the hitbox a circle

        Should have constant speed + rand angle, angle in radians [-2pi, 2pi]

        Need to make sure it doesn't hit a wall
    '''
    def __init__(self, type, x, y, v, angle):
        self.type = type
        self.x = x
        self.y = y
        self.v = v
        self.angle = angle

        self.image = pygame.image.load(images[type])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update_type(self, new_type):
       self.image = pygame.image.load(images[new_type]) 
       self.type = new_type

    def update_pos(self, dt):
        if self.rect.x <= 0 or self.rect.x + img_dimensions[0] >= width: 
            self.angle = 2*np.pi - self.angle
            self.v = -self.v

        if self.rect.y <= 0 or self.rect.y + img_dimensions[1] >= height:
            self.angle = 2*np.pi - self.angle

        self.rect.x += self.v * np.cos(self.angle) * dt
        self.rect.y += self.v * np.sin(self.angle) * dt
    


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rock paper scissors thing')
all_elements = [] # store all objects with their info

running = True
clock = pygame.time.Clock()

elements = ["rock", "paper", "scissors"]
spawn_areas = [[0,0], [width-100, height-100], [width-100, 0]]
# fiks riktig startangles todo ig
for i, element in enumerate(elements):
    for k in range(amounts):
        spawn_area = spawn_areas[i]
        x = spawn_area[0] + random.uniform(0, 50)
        y = spawn_area[1] + random.uniform(0, 50) 
        all_elements.append(Sprite(element, x, y, speed, random.uniform(-np.radians(-45), np.radians(45))))
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  dt = clock.tick(60) / 1000.0
  screen.fill((0,0,0))
  for i, element in enumerate(all_elements):
     # need to handle collisions here
     for j, element2 in enumerate(all_elements):
        if i == j: continue
        if element.rect.colliderect(element2.rect):
           # see which one blah
           # print(f"element {i} collides with {j}")
           if element.type == element2.type: continue
           if win_map[element.type] == element2.type:  
              # element 1 wins
              element2.update_type(element.type)
           else:
              # element 2 wins
              element.update_type(element2.type)
     element.update_pos(dt)
     screen.blit(element.image, element.rect)
  pygame.display.flip()
  