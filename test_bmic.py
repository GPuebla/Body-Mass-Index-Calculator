import pytest
from pytest import approx
from bmic import calculate_BMI, select_porcentile_range, convert_feet_inches_to_cm,convert_pounds_to_kg,get_bmi_list_csv

def test_calculate_BMI():
    assert calculate_BMI(173, 74) == approx(24,72)
    assert calculate_BMI(180, 50) == approx(15,43)
    assert calculate_BMI(80, 15) == approx(23,43)
    assert calculate_BMI(80, 5) == approx(7,812)

list_example_1 = [13.488,14.814,16.14,17.802,19.96,22.903,27.21,34.275,41.341]
list_example_2 = [14.01,15.534,17.059,18.944,21.34,24.494,28.85,35.287,41.724]
list_example_3 = [14.153,15.834,17.515,19.564,22.114,25.366,29.646,35.512,41.378]
list_example_4 = [14,16,17,18.5,20,25,30,35,40]
list_example_5 = [13.036,14.73,16.424,18.525,21.194,24.691,29.455,36.296,43.137]
list_example_6 = [10.758,11.74,12.721,13.907,15.372,17.231,19.68,23.071,26.461]

def test_select_porcentile_range():

    assert select_porcentile_range(list_example_1,41.350) == 9
    assert select_porcentile_range(list_example_2,17) == 3
    assert select_porcentile_range(list_example_3,29.646) == 7
    assert select_porcentile_range(list_example_4,25) == 6
    assert select_porcentile_range(list_example_5,13) == 1
    assert select_porcentile_range(list_example_6,12) == 3

def test_convert_feet_inches_to_cm():
    assert convert_feet_inches_to_cm(5,10) == approx(177,8)
    assert convert_feet_inches_to_cm(3,0) == approx(91,44)
    assert convert_feet_inches_to_cm(7,8) == approx(233,68)
    assert convert_feet_inches_to_cm(1,6) == approx(45,72)
    assert convert_feet_inches_to_cm(0,10) == approx(25,4)

def test_convert_pounds_to_kg():
    assert convert_pounds_to_kg(100) == approx(45,35)
    assert convert_pounds_to_kg(10) == approx(4,535)
    assert convert_pounds_to_kg(290) == approx(131,54)
    assert convert_pounds_to_kg(6) == approx(2,721)
    assert convert_pounds_to_kg(120) == approx(54,431)

def test_get_bmi_list_csv():
    file1 = "bmi-boys.csv"
    file2 = "bmi-girls.csv"

    list73_boys = [11.249,12.148,13.047,14.09,15.317,16.78,18.554,20.751,22.948]
    list109_boys = [11.647,12.578,13.508,14.646,16.078,17.952,20.54,24.426,28.312]

    list73_girls = [10.745,11.722,12.699,13.863,15.276,17.029,19.264,22.217,25.17]
    list109_girls = [11.075,12.12,13.165,14.465,16.136,18.381,21.599,26.692,31.786]

    assert get_bmi_list_csv(file1,"73") == list73_boys
    assert get_bmi_list_csv(file2,"73") == list73_girls
    assert get_bmi_list_csv(file1,"109") == list109_boys
    assert get_bmi_list_csv(file2,"109") == list109_girls
    

pytest.main(["-v", "--tb=line", "-rN", __file__])