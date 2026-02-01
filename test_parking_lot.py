from parking_lot import ParkingLot, Vehicle


def test_basic_parking_flow():
    lot = ParkingLot(2)

    car1 = Vehicle("KA-01")
    car2 = Vehicle("KA-02")

    spot1 = lot.park_vehicle(car1)
    assert spot1 == 0

    spot2 = lot.park_vehicle(car2)
    assert spot2 == 1

    assert lot.available_spots() == 0


def test_remove_vehicle():
    lot = ParkingLot(1)
    car = Vehicle("KA-03")

    lot.park_vehicle(car)
    lot.remove_vehicle("KA-03")

    assert lot.available_spots() == 1


def test_parking_when_full():
    lot = ParkingLot(1)
    lot.park_vehicle(Vehicle("KA-04"))

    try:
        lot.park_vehicle(Vehicle("KA-05"))
        assert False, "Expected exception when parking full lot"
    except ValueError:
        assert True


def test_duplicate_vehicle():
    lot = ParkingLot(1)
    car = Vehicle("KA-06")

    lot.park_vehicle(car)

    try:
        lot.park_vehicle(car)
        assert False, "Expected exception for duplicate parking"
    except ValueError:
        assert True
