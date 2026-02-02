"""
INTERVIEW QUESTION: DESIGN A SIMPLE PARKING LOT

Time Limit:
-----------
30 minutes total
- 20 minutes: implement the solution
- 10 minutes: write tests + explain trade-offs

Problem Description:
--------------------
Design a simple parking lot system.

The parking lot:
- Has a fixed number of parking spots
- Supports only cars
- Assigns the FIRST available spot to a car
- Spot numbering starts from 0

You must implement the ParkingLot class below.

Rules & Constraints:
--------------------
1. A car cannot be parked more than once
2. If the parking lot is full, park() must raise an exception
3. If remove() is called for a car that is not parked, raise an exception
4. License plate is a non-empty string
5. You may choose any internal data structures

Performance Expectations:
-------------------------
- park()      → O(N) or better
- remove()    → O(1)
- available_spots() → O(1) or O(N)

(Explain how you would optimize park() to O(1) if asked)

Example Usage:
--------------
# lot = ParkingLot(2)
# lot.park("KA-01")      # returns 0
# lot.park("KA-02")      # returns 1
# lot.available_spots()  # returns 0
# lot.remove("KA-01")
# lot.available_spots()  # returns 1
# lot.park("KA-03")      # returns 0

What We Are Evaluating:
----------------------
- Clarity of design
- Correctness of logic
- Edge case handling
- Test coverage
- Ability to explain trade-offs
"""

class ParkingLot:
    def __init__(self, total_spots: int):
        pass

    def park(self, license_plate: str) -> int:
        """
        Parks a car and returns the allocated spot number.
        """
        pass

    def remove(self, license_plate: str) -> None:
        """
        Removes the given car from the parking lot.
        """
        pass

    def available_spots(self) -> int:
        """
        Returns the number of free parking spots.
        """
        pass



class ParkingLot:
    def __init__(self, total_spots: int):
        pass

    def park(self, license_plate: str) -> int:
        """
        Parks a car.
        Returns the spot number.
        """
        pass

    def remove(self, license_plate: str) -> None:
        pass

    def available_spots(self) -> int:
        pass
