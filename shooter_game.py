#Создай собственный Шутер!
from random import *
from pygame import *
from time import time as timer

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Space shoot')
game = True

FPS = 120
clock = time.Clock()

galaxy = transform.scale(image.load('ioi.jpg'), (700, 500))

mixer.init()
mixer.music.load('megalovania.mp3')
mixer.music.play()
#pygame.mixer.Sound("minecraft.mp3")
fire = mixer.Sound('fire.ogg')
#boom = mixer.Sound('minecraft.mp3')

#eer

amount_kill = 0

life = 3

amount_lose = 0

rel_time = False

num_fire = 0


font.init()
font = font.Font(None, 40)

score_kill = font.render(f'YOU LOST: '+ str(amount_kill), True, (100, 100, 100))
score_lose = font.render(f'YOU KILL: '+ str(amount_lose), True, (100, 100, 100))
#font 2 = font.Font(None, 70)

win = font.render('YOU WIN!', True, (0, 255, 0))
defeat = font.render('YOU LOSE!', True, (255, 0, 0))



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

# ---Класс bandint---
class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y < 635:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
    
    def fire (self):
        #keys = key.get_pressed()
        bulet = Bullet('rte.png', self.rect.x + 20, Hero.rect.y, 20, 20 , 30)
        fire.play()
        bullets.add(bulet)
            
class Player2 (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y < 635:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 635:
            self.rect.y += self.speed
    
    def fire (self):
        #keys = key.get_pressed()
        bulet = Bullet('rte.png', self.rect.x + 20, Hero.rect.y, 20, 20 , 30)
        fire.play()
        bullets.add(bulet)

            
        

#----Создание противников------
class Enemy (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        global amount_lose
        if self.rect.y >= 490:
            self.rect.y = 0
            self.rect.x = randint(10, 690)
            amount_lose+= 1

        
#класс пули
class Bullet (GameSprite):
    
    def update(self):
        global amount_kill
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        
class Asteroid (GameSprite):
    direction = 'left'
    def update(self):
        self.rect.y += self.speed
        global amount_lose
        if self.rect.y >= 490:
            self.rect.y = 0
            self.rect.x = randint(10, 690)
            amount_lose+= 0       
            
        




        



Hero = Player('ytyt.png', 100, 400, 65, 60, 5)
#Her = Player2('ytyt.png', 100, 400, 65, 60, 5)

monsters = sprite.Group()

for i in range(1, 6):
    enemy = Enemy('ufo.png', randint(100, 690), -40, 50, 50, randint(1,4))
    monsters.add(enemy)

bullets = sprite.Group()
asteroids = sprite.Group()

for i in range(1, 6):
    enemy = Asteroid('asteroid.png', randint(100, 690), -30, 50, 50, randint(1,4))
    asteroids.add(enemy)

bullets = sprite.Group()





finish = False



while game:
    
    


    keys = key.get_pressed()
    


    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 100 and rel_time == False:
                    num_fire += 1
                    #fire_sound.play()
                    Hero.fire()

                if num_fire >= 100 and rel_time == False:
                    last_time = timer()
                    rel_time = True


    if finish != True:
        window.blit(galaxy, (0, 0))
        
        #sprite_list = sprite.groupcollide(monsters, bullets, True, True)
        #for sprite in sprite_list:
        #    amount_kill += 1
        #    enemy = Enemy('ufo.png', randint(10, 690), 10, 65, 65, randint(1,4))
        #    monsters.add(enemy)
    


        Hero.reset()
        Hero.update()

        #Her.reset()
        #Her.update()
        
        asteroids.draw(window)
        asteroids.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()

        

        score_kill = font.render(f'YOU KILL: '+ str(amount_kill), True, (100, 100, 100))
        score_lose = font.render(f'YOU LOST: '+ str(amount_lose), True, (100, 100, 100))
        window.blit(score_kill, (0, 30))
        window.blit(score_lose, (0, 50))


        #monsters.reset()
        
        #if sprite.collide_rect(Hero, exited):f
        #    money.play()
        #    window.blit(win, (200,200))
        #if sprite.collide_rect(Hero, enemy) or sprite.collide_rect(Hero, wall_1) or sprite.collide_rect(Hero, wall_2) or sprite.collide_rect(Hero, wall_3) or sprite.collide_rect(Hero, wall_4):
        #    finish = True
        #    kick.play()
        #    window.blit(defeat, (200,200))

        if sprite.groupcollide(monsters, bullets, True, True):
            enemy = Enemy('ufo.png', randint(10, 690), -40, 50, 50, randint(1,4))
            monsters.add(enemy)   
            amount_kill += 1
        
        if sprite.spritecollide(Hero, asteroids, False) or sprite.spritecollide(Hero, monsters, False):
            
            sprite.spritecollide(Hero, asteroids, True)
            sprite.spritecollide(Hero, monsters, True)
            life = life -1
            
        if life == 0 or amount_lose >= 10:
            finish = True
            window.blit(defeat, (300,200))
            

        if amount_lose > 10 or  sprite.spritecollide(Hero, monsters, False):
            finish = True
            window.blit(defeat, (300,200))
        if amount_kill > 100:
            finish = True
            window.blit(win, (300,200))

        if rel_time ==True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font.render('Reloading...', 1, (150, 0,0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False   
        if life == 3:
            life_color = (0,255,0)
        if life == 2:
            life_color = (255,255,0)
        if life == 1:
            life_color = (255,0,0)

        text_life = font.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))
        clock.tick(FPS)
        display.update()

    else: 
        finish = False
        amount_kill = 0 
        amount_lose = 0 
        num_fire = 0
        life = 3
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        for a in asteroids:
            a.kill()

        time.delay(2000)
        for i in range(1, 6):
            enemy = Enemy('ufo.png', randint(100, 690), -40, 50, 50, randint(1,4))
            monsters.add(enemy) 
        for i in range(1, 6):
            enemy = Asteroid('asteroid.png', randint(100, 690), -40, 50, 50, randint(1,4))
            monsters.add(enemy)



    
