class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(zip(position, speed), reverse = True)
        stack = []
        for position, speed in car:
            time = (target - position) / speed
            if stack and  time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)