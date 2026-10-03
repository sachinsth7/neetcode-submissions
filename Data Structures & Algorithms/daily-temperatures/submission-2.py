class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for current_index, current_temperature in enumerate(temperatures):
            while stack and current_temperature > temperatures[stack[-1]]:
                waiting_index = stack.pop()
                result[waiting_index] = current_index - waiting_index
            stack.append(current_index)
        return result