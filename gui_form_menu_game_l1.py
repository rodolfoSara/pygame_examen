import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from objetos import Object
from plataforma import Plataform
from background import Background
from bullet import Bullet
from gui_widget import Widget
from auxiliar import Auxiliar


class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        #player
        self.player_1 = Player(x=0, y=500, speed_walk=6, speed_run=12, gravity=14, jump_power=30, frame_rate_ms=100,
                               move_rate_ms=50, jump_height=140, p_scale=1.8, interval_time_jump=300)

        #self.boton1 = Button(master=self, x=0, y=0, w=250, h=50, color_background=C_BLACK, color_border=None, image_background=None, on_click=self.load_nivel, on_click_param="form_menu_B", text="SAVE LEVEL", font="Helvetica", font_size=20, font_color=C_WHITE)

        # --- GUI WIDGET ---
        #self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=253,y=0,w=250,h=40,color_background=C_BLACK,color_border=None,image_background=None,on_click=self.on_click_boton1,on_click_param="form_menu_B",text="Pause",font="Helvetica",font_size=20,font_color=C_WHITE)
        #self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
        self.textScore = Widget(master_form=self,x=507,y=0,w=250,h=40,color_background=C_BLACK, color_border=None,image_background= None,text= f"score {self.player_1.score}" ,font="Helvetica",font_size=20, font_color=C_WHITE)
        self.textLives = Widget(master_form=self, x=759, y=0, w=250, h=40, color_background=C_BLACK, color_border=None, image_background=None, text=f"Lives {self.player_1.lives}", font="Helvetica", font_size=20, font_color=C_WHITE)

        #self.pb_lives = ProgressBar(master=self,x=700,y=0,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton2, self.textScore, self.textLives]



        # --- GAME ELEMNTS ---
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/fondo1.png")


        self.enemy_list = []
        self.enemy_list.append (Enemy(x=100,y=50,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.6,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=1200,y=50,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.6,interval_time_jump=300))

        self.enemy_list.append(Enemy(x=350, y=200, speed_walk=6, speed_run=5, gravity=14, jump_power=30, frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.6, interval_time_jump=300))
        self.enemy_list.append(Enemy(x=1050, y=100, speed_walk=6, speed_run=5, gravity=14, jump_power=30, frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.6, interval_time_jump=300))

        self.enemy_list.append(Enemy(x=620, y=420, speed_walk=6, speed_run=5, gravity=14, jump_power=30, frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.6, interval_time_jump=300))
        self.enemy_list.append(Enemy(x=1300, y=340, speed_walk=6, speed_run=5, gravity=14, jump_power=30, frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.6, interval_time_jump=300))

        #object list
        self.object_list = []
        self.object_list.append(Object(x=10,y=115,speed_walk=6,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.8,interval_time_jump=300))
        self.object_list.append(Object(x=1435, y=510, speed_walk=6, frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.8, interval_time_jump=300))
        self.object_list.append(Object(x=820, y=115, speed_walk=6, frame_rate_ms=150, move_rate_ms=50, jump_height=140, p_scale=0.8, interval_time_jump=300))

        #plataforma
        self.plataform_list = []

        '''
        self.plataform_list.append(Plataform(x=0, y=200, width=200, height=50, type=3))
        self.plataform_list.append(Plataform(x=350, y=200, width=200, height=50, type=3))
        self.plataform_list.append(Plataform(x=750, y=200, width=200, height=50, type=3))
        self.plataform_list.append(Plataform(x=1100, y=200, width=200, height=50, type=3))

        self.plataform_list.append(Plataform(x=260, y=350, width=200, height=50, type=3))
        self.plataform_list.append(Plataform(x=950, y=350, width=200, height=50, type=3))

        self.plataform_list.append(Plataform(x=0, y=450, width=200, height=50, type=3))
        self.plataform_list.append(Plataform(x=650, y=450, width=200, height=50, type=3))

        self.plataform_list.append(Plataform(x=100, y=600, width=400, height=50, type=3))
        self.plataform_list.append(Plataform(x=500, y=600, width=400, height=50, type=3))
        self.plataform_list.append(Plataform(x=1400, y=600, width=250, height=50, type=3))

        self.plataform_list.append(Plataform(x=0, y=750, width=900, height=50, type=3))
        self.plataform_list.append(Plataform(x=900, y=750, width=600, height=50, type=3))
        '''





        self.load_nivel()

    def load_nivel(self, parametro = 1):
        dato_nivel = Auxiliar.load_json("nivel_1.json")

        '''
        enemigos = dato_nivel["enemigos"]
        for enemy in enemigos:
            for _ in range(len(enemigos)):
                self.enemy_list.append(Enemy(x=enemy["x"], y=enemy["y"], speed_walk=enemy["speed_walk"], speed_run=enemy["speed_run"],
                          gravity=enemy["gravity"], jump_power=["jump_power"], frame_rate_ms=enemy["frame_rate_ms"],
                          move_rate_ms=["move_rate_ms"], jump_height=enemy["jump_height"], p_scale=enemy["p_scale"],
                          interval_time_jump=enemy["interval_time_jump"]))
        '''

        plataformas = dato_nivel["plataformas"]
        for plataform in plataformas:
            for _ in range(len(plataformas)):
                self.plataform_list.append(Plataform(x= plataform["x"], y=plataform["y"], width=plataform["width"], height=plataform["height"], type=plataform["type"]))


    #botones
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        #cuando todos estan muertos
        nivel_terminado = False
        for enemy in self.enemy_list:
            if enemy.is_dead == False:
                nivel_terminado = False
                break
            nivel_terminado = True
        if nivel_terminado == True:
            self.active("form_game_L3")


        for object_element in self.object_list:
            object_element.update(delta_ms,self.plataform_list)

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)

        self.player_1.atack_colission(self.enemy_list)
        self.player_1.object_colision(self.object_list)
        self.player_1.enemy_colission(self.enemy_list)
        self.textScore._text = f"score {self.player_1.score}"
        self.textLives._text =f"Lives {self.player_1.lives}"


        #score
        #self.textScore += self.player.score




    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        for object_element in self.object_list:
            object_element.draw(self.surface)

        self.player_1.draw(self.surface)


