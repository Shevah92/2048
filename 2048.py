#!/usr/bin/env python
import curses
import random
import time
import csv
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN


def add_up():  # addition after up arrow key
    global list_of_numbers
    global valid_move
    global score
    for j in range(4):  # for doing the addition in every column
        for i in range(3):  # compares neighbor numbers with the if
            if list_of_numbers[i][j] == list_of_numbers[i+1][j] and list_of_numbers[i][j] != 0:
                # if true runs the addition sequence
                list_of_numbers[i][j] = list_of_numbers[i][j]+list_of_numbers[i+1][j]
                score += list_of_numbers[i][j]  # adds the created number to the score
                list_of_numbers[i+1][j] = 0
                valid_move[1] = 1  # indicates that a valid move was made


def add_down():  # addition after down key
    global list_of_numbers
    global valid_move
    global score
    for j in range(4):  # for doing the addition in every column
        for i in range(3):  # compares neighbor numbers
            if list_of_numbers[3-i][j] == list_of_numbers[3-(i+1)][j] and list_of_numbers[3-i][j] != 0:
                # if true runs the addition sequence
                list_of_numbers[3-i][j] = list_of_numbers[3-i][j]+list_of_numbers[3-(i+1)][j]
                score += list_of_numbers[3-i][j]  # adds the created number to the score
                list_of_numbers[3-(i+1)][j] = 0
                valid_move[2] = 1  # indicates that a valid move was made


def add_left():  # addition after left key
    global list_of_numbers
    global valid_move
    global score
    for i in range(4):  # for doing the addition in every row
        for j in range(3):  # compares neighbor numbers
            if list_of_numbers[i][j] == list_of_numbers[i][j+1] and list_of_numbers[i][j] != 0:
                # if true runs the addition sequence
                list_of_numbers[i][j] = list_of_numbers[i][j]+list_of_numbers[i][j+1]
                score += list_of_numbers[i][j]  # adds the created number to the score
                list_of_numbers[i][j+1] = 0
                valid_move[0] = 1  # indicates that a valid move was made


def add_right():  # addition after right key
    global list_of_numbers
    global valid_move
    global score
    for i in range(4):  # for doing the addition in every row
        for j in range(3):  # compares neighbor numbers
            if list_of_numbers[i][3-j] == list_of_numbers[i][3-(j+1)] and list_of_numbers[i][3-j] != 0:
                # if true runs the addition sequence
                list_of_numbers[i][3-j] = list_of_numbers[i][3-j]+list_of_numbers[i][3-(j+1)]
                score += list_of_numbers[i][3-j]  # adds the created number to the score
                list_of_numbers[i][3-(j+1)] = 0
                valid_move[3] = 1  # indicates that a valid move was made


def move_up():  # movement after up arrow key
    global list_of_numbers
    global valid_move
    i = 0
    for j in range(4):  # for moving in every column
        if list_of_numbers[i+1][j] != 0 or list_of_numbers[i+2][j] != 0 or list_of_numbers[i+3][j] != 0:
            # checks if moving is necessary (no need to move zeros)
            if list_of_numbers[i][j] == 0:
                while list_of_numbers[i][j] == 0:
                    # needed to move the first non-zero number in the column to this position
                    list_of_numbers[i][j] = list_of_numbers[i+1][j]
                    list_of_numbers[i+1][j] = list_of_numbers[i+2][j]
                    list_of_numbers[i+2][j] = list_of_numbers[i+3][j]
                    list_of_numbers[i+3][j] = 0
                valid_move[1] = 1  # indicates that a valid move was made
            if list_of_numbers[i+1][j] == 0 and (list_of_numbers[i+2][j] != 0 or list_of_numbers[i+3][j] != 0):
                # checks is moving is still necessary
                while list_of_numbers[i+1][j] == 0:  # moves the 2nd non-zero in the column to this position
                    list_of_numbers[i+1][j] = list_of_numbers[i+2][j]
                    list_of_numbers[i+2][j] = list_of_numbers[i+3][j]
                    list_of_numbers[i+3][j] = 0
                valid_move[1] = 1  # indicates that a valid move was made
            if list_of_numbers[i+2][j] == 0 and list_of_numbers[i+3][j] != 0:
                # moves the last non-zero to this position
                list_of_numbers[i+2][j] = list_of_numbers[i+3][j]
                list_of_numbers[i+3][j] = 0
                valid_move[1] = 1  # indicates that a valid move was made


def move_down():
    # movement after down arrow key, find the rest of the explanation
    # at def move_up function with the obvious differences
    global list_of_numbers
    global valid_move
    i = 3
    for j in range(4):
        if list_of_numbers[i-1][j] != 0 or list_of_numbers[i-2][j] != 0 or list_of_numbers[i-3][j] != 0:
            if list_of_numbers[i][j] == 0:
                while list_of_numbers[i][j] == 0:
                    list_of_numbers[i][j] = list_of_numbers[i-1][j]
                    list_of_numbers[i-1][j] = list_of_numbers[i-2][j]
                    list_of_numbers[i-2][j] = list_of_numbers[i-3][j]
                    list_of_numbers[i-3][j] = 0
                valid_move[2] = 1
            if list_of_numbers[i-1][j] == 0 and (list_of_numbers[i-2][j] != 0 or list_of_numbers[i-3][j] != 0):
                while list_of_numbers[i-1][j] == 0:
                    list_of_numbers[i-1][j] = list_of_numbers[i-2][j]
                    list_of_numbers[i-2][j] = list_of_numbers[i-3][j]
                    list_of_numbers[i-3][j] = 0
                valid_move[2] = 1
            if list_of_numbers[i-2][j] == 0 and list_of_numbers[i-3][j] != 0:
                list_of_numbers[i-2][j] = list_of_numbers[i-3][j]
                list_of_numbers[i-3][j] = 0
                valid_move[2] = 1


def move_left():
    # movement after left arrow key, find the rest of the explanation
    # at def move_up function with the obvious differences
    global list_of_numbers
    global valid_move
    j = 0
    for i in range(4):
        if list_of_numbers[i][j+1] != 0 or list_of_numbers[i][j+2] != 0 or list_of_numbers[i][j+3] != 0:
            if list_of_numbers[i][j] == 0:
                while list_of_numbers[i][j] == 0:
                    list_of_numbers[i][j] = list_of_numbers[i][j+1]
                    list_of_numbers[i][j+1] = list_of_numbers[i][j+2]
                    list_of_numbers[i][j+2] = list_of_numbers[i][j+3]
                    list_of_numbers[i][j+3] = 0
                valid_move[0] = 1
            if list_of_numbers[i][j+1] == 0 and (list_of_numbers[i][j+2] != 0 or list_of_numbers[i][j+3] != 0):
                while list_of_numbers[i][j+1] == 0:
                    list_of_numbers[i][j+1] = list_of_numbers[i][j+2]
                    list_of_numbers[i][j+2] = list_of_numbers[i][j+3]
                    list_of_numbers[i][j+3] = 0
                valid_move[0] = 1
            if list_of_numbers[i][j+2] == 0 and list_of_numbers[i][j+3] != 0:
                list_of_numbers[i][j+2] = list_of_numbers[i][j+3]
                list_of_numbers[i][j+3] = 0
                valid_move[0] = 1


def move_right():
    # movement after right arrow key, find the rest of the explanation
    # at def move_up function with the obvious differences
    global list_of_numbers
    global valid_move
    j = 3
    for i in range(4):
        if list_of_numbers[i][j-1] != 0 or list_of_numbers[i][j-2] != 0 or list_of_numbers[i][j-3] != 0:
            if list_of_numbers[i][j] == 0:
                while list_of_numbers[i][j] == 0:
                    list_of_numbers[i][j] = list_of_numbers[i][j-1]
                    list_of_numbers[i][j-1] = list_of_numbers[i][j-2]
                    list_of_numbers[i][j-2] = list_of_numbers[i][j-3]
                    list_of_numbers[i][j-3] = 0
                valid_move[3] = 1
            if list_of_numbers[i][j-1] == 0 and (list_of_numbers[i][j-2] != 0 or list_of_numbers[i][j-3] != 0):
                while list_of_numbers[i][j-1] == 0:
                    list_of_numbers[i][j-1] = list_of_numbers[i][j-2]
                    list_of_numbers[i][j-2] = list_of_numbers[i][j-3]
                    list_of_numbers[i][j-3] = 0
                valid_move[3] = 1
            if list_of_numbers[i][j-2] == 0 and list_of_numbers[i][j-3] != 0:
                list_of_numbers[i][j-2] = list_of_numbers[i][j-3]
                list_of_numbers[i][j-3] = 0
                valid_move[3] = 1


def spawn():  # function responsible for spawning new numbers after valid moves
    global list_of_numbers
    x = random.randint(0, 3)  # generates where the new number will spawn
    y = random.randint(0, 3)  # generates where the new number will spawn
    chance = random.uniform(0, 1)  # responsible for generating number 4 to spawn
    if chance >= 0.9:  # according to Reddit, chance to spawn number 4 is 10%
        spawn_num = 4
    else:  # 90% of the time number 2 will spawn
        spawn_num = 2
    if list_of_numbers[x][y] == 0:  # checks if the generated location is empty
        list_of_numbers[x][y] = spawn_num
    else:  # if it's not empty the function calls itself again, thus running until an empty location is found
        spawn()


def show_numbers(screen):
    global list_of_numbers
    for i in range(4):
        for j in range(4):
            numbers = str(list_of_numbers[i][j])  # needed to convert int into string
            # so the addstr can print it into the screen
            color_numbers(screen, i, j, numbers)


def color_numbers(screen, i, j, numbers):  # responsible for the different colors of numbers
    global list_of_numbers
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    if list_of_numbers[i][j] == 2:
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(1))
    elif list_of_numbers[i][j] == 4:
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(2))
    elif list_of_numbers[i][j] == 8:
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(3))
    elif list_of_numbers[i][j] == 16:
        curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(4))
    elif list_of_numbers[i][j] == 32:
        curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(5))
    elif list_of_numbers[i][j] == 64:
        curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(6))
    elif list_of_numbers[i][j] == 128:
        screen.addstr((i+1)*4, (j+1)*15, numbers)
    elif list_of_numbers[i][j] == 256:
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(1))
    elif list_of_numbers[i][j] == 512:
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(2))
    elif list_of_numbers[i][j] == 1024:
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(3))
    elif list_of_numbers[i][j] == 2048:
        screen.addstr((i+1)*4, (j+1)*15, numbers, curses.color_pair(4))
    else:
        screen.addstr((i+1)*4, (j+1)*15, numbers)  # zeros are white


def draw_grid(screen):  # responsible for drawing a grid around the numbers
    screen.hline(2, 12, "_", 53)
    screen.hline(6, 11, "_", 54)
    screen.hline(10, 11, "_", 54)
    screen.hline(14, 11, "_", 54)
    screen.hline(18, 11, "_", 54)
    screen.vline(3, 23, "|", 16)
    screen.vline(3, 38, "|", 16)
    screen.vline(3, 53, "|", 16)
    screen.vline(3, 11, "|", 16)
    screen.vline(3, 65, "|", 16)


def import_scores():  # responsible for importing scores from a csv file
    global score_list
    global name_list
    with open("highscores.csv") as infile:
        readCSV = csv.reader(infile, delimiter=',')
        for row in readCSV:  # creates two lists, one for keys and one for values
            name_in_file = row[0]
            score_in_file = row[1]
            score_list.append(score_in_file)
            name_list.append(name_in_file)


def export_scores(screen, score):  # responsible for exporting the scores
    screen.clear()
    global score_list
    global name_list
    name = "Enter your name:"
    screen.addstr(curses.LINES // 2, (curses.COLS - len(name)) // 2, name)
    curses.echo()
    input_name = screen.getstr(curses.LINES // 2 + 1, curses.COLS // 2)  # handles user input
    input_name = str(input_name, "utf-8")  # converts bytes to string format
    # this long part is responsible for inserting names and scores into the correct place
    if len(score_list) == 0:
        score_list.append(score)
        name_list.append(input_name)
    elif len(score_list) == 1:
        if int(score_list[0]) <= score:
            score_list.insert(0, score)
            name_list.insert(0, input_name)
        else:
            score_list.append(score)
            name_list.append(input_name)
    else:
        i = 0
        for i in range(len(score_list)):
            if int(score) > int(score_list[0]):
                score_list.insert(0, score)
                name_list.insert(0, input_name)
                break
            elif int(score_list[i]) >= int(score) and int(score) > int(score_list[i+1]):
                score_list.insert(i + 1, score)
                name_list.insert(i + 1, input_name)
                break
            elif int(score_list[len(score_list) - 1]) >= int(score):
                score_list.append(score)
                name_list.append(input_name)
                break
    with open("highscores.csv", 'w', newline='') as outfile:  # actual exporting happens here
        writer = csv.writer(outfile, delimiter=',')
        for i in range(len(score_list)):
            outlist = [name_list[i], score_list[i]]
            writer.writerow(outlist)
    show_highscores(screen)


def show_highscores(screen):  # shows the highest scores on the screen after the game is over
    screen.clear()
    global score_list
    global name_list
    highscore = "Highscores:"
    screen.addstr(1, (curses.COLS - len(highscore)) // 2, highscore)
    if len(score_list) <= 10:  # shows every highscore if there are less then 10
        for i in range(len(score_list)):
            screen.addstr(i * 2 + 3, curses.COLS // 2 - len(name_list[i]), name_list[i])
            screen.addstr(i * 2 + 3, curses.COLS // 2 + 1, str(score_list[i]))
    else:
        for i in range(10):  # shows the 10 highest scores
            screen.addstr(i * 2 + 3, curses.COLS // 2 - len(name_list[i]), name_list[i])
            screen.addstr(i * 2 + 3, curses.COLS // 2 + 1, str(score_list[i]))
    screen.refresh()
    time.sleep(5)


def main(scr):
    # the usual curses initialization
    screen = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)
    import_scores()  # importing scores from a csv file
    # we run spawn twice when the game start so 2 numbers will be placed in the grid, just like in the original game
    spawn()
    spawn()

    while True:  # the loop which keeps running until an exit criteria is achieved
        # this part is responsible for clearing the
        # screen at the start of each loop and printing out the border, score and grid
        screen.clear()
        screen.border(0)
        title = '*** Welcome to the GAME 2048! *** '
        screen.addstr(0, (curses.COLS - len(title)) // 2, title)
        your_score = "Your score:"
        screen.addstr(20, 30, your_score)
        show_score = str(score)  # needed to convert int into string so the addstr can print it into the screen
        screen.addstr(20, 42, show_score)
        draw_grid(screen)

        # this part is responsible for printing the numbers from the 2D list to the screen
        show_numbers(screen)

        # this part is responsible for handling the input and calling the right functions
        event = screen.getch()
        if event == ord("q"):  # key command to exit
            break
        elif event == ord("w"):  # for the demo, to show the part if the player succedd to create a 2048 tile
            list_of_numbers[0][0] = 2048
        elif event == curses.KEY_UP:
            valid_move[1] = 0  # tells the program that the particular key was pressed down
            move_up()  # responsible for deleting zeros among the other numbers
            add_up()  # responsible for adding together neighbor numbers
            move_up()  # after addition new zeros could appear, this is responsible for deleting those among numbers
            if valid_move[1] == 1:  # makes sure a new number only spawn if a valid move was made
                spawn()

        elif event == curses.KEY_DOWN:  # see explanation at KEY.UP event
            valid_move[2] = 0
            move_down()
            add_down()
            move_down()
            if valid_move[2] == 1:
                spawn()

        elif event == curses.KEY_RIGHT:  # see explanation at KEY.UP event
            valid_move[3] = 0
            move_right()
            add_right()
            move_right()
            if valid_move[3] == 1:
                spawn()

        elif event == curses.KEY_LEFT:  # see explanation at KEY.UP event
            valid_move[0] = 0
            move_left()
            add_left()
            move_left()
            if valid_move[0] == 1:
                spawn()
        show_numbers(screen)
        screen.refresh()
        count_of_non_zeros = 0
        # checks if a 2048 "tile" exists, and count how many non-zero numbers are in the list
        for i in range(4):
            for j in range(4):
                if list_of_numbers[i][j] == 2048:  # if 2048 exists in the list, runs the victory sequence
                    screen.refresh()
                    time.sleep(3)
                    screen.clear()
                    victory = "Congratulations! You beat the game! :)"
                    screen.addstr(curses.LINES // 2, (curses.COLS - len(victory)) // 2, victory)
                    screen.addstr((curses.LINES // 2)+1, (curses.COLS - len(your_score)) // 2, your_score)
                    screen.addstr((curses.LINES // 2)+2, (curses.COLS - len(show_score)) // 2, show_score)
                    screen.refresh()
                    time.sleep(3)
                    export_scores(screen, score)  # export scores to a csv file
                    try:
                        curses.endwin(screen)
                    except TypeError:
                        exit()
                if list_of_numbers[i][j] != 0:
                    count_of_non_zeros += 1

        if count_of_non_zeros == 16:  # checks if all numbers in the list are non-zero
            if valid_move.count(0) == 4:  # checks if any valid movement is possibel, if not runs the game over sequence
                screen.clear()
                game_over = "Game over! :*("
                screen.addstr(curses.LINES // 2, (curses.COLS - len(game_over)) // 2, game_over)
                screen.addstr((curses.LINES // 2)+1, (curses.COLS - len(your_score)) // 2, your_score)
                screen.addstr((curses.LINES // 2)+2, (curses.COLS - len(show_score)) // 2, show_score)
                screen.refresh()
                time.sleep(3)
                export_scores(screen, score)  # export scores to a csv file
                break

        screen.refresh()
score_list = []
name_list = []
list_of_numbers = [[0 for i in range(4)] for j in range(4)]  # generates a 4*4 two-dimensional list and
# fills it up with zeros, this list is responsible for storing numbers
valid_move = [1 for i in range(4)]  # generates a 4 long list filled up with 1s,
# this list is responsible for keeping track is a valid move was made.
# 0th eleement is for Left, 1st is for Up, 2nd is for Down, 3rd is for Right.
score = 0  # sets the score zero at the beginning of the game.
curses.wrapper(main)
