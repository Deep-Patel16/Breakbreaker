from tkinter import *
import time 



global score
score= 0
global is_paused
is_paused = False
global  cheat
cheat = False


def change_to_main_window(): #  when button pressed to change from game window to menu window(main window)
    canvas_window.pack(fill='both',expand=1)
    canvas_game.forget()
def change_to_continue_window(): #  when button pressed to change from menu window(main window) to continue_window
    canvas_continue_window.pack(fill='both',expand=1)
    canvas_window.forget()
def change_to_new_player_window(): # when button pressed to change from main window (main window) to new_player window
    canvas_new_player.pack(fill='both',expand=1)
    canvas_window.forget()
def button_start_game1(): # when button pressed to change from new_player window to game window
    canvas_game.pack(fill='both',expand=1)
    canvas_new_player.forget()
def save_file(): # function which saves the name of the player in the text file which he/she enters in the new player window
    new_player_name = entry1.get()
    new_player_nickname = entry2.get()
    file = open("brickbreaker.txt","a")
    file.write(new_player_name+',')
    file.write(new_player_nickname+',')
    file.write('0')
    file.write('\n')
    file.close()
    name_of_players()
    drop_menu = OptionMenu(canvas_continue_window,clicked,*names_list,command=display_selected)
    canvas_continue_window.create_window(640,290,window=drop_menu)
    drop_menu.update()
def name_of_players(): # this function reads the name of player from the text file and save it in the list containing player names
    global names_list
    file2 = open('brickbreaker.txt','r').readlines()
    remove_line=[]
    names_list=[]
    for line2 in file2:
        whatweneed1 = line2.replace('\n','')
        remove_line.append(whatweneed1)
    for j in remove_line:
        c = j.split(',')
        names_list.append(c[0])

def save_score(*args): # we save the updated score of the player in the text file
    global name,score
    name= clicked_selected
    score = ball.score
    remove_line = []
    file2 = open('brickbreaker.txt','r').readlines()
    file3 = open('brickbreaker.txt','w')
    for line in file2:
        whatweneed = line.replace('\n','')
        remove_line.append(whatweneed)
    for each in remove_line:
        a=each.split(',')
        if a[0] == name:
            a[2]=int(a[2])
            a[2]+=ball.score
        file3.write(a[0]+","+a[1]+','+str(a[2]))
        file3.write('\n')
        
def leaderboard_sort(): # this function sorts the score of the players in descending order after reading it from the text file saves the updated order in text file
    global remove_lines1
    file = open('brickbreaker.txt','r').readlines()
    remove_lines1 = []
    for line in file:
        whatweneed1 = line.replace('\n','')
        whatweneed1 = whatweneed1.split(',')
        remove_lines1.append(whatweneed1)
    for k in remove_lines1:
        if k==['']:
            remove_lines1.remove(k)
    for i in remove_lines1:
        i[2]=int(i[2])
    remove_lines1.sort(key = lambda x: x[2],reverse=True)
def button_start_game2(): # this function is callback function which starts the game window and closes the continue window
    # global color_choosen2,color_choosen1
    canvas_game.pack(fill='both',expand=1)
    canvas_continue_window.forget()
def button_to_menu(): # this function is callback function which starts the main window (menu window) and closes the game window
    canvas_window.pack(fill='both',expand=1)
    canvas_game.forget()


def button_to_menu4(): # this function is callback function which starts the main window and closes the game window
    canvas_window.pack(fill='both',expand=1)
    canvas_new_player.forget()
def button_to_menu5(): # this function is callback function which starts the main window(menu window) and closes the continue window
    canvas_window.pack(fill='both',expand=1)
    canvas_continue_window.forget()


def button_to_leader1(*args): # this function is callback function which starts the leaderboard window and closes the main window (menu window)
    canvas_leaderboard.pack(fill='both',expand=1)
    canvas_window.forget()

def menu_screen_leader(*args): # this function is callback function which starts the main window and closes the leaderboard window
    canvas_window.pack(fill='both',expand=1)
    canvas_leaderboard.forget()
def cheatkey(*args):
    global cheat
    if cheat == False:
        cheat = True
    else:
        cheat = False
def bosskey(*args): # this function save scores, updates the leaderboard, opens boss window and closes the game window
    save_score()
    leaderboard_sort()
    canvas_boss_window.pack(fill='both',expand=1)
    canvas_game.forget()
def menu_button9(*args): # this function is callback function which starts the main window (menu window) and closes the game  window
    canvas_window.pack(fill='both',expand=1)
    canvas_game.forget()

window = Tk() 
window.title("Pong Game")
canvas_window = Canvas(window,width=1280,height=720)  # creates canvas_window window
canvas_new_player = Canvas(window,width=1280,height=720) # creates canvas_new_player window
canvas_boss_window = Canvas(window,width=1280,height=720)# creates canvas_boss_key window
canvas_window.pack(expand=True)
canvas_continue_window = Canvas(window,width=1280,height=720)  # creates canvas_continue window
canvas_leaderboard = Canvas(window,width=1280,height=720) # creates canvas window for leaderboard
canvas_game = Canvas(window,width=1280,height=720,bg='black') # creates window for game with black background

bg = PhotoImage(file='main.png') 
bk = PhotoImage(file='boss.png')
canvas_window.create_image(0,0,image=bg,anchor='nw') # inserts background image in the canvas_window 
canvas_continue_window.create_image(0,0,image=bg,anchor='nw') # inserts background image in the canvas_continue_window
canvas_new_player.create_image(0,0,image=bg,anchor='nw') # inserts background image in the canvas_new_player
canvas_leaderboard.create_image(0,0,image=bg,anchor='nw') # inserts background image in the leaderboard window
canvas_boss_window.create_image(0,0,image=bk,anchor='nw')

leaderboard_sort() # this is function callback for sorting leaderboard
#creates text to display leaderboard in the leaderboard window
canvas_leaderboard.create_text(640,110,text="Name - NickName - Score",fill='#F55919',font=('Helvatical bold',35,'italic')) 
canvas_leaderboard.create_text(640,170,text=remove_lines1[0],fill='#F55919',font=('Helvatical bold',35,'italic'))
canvas_leaderboard.create_text(640,230,text=remove_lines1[1],fill='#F55919',font=('Helvatical bold',35,'italic'))
canvas_leaderboard.create_text(640,290,text=remove_lines1[2],fill='#F55919',font=('Helvatical bold',35,'italic'))
canvas_leaderboard.create_text(640,350,text=remove_lines1[3],fill='#F55919',font=('Helvatical bold',35,'italic'))
canvas_leaderboard.create_text(640,410,text=remove_lines1[4],fill='#F55919',font=('Helvatical bold',35,'italic'))


canvas_window.create_text(640,50,text="Pong Game",fill='#F55919',font=('Helvatical bold',40,'italic')) # add text in menu window (canvas_window)
canvas_new_player.create_text(400,260,text='Name',fill='#F55919',font=('Helvatical bold',20,'italic')) # add text in the new_player window
canvas_new_player.create_text(400,300,text='Nickname',fill='#F55919',font=('Helvatical bold',20,'italic')) # add text in the new_player window
canvas_leaderboard.create_text(640,50,text='Leader Board (Top 5 Player)',fill='#F55919',font=('Helvatical bold',40,'italic'))

button1 = Button(text='Continue Game',command=change_to_continue_window,height=1,width=12) # creates button in the menu window (main window)
button1_window = canvas_window.create_window(640,330,window=button1)
button1.update()

name_of_players()
clicked = StringVar()
clicked.set("Select your Name")
def display_selected(choice):
    global clicked_selected
    clicked_selected = ""
    choice = clicked.get()
    if choice !="Select your name":
        clicked_selected=choice
    else:
        clicked_selected = entry1_text.get()

#drop down menu which contains names of past players who played the game 
clicked1 = IntVar() 
clicked1.set("Select the name")
drop_menu = OptionMenu(canvas_continue_window,clicked,*names_list,command=display_selected)
canvas_continue_window.create_window(640,290,window=drop_menu)
drop_menu.update()

# creates button in the new_player_window
button2 = Button(text='New Player',command=change_to_new_player_window,height=1,width=12)
button2_window = canvas_window.create_window(640,370,window=button2)
button2.update()

# entry widget in new_player window where player enter his name
entry1 = Entry(canvas_new_player) 
canvas_new_player.create_window(640, 250, window=entry1)
entry1.update()
entry1_text = entry1.get()

#entry widget in new_player window wehere player enter his nickname
entry2 = Entry(canvas_new_player) 
canvas_new_player.create_window(640, 300, window=entry2)
entry2.update()
entry2_text = entry2.get()

# creates save button in the new_player window 
button_start_game = Button(text='Save',command=save_file,height=1,width=12)
buttonstart_window=canvas_new_player.create_window(640,360,window=button_start_game)
button_start_game.update()

# creates start button in the continue_window
button_start_game2 = Button(text='Start Game',command=button_start_game2,height=1,width=12)
buttonstart1_window = canvas_continue_window.create_window(640,330,window=button_start_game2)
# button_to_menu = Button(text='Back to Menu',command=button_to_menu,height=1,width=12)
# buttontomenu1_window = canvas_game.create_window(640,580,window = button_to_menu)

# creates menu button in the new_player_window
button_to_menu4 = Button(text='Menu',command=button_to_menu4,height=1,width=12)
buttontomenu4_window = canvas_new_player.create_window(640,410,window = button_to_menu4)
button_to_menu4.update()

# creates menu button continue_window
button_to_menu5 = Button(text="Menu",command=button_to_menu5,height=1,width=12)
buttontomenu5_window = canvas_continue_window.create_window(640,370,window = button_to_menu5)
button_to_menu5.update()

# creates leadboard button on the canvas_window
button_to_leader = Button(text='LeaderBoard',command=button_to_leader1,height = 1, width =12)
buttontoleader = canvas_window.create_window(640,410,window=button_to_leader)
button_to_leader.update()

# creates the menu in canvas_leaderboard window
button8 = Button(text='Menu',command=menu_screen_leader,height=1,width=12)
button8_window = canvas_leaderboard.create_window(640,530,window=button8)
button8.update()

global paused
paused = False
def button_to_pause(*args): # function used to implement pause function
    global paused
    paused = True
def button_to_unpause(*args): # function used to implement unpause function
    global paused
    paused = False

# class containing all properties of the ball 
class Ball:
    def __init__(self, canvas, color, size, paddle):
        
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(5, 5, size, size, fill='red')
        self.canvas.move(self.id, 245, 100)
        self.xspeed = 4 # x component of the ball speed
        self.yspeed = 4 # y component of the ball speed
        self.hit_bottom = False 
        self.score = 0
        self.lives = 1
        
    def draw(self):
        global cheat
        if cheat == False: # if cheat key is not activated (as cheat key decrease the ball speed by 2)
            if not paused: # if the pause is not activated
                self.canvas.move(self.id, self.xspeed, self.yspeed) # move the ball 
            pos = self.canvas.coords(self.id) # get the position of the ball
            if pos[1] <= 80:  # if the ball hit the upper barrier
                self.yspeed = 4
            if pos[3] >= 650: # if the ball hit the lower barrirer
                self.hit_bottom = True
                self.lives -= 1 
            if pos[0] <= 0: # if the ball hit left side of the window
                self.xspeed = 4
            if pos[2] >= 1280: # if the ball hit the right side of the window
                self.xspeed = -4
            if self.hit_paddle(pos) == True: # if the ball hit the paddle
                self.yspeed = -4
                self.score += 1
        elif cheat == True: # if the cheat key is pressed (i.e the cheat function is activated)
            if not paused: # if the pause is not activated
                self.canvas.move(self.id, self.xspeed, self.yspeed)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 80:
                self.yspeed = 2
            if pos[3] >= 650:
                self.hit_bottom = True
                self.lives -= 1
            if pos[0] <= 0:
                self.xspeed = 2
            if pos[2] >= 1280:
                self.xspeed = -2
            if self.hit_paddle(pos) == True:
                self.yspeed = -2
                self.score += 1

    def hit_paddle(self, pos): 
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

# the class containing all properties of the paddle
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 220, 10, fill='orange') # creates the reactangle
        self.canvas.move(self.id, 640,600 ) 
        if not paused:
            self.canvas.bind_all('<Left>', self.move_left) # we bind the left key on the keyboard which moves the paddle left
            self.canvas.bind_all('<Right>', self.move_right) # we bind the right key on the keyboard which moves the paddle right
 
    def draw(self):  # function used to determine the position of the paddle
        global pos
        pos = self.canvas.coords(self.id)

    def move_left(self, *args): # callback function when press the left key which moves the paddle left
        if pos[0]>0:
            self.canvas.move(self.id,-25,0)
    
    def move_right(self, *args): # callback function when press the right key which moves the paddle right
        if pos[2]<1280:
            self.canvas.move(self.id,25,0)



def game_start():
    global label,label1,barrier,color_choosen1
    #add text and to the respective window
    label = canvas_game.create_text(5, 25, anchor=NW, text="Score: 0",fill='red',font=('Helvatical bold',15,'italic'))
    label1 = canvas_game.create_text(105, 25, anchor=NW, text="Lives: 3",fill='red',font=('Helvatical bold',15,'italic'))
    label2 = canvas_game.create_text(205, 25, anchor=NW, text="Press p to Pause",fill='red',font=('Helvatical bold',15,'italic'))
    label3 = canvas_game.create_text(405,25,anchor=NW,text='Press t to unpause',fill='red',font=('Helvatical bold',15,'italic'))
    label5 = canvas_game.create_text(600,25,anchor=NW,text='Press c to decrease speed of the ball',fill='red',font=('Helvatical bold',15,'italic'))
    label6 = canvas_game.create_text(900,25,anchor=NW,text='Press b for bosskey',fill='red',font=('Helvatical bold',15,'italic'))

    barrier = canvas_game.create_rectangle(0,60,1280,80,fill='orange') # creates orange colored reactangular barrier 
    barrier1 = canvas_game.create_rectangle(0,650,1280,670,fill='orange')# creates orange colored reactangular barrier 
    global paddle,ball,label4
    paddle = Paddle(canvas_game, 'orange') 
    ball = Ball(canvas_game, 'yellow', 25, paddle)
    label4 = canvas_game.create_text(600,360,anchor=NW,text='Press Space to Start',fill='yellow',font=('Helvatical bold',20,'italic'))
    canvas_game.bind_all('<space>',game_loop) # bind space key and when it is pressed game_loop function is callled

    # create save button in game_window
    button_to_save1 = Button(text="Save",command=save_score,height=1,width=12) 
    buttontosave_window = canvas_game.create_window(600,700,window = button_to_save1)
    button_to_save1.update()

    #create menu button in game_window
    button_to_menu9 = Button(text="Menu",command=menu_button9,height=1,width=12)
    buttontomenu9 = canvas_game.create_window(760,700,window = button_to_menu9)
    button_to_menu9.update()

def game_loop(*args):
    canvas_game.delete(label4) # delete the label4
    while True:
        if ball.lives>0: # loop runs if the lives of the ball is greater then 0.
            canvas_game.unbind('<space>') # unbind the space the function
            canvas_game.bind_all('<p>',button_to_pause) # bind p button to act as pause button
            canvas_game.bind_all('<t>',button_to_unpause) # bind t button to act as unpasue button 
            canvas_game.bind_all('<c>',cheatkey) # bind t button to act as cheat key
            canvas_game.bind_all('<b>',bosskey) # bind b button to act as bosskey
            ball.draw() 
            paddle.draw()
            canvas_game.itemconfig(label, text="Score: "+str(ball.score)) # this updates the score text in the game window
            canvas_game.itemconfig(label1, text="Lives: "+str(ball.lives)) # this updates the lives text in the game window
            time.sleep(0.001)
            canvas_game.update() # this updates screen widgets
            canvas_game.update_idletasks()
        
        else: # loop runs when the game is over
            # displays Game Over text on the window
            label7 = canvas_game.create_text(600,360,anchor=NW,text='Game Over',fill='yellow',font=('Helvatical bold',20,'italic'))
            time.sleep(0.1)
            break
    
game_start()
window.mainloop()