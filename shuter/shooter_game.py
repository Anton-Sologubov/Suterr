#Создай собственный Шутер!
from random import *
from pygame import *
from time import time as timer
live = 3
 
width = 700
height = 500
fire_play = '123.mp3'
window = display.set_mode((width, height))
display.set_caption('Space shoot')
game = True
FPS = 60
clock = time.Clock()
galaxy = transform.scale(image.load('fon.jpeg'), (700, 500))
mixer.init()
mixer.music.load('2cac23a4fb05632.mp3')
mixer.music.play()
boom = mixer.Sound('fire.ogg')
fire = mixer.Sound('fire.ogg')
amount_kill = 0
amount_lose = 0
amount_bullet = 0
rel_time = False
num_fire = 0
a = 0
b = False
font.init()
font = font.Font(None, 30)
score_kill = font.render(f'Вы уничтожили: '+ str(amount_kill), True, (100, 100, 100))
score_lose = font.render(f'Вы упустили: '+ str(amount_lose), True, (100, 100, 100))
score_bullet = font.render(f'Вы выстрелили: '+ str(amount_bullet//4), True, (100, 100, 100))
warning = font.render(f'Осталось патрон: '+ str(20-amount_bullet//4), True, (100, 100, 100))
Heart = font.render(f''+ str(live), True, (0, 255, 0))
#font 2 = font.Font(None, 70)
win = font.render('Вы выиграли!', True, (0, 255, 0))
defeat = font.render('Вы проиграли!', True, (100, 0, 0))
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
# Класс игрок
class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y < 435:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed 
    def fire (self):
        #keys = key.get_pressed()       
        bulet = Bullet('tennis.png', self.rect.x + 20, Hero.rect.y, 20, 20 , 5)
        fire.play()
        bullets.add(bulet)
class Player2 (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y < 435:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed 
    def fire (self):
        #keys = key.get_pressed()       
        bulet = Bullet('tennis.png', self.rect.x + 20, Hero.rect.y, 20, 20 , 5)
        fire.play()
        bullets.add(bulet)

#----Создание противников------
class Enemy (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        global amount_lose
        if self.rect.y >= height:
            self.rect.y = 0
            self.rect.x = randint(10, width-50)
            amount_lose+= 1 
class Asteroid (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= height:
            self.rect.y = 0
            self.rect.x = randint(10, width-50)
class Robot (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= height:
            self.rect.y = 0
            self.rect.x = randint(10, width-50)                 
#класс пули
class Bullet (GameSprite):   
    def update(self):
        global amount_kill
        self.rect.y -= self.speed
        if self.rect.y < 5:
            self.kill()
Hero = Player('tenis_raketka.png', 350, 400, 65, 65, 10)
Hero2 = Player2('tenis_raketka.png', 350, 400, 65, 65, 10)
wall_1 = Wall(0, 0, 0, 0, 380, 700, 0.5)
monsters = sprite.Group()
asteroids = sprite.Group()
robots = sprite.Group()
for i in range(2):
    robot = Robot('pixil-frame-0.png', randint(10, 690), 10, 65, 65, randint(1,4))
    robots.add(robot)
for i in range(5):
    enemy = Enemy('ufo.png', randint(10, 690), 10, 65, 65, randint(1,2))
    monsters.add(enemy)
    asteroid = Asteroid('asteroid.png', randint(10, 690), 10, 65, 65, randint(1,4))
    asteroids.add(asteroid)
bullets = sprite.Group()
finish = False
while game:   
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire % 5 != 0 and rel_time == False or num_fire == 0:
                    num_fire += 1
                    fire.play()
                    Hero.fire()
                if num_fire % 5 == 0 and rel_time == False and num_fire != 0:
                    last_time = timer()
                    rel_time = True
    if finish != True:
        window.blit(galaxy, (0, 0))        
        wall_1.draw_wall()
        robots.draw(window)
        robots.update()
        asteroids.draw(window)
        asteroids.update()
        Hero2.reset()
        Hero2.update()
        Hero.reset()
        Hero.update()        
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font.render('Перезарядка', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire += 1
                rel_time = False
        score_kill = font.render(f'Вы уничтожили: '+ str(amount_kill), True, (100, 100, 100))
        score_lose = font.render(f'Вы упустили: '+ str(amount_lose), True, (100, 100, 100))
        score_bullet = font.render(f'Вы выстрелили: '+ str(num_fire), True, (100, 100, 100))
        warning = font.render(f'Осталось патрон: '+ str(20-num_fire), True, (100, 100, 100))
        Heart = font.render(f''+ str(live), True, (0, 255, 0))
        if live == 2:
            Heart = font.render(f''+ str(live), True, (255, 255, 0))
        elif live == 1:
            Heart = font.render(f''+ str(live), True, (255,0 , 0))
        window.blit(Heart, (400, 50))
        window.blit(warning, (350, 30))
        window.blit(score_bullet, (0, 70))
        window.blit(score_kill, (0, 30))
        window.blit(score_lose, (0, 50))
        if Hero.speed >= 80:
            Hero.speed = 10
        if sprite.spritecollide(wall_1, bullets, False):
            amount_bullet += 1
        if sprite.groupcollide(monsters, bullets, True, True):
            enemy = Enemy('ufo.png', randint(10, 690), 10, 65, 65, randint(1,4))
            monsters.add(enemy)   
            amount_kill += 1
        if sprite.spritecollide(Hero, asteroids, True):
            Hero.speed = Hero.speed // 2
            boom.play()
        if sprite.spritecollide(Hero, robots, True):
            Hero.speed = Hero.speed * 2
        if sprite.groupcollide(asteroids, bullets, b, True):
            a += 1
            if a % 3 == 0:
                b = True
                asteroid = Asteroid('asteroid.png', randint(10, 690), 10, 65, 65, randint(1,4))
                asteroids.add(asteroid)
            else:
                b = False
        if sprite.spritecollide(Hero, monsters, True):
            live -= 1                 
        
        if amount_lose > 4 or num_fire == 20 or live <= 0:
            finish = True
            window.blit(defeat, (width//2,height//2))
        if amount_kill > 10:
            finish = True
            window.blit(win, (width//2,height//2))

        clock.tick(FPS)
        display.update()





    else:
        finish = False
        a = 0
        num_fire = 0
        amount_bullet = 0
        amount_kill = 0
        amount_lose = 0
        live = 3
        for c in asteroids:
            c.kill()
        for t in bullets:
            t.kill()
        for m in monsters:
            m.kill()
        for r in robots:
            r.kill()
        Hero.speed = 10


        time.delay(3000)
        for i in range(5):
            enemy = Enemy('ufo.png', randint(10, 690), 10, 65, 65, randint(1,2))
            monsters.add(enemy)
            asteroid = Asteroid('asteroid.png', randint(10, 690), 10, 65, 65, randint(1,4))
            asteroids.add(asteroid)
        for i in range(2):
            robot = Robot('pixil-frame-0.png', randint(10, 690), 10, 65, 65, randint(1,4))
            robots.add(robot)



    time.delay(50)