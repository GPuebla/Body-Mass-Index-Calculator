from bmic import calculate_BMI, convert_feet_inches_to_cm, convert_pounds_to_kg, calculate_total_months, calculate_BMI_status, select_porcentile_range, get_bmi_list_csv
from os import path
from pytest import approx
import pytest

def test_calculate_BMI():
    assert calculate_BMI(173, 74) == approx(24,72)
    assert calculate_BMI(180, 50) == approx(15,43)
    assert calculate_BMI(80, 15) == approx(23,43)
    assert calculate_BMI(80, 5) == approx(7,812)

# def test_cels_from_fahr():
  
#     assert cels_from_fahr(-25) == approx(-31.66667)
#     assert cels_from_fahr(0) == approx(-17.77778)
#     assert cels_from_fahr(32) == approx(0)
#     assert cels_from_fahr(70) == approx(21.1111)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])