import tkinter
import os
import random
import tkinter.messagebox as msg


###### world list fucntion

def word_list():
    with open("words.txt", "r") as my_file:
        words = my_file.read()
        return words.split("\n")

###  all global variable and arrays
# img_lst = sorted(os.listdir("./images"))
# print (img_lst)
# print (img_lst)
idx_img = 0
words = word_list()
random.shuffle(words)
word = words[0].lower()
print (word)
left_life = 6
list_of_word = [i for i in word]
r = ["_"]*len(word)
guess_start = ' '.join(r)

#####fucn

def play(guess):
    print (guess)
    global word, left_life, guess_start, r, list_of_word, idx_img
    p = guess.lower()
    if guess.lower() in word:
        a = []
        for i in range(0,word.count(p)):
            y = list_of_word.index(p)
            a.append(y)
            list_of_word.pop(y)                       
            list_of_word.insert(y,"0")
        for i in a:
            r.pop(i)
            r.insert(i,p)
        o = " ".join(r)
        guess_word.config(text=o)
        if word == "".join(r):
            Try = msg.askokcancel("Yeah! you win", "want to play again")
            if Try == True:
                idx_img = 0
                random.shuffle(words)
                word = words[0]
                # photo = tkinter.PhotoImage(file=f"./images/{img_lst[idx_img]}")
                throwing_image.config(image=img_lst[idx_img])
                left_life = 6
                leftlife.config(text=left_life)
                list_of_word = [i for i in word]
                r = ["_"]*len(word)
                guess_start = ' '.join(r)
                print (word)
                guess_word.config(text=guess_start)
            else:
                quit()
                            
    else:
        idx_img += 1
        left_life -= 1
        leftlife.config(text=left_life) 
        # photo = tkinter.PhotoImage(file=f"./images/{img_lst[idx_img]}")
        throwing_image.config(image=img_lst[idx_img])
        if left_life == 0:
            Try = msg.askretrycancel(f"sorry! word were {word}" "wanna try again!")
            if Try == True:
                idx_img = 0
                random.shuffle(words)
                word = words[0]
                # photo = tkinter.PhotoImage(file=f"./images/{img_lst[idx_img]}")
                throwing_image.config(image=img_lst[idx_img])
                left_life = 6
                leftlife.config(text=left_life)
                list_of_word = [i for i in word]
                r = ["_"]*len(word)
                guess_start = ' '.join(r)
                print (word)
                guess_word.config(text=guess_start)
            else:
                quit()

# random.shuffle(words)
# word = words[0]
main_frame = tkinter.Tk()
main_frame.geometry("740x560")
main_frame.resizable(False, False)
main_frame.config(background="light green")

# img_lst = [tkinter.PhotoImage(i) for i in img_lst]
img_lst = [tkinter.PhotoImage(file='./images/hangman0.png'), tkinter.PhotoImage(file='./images/hangman1.png'), tkinter.PhotoImage(file='./images/hangman2.png'), tkinter.PhotoImage(file='./images/hangman3.png'), tkinter.PhotoImage(file='./images/hangman4.png'), tkinter.PhotoImage(file='./images/hangman5.png'), tkinter.PhotoImage(file='./images/hangman6.png')]

# print (img_lst)

###Label
heading = tkinter.Label(main_frame, text="The Hangman Game", font="lucida 20 bold", fg="blue", bg="light green")
heading.place(x=200, y=5)

lifeLabel = tkinter.Label(main_frame, text="You have left", font="arial 25 bold", fg="red", bg="light green")
lifeLabel.place(x=490,y=80)

leftlife = tkinter.Label(main_frame, text=left_life, font="arial 35 bold", bg="light green", fg="red")
leftlife.place(x=575, y=125)

guess_word = tkinter.Label(main_frame, text=guess_start, font="arial 35 bold", bg="light green", fg="black")
guess_word.place(x=60, y=230)

####buttons A-Z
x1 = 15
for i in [j for j in  "ABCDEFGH"]:
    # print (i)
    tkinter.Button(main_frame,font="arial 15 bold",bg="orange", text=i,command=lambda i=i: play(i)).place(x=x1,y=330)
    x1 += 50

x1 = 15
for i in [j for j in  "IJKLMNOP"]:
    # print (i)
    tkinter.Button(main_frame,font="arial 15 bold",bg="orange", text=i,command=lambda i=i: play(i)).place(x=x1,y=380)
    x1 += 50
x1 = 15
for i in [j for j in  "QRSTUVWX"]:
    # print (i)
    tkinter.Button(main_frame,font="arial 15 bold",bg="orange", text=i,command=lambda i=i: play(i)).place(x=x1,y=420)
    x1 += 50
x1 = 170
for i in [j for j in  "YZ"]:
    # print (i)
    tkinter.Button(main_frame,font="arial 15 bold",bg="orange", text=i,command=lambda i=i: play(i)).place(x=x1,y=460)
    x1 += 50

##### image throwing
# print (img_lst)
# photo = tkinter.PhotoImage(file=f"./images/{img_lst[idx_img]}")
throwing_image = tkinter.Label(main_frame, bg="light green")
throwing_image.place(x=510, y=280)

throwing_image.config(image=img_lst[0])

main_frame.mainloop()
