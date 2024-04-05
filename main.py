#!/bin/python3
import turtle
from Game import *
import random
board_size = 64
grid =[[None for x in range(0,4)] for y in range (0,4)]
def num_horizontal_mergers_right(y):
  num_hor_mergers_right =0
  for x in range(3):
    neighbor = x+1
    while neighbor<=4:
      if get(x,y) == 0:
        continue
      elif get(x,y)!=0:
        if get(x,y) == get(neighbor,y) and get(neighbor,y)!=0:
          num_hor_mergers_right+=1
          neighbor+=1
        elif get(x,y) != get(neighbor,y):
          continue
      neighbor+=1
  return num_hor_mergers_right
def num_vert_merg_down(x):
  num_vert_merger_down = 0
  neighbor = 0
  for y in range(3):
    neighbor = y+1
    while neighbor <=3:
      if get(x,y) ==0:
        continue
      elif get(x,y)!= 0:
        if get(x,y) == get(x,neighbor) and get(x,neighbor)!= 0:
          num_vert_merger_down +=1
          neighbor+=1
        elif get(x,y) != get(x,neighbor):
          continue
      neighbor+=1
  return num_vert_merger_down

   
def total_vertical_mergers(): 
  go_up = num_vert_merg_down(1)+num_vert_merg_down(2)+num_vert_merg_down(3)+ num_vert_merg_down(4)
  return go_up
def total_horizontal_mergers():
  go_right = num_horizontal_mergers_right(1)+num_horizontal_mergers_right(2)+num_horizontal_mergers_right(3)+num_horizontal_mergers_right(4)
  return go_right

        
  




    
while can_go_up()==True or can_go_down() ==True or can_go_right() == True or can_go_left() == True:
  
  
  right()
  down()
  left()
  up()
total_horizontal_mergers() 
  
total_vertical_mergers()
