from player import *
from constantes import *
from auxiliar import Auxiliar


class Object():

    def __init__(self, x, y, speed_walk, frame_rate_ms, move_rate_ms, jump_height, p_scale=1, interval_time_jump=100) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/object/food.png", 13, 7, scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/object/food.png", 13, 7, flip=True, scale=p_scale)


        self.contador = 0
        self.frame = 0
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk


        self.animation = self.walk_r

        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x + self.rect.width / 3, y, self.rect.width / 3, self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)

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
        self.tiempo_last_jump = 0  # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    # delta x es move_x
    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if (self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if self.contador <= 20:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.contador += 1
            elif self.contador <= 40:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.contador += 1
            else:
                self.contador = 0



    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
                # print(self.frame)
            else:
                self.frame = 0

    def update(self, delta_ms, plataform_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def draw(self, screen):

        if (DEBUG):
            pygame.draw.rect(screen, color=(255, 0, 0), rect=self.collition_rect)
            pygame.draw.rect(screen, color=(255, 255, 0), rect=self.ground_collition_rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)



    # delta x es move_x
    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if (self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0


    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
                # print(self.frame)
            else:
                self.frame = 0

    def update(self, delta_ms, plataform_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def draw(self, screen):
        DEBUG =True
        if (DEBUG):

            pygame.draw.rect(screen, color=(255, 0, 0), rect=self.collition_rect)
            pygame.draw.rect(screen, color=(255, 255, 0), rect=self.ground_collition_rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

