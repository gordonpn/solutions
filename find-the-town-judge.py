class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (N + 1)
        
        for out_deg, in_deg  in trust:
            trust_count[out_deg] -= 1
            trust_count[in_deg] += 1
            
        for person in range(1, N + 1):
            if trust_count[person] == N - 1:
                return person
        
        return -1
​
