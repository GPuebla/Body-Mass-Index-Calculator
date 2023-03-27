import tkinter as tk
from tkinter.ttk import *
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Body Mass Index Calculator")
    frm_main.pack(padx=6, pady=4, fill=tk.BOTH, expand=1)

    # Call the main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.

    main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def main_window(frm_main):
    # Create a labels that displays texts
    lbl_unit = Label(frm_main, text="Unit" )
    lbl_unit.grid(row=0, column=0)

    # Creat a combobox that display two options of units
    comb = Combobox(frm_main)
    comb["values"] = ("Metric","Us")
    comb.current(0)
    comb.grid(row=0, column=1)

    # Creat a section witch show the leabel "Age" and get the years of the user.
    lbl_age = Label(frm_main, text="Age")
    lbl_age.grid(row=1, column=0)
    ent_age = IntEntry(frm_main, width=15, lower_bound=2, upper_bound=120)
    ent_age.grid(row=1, column=1)
    lbl_age_range = Label(frm_main, text="ages: 2 - 120")
    lbl_age_range.grid(row=1, column=2)

    # Creat a section witch show the leabel "Gender" and get the gender of the user.
    lbl_gender = Label(frm_main, text="Gender" )
    lbl_gender.grid(row=2, column=0)
    rad1 = Radiobutton(frm_main, text="Male", value=1)
    rad1.grid(row=2, column=1)
    rad2 = Radiobutton(frm_main, text="Famale", value=2)
    rad2.grid(row=2, column=2)


    lbl_height = Label(frm_main, text="Height" )
    lbl_height.grid(row=3, column=0)
    ent_height = FloatEntry(frm_main, width=15, lower_bound=60, upper_bound=2000)
    ent_height.grid(row=3, column=1)
    lbl_height_unit = Label(frm_main, text="cm")
    lbl_height_unit.grid(row=3, column=2)

    lbl_Weight = Label(frm_main, text="Weight" )
    lbl_Weight.grid(row=4, column=0)
    ent_Weight = FloatEntry(frm_main, width=15, lower_bound=60, upper_bound=2000)
    ent_Weight.grid(row=4, column=1)
    lbl_Weight_unit = Label(frm_main, text="kg")
    lbl_Weight_unit.grid(row=4, column=2)


    btn_calculate = Button(frm_main, text="Calculate", background= "green")
    btn_calculate.grid(row=5, column=1)
    btn_clear = Button(frm_main, text="Clear", background= "gray")
    btn_clear.grid(row=5, column=2)

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_age.clear()
        ent_height.clear()
        ent_Weight.clear()
        ent_age.focus()


    btn_clear.config(command=clear)

if __name__ == "__main__":
    main()