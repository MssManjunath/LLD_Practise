def test_parking_lot():
    lot = ParkingLot(2)

    s1 = lot.park("KA-01")
    assert s1 == 0

    s2 = lot.park("KA-02")
    assert s2 == 1

    assert lot.available_spots() == 0

    lot.remove("KA-01")
    assert lot.available_spots() == 1


def test_parking_full():
    lot = ParkingLot(1)
    lot.park("KA-03")

    try:
        lot.park("KA-04")
        assert False
    except ValueError:
        pass
