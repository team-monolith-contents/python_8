from ipywidgets import Image
from ipycanvas import Canvas
import ipywidgets as widgets
from IPython.display import display, clear_output

import random

from ipywidgets import Image
from ipycanvas import Canvas
import ipywidgets as widgets
from IPython.display import display, clear_output

def make_answer():
    while True:
        answer = random.randint(100,999)
        answer = str(answer)
        if answer[0] != answer[1] and answer[0] != answer[2] and answer[1] != answer[2]:
            return answer
        
def strike_ball(player, answer):
    s = 0
    b = 0
    for j in range(len(player)):
        if player[j] == answer[j]:
            s += 1
        elif player[j] in answer:
            b += 1
    return s, b

def judge(s, b):
    if s == 3:
        return True
    else:
        return False
    
def add_history(history, result, player, s,b):
    history.append(player)
    result.append([s,b])
    return history, result

class Baseball():
    def __init__(self):
        self.__make_answer = make_answer
        self.__strike_ball = strike_ball
        self.__judge = judge
        self.__add_history = add_history
        
        self.__canvas = Canvas(width=1280, height=720)
        self.__canvas.draw_image(Image.from_file("baseball.png"), 0,0)
        
        self.__inning = 0
        self.__player = None
        self.__history = []
        self.__result = []
        self.__flag = 0
        
        self.__play_button = widgets.Button(
            description='PLAY',
            disabled=False,
            button_style='',
            tooltip='PLAY'
        )
        self.__player_answer = widgets.BoundedIntText(
            min=0,
            max=999,
            step=1,
            description='정답 입력:',
            disabled=False
        )
        self.__output = widgets.Output()
        display(self.__play_button, self.__player_answer, self.__canvas, self.__output)
        
        self.__player_answer.observe(self.__on_player_answer_change, names='value')
        self.__play_button.on_click(self.__play)
            
    def __on_player_answer_change(self, change):
        with self.__output:
            self.__player = f"{change['new']:03}"
            if self.__player and self.__check_input(self.__player):
                s,b = self.__strike_ball(self.__player, self.__answer)
                self.__history, self.__result = self.__add_history(self.__history, self.__result, self.__player, s, b)
                if judge(s,b):
                    self.__inning = 10
                    self.__flag = 1
                    self.__show_end()
                else:
                    self.__inning += 1
                    self.__show_play()
                    
            self.__canvas.fill_style = "white"
            self.__canvas.font = "200px serif"
            self.__canvas.fill_text(f"{self.__player}", 200, 420)
            
            if self.__inning == 10:
                self.__show_end()
            
    def __check_input(self, num):
        return num[0] != num[1] and num[0] != num[2] and num[1] != num[2]
    
    def __show_play(self):
        with self.__output:
            self.__canvas.clear()
            self.__canvas.draw_image(Image.from_file("background.png"), 0,0)
            self.__canvas.fill_style = "white"
            self.__canvas.font = "40px serif"
            self.__canvas.fill_text(f"{self.__inning} 번째 이닝({self.__inning}/9)", 110, 75)
            
            for idx, his in enumerate(self.__history):
                self.__canvas.fill_style = "black"
                self.__canvas.font = "40px serif"
                self.__canvas.fill_text(f"{his}", 910, idx*58 + 190)
            
            for idx, res in enumerate(self.__result):
                self.__canvas.fill_style = "black"
                self.__canvas.font = "40px serif"
                self.__canvas.fill_text(f"S:{res[0]}   B:{res[1]}", 1000, idx*58 + 190)
            
    def __show_end(self):
        self.__canvas.clear()
        if self.__flag:
            self.__canvas.draw_image(Image.from_file("end_success.png"), 0,0)
        else:
            self.__canvas.draw_image(Image.from_file("end_fail.png"), 0,0)
    
    def __play(self, button):
        self.__inning = 1
        self.__answer = self.__make_answer()
        self.__player = "000"
        self.__history = []
        self.__result = []
        self.__flag = 0
        self.__player_answer.value = 0
        self.__show_play()
        self.__play_button.description = 'REPLAY'
        self.__play_button.tooltip = 'REPLAY'
        
class Project1():
    def __init__(self, make_answer, strike_ball, judge, add_history):
        self.__make_answer = make_answer
        self.__strike_ball = strike_ball
        self.__judge = judge
        self.__add_history = add_history
        
        self.__canvas = Canvas(width=1280, height=720)
        self.__canvas.draw_image(Image.from_file("baseball.png"), 0,0)
        
        self.__inning = 0
        self.__player = None
        self.__history = []
        self.__result = []
        self.__flag = 0
        
        self.__play_button = widgets.Button(
            description='PLAY',
            disabled=False,
            button_style='',
            tooltip='PLAY'
        )
        self.__player_answer = widgets.BoundedIntText(
            min=0,
            max=999,
            step=1,
            description='정답 입력:',
            disabled=False
        )
        self.__output = widgets.Output()
        display(self.__play_button, self.__player_answer, self.__canvas, self.__output)
        
        self.__player_answer.observe(self.__on_player_answer_change, names='value')
        self.__play_button.on_click(self.__play)
            
    def __on_player_answer_change(self, change):
        with self.__output:
            self.__player = f"{change['new']:03}"
            if self.__player and self.__check_input(self.__player):
                s,b = self.__strike_ball(self.__player, self.__answer)
                self.__history, self.__result = self.__add_history(self.__history, self.__result, self.__player, s, b)
                if judge(s,b):
                    self.__inning = 10
                    self.__flag = 1
                    self.__show_end()
                else:
                    self.__inning += 1
                    self.__show_play()
                    
            self.__canvas.fill_style = "white"
            self.__canvas.font = "200px serif"
            self.__canvas.fill_text(f"{self.__player}", 200, 420)
            
            if self.__inning == 10:
                self.__show_end()
            
    def __check_input(self, num):
        return num[0] != num[1] and num[0] != num[2] and num[1] != num[2]
    
    def __show_play(self):
        with self.__output:
            self.__canvas.clear()
            self.__canvas.draw_image(Image.from_file("background.png"), 0,0)
            self.__canvas.fill_style = "white"
            self.__canvas.font = "40px serif"
            self.__canvas.fill_text(f"{self.__inning} 번째 이닝({self.__inning}/9)", 110, 75)
            
            for idx, his in enumerate(self.__history):
                self.__canvas.fill_style = "black"
                self.__canvas.font = "40px serif"
                self.__canvas.fill_text(f"{his}", 910, idx*58 + 190)
            
            for idx, res in enumerate(self.__result):
                self.__canvas.fill_style = "black"
                self.__canvas.font = "40px serif"
                self.__canvas.fill_text(f"S:{res[0]}   B:{res[1]}", 1000, idx*58 + 190)
            
    def __show_end(self):
        self.__canvas.clear()
        if self.__flag:
            self.__canvas.draw_image(Image.from_file("end_success.png"), 0,0)
        else:
            self.__canvas.draw_image(Image.from_file("end_fail.png"), 0,0)
    
    def __play(self, button):
        self.__inning = 1
        self.__answer = self.__make_answer()
        self.__player = "000"
        self.__history = []
        self.__result = []
        self.__flag = 0
        self.__player_answer.value = 0
        self.__show_play()
        self.__play_button.description = 'REPLAY'
        self.__play_button.tooltip = 'REPLAY'