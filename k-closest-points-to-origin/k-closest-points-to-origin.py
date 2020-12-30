class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []

        for point in points:
            distance = math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
            distances.append((point, distance))

        distances = sorted(distances, key=lambda x: x[1])

        return [distances[n][0] for n in range(K)]
