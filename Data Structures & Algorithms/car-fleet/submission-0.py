class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = []
        for position, speed in cars:
            time_to_target = (target - position)/ speed
            fleets.append(time_to_target)

            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)