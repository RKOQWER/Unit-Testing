import maths
import pytest
import sys

@pytest.mark.skip(reason="I dont want to execute this test")
def test_calc_total():

    total=maths.calc_total(4,5)

    assert total==9

@pytest.mark.skipif(sys.version_info<(3,6), reason="Old version")
def test_calc_multiplication():

    # Skip this test if python version below 3.6  (written as (3.6))

    total=maths.calc_multiplication(4,5)

    assert total==20

