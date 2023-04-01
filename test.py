from datetime import datetime
from dateutil import relativedelta
import csv

# # get two dates
# d1 = '1/3/2019'
# d2 = '16/3/2022'

# today = datetime.today()

# day = today.day
# month = today.month
# year = today.year

# str_today = f"{day}/{month}/{year}"

# d2 = str_today

# # convert string to date object
# start_date = datetime.strptime(d1, "%d/%m/%Y")
# end_date = datetime.strptime(d2, "%d/%m/%Y")

# # Get the relativedelta between two dates
# delta = relativedelta.relativedelta(end_date, start_date)
# print('Years, Months, Days between two dates is')
# print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
# print(str_today)

# def test_funcrion(rate):
#     dates = []
#     years_to_show = rate
#     current_year = datetime.today().year
#     starting_date = current_year - years_to_show + 1

#     for x in range (years_to_show):
#         dates.append(starting_date)
#         starting_date += 1

#     return dates

# years = test_funcrion(120)

# print(years)

# def read_dictionary(filename, index):
#     """Read the contents of a CSV file and return a list.

#     Parameters
#         filename: the name of the CSV file to read.
        
#     Return: a list with the values of de index month
#     """
#     bmi_percentils = []

    
#     with open(filename, "rt") as csv_file:

#         reader = csv.reader(csv_file)
#         next(reader)
        
#         for row_list in reader:
#             if row_list[0] == index:
#                 for n in row_list[1:]:
#                     bmi_percentils.append(float(n))


#     return bmi_percentils

# x = read_dictionary("bmi-girls.csv","120")

# print(x)

# def creat_lis_of_years(range_year):
#         """ Range: years taht you want to show """
#         dates = []
#         years_to_show = range_year
#         current_year = datetime.today().year
#         starting_date = current_year - years_to_show + 1

#         for x in range (years_to_show):
#             dates.append(starting_date)
#             starting_date += 1

#         return dates