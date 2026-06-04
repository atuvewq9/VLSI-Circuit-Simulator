from tkinter import *


def submit_button_A():
    if x.get() == -1:
        result_A.config(text="Please select an input")
        return

    result_A.config(text=f"{x.get()}")
    radiobutton_0.place_forget()
    radiobutton_1.place_forget()
    submit_buttonA.place_forget()
    btn_submit_B.place(x=1280, y=500)
    label_B.place(x=1100, y=300)
    radiobutton_B0.place(x=1280, y=300)
    radiobutton_B1.place(x=1280, y=400)

def submit_button_B():
    if y.get() == -1:
        result_B.config(text="Please select an input")
        return

    result_B.config(text=f"{y.get()}")

    radiobutton_B0.place_forget()
    radiobutton_B1.place_forget()
    btn_submit_B.place_forget()
    rb_and.place(x=500, y=650)
    rb_or.place(x=700, y=650)
    rb_nand.place(x=900, y=650)
    rb_nor.place(x=1100, y=650)
    label_gate.place(x=700, y=500)
    btn_gate_submit.place(x=800, y=700)
window=Tk()

window.title("Simulator")


def submit_gate():

    gate = gate_var.get()

    if gate == "":
        result_gate.config(text="Select a gate")
        return

    A = x.get()
    B = y.get()

    if gate == "AND":
        output = A & B

    elif gate == "OR":
        output = A | B

    elif gate == "NAND":
        output = int(not (A & B))

    elif gate == "NOR":
        output = int(not (A | B))

    result_gate.config(
        text=f"{gate} Output = {output}"
    )
    rb_and.place_forget()
    rb_or.place_forget()
    rb_nand.place_forget()
    rb_nor.place_forget()

    btn_gate_submit.place_forget()
    label_gate.place_forget()
    result_gate.config(text=f"{gate} Output = {output}")

    rb_and.place_forget()
    rb_or.place_forget()
    rb_nand.place_forget()
    rb_nor.place_forget()

    btn_gate_submit.place_forget()
    label_gate.place_forget()

    btn_reset.place(x=900, y=700)
    result_gate.place(x=900, y=650)
    result_gate.config(text=f"{gate} Output = {output}")
def reset_simulator():

    x.set(-1)
    y.set(-1)
    gate_var.set("")

    result_A.config(text="")
    result_B.config(text="")
    result_gate.config(text="")


    label_A.place(x=600,y=300)
    radiobutton_0.place(x=800,y=300)
    radiobutton_1.place(x=800,y=400)
    submit_buttonA.place(x=800,y=500)


    label_B.place_forget()
    radiobutton_B0.place_forget()
    radiobutton_B1.place_forget()
    btn_submit_B.place_forget()

    rb_and.place_forget()
    rb_or.place_forget()
    rb_nand.place_forget()
    rb_nor.place_forget()
    btn_gate_submit.place_forget()
    label_gate.place_forget()


    result_gate.place_forget()
    btn_reset.place_forget()

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
label_gate = Label(window,
                   text="Select Gate",
                   font=("Arial",25),
                   fg="white",
                   bg="blue")

label_gate.place(x=700,y=500)
label_gate.place_forget()
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
                      command=submit_button_A

                    )
submit_buttonA.place(x=800,y=500)

btn_submit_B = Button(window,
                      text="Submit B",
                      font=("Arial",25),
                      fg="white",
                      bg="blue",
                      command=submit_button_B)

btn_submit_B.place(x=800,y=600)
btn_submit_B.place_forget()


gate_var = StringVar(value="")
rb_and = Radiobutton(window,
                     text="AND",
                     variable=gate_var,
                     value="AND",
                     font=("Arial",25),
                     fg="white",
                     bg="pink",
                    )


rb_or = Radiobutton(window,
                    text="OR",
                    variable=gate_var,
                    value="OR",
                    font=("Arial",25),
                    fg="white",
                    bg="pink",
                   )


rb_nand = Radiobutton(window,
                      text="NAND",
                      variable=gate_var,
                      value="NAND",
                      font=("Arial",25),
                      fg="white",
                      bg="pink",
                     )


rb_nor = Radiobutton(window,
                     text="NOR",
                     variable=gate_var,
                     value="NOR",
                     font=("Arial",25),
                     fg="white",
                     bg="pink",

                )
rb_and.place(x=550,y=600)
rb_or.place(x=700,y=600)
rb_nand.place(x=850,y=600)
rb_nor.place(x=1050,y=600)


rb_and.place_forget()
rb_or.place_forget()
rb_nand.place_forget()
rb_nor.place_forget()
btn_gate_submit = Button(window,
                         text="Submit Gate",
                         font=("Arial",20),
                         bg="blue",
                         fg="white",
                         command=submit_gate)


btn_gate_submit.place_forget()
result_gate = Label(window,
                    text="",
                    font=("Arial",25),
                    fg="white",
                    bg="green",)

result_gate.place(x=900,y=650)

btn_gate_submit.place_forget()
btn_reset = Button(window,
                   text="Reset",
                   font=("Arial",20),
                   fg="white",
                   bg="red",
                   command=reset_simulator)


btn_reset.place_forget()
window.mainloop()
