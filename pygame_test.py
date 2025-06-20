# import pygame module in this program 
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
# set the pygame window name 
pygame.display.set_caption("Jump Game")
# object current co-ordinates
x = 0
y = 0
# dimensions of the object
width = 5
height = 5
# Stores if player is jumping or not
isjump = False
# Force (v) up and mass m.
v = 5
m = 1
# Indicates pygame is running
run = True
# infinite loop
while run:
    win.fill((0, 0, 0))
    # drawing object on screen which is rectangle here 
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()
    if isjump == False:
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            # make isjump equal to True
            isjump = True
    if isjump :
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F =(1 / 2)*m*(v**2)
        # change in the y co-ordinate
        y-= F
        # decreasing velocity while going up and become negative while coming down
        v = v-1
        # object reached its maximum height
        if v<0:
            # negative sign is added to counter negative velocity
            m =-1
        # objected reaches its original state
        if v ==-6:
            # making isjump equal to false 
            isjump = False
            # setting original values to v and m
            v = 5
            m = 1
    # creates time delay of 10ms
    pygame.time.delay(10)
    # it refreshes the window
    pygame.display.update() 
# closes the pygame window    
pygame.quit()