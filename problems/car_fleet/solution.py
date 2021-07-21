class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        previous_time = None
        fleets = 0
        
        for position_, velocity in sorted(zip(position, speed), reverse=True):
            distance = target - position_
            time_remaining = distance / velocity
           
            if previous_time is None or time_remaining > previous_time:
                previous_time = time_remaining
                fleets += 1
                
        return fleets
                
        