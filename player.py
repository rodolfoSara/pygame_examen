import pygame
from constantes import *
from auxiliar import Auxiliar
class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        """
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        """

        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight/01_idle/idle_{0}.png",1,8,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight/01_idle/idle_{0}.png",1,8,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight/03_jump_up/jump_up_{0}.png",1,3,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight/03_jump_up/jump_up_{0}.png",1,3,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight/02_run/run_{0}.png",1,8,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight/02_run/run_{0}.png",1,8,flip=True,scale=p_scale)
        #self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight/05_1_atk/1_atk_{0}.png",1,11,flip=False,scale=p_scale,repeat_frame=2)[::4]
        #self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight/05_1_atk/1_atk_{0}.png",1,11,flip=True,scale=p_scale,repeat_frame=2)[::4]
        #corregir
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight/05_1_atk/idle_{0}.png",1,11,flip=False,scale=p_scale,repeat_frame=2)[::4]
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight/05_1_atk/idle_{0}.png",1,11,flip=True,scale=p_scale,repeat_frame=2)[::4]

        self.frame = 0
        self.lives = 100
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.collition_rect = pygame.Rect(x + (self.rect.width/2.1),y + (self.rect.height / 1.5) ,self.rect.width/13,self.rect.height/4)
        self.collition_rect = pygame.Rect(x + self.rect.width/2.2, y + (self.rect.height / 1.5), self.rect.width/10, self.rect.height/4)
        self.collition_attack_rect_r = pygame.Rect(self.rect.x + (self.rect.width/1.8),self.rect.y + (self.rect.height / 1.4) ,self.rect.width/2.5,self.rect.height/2.5)
        self.collition_attack_rect_l = pygame.Rect( self.rect.x - (self.rect.width/20),self.rect.y + (self.rect.height / 1.4) ,self.rect.width/3.5,self.rect.height/2.5)
        #self.collition_attack_rect_l = pygame.Rect(self.rect.x - (self.rect.width/1.8),self.rect.y + (self.rect.height / 1.4) ,self.rect.width/6,self.rect.height/5)
        self.attacking = False


        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l



    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def receive_shoot(self):
        self.lives -= 1

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l
            self.attacking = True

    # COLLISION
    #CHECK IF PLAYER CLISSION with enemy when attack
    def atack_colission(self, enemy_list):
        for enemy in enemy_list:
            if (self.collition_attack_rect_r.colliderect(enemy.rect) or self.collition_attack_rect_l.colliderect(enemy.rect)) and self.attacking == True:
                enemy.lives -= 1
                self.score += 1


    def enemy_colission(self, enemy_list):
        for enemy in enemy_list:
            if self.collition_rect.colliderect(enemy.rect) and enemy.is_dead == False:
                self.lives -=1



    def object_colision(self, object_list):
        for object in object_list:
            if self.collition_rect.colliderect(object.rect):
                self.score += 10
                object_list.remove(object)
                del object




    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x * 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x * 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            self.attacking = False

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.collition_attack_rect_r.x += delta_x
        self.collition_attack_rect_l.x += delta_x


    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.collition_attack_rect_r.y += delta_y
        self.collition_attack_rect_l.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump):
                    self.jump(False)
                self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno                 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 

            else:
                self.frame = 0
 
    def update(self,delta_ms,plataform_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        DEBUG = True
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            pygame.draw.rect(screen, color=(120, 240, 0), rect=self.collition_attack_rect_r)
            pygame.draw.rect(screen, color=(255, 240, 255), rect=self.collition_attack_rect_l)


        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms

        #if attack is false:
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido



        if(not keys[pygame.K_a]):
            self.shoot(False)



        if(not keys[pygame.K_a]):
            self.knife(False)

        """
        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.shoot()
        """


        if keys[pygame.K_a]:
            self.knife(True)


