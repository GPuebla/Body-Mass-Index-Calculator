import tkinter as tk
from tkinter.ttk import *
from tkinter import Frame, Label, Button, IntVar

from number_entry import IntEntry, FloatEntry

from datetime import datetime

import csv


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
    lbl_age = Label(frm_main, text="Birth year")
    lbl_age.grid(row=1, column=0)
    # ent_age = IntEntry(frm_main, width=15, lower_bound=2, upper_bound=120)
    # ent_age.grid(row=1, column=1)
    lbl_age_range = Label(frm_main, text="birth month:")
    lbl_age_range.grid(row=1, column=2)
    
    # Creat a combobox that display the months of year
    comb_months = Combobox(frm_main, width=4 )
    comb_months["values"] = (' ','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    comb_months.grid(row=1, column=3)

    # Creat a combobox that display the last 120 years.
    comb_years = Combobox(frm_main, width=4 )
    comb_years["values"] = ("",1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018)
    comb_years.grid(row=1, column=1)

    # Creat a section witch show the  "Gender" and get the gender of the user.
    lbl_gender = Label(frm_main, text="Gender" )
    lbl_gender.grid(row=2, column=0)
    radio = IntVar()  
    rad1 = Radiobutton(frm_main, variable= radio, text="Male", value= 1)
    rad1.grid(row=2, column=1)
    rad2 = Radiobutton(frm_main, variable= radio, text="Famale", value= 2)
    rad2.grid(row=2, column=2)

    lbl_height = Label(frm_main, text="Height" )
    lbl_height.grid(row=3, column=0)
    ent_height = FloatEntry(frm_main, width=15, lower_bound=0, upper_bound=2000)
    ent_height.grid(row=3, column=1)
    lbl_height_unit = Label(frm_main, text="cm")
    lbl_height_unit.grid(row=3, column=2)

    lbl_Weight = Label(frm_main, text="Weight" )
    lbl_Weight.grid(row=4, column=0)
    ent_Weight = FloatEntry(frm_main, width=15, lower_bound=0, upper_bound=400)
    ent_Weight.grid(row=4, column=1)
    lbl_Weight_unit = Label(frm_main, text="kg")
    lbl_Weight_unit.grid(row=4, column=2)

    ent_height2 = FloatEntry(frm_main, width=7, lower_bound=0, upper_bound=300)
    lbl_height2_unit = Label(frm_main, text="inches")

    lbl_result = Label(frm_main, text=" ")
    lbl_result.grid(row=6, column=1)


    btn_calculate = Button(frm_main, text="Calculate", background= "green")
    btn_calculate.grid(row=9, column=1)

    btn_clear = Button(frm_main, text="Clear", background= "gray")
    btn_clear.grid(row=9, column=2)

    
     
        

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_height.clear()
        ent_height2.clear()
        ent_Weight.clear()
        comb_months.current(0)
        comb_years.current(0)

        lbl_result.config(text="")


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
        
        m = comb_months.current()
        y = int(comb_years.get())

        gender = radio.get()
        t_months = calculate_total_months(y,m)

        result = calculate_BMI(height, weight)
        status = calculate_BMI_status(t_months,gender,result)
        
        
        lbl_result.config(text= f'{result:0.2f} kg/m2 {t_months} Status:{status}')



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


def calculate_BMI(height,weight):

        result = weight / (height/100)**2

        return result

def select_porcentile_range(list_bmi_ranges, bmi):

        range1 = list_bmi_ranges[0]
        range2 = list_bmi_ranges[1]
        range3 = list_bmi_ranges[2]
        range4 = list_bmi_ranges[3]
        range5 = list_bmi_ranges[4]
        range6 = list_bmi_ranges[5]
        range7 = list_bmi_ranges[6]
        range8 = list_bmi_ranges[7]
        range9 = list_bmi_ranges[8]

        if bmi <= range1 :
            return 1
        elif bmi > range1 and bmi <= range2:
            return 2
        elif bmi > range2 and bmi <= range3:
            return 3
        elif bmi > range3 and bmi <= range4:
            return 4
        elif bmi > range4 and bmi < range6:
            return 5
        elif bmi >= range6 and bmi < range7:
            return 6
        elif bmi >= range7 and bmi < range8:
            return 7
        elif bmi >= range8 and bmi < range9:
            return 8
        elif bmi >= range9:
            return 9

def convert_feet_inches_to_cm(feet, inches):
        result_cm = (feet * 0.3048 + inches * 0.0254)*100

        return result_cm
    
def convert_pounds_to_kg(pounds):
    result_kg = pounds * 0.45359237

    return result_kg

def calculate_total_months(birth_year,birth_month):
    current_month = datetime.today().month
    current_year = datetime.today().year
    total_months = (current_year - birth_year) * 12 - (birth_month - current_month )

    return total_months

def calculate_BMI_status(months, gender, bmi):
    
    status_list = ["Severe Thinness II","Severe Thinness I","Moderate Thinness","Mild Thinness","Normal","Overweight","Obese Class I","Obese Class II","Obese Class III"]

    adult_bmi_ranges = [14,16,17,18.5,20,25,30,35,40]


    if months > 61 and months <229:
        if gender == 1:
            bmi_range = get_bmi_list_csv("bmi-boys.csv",str(months))
            status = select_porcentile_range(bmi_range, bmi)
            status_text =status_list[status - 1]
            return status_text 

        elif gender == 2:
            bmi_range = get_bmi_list_csv("bmi-girls.csv",str(months))
            status = select_porcentile_range(bmi_range, bmi)
            status_text =status_list[status - 1]
            return status_text 
    
    elif months >= 229:
            status = select_porcentile_range(adult_bmi_ranges, bmi)
            status_text =status_list[status - 1]
            return status_text
    
def get_bmi_list_csv(filenam, index_bmi):
    bmi_ranges = []
    
    with open(filenam, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)
        
        for row_list in reader:
            if row_list[0] == index_bmi:
                for n in row_list[1:]:
                    bmi_ranges.append(float(n))

    return bmi_ranges
    

if __name__ == "__main__":
    main()
