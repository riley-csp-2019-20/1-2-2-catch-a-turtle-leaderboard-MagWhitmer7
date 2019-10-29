# a122_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
shape = "circle"
size= .5
colour= "palegreen"
score= 0

font_setup = ("Times New Roman", 20, "italic")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name: ")

#-----initialize turtle-----
neb = trtl.Turtle(shape=shape)
neb.turtlesize(size)
neb.fillcolor(colour)
neb.pencolor(colour)
neb.speed(0)

keeper = trtl.Turtle(shape="circle")
keeper.ht()
keeper.penup()
keeper.goto(-350, 250)
keeper.pendown()
keeper.pencolor("limegreen")
font = ("Times New Roman", 30, "bold")

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(290, -350)
counter.pendown()
counter.pencolor("aquamarine")

#-----game functions--------
def turtle_clicked (x,y):
    move_neb()
    score_keeper()
def move_neb ():
    neb.penup()
    neb.ht()
    new_xpos= random.randint(-400, 400)
    new_ypos= random.randint(-300, 300)
    neb.goto(new_xpos, new_ypos)
    neb.showturtle()     
def score_keeper ():
    global score
    score+=1
    keeper.clear()
    keeper.write (score, font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    game_over()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def game_over ():
    neb.penup()
    neb.goto(500 , 500)
    wn.bgcolor("midnightblue")
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global neb
  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, neb, score)
  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, neb, score)

#-----events----------------
neb.onclick(turtle_clicked)


wn = trtl.Screen()
wn.bgcolor("dimgrey") # customization - changed background colour
wn.ontimer(countdown, counter_interval)
wn.mainloop()