
import pytest
from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout,
)


def test_annual_premium_sedan_no_claims():
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_annual_premium_young_driver():
    assert annual_premium("hatchback", 20, 1, False) == 12000


def test_annual_premium_senior_driver():
    assert annual_premium("suv", 65, 1, False) == 17000


def test_annual_premium_multiple_claims_with_anti_theft():
    assert annual_premium("sedan", 35, 3, True) == 23500


def test_annual_premium_unknown_car():
    with pytest.raises(ValueError, match="unknown car type"):
        annual_premium("truck", 30, 0, False)


def test_annual_premium_underage_driver():
    with pytest.raises(ValueError, match="driver too young"):
        annual_premium("sedan", 17, 0, False)


def test_no_claim_bonus_negative_years():
    with pytest.raises(ValueError, match="invalid years"):
        no_claim_bonus(-1)


def test_no_claim_bonus_five_years():
    assert no_claim_bonus(5) == 50


def test_no_claim_bonus_three_years():
    assert no_claim_bonus(3) == 35


def test_no_claim_bonus_one_year():
    assert no_claim_bonus(1) == 20


def test_no_claim_bonus_zero_years():
    assert no_claim_bonus(0) == 0


def test_claim_payout_negative_damage():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(-1, 10000, 500, False)


def test_claim_payout_negative_deductible():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(5000, 10000, -1, False)


def test_claim_payout_total_loss():
    assert claim_payout(5000, 20000, 500, True) == 20000


def test_claim_payout_below_deductible():
    assert claim_payout(500, 10000, 500, False) == 0


def test_claim_payout_above_insured_value():
    assert claim_payout(15000, 10000, 500, False) == 10000


def test_claim_payout_normal():
    assert claim_payout(5000, 10000, 500, False) == 4500
