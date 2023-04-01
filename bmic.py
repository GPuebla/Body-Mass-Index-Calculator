import tkinter as tk
from tkinter.ttk import *
from tkinter import Frame, Label, Button

from number_entry import IntEntry, FloatEntry

from datetime import datetime
from dateutil import relativedelta

import csv

x = 0

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
    lbl_age = Label(frm_main, text="year month:")
    lbl_age.grid(row=1, column=0)
    # ent_age = IntEntry(frm_main, width=15, lower_bound=2, upper_bound=120)
    # ent_age.grid(row=1, column=1)
    lbl_age_range = Label(frm_main, text="birth month:")
    lbl_age_range.grid(row=1, column=2)
    
    # Creat a combobox that display the months of year
    comb_months = Combobox(frm_main, width=4 )
    comb_months["values"] = (' ','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    comb_months.grid(row=1, column=3)

    comb_years = Combobox(frm_main, width=4 )
    comb_years["values"] = ("",1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023)
    comb_years.grid(row=1, column=1)


    # Creat a section witch show the leabel "Gender" and get the gender of the user.
    lbl_gender = Label(frm_main, text="Gender" )
    lbl_gender.grid(row=2, column=0)
    rad1 = Radiobutton(frm_main, text="Male", value= 1)
    rad1.grid(row=2, column=1)
    rad2 = Radiobutton(frm_main, text="Famale", value= 2)
    rad2.grid(row=2, column=2)

    lbl_height = Label(frm_main, text="Height" )
    lbl_height.grid(row=3, column=0)
    ent_height = FloatEntry(frm_main, width=15, lower_bound=0, upper_bound=2000)
    ent_height.grid(row=3, column=1)
    lbl_height_unit = Label(frm_main, text="cm")
    lbl_height_unit.grid(row=3, column=2)

    lbl_Weight = Label(frm_main, text="Weight" )
    lbl_Weight.grid(row=4, column=0)
    ent_Weight = FloatEntry(frm_main, width=15, lower_bound=60, upper_bound=2000)
    ent_Weight.grid(row=4, column=1)
    lbl_Weight_unit = Label(frm_main, text="kg")
    lbl_Weight_unit.grid(row=4, column=2)

    ent_height2 = FloatEntry(frm_main, width=7, lower_bound=0, upper_bound=200)
    lbl_height2_unit = Label(frm_main, text="inches")

    lbl_result = Label(frm_main, text="----TEST_RESULT----")
    lbl_result.grid(row=5, column=1)


    btn_calculate = Button(frm_main, text="Calculate", background= "green")
    btn_calculate.grid(row=6, column=1)
    btn_clear = Button(frm_main, text="Clear", background= "gray")
    btn_clear.grid(row=6, column=2)

    def calculate_BMI(height,weight):

        result = weight / (height/100)**2
        return result
    
    def convert_feet_inches_to_cm(feet, inches):
        result_cm = (feet * 0.3048 + inches * 0.0254)*100
        return result_cm
    
    def convert_pounds_to_kg(pounds):
        result_kg = pounds * 0.45359237
        return result_kg
    
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_height.clear()
        ent_height2.clear()
        ent_Weight.clear()
        comb_months.current(0)
        comb_years.current(0)

    def calculate():
        units = comb.get()
        
        if units == "Metric":
            height = ent_height.get()
            weight = ent_Weight.get()
        elif units == "Us":
            feet = ent_height.get()
            inches = ent_height2.get()
            pounds = ent_Weight.get()

            height = convert_feet_inches_to_cm(feet,inches)
            weight = convert_pounds_to_kg(pounds)

        test_gender = rad1.get()
        result = calculate_BMI(height, weight)
        lbl_result.config(text= f'{result:0.2f} kg/m2')
        
    def callbackFunc(event):
        unit = event.widget.get()

        if unit == "Metric":
                        
            lbl_height_unit.config(text="cm")
            lbl_Weight_unit.config(text="kg")

            ent_height2.grid_forget()
            lbl_height2_unit.grid_forget()

        elif unit == "Us":

            ent_height2.config(width=7)
            lbl_height2_unit.config(text="inches")

            lbl_height_unit.config(text="feet")
            lbl_Weight_unit.config(text="pounds")

            ent_height2.grid(row=3, column=3)
            lbl_height2_unit.grid(row=3, column=4)

    btn_clear.config(command=clear)
    btn_calculate.config(command=calculate) 

    comb.current()
    comb.bind("<<ComboboxSelected>>", callbackFunc)

def read_dictionary(filename, index):
        """Read the contents of a CSV file and return a list.

        Parameters
            filename: the name of the CSV file to read.
            
        Return: a list with the values of de index month
        """
        bmi_percentils = []

        
        with open(filename, "rt") as csv_file:

            reader = csv.reader(csv_file)
            next(reader)
            
            for row_list in reader:
                if row_list[0] == index:
                    for n in row_list[1:]:
                        bmi_percentils.append(float(n))

        return bmi_percentils



if __name__ == "__main__":
    main()
