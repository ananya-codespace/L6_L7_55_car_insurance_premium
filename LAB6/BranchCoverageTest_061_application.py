
import pytest
from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout,
)


def test_unknown_car_type():
    with pytest.raises(ValueError, match="unknown car type"):
        annual_premium("truck", 30, 1, False)


def test_driver_too_young():
    with pytest.raises(ValueError, match="driver too young"):
        annual_premium("sedan", 17, 1, False)


def test_young_driver():
    assert annual_premium("hatchback", 20, 1, False) == 12000


def test_regular_age_driver():
    assert annual_premium("sedan", 30, 1, False) == 12000


def test_senior_driver():
    assert annual_premium("suv", 60, 1, False) == 17000


def test_zero_claims():
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_more_than_two_claims_with_anti_theft():
    assert annual_premium("sedan", 30, 3, True) == 23500


def test_negative_claim_free_years():
    with pytest.raises(ValueError, match="invalid years"):
        no_claim_bonus(-1)


def test_zero_claim_free_years():
    assert no_claim_bonus(0) == 0


def test_one_claim_free_year():
    assert no_claim_bonus(1) == 20


def test_three_claim_free_years():
    assert no_claim_bonus(3) == 35


def test_five_claim_free_years():
    assert no_claim_bonus(5) == 50


def test_negative_damage_cost():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(-1, 10000, 500, False)


def test_negative_deductible():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(5000, 10000, -1, False)


def test_total_loss():
    assert claim_payout(5000, 20000, 500, True) == 20000


def test_damage_equal_to_deductible():
    assert claim_payout(500, 10000, 500, False) == 0


def test_damage_below_deductible():
    assert claim_payout(300, 10000, 500, False) == 0


def test_payout_exceeds_insured_value():
    assert claim_payout(15000, 10000, 500, False) == 10000


def test_normal_claim_payout():
    assert claim_payout(5000, 10000, 500, False) == 4500
