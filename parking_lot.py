from typing import Dict, Optional


class Vehicle:
    def __init__(self, license_plate: str) -> None:
        if not license_plate:
            raise ValueError("License plate cannot be empty.")
        self.license_plate = license_plate


class ParkingSpot:
    def __init__(self, spot_id: int) -> None:
        self.spot_id = spot_id
        self.vehicle: Optional[Vehicle] = None

    def is_free(self) -> bool:
        # TODO: return True if no vehicle is parked
        pass

    def park(self, vehicle: Vehicle) -> None:
        # TODO:
        # 1. If spot is occupied -> raise ValueError
        # 2. Else assign vehicle
        pass

    def remove_vehicle(self) -> None:
        # TODO:
        # 1. If spot is empty -> raise ValueError
        # 2. Else remove vehicle
        pass


class ParkingLot:
    def __init__(self, total_spots: int) -> None:
        if total_spots <= 0:
            raise ValueError("Total spots must be > 0")

        self.spots = [ParkingSpot(i) for i in range(total_spots)]
        self.parked_vehicles: Dict[str, ParkingSpot] = {}

    def park_vehicle(self, vehicle: Vehicle) -> int:
        # TODO:
        # 1. If vehicle already parked -> raise ValueError
        # 2. Find first free spot
        # 3. Park vehicle
        # 4. Track it in parked_vehicles
        # 5. Return spot_id
        pass

    def remove_vehicle(self, license_plate: str) -> None:
        # TODO:
        # 1. If vehicle not found -> raise ValueError
        # 2. Remove vehicle from its spot
        # 3. Delete from parked_vehicles
        pass

    def available_spots(self) -> int:
        # TODO: return number of free spots
        pass
