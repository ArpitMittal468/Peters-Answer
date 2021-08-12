import tkinter as tk
import threading
from time import sleep


main = tk.Tk()
main.title("Peter Answers")
WIDTH = 600
HEIGHT = 600
main.resizable(False, False)
main.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, (main.winfo_screenwidth() - WIDTH) // 2,
                                   (main.winfo_screenheight() - HEIGHT) // 2 - 50))
main.config(bg="#fff")
main.wm_iconbitmap("favicon.ico")

string1 = "Peter Please Answer The Following Question "
counter = 0

HIDDENSTATE = False
HIDDENCODE = []

goback=0
answerlabel=0


def keypressed(self):
    global counter, HIDDENSTATE
    temp = counter
    try:
        aa = self.char
        if aa == ".":
            if not HIDDENSTATE:
                HIDDENSTATE = True
            else:
                HIDDENSTATE = False
                pettionentry.delete(counter)
                pettionentry.insert(tk.END, string1[temp])
                HIDDENCODE.append(" ")

        keycode = ord(aa)
        if keycode in (9, 27, 13): pass

        elif keycode != 8:
            if counter >= 43: temp = 42
            if HIDDENSTATE:
                pettionentry.delete(counter)
                pettionentry.insert(tk.END, string1[temp])
                if aa != ".":
                    HIDDENCODE.append(aa)
            else:
                HIDDENCODE.append(" ")
            counter += 1
        else:
            if counter <= 0:
                HIDDENSTATE = False
                counter = 1
            counter -= 1
            HIDDENCODE.pop(counter)
    except (TypeError, IndexError):
        pass
    #print(HIDDENCODE)


def strartthread(self):
    threading.Thread(target=keypressed, args=(self,), name="Thread-1").start()


def overlabel1(self):
    text1.config(fg="#a40000")
    questionlabel.config(bg="#a40000")
    text2.config(fg="grey")
    if pettionlabel["bg"] != "grey":
        pettionlabel["bg"] = "grey"
    #pettionentry.place(relwidth=1, relheight=0.95)


def overlabel2(self):
    text1.config(fg="grey")
    if questionlabel["bg"] != "grey":
        questionlabel["bg"] = "grey"
    text2.config(fg="#a40000")
    pettionlabel.config(bg="#a40000")


def unpack():
    global goback, HIDDENSTATE, counter, questionentry, pettionentry, HIDDENCODE
    counter = 0
    HIDDENSTATE = False
    goback.pack_forget()
    for i in range(8):
        sleep(0.03)
        answerlabel["height"] -= 1
    answerlabel.pack_forget()

    text1.pack(pady=(60, 2))
    questionlabel.pack(pady=(0, 30))
    text2.pack(pady=(0, 2))
    pettionlabel.pack()
    askbutton.pack(pady=(40, 0))
    questionentry.delete(0, tk.END)
    pettionentry.delete(0, tk.END)
    HIDDENCODE = []


def askclicked():
    global goback, answerlabel
    stat1 = questionentry.get()
    stat2 = pettionentry.get()
    answer = "".join(HIDDENCODE).strip()
    # print("{", stat1, "}")
    # print("{", stat2, "}")
    # print("{", answer, "}")
    # print()
    #askbutton["state"] = tk.DISABLED
    text1.pack_forget()
    questionlabel.pack_forget()
    pettionlabel.pack_forget()
    text2.pack_forget()
    askbutton.pack_forget()

    answerlabel = tk.Label(main, bd=0, bg="#a40000", fg="#fff", font=("Sans-serif", 20, "bold"), anchor=tk.CENTER,
                           height=1, wrap=WIDTH - 100)
    answerlabel.pack(fill=tk.X)

    if stat1 == "":
        answerlabel["text"] = "You must enter a valid question."
    elif stat2.title().strip() not in ["Peter Please Answer The Following Question", "Peter Please Answer"]:
        answerlabel["text"] = "The way in which you are making the petition is incorrect, please ask for help."
    else:
        if answer != "":
            answerlabel["text"] = answer.title()
        else:
            answerlabel["text"] = "I'm not answering that question."

    for i in range(8):
        sleep(0.03)
        answerlabel["height"] += 1

    goback = tk.Button(main, text="BACK", command=newthread2, fg="#fff", bg="#a40000", activebackground="#fff",
                       activeforeground="#a40000", bd=0, height=1, width=8, font=("Sans-serif", 16))
    goback.pack(pady=(40, 0))


def newthread():
    thread2 = threading.Thread(target=askclicked, daemon=True, name="Thread-2")
    thread2.start()


def newthread2():
    thread2 = threading.Thread(target=unpack, daemon=True, name="Thread-3")
    thread2.start()


logo = tk.PhotoImage(file="peter-answers-logo.png")
upperlabel = tk.Label(main, bg="#a40000", image=logo, height=150)
upperlabel.pack(fill="both")


text1 = tk.Label(main, fg="grey",  bg="#fff", width=35, bd=0, text="Question: ", anchor=tk.W, font=("Sans-serif", 18))
text1.pack(pady=(60, 2))

questionlabel = tk.Label(main, bg="grey", width=70, height=3, bd=0)
questionlabel.pack(pady=(0, 30))
questionentry = tk.Entry(questionlabel, bd=0, font=("Sans-serif", 15))
questionentry.place(relwidth=1, relheight=0.95)


text2 = tk.Label(main, fg="grey",  bg="#fff", width=35, bd=0, text="Petition: ", anchor=tk.W, font=("Sans-serif", 18))
text2.pack(pady=(0, 2))

pettionlabel = tk.Label(main, bg="grey", width=70, height=3, bd=0)
pettionlabel.pack()
pettionentry = tk.Entry(pettionlabel, bd=0, font=("Sans-serif", 15))
pettionentry.place(relwidth=1, relheight=0.95)


askbutton = tk.Button(main, text="ASK", command=newthread, fg="#fff", bg="#a40000", activebackground="#fff",
                      activeforeground="#a40000", bd=0, height=1, width=8, font=("Sans-serif", 16))

askbutton.pack(pady=(40, 0))

pettionentry.bind("<Key>", strartthread)
questionentry.bind("<Button-1>", overlabel1)
pettionentry.bind("<Button-1>", overlabel2)


main.mainloop()
