from BANK import details

def test_bank_details():
    assert details("Rahul", 100000, "50000", "5000") == 145000

def test_bank_details_1():
    assert details("Rohit", 100000, "40000", "4000") == 145000

