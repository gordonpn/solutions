class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        pressTimes = []
        for index in range(0, len(releaseTimes)):
            if index == 0:
                previousPress = releaseTimes[index]
            else:
                previousPress = releaseTimes[index] - releaseTimes[index - 1]
                
            pressTimes.append((keysPressed[index], previousPress))
        pressTimes.sort(key=lambda x:x[0], reverse=True)
        return max(pressTimes, key=lambda x:x[1])[0]
