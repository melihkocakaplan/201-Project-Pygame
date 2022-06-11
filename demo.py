import pygame
import random
import time
import numpy 

pygame.init()
class Music():
    def __init__(self, music = '') -> None:
        try:
            self.pop = pygame.mixer.Sound(music)
        except:
            self.pop = music
        try:
            self.music = pygame.mixer.music.load(music)
        except:
            self.music = music
        
    def create_music(self):
        a = Music("music.ogg")
        return a

    def play_game_music(self):
        music = Music().create_music().music
        pygame.mixer.music.play(-1)

    def create_bullet_music(self):
        a = Music("pop.ogg")
        return a

    def play_bullet_music(self):
        Music().create_bullet_music().pop.play()

class User():
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.velx = 15
        self.vely = 15
        self.bullets = []

    def create_user(self):
        a = User(self.x, self.y, self.image)
        return a

    def change_user_coordinate(self,a):
        if a == 0 and self.y >= 0:
            self.y -= self.vely
            if self.y < 0:
                self.y = 0

        elif a == 1 and self.y <= 450:
            self.y += self.vely
            if self.y > 450:
                self.y = 450

    def coordinates_of_user(self):
        return self.x, self.y
    
    def shoot(self):
        newbullet = Bullet(self.x, self.y + 30)
        self.bullets.append(newbullet)
class Image():
    def __init__(self, image= "") -> None:
        try:
            self.image = pygame.image.load(image)
        except:
            self.image = image

    def create_start_page_image(self):
        a = Image('start_page_image.png')
        return a

    def create_ball_image(self):
        if self.image == 0:
            b = Image('regular_ball_image.png')
            return b
        elif self.image == 1:
            b = Image('level_boss_image.png')
            return b
        elif self.image == 2:
            b = Image('ball_bonus_image.png')
            return b
        elif self.image == 3:
            b = Image('bullet_bonus_image.png')
            return b
        elif self.image == 4:
            b = Image('bigger_ball_image.png')
            return b

    def create_game_over_image(self):
        a = Image('game_over_image.png')
        return a
        
    def create_level_image(self):
        if self.image == 0:
            b = Image('level_one.png')
            return b
        elif self.image == 1:
            b = Image('level_two.png')
            return b
        elif self.image == 2:
            b = Image('level_three.png')
            return b
        elif self.image == 3:
            b = Image('level_four.png')
            return b
        elif self.image == 4:
            b = Image('level_five.png')
            return b

    def create_bullet_image(self):
        a = Image('bullet.png')
        return a

    def create_countdown_image(self):
        if self.image == 3:
            b = Image('countdown_start.png')
            return b
        elif self.image == 2:
            b = Image('countdown_one.png')
            return b
        elif self.image == 1:
            b = Image('countdown_two.png')
            return b
        elif self.image == 0:
            b = Image('countdown_three.png')
            return b

    def create_background_choose_image(self):
        a = Image('choose_background_image.png')
        return a

    def create_user_choose_image(self): 
        a = Image('choose_user_image.png')
        return a 

    def create_background_image(self):
        if self.image == 1:
            b = Image('fall.png')
            return b
        elif self.image == 3:
            b = Image('spring.png')
            return b
        elif self.image == 0:
            b = Image('summer.png')
            return b
        elif self.image == 2:
            b = Image('winter.png')
            return b

    def create_user_image(self):
        if self.image == 2:
            b = Image('airplane.png')
            return b
        elif self.image == 1:
            b = Image('airship.png')
            return b
        elif self.image == 0:
            b = Image('helicopter.png')
            return b

    def create_congrats_image(self):
        a = Image('congrats.png')
        return a
class Menu():
    def __init__(self,a = "") -> None:
        self.a = a

    def get_image(self): 
        if self.a == 0: 
            return Image().create_background_choose_image().image
        elif self.a == 1:
            return Image().create_user_choose_image().image
        elif self.a == 2:
            return Image().create_start_page_image().image 

class Bullet():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        #self.image = image
        self.velx = 15
        self.direction = (1,0)

    def create_bullet(self):
        b = Bullet(self.x,self.y)
        return b 
    
    def draw_bullet(self):
        Game().window.blit(Image().create_bullet_image().image, (self.x, self.y))

    def change_bullet_coordinate(self):
        return self.x + 15
    def change_three_direction_up(self):
        return self.x + 15, self.y - 3
    def change_three_direction_down(self):
        return self.x + 15, self.y + 3
         

class Ball():
    def __init__(self, x, y, image) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.velx = 10
        self.direction = (-1,0)

    def create_ball(self):
        b = Ball(self.x,self.y,self.image)
        return b 

    def change_ball_coordinate(self):
        return self.x - self.velx

class Level_Boss(Ball):
    def __init__(self,x,y,image) -> None:
        super().__init__(x,y,image)
        self.to_be_killed = 0
        self.velx = 10
        self.direction = (-1,0)

    def create_ball(self):
        b = Level_Boss(self.x,self.y,self.image)
        return b 

    def change_image_coordinate(self):
        self.x -= self.velx

class Bonus(Ball):
    def __init__(self,x,y,image) -> None:
        super().__init__(x,y,image)
        self.random = random.randint(0,1)
        self.velx = 10
        self.direction = (-1,0)

    def create_ball(self):
        b = Level_Boss(self.x,self.y,self.image)
        return b 

    def change_image_coordinate(self):
        return self.x - 15

class BallBonus(Bonus):
    def __init__(self,x,y,image) -> None:
        super().__init__(x,y,image) 
    
    def slower_ball(self, i):
        i.velx = 5  

    def bigger_ball(self, a):
        a.image = pygame.transform.scale(a.image, (100,100))

class BulletBonus(Bonus):
    def __init__(self,x,y,image) -> None:
        super().__init__(x,y,image)

    def three_bullets(self,a):
        bullet1 = Bullet(a.x,a.y)
        bullet3 = Bullet(a.x,a.y)
        return bullet1, bullet3
class Game():
    def __init__(self):
        self.choose_background_image_dict = {0:[175,525,100,325], 1:[575,925,350,575], 2:[175,525,100,325], 3:[575,925,350,575]}
        self.choose_user_image_dict  = {0:[1,2,3,4], 1:[1,2,3,4], 2:[1,2,3,4]}
        self.win_height = 600
        self.win_width = 1100
        self.window = pygame.display.set_mode((1100, 600))
        self.mybg = int
        self.myuser = int
        self.user = User(0,0,0)
        self.numberofkills = 0 
        self.balls = [] 
        self.clock = pygame.time.Clock()
        self.score = 0
        self.pause = 0
        self.newgame = 1
        self.bonus_exploited = 0
        self.three_bullets = 0
        self.bulletss = 0
    def get_start_page_image(self):
        return Menu(2).get_image()

    def draw_start_page_image(self):
        self.window.blit(self.get_start_page_image(), (0,0))


    def get_background_choose_image(self):
        return Menu(0).get_image()

    def draw_background_choose_image(self):
        self.window.blit(self.get_background_choose_image(), (0,0))
        

    def start_decision_screen(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.draw_background_choose_image()
                        pygame.display.update()
                        running = False

    def check_mouse(self):
        pass

    def get_user_choose_image(self):
        return Menu(1).get_image()

    def draw_user_choose_image(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.mybg = 0
                        self.window.blit(self.get_user_choose_image(), (0,0))
                    elif event.key == pygame.K_b:
                        self.mybg = 1
                        self.window.blit(self.get_user_choose_image(), (0,0))
                    elif event.key == pygame.K_c:
                        self.mybg = 2
                        self.window.blit(self.get_user_choose_image(), (0,0))
                    elif event.key == pygame.K_d:
                        self.mybg = 3
                        self.window.blit(self.get_user_choose_image(), (0,0))
                    pygame.display.update()
                    running = False
    
    def get_countdown_image(self, a):
        return Image(a).create_countdown_image().image

    def draw_countdown_image(self, a):
        if a == 0:
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.myuser = 0
                            self.window.blit(self.get_countdown_image(a), (0,0))
                        elif event.key == pygame.K_b:
                            self.myuser = 1
                            self.window.blit(self.get_countdown_image(a), (0,0))
                        elif event.key == pygame.K_c:
                            self.myuser = 2
                            self.window.blit(self.get_countdown_image(a), (0,0))
                        
                        pygame.display.update()
                        running = False
        else:
            self.window.blit(self.get_countdown_image(a), (0,0))
            pygame.display.update()
        

    def get_background(self, a):
        return Image(a).create_background_image().image

    def draw_background(self, a):
        self.window.blit(self.get_background(a), (0,0))

    def get_user(self, a):
        c = Image(a).create_user_image().image
        b = User(0, 250, c).create_user()
        self.user = b

    def draw_user(self, a):
        self.get_user(a)
        self.window.blit(self.user.image, (self.user.x, self.user.y))
        pygame.display.update()

    def get_level_image(self, a):
        return Image(a).create_level_image().image

    def draw_level_image(self, a):
        self.window.blit(self.get_level_image(a), (0,0))
        pygame.display.update()
        time.sleep(1)

    
    def move_user_up(self):
        self.user.change_user_coordinate(0)

    def move_user_down(self):
        self.user.change_user_coordinate(1)

    def ball_type(self):
        if self.numberofkills == 10:
            b = 1
        else:
            b = random.randint(0,1)*2
        return b

    def get_ball_instance(self, a):
        x = 1100
        y = random.randint(50,450)
        b = Image(a).create_ball_image().image
        if a == 0:
            c = Ball(x,y,b).create_ball()
            self.balls.append(c)
        elif a == 1:
            c = Level_Boss(x,y,b).create_ball()
            self.balls.append(c)
        elif a == 2:
            c = BallBonus(x,y,b).create_ball()
            self.balls.append(c)
            self.bonus_exploited = 3
        elif a == 3:
            c = BulletBonus(x,y,b).create_ball()
            self.balls.append(c)
            self.bonus_exploited = 2
        elif a == 4:
            c = BallBonus(x,y,b).create_ball()
            self.balls.append(c)
            self.bonus_exploited = 1

    def get_bullet(self):
        b = Image().create_bullet_image().image
        c = Bullet(self.user.x,self.user.y).create_bullet()
        self.bullets.append(c)
        return c

    def collision(self):
        for i in self.user.bullets:
            for j in self.balls:
                if j.x <= i.x + 40 <= j.x + j.image.get_width()  and j.y <= i.y + 20 <= j.y + j.image.get_height():
                    self.balls.remove(j)
                    self.user.bullets.remove(i)
                    self.score += 1
    
    def level_change(self):
        self.draw_game()
        if self.score == 5:
            self.draw_level_image(1)
            self.score += 1
            self.draw_game()
        elif self.score == 11:
            self.draw_level_image(2)
            self.score += 1
            self.draw_game()
        elif self.score == 17:
            self.pause = 2

    def congrats(self):
        self.window.blit(Image().create_congrats_image().image,(0,0))
        pygame.display.update()
        
    def check_game_over(self):
        for i in self.balls:
            if i.x <= 0:
                self.window.blit(Image().create_game_over_image().image,(0,0))
                pygame.display.update()
                self.pause = 1 

    def draw_game(self):
        self.window.fill((0, 0, 0)) 
        self.draw_background(self.mybg) 
        self.window.blit(self.user.image,(self.user.x,self.user.y))
        if self.three_bullets == 1 and self.bulletss == 1:
            self.window.blit(Image().create_bullet_image().image, (self.user.bullets[-1].x, self.user.bullets[-1].y))
            self.user.bullets[-2].x, self.user.bullets[-2].y = self.user.bullets[-2].change_three_direction_up()
            self.window.blit(Image().create_bullet_image().image, (self.user.bullets[-2].x, self.user.bullets[-2].y))
            self.user.bullets[-3].x, self.user.bullets[-3].y = self.user.bullets[-3].change_three_direction_down()
            self.window.blit(Image().create_bullet_image().image, (self.user.bullets[-3].x, self.user.bullets[-3].y))

            try:
                for i in self.user.bullets[:-3]:
                    self.window.blit(Image().create_bullet_image().image, (i.x, i.y))
            except:
                pass
            self.three_bullets = 0
        else:
            for bull in self.user.bullets: 
                self.window.blit(Image().create_bullet_image().image, (bull.x, bull.y))
        

        if len(self.balls) == 0 and self.pause == 0:
            if self.score == 4 or self.score == 10 or self.score == 16: 
                self.bonus_exploited = 0
                rand = 1
            else:
                rand = numpy.random.choice([0,2,3,4], p=[0.7,0.1,0.1,0.1])
            if self.bonus_exploited == 0:
                self.get_ball_instance(rand)
            elif self.bonus_exploited == 1:
                self.get_ball_instance(0)
                for i in self.balls:
                    BallBonus(0,0,Image(0).create_ball_image().image).bigger_ball(i)
                self.bonus_exploited = 0
            elif self.bonus_exploited == 2:
                self.get_ball_instance(0)
                self.three_bullets = 1
                
            elif self.bonus_exploited == 3:
                self.get_ball_instance(0)
                for i in self.balls:
                    BallBonus(0,0,Image(0).create_ball_image().image).slower_ball(i)
                self.bonus_exploited = 0
            if 5 <= self.score < 11:
                for i in self.balls:
                    i.velx = 15
            if 11 <= self.score < 17:
                for i in self.balls:
                    i.velx = 20
            
        
        for bal in self.balls:
            self.window.blit(bal.image,(bal.x,bal.y)) 
        
        pygame.time.delay(30)
        pygame.display.update()

    def total(self):
        self.window.fill((0, 0, 0))
        self.draw_start_page_image()
        pygame.display.flip()
        Music().play_game_music()
        self.start_decision_screen()
        self.draw_user_choose_image()
        for i in range(4):
            self.draw_countdown_image(i)
            time.sleep(1)          
        pygame.mixer.music.stop()

        self.draw_background(self.mybg)
        self.draw_level_image(0)
        self.draw_background(self.mybg)
        self.draw_user(self.myuser)

        run = True
        while run:
            """
            self.draw_background(self.mybg)
            self.window.blit(self.user.image,(self.user.x,self.user.y))
            for bul in self.bullets:
                bul.change_bullet_coordinate()
                self.blit_bullet()
            pygame.display.update()    
            pygame.time.delay(30)
            # Quit Game"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        game.move_user_down()

                    if event.key == pygame.K_UP: 
                        game.move_user_up()
                    #if event.key == pygame.K_r:
                        #pygame.time.wait()
                    if event.key == pygame.K_r:
                        self.newgame = 0
                    if event.key == pygame.K_n:
                        self.newgame = 2
                        

                    if event.key == pygame.K_SPACE:
                        if self.three_bullets == 1:
                            bullet1, bullet3 = BulletBonus(self.user.x+100, self.user.y+30, Image().create_bullet_image().image).three_bullets(self.user)
                            self.user.bullets.append(bullet1)
                            self.user.bullets.append(bullet3)
                            self.bonus_exploited = 0
                            self.bulletss = 1
                        newbullet = Bullet(self.user.x + 100, self.user.y + 30)
                        self.user.bullets.append(newbullet)
                        Music().play_bullet_music()
                        
                        
                        
            for bullet in self.user.bullets:
                bullet.x = bullet.change_bullet_coordinate()
            for bal in self.balls:
                bal.x = bal.change_ball_coordinate()
            self.collision()
            if self.pause != 2:
                self.check_game_over()
            if self.pause == 0:
                self.level_change()
            if self.pause == 2:
                self.congrats()
            if self.newgame == 0:
                self.draw_background(self.mybg)
                self.draw_level_image(0)
                self.draw_background(self.mybg)
                self.draw_user(self.myuser)
                self.balls = []
                self.pause = 0
                self.score = 0
                self.newgame = 1
            if self.newgame == 2:
                self.window.fill((0, 0, 0))
                self.draw_start_page_image()
                pygame.display.flip()
                Music().play_game_music()
                self.start_decision_screen()
                self.draw_user_choose_image()
                for i in range(4):
                    self.draw_countdown_image(i)
                    time.sleep(1)          
                pygame.mixer.music.stop()

                self.draw_background(self.mybg)
                self.draw_level_image(0)
                self.draw_background(self.mybg)
                self.draw_user(self.myuser)
                self.balls = []
                self.pause = 0
                self.score = 0
                self.newgame = 1
                



game = Game()
game.total()