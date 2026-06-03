from tkinter import *

def submit_buttonA():
    if x.get() == -1:
        result_A.config(text="Please select an input")
        return

    result_A.config(text=f"{x.get()}")

    radiobutton_0.destroy()
    radiobutton_1.destroy()
    submit_buttonA.destroy()
    btn_submit_B.place(x=1280, y=500)
    label_B.place(x=1100, y=300)
    radiobutton_B0.place(x=1280, y=300)
    radiobutton_B1.place(x=1280, y=400)

def submit_buttonB():
    if y.get() == -1:
        result_B.config(text="Please select an input")
        return

    result_B.config(text=f"{y.get()}")

    radiobutton_B0.destroy()
    radiobutton_B1.destroy()
    btn_submit_B.destroy()
window=Tk()
window.title("Simulator")

label=Label(window,
            text="VLSI Logic Gate Simulator",
            font=("Arial", 25),
            fg="white",
            bg="blue",
            padx=10,
            pady=10)
label.pack()
label_A=Label(window, text="Input A =",
          font=("Arial", 25),
          fg="white",
          bg="pink",
          padx=10,
          pady=10,
         )
label_A.place(x=600,y=300)
result_A = Label(window,
                 text="",
                 font=("Arial",30),
                 fg="black",
                bg="light grey",)
result_A.place(x=850,y=300)
result_B = Label(window,
                 text="",
                 font=("Arial",30),
                 fg="black",
                 bg="light grey",)
result_B.place(x=1400,y=300)
label_B = Label(window, text="Input B =",
                font=("Arial", 25),
                  fg="white",
                bg="pink",
                padx=10,
                pady=10,
                )
label_B.place(x=1100,y=300)
x = IntVar(value=-1)
radiobutton_0=Radiobutton(window, text="0",
                          font=("Arial", 25),
                          value=0,
                          fg="white",
                          bg="green",
                           variable = x
                    )
radiobutton_0.place(x=800,y=300)
radiobutton_1=Radiobutton(window, text="1",
                          font=("Arial", 25),
                          value=1,
                          fg="white",
                          bg="green",
                          variable=x)
radiobutton_1.place(x=800,y=400)
y= IntVar(value=-1)
radiobutton_B0 = Radiobutton(window,
                             text="0",
                             font=("Arial", 25),
                             fg="white",
                             bg="green",
                             variable=y,
                             value=0)
radiobutton_B0.place(x=1280,y=300)

radiobutton_B1 = Radiobutton(window,
                             text="1",
                             font=("Arial", 25),
                             fg="white",
                             bg="green",
                             variable=y,
                             value=1)
radiobutton_B1.place(x=1280,y=400)


label_B.place_forget()
radiobutton_B0.place_forget()
radiobutton_B1.place_forget()

submit_buttonA=Button(window, text="Submit",
                     font=("Arial", 25),

                     fg="white",
                     bg="blue",
                      command=submit_buttonA

                    )
submit_buttonA.place(x=800,y=500)

btn_submit_B = Button(window,
                      text="Submit B",
                      font=("Arial",25),
                      fg="white",
                      bg="blue",
                      command=submit_buttonB)

btn_submit_B.place(x=800,y=600)
btn_submit_B.place_forget()

window.mainloop()
