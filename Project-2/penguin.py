# Screen resolution 1280x720
from tkinter import *
from time import sleep
import random
import time
from random import randint


root = Tk()

# function to display the menu
def window_Edit():
    root.title("Penguin run")
    root.geometry("1280x720")
    root.resizable(False, False)  # dosent let the screen be resized
    root.configure(bg="#006994")
    global Entry_name
    Entry_name = Entry(root, width=30)
    Entry_name.place(x=(width / 2) - 160, y=190)
    Entry_name.bind("<Return>", start_Game)
    global label_2
    label_2 = Label(
        root,
        text="Please enter your penguin name and press enter: ",
        font=("Arial", 20),
        background="#006994",
        fg="white",
    )
    label_2.place(x=270, y=140)
    global label_1
    label_1 = Label(
        root,
        text="Penguin Run",
        font=(" MS Sans Serif bold ", 35),
        background="#006994",
        fg="white",
    )
    label_1.place(x=(width / 2) - 210, y=50)
    label_1.configure(font="Verdana 35 bold underline")
    

    global label_3
    label_3 = Label(
        root,
        text="Choose a difficulty or load game : ",
        font=("Arial", 20),
        background="#006994",
        fg="white",
    )
    label_3.place(x=(width / 2) - 225, y=230)
    start_button()
# ----------------------------------------------- #
def start_Game(event):   # Function to make sure a name is always entered
    global name
    name = Entry_name.get()

    global easy, medium, hard
    if len(name) > 0:
        button_Play.bind(
            "<Button-1>",
            display_canvas,
            delete
        )
        button_medium.bind(
            "<Button-1>",
            medium_canvas,
            delete
        )
        button_hard.bind(
            "<Button-1>",
            hard_canvas,
            delete
        )
        button_load.bind(
            "<Button-1>",
            load_canvas,
            delete
        )


# -------------------------------------------#
# function for the buttons used on the menu
def start_button():
    global button_Play
    button_Play = Button(
        root,
        text="Easy",
        background="#006994",
        font=("Arial", 25),
        width=8,
        fg="white"
    )
    button_Play.place(x=300, y=290)

    global button_medium
    button_medium = Button(
        root,
        text="Medium",
        background="#006994",
        font=("Arial", 25),
        width=8,
        fg="Yellow",
    )
    button_medium.place(x=530, y=290)

    global button_hard
    button_hard = Button(
        root,
        text="Hard",
        background="#006994",
        font=("Arial", 25),
        width=8,
        fg="red"
    )
    button_hard.place(x=770, y=290)

    global button_quit
    button_quit = Button(
        root,
        text="Quit",
        background="#006994",
        font=("Arial", 25),
        width=24,
        command=root.destroy,
        fg="white",
    )
    button_quit.place(x=340, y=410)

    global button_load
    button_load = Button(
        root,
        text="Load Game",
        background="#006994",
        font=("Arial", 25),
        width=24,
        fg="white"
    )
    button_load.place(x=340, y=535)


def collision(i):  # function for collision detection
    # allows the images to have 4 coords instead of 2
    mbox = canvas.bbox(monster[i])
    pbox = canvas.bbox(penguin)
    if (
        pbox[0] < mbox[2] and
        pbox[2] > mbox[0] and
        pbox[1] < mbox[3] and
        pbox[3] > mbox[1]
    ):
        return True
    return False
    game_Over()
    # Always checking if lives = 0


def left_Key(event):
    peng_pos = canvas.coords(penguin)
    x = -40
    y = 0
    # stop the movement if pause is true
    if paused is True:
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",)
    else:
        canvas.delete("pausing")
        if peng_pos[0] > 0:
            canvas.move(penguin, x, y)
        for i in range(len(monster)):
            # if there is a collison, move the postion of the monster
            if collision(i):
                global lives
                monster_X = random.randint(10, 1100)
                monster_Y = random.randint(-400, -100)
                canvas.coords(monster[i], monster_X, monster_Y)
                lives = lives - 1
                if lives == 0:
                    game_Over()
                # Update lives when a collison does occur
                canvas.itemconfigure(
                    lives_Text,
                    text="Lives: " + str(lives)
                )
                i += 1


# function to move right but stop at a certain point
def right_Key(event):
    peng_pos = canvas.coords(penguin)
    x = 40
    y = 0
    if paused is True:
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",
        )
    else:
        canvas.delete("pausing")
        if peng_pos[0] < 1150:
            canvas.move(penguin, x, y)
        for i in range(len(monster)):
            if collision(i):
                global lives
                monster_X = random.randint(10, 1200)
                monster_Y = random.randint(-400, -100)
                canvas.coords(monster[i], monster_X, monster_Y)
                lives = lives - 1
                if lives == 0:
                    game_Over()
                canvas.itemconfigure(lives_Text, text="Lives: " + str(lives))
                i += 1


# allows the user to gain more lives
def cheat_Key(event):
    global lives
    if paused is True:
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",
        )
    else:
        canvas.delete("pausing")
        lives += 1
        canvas.itemconfigure(lives_Text, text="Lives: " + str(lives))


# allows you to increase the score
def score_Up(event):
    global score
    if paused is True:
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",
        )
    else:
        canvas.delete("pausing")
        score += 1
        canvas.itemconfigure(score_Text, text="Score: " + str(score))


# canvas when loading a saved game
def load_canvas(event):
    canvas.pack(fill="both", expand=True)
    load_It()
    respawning()


# canvas for easy mode
def display_canvas(event):
    canvas.pack(fill="both", expand=True)
    global lives
    respawning()


def medium_canvas(event):
    canvas.pack(fill="both", expand=True)
    global lives
    # reduce lives in medium mode
    lives = lives - 1
    Text = "Lives: " + str(lives)
    canvas.itemconfigure(lives_Text, text="Lives: " + str(lives))
    respawning()


def hard_canvas(event):
    canvas.pack(fill="both", expand=True)
    global lives
    # reduce lives in hard mode
    lives = lives - 2
    Text = "Lives: " + str(lives)
    canvas.itemconfigure(lives_Text, text="Lives: " + str(lives))
    respawning()


# function to incre,ment the score
def score_increase():
    global score
    if paused is True:
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",
        )
    else:
        canvas.delete("pausing")
        for i in range(len(monster)):
            # if monsters go to the end of the screen,
            # move them back to the top
            if (canvas.coords(monster[i])[1]) >= 720:
                monster_X = random.randint(10, 1100)
                monster_Y = random.randint(-400, -100)
                canvas.coords(monster[i], monster_X, monster_Y)
                # increment score
                score += 1
                canvas.itemconfigure(score_Text, text="Score:" + str(score))
                i = i + 1
            else:
                pass


def respawning():
    monster.append(
        canvas.create_image(
           randint(10, 1100), -100,
           image=monster_image, anchor="nw", tag="monsterman"
        )
    )
    # create monsters until there is the right number
    if len(monster) != 4:
        # loop back to the top of the function
        root.after(1, respawning)
    if paused is True:
        # creates an image so user knows its paused
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",
        )
    else:
        canvas.delete("pausing")
        for i in range(len(monster)):
            monster_Move()
        monster_X = random.randint(10, 1200)
        monster_Y = random.randint(-400, -100)
        canvas.coords(monster[i], monster_X, monster_Y)


# function for all the binding and movement
def monster_Move():
    if paused is True:
        pausing = canvas.create_oval(
            0,
            0,
            20,
            20,
            fill="#0EBFE9",
            tag="pausing",
        )
    else:
        global lives
        canvas.delete("pausing")
        for i in range(len(monster)):
            canvas.move(monster[i], 0, 5)
    canvas.bind("<Left>", left_Key)
    canvas.bind("<Right>", right_Key)
    canvas.bind("<Up>", cheat_Key)
    canvas.bind("<z>", score_Up)
    canvas.focus_set()
    root.after(100, monster_Move)
    score_increase()
    for i in range(len(monster)):
        if collision(i):
            monster_X = random.randint(10, 1200)
            monster_Y = random.randint(-400, -100)
            canvas.coords(monster[i], monster_X, monster_Y)
            lives = lives - 1
            if lives == 0:
                game_Over()
            canvas.itemconfigure(lives_Text, text="Lives: " + str(lives))
            i += 1


# function to delete everything,
# from the main menu
def delete():
    Entry_name.pack_forget()
    label_1.pack_forget()
    label_2.pack_forget()
    label_3.pack_forget()
    button_Play.pack_forget()
    button_board.pack_forget()
    button_quit.pack_forget()


# function forGame over screen
def game_Over():
    global lives, score, paused, leaderboard, Game_Over
    # create bubbles on the canvas
    bubble = []
    c = ["#008B8B", "#5F9F9F", "#008080"]
    for i in range(400):
        x = randint(1, 1280)
        y = randint(1, 720)

        size = randint(2, 5)
        f = randint(0, 2)

        xy = (x, y, x + size, y + size)
        tmp_bubble = my_canvas.create_oval(xy)

        my_canvas.itemconfig(tmp_bubble, fill=c[f])

        bubble.append(tmp_bubble)
    Game_Over = True
    # Pause the game
    paused = True
    # delete the game canvas
    canvas.pack_forget()
    # Display final score
    f_txt = "Final Score:" + str(score)
    my_canvas.itemconfigure(f_txt, text="Score:" + str(score))
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_text(
        (width / 2) - 40,
        100,
        fill="white",
        font=("Arial", 40),
        text="Game Over!",
        tag="Game_Over",
    )
    my_canvas.create_text(
        (width / 2) - 40, 170, fill="red", font=("Arial", 30), text=f_txt
    )
    button_quit = Button(
        my_canvas,
        text="Quit",
        borderwidth=0,
        font=("Arial", 25),
        width=20,
        command=root.destroy,
        bg="#006994",
        fg="white",
    )
    button_quit.place(x=(width / 2) - 210, y=250)
    my_canvas.create_text(
        (1280 / 2) - 40,
        350,
        fill="white",
        font=("Arial", 40),
        text="Leaderboard",
        tag="Lboard",
    )
    global Entry_name
    # Get users entry name
    name = Entry_name.get()
    final_score = str(score)
    user_stuff = final_score + " " + name
    # append the score to the leaderboard file
    uscr = open("leaderboard.txt", "a")
    uscr.write(user_stuff + "\n")
    uscr.close()
    # empty array for leaderboard
    leaderboard = []
    # sort the leaderboard
    with open("leaderboard.txt") as f:
        for line in f:
            leaderboard.append(line.split())
    leaderboard = sorted(leaderboard, key=lambda x: int(x[0]), reverse=True)
    # Display leaderboard to user
    try:
        my_canvas.create_text(
            (1280 / 2) - 40,
            450,
            fill="white",
            font=("Times 20 italic bold", 30),
            text="1. " +
            leaderboard[0][0] +
            str(" ") +
            leaderboard[0][1] +
            str(" -High score!!"),
        )
        my_canvas.create_text(
            (1280 / 2) - 45,
            525,
            fill="white",
            font=("Times 20 italic bold", 30),
            text="2. " + leaderboard[1][0] + str(" ") + leaderboard[1][1],
        )
        my_canvas.create_text(
            (1280 / 2) - 40,
            600,
            fill="white",
            font=("Times 20 italic bold", 30),
            text="3. " + leaderboard[2][0] + str(" ") + leaderboard[2][1],
        )
    except:
        pass


# function to display the boss key
def boss_key(event):
    canvas.unbind("<b>")
    canvas.bind("<b>", no_boss)
    global paused, boss_image, show_boss, paused
    # pause game
    paused = True
    pause_button.place_forget()
    save_button.place_forget()
    show_boss = canvas.create_image(
        (0, 0), image=boss_image, anchor="nw", tag="boss_ones"
    )


# function to remove boss image
def no_boss(event):
    global paused
    canvas.unbind("<b>")
    canvas.bind("<b>", boss_key)
    # delete boss image
    canvas.delete(show_boss)
    pause_button.place(x=1200, y=100)
    save_button.place(x=10, y=100)
    # continue the game
    paused = False


# function for pausing
def pause_It():
    global paused
    if paused is False:
        paused = True
    elif paused is True:
        paused = False
    else:
        None


# function to the save the game
def save_It():
    global lives, score
    save_lives = lives
    save_score = score
    save_penguin = canvas.coords(penguin)
    file_save(
        str(save_lives),
        str(save_score),
        str(save_penguin)
    )
    # end game after being clicked
    root.destroy()


# fucntion to append saved items to a file
def file_save(
                save_lives,
                save_score,
                save_penguin
):
    game_file = open(
        "game_file.txt",
        "w"
    )
    game_file.write(
        save_lives +
        "\n"
    )
    game_file.write(
        save_score +
        "\n"
    )
    game_file.write(
        save_penguin +
        "\n"
    )
    game_file.close()


# function to read saved data
def read_save():
    save_data = []
    game_file = open("game_file.txt")
    save_data = game_file.readlines()
    game_file.close()
    return save_data


# function to load saved data
def load_It():
    save_data = read_save()
    global lives, score
    temp_lives = save_data[0]
    lives = int(temp_lives)
    canvas.itemconfigure(lives_Text, text="Lives: " + str(lives))
    temp_score = save_data[1]
    score = int(temp_score)
    canvas.itemconfigure(score_Text, text="Score: " + str(score))
    # empty array to store penguin pos
    penguin_Data = []
    penguin_Data = save_data[2].split(",")
    penguin_Data[-1] = penguin_Data[-1].strip()
    pengx = penguin_Data[1].replace(
        "]",
        ""
    )
    pengy = penguin_Data[0].replace(
        "[",
        ""
    )
    # Change coords to previously saved
    canvas.coords(
        penguin,
        pengy,
        pengx
    )


# #--------------------------------Main body-------------------------------##
Game_Over = False
width = 1280
height = 720
paused = False
easy = False
medium = False
hard = False
global boss_image
global show_boss
window_Edit()
canvas = Canvas(root, width=1280, height=720, background="#006994")
canvas.bind("<b>", boss_key)
my_canvas = Canvas(root, width=1280, height=720, background="#006994")

# ------ Various images------#
background = PhotoImage(file="background.png")
background_label = canvas.create_image((0, 0), image=background, anchor="nw")
penguin_image = PhotoImage(file="penguin.png")
penguin = canvas.create_image((640, 500), image=penguin_image, anchor="nw")
monster_image = PhotoImage(file="monster.png")
boss_image = PhotoImage(file="boss.png")
pause_image = PhotoImage(file="pause.png")
pause_label = Label(image=pause_image)
pause_button = Button(
    canvas,
    image=pause_image,
    borderwidth=0,
    bg="white",
    command=pause_It
)
pause_button.place(x=1200, y=100)
save_image = PhotoImage(file="save.png")
save_label = Label(image=save_image)
save_button = Button(
    canvas,
    image=save_image,
    borderwidth=0,
    command=save_It
)
save_button.place(x=10, y=100)
# -----------------------------------------------------#

# counter for score
score = 0
txt = "Score:" + str(score)
f_txt = "Final Score:" + str(score)
score_Text = canvas.create_text(
    80, 50, fill="red", font=("Times 20 italic bold", 25), text=txt
)

# counter for lives
lives = 3
Text = "Lives: " + str(lives)
lives_Text = canvas.create_text(
    1200, 50, fill="black", font=("Times 20 italic bold", 25), text=Text
)
save_lives = 0

# empty array to create monster
monster = []
root.mainloop()

