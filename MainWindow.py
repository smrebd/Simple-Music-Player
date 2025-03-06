from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import customtkinter


window = Tk()
window.title("Music Player  \O/ ")
window.geometry('350x250')
window.resizable(False, False)
window.configure(bg='black')


mixer.init()


#icon
icon = PhotoImage(file='icon/icon.png')
window.iconphoto(False, icon) 



#functions
def add_song(): 
    songs = filedialog.askopenfilenames(initialdir='Music/', title="chose your song", filetypes=(("All Files", "*.*"),))
    for song in songs:
        songBox.insert(END, song)



def play():
    song = songBox.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play(0)


        
def nextsong():
    try:
        nextsong = songBox.curselection()
        nextsong = nextsong[0]+1
        song = songBox.get(nextsong)
        mixer.music.load(song)
        mixer.music.play()
        songBox.selection_clear(0, END)
        songBox.activate(nextsong)
        songBox.selection_set(nextsong, last=None)

    except IndexError:
        messagebox.showwarning("Warning", "You Must Select A Song Then Chose To Go Next Song")




global paused
paused = False

def pause(ispaused):
    global paused
    paused = ispaused
    
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True
        


def repeat():
    mixer.music.rewind()



def skip_backward():
    n1 = en1.get()
    n2 = mixer.music.get_pos()
    try:

        if float(n2/1000) > float(n1):
            userskip = float(n2/1000) - float(n1) 
            mixer.music.set_pos(userskip)
        else:
            userskip = float(n1) - float(n2/1000)
            mixer.music.set_pos(userskip)

    except ValueError:
        en1.config(bg="#a75959", fg="black")


def skip_forward():
    n1 = en1.get()
    n2 = mixer.music.get_pos()

    try: 

        userskip = float(n1) + float(n2/1000)
        mixer.music.set_pos(userskip)

    except ValueError:
        en1.config(bg="#a75959", fg="black")
    
    

def volume(value):
    mixer.music.set_volume(value)
       






    
# frame for buttons
frame_btn = Frame(window, height=10, bg="gray")
frame_btn.pack(pady=2, padx=2, fill="x", side="bottom")



# images of buttons
playBtnImage = PhotoImage(file="icon/play.png")
stopBtnImage = PhotoImage(file="icon/pause.png")
nextBtnImage = PhotoImage(file="icon/next.png")
repeatBtnImage = PhotoImage(file="icon/repeat.png")
skipbackwardBtnImage = PhotoImage(file="icon/left.png")
skipforwardBtnImage = PhotoImage(file="icon/right.png")
speedbutton = PhotoImage(file="icon/speed.png")



# take buttons with their icons
Label(frame_btn, text="         ", bg='gray', fg="gray").pack(padx=0.7, pady=4.7, side="left")

left_btn = customtkinter.CTkButton(frame_btn, image=skipbackwardBtnImage, width=10, text="", fg_color=("black", "lightgray"), command=skip_backward)
left_btn.pack(padx=5.7, pady=4.7, side="left")

repeat_btn = customtkinter.CTkButton(frame_btn, image=repeatBtnImage, width=10, text="", fg_color=("black", "lightgray"), command=repeat)
repeat_btn.pack(padx=5.7,pady=2.7, side="left")

play_btn = customtkinter.CTkButton(frame_btn, image=playBtnImage, width=10, text="", fg_color=("black", "lightgray"), command=play)
play_btn.pack(padx=5.7,pady=2.7, side="left")

pause_btn = customtkinter.CTkButton(frame_btn, image=stopBtnImage, width=10, text="", fg_color=("black", "lightgray"), command= lambda: pause(paused))
pause_btn.pack(padx=5.7,pady=2.7, side="left")

right_btn = customtkinter.CTkButton(frame_btn, image=skipforwardBtnImage, width=10, text="", fg_color=("black", "lightgray"), command= skip_forward)
right_btn.pack(padx=5.7,pady=2.7, side="left")

next_btn = customtkinter.CTkButton(frame_btn, image=nextBtnImage, width=10, text="", fg_color=("black", "lightgray"), command=nextsong)
next_btn.pack(padx=5.7,pady=2.7, side="left")



#volum
slider = customtkinter.CTkSlider(master=window, from_= 0, to=1, command=volume, width=210, height=8)
slider.pack(padx=0.5, pady=3, side="bottom")


#a listbox for show list of songs that added
songBox = Listbox(window, bg="black", fg="#CC99FF", width=56, height=8, selectbackground="gray", selectforeground="purple", highlightbackground="black")
songBox.pack(pady=4)




# entry: take numbers for skipbackwar, skipforward & spead butons 
Label(window, text="  ", fg="black", bg="black").pack(side="left", padx=3)

Label(window, text="skip :", bg="black", fg="white").pack(side="left", padx=5)
en1 = Entry(window, bg="black", fg="#c63939", width=6)
en1.pack(padx=2, pady=4, side="left")

Label(window, text="  ", fg="black", bg="black").pack(side="left", padx=40)

Label(window, text="speed :", bg="black", fg="white").pack(side="left", padx=5)
en2 = Entry(window, bg="black", fg="#c63939", width=6)
en2.pack(padx=2, pady=4, side="left")

Button(window, image=speedbutton, width=5, height=6, bg="black").pack(padx=3,pady=1, side="left")


# menu for speed option and take music files
menubar = Menu(window, background='black', fg="gray")
window.config(menu= menubar)

options = Menu(menubar, tearoff=0, background="black", fg="gray")
options.add_command(label="Add files", command=add_song)
options.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="File", menu=options)







window.mainloop()
