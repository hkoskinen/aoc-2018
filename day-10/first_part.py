import sys, pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

filename = 'input.txt'

# read the coordinates from the file
coords = []
with open(filename) as file_obj:
  for line in file_obj:
    line = line.strip()
    coords.append({
      'x': int(line[10:16]),
      'y': int(line[18:24]),
      'vx': int(line[36:38]),
      'vy': int(line[40:42])
    })

timer = 0
def move(forward):
  global timer
  if forward:
    timer += 1
    for i in range(0, len(coords)):
      coords[i]['x'] += coords[i]['vx']
      coords[i]['y'] += coords[i]['vy']
  else:
    timer -= 1
    for i in range(0, len(coords)):
      coords[i]['x'] -= coords[i]['vx']
      coords[i]['y'] -= coords[i]['vy']

  print(timer)

pygame.init()
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('The Stars Align')

# To pause the execution just press space, to continue
# press space again. To step backwards press left arrow,
# and to step forward press right arrow.

moving = True
while True:
  surface.fill((250, 250, 250))

  for c in coords:
    pygame.draw.rect(surface, (55, 10, 0), (c['x'], c['y'], 2, 2))

  if moving:
    move(True)

  for event in GAME_EVENTS.get():
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        move(False)
      if event.key == pygame.K_RIGHT:
        move(True)
      if event.key == pygame.K_SPACE:
        if moving:
          moving = False
        else:
          moving = True

    if event.type == GAME_GLOBALS.QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()