from typing import List


def movies_on_flight(movie_duration: List[int], flight_duration: int):
    flight_duration -= 30
    movie_duration.sort()
    left_pointer = 0
    right_pointer = len(movie_duration) - 1
    movies = {}

    while left_pointer < right_pointer:
        duration_sum = movie_duration[left_pointer] + movie_duration[right_pointer]

        if duration_sum <= flight_duration:
            movies[(left_pointer, right_pointer)] = duration_sum
            left_pointer += 1
        else:
            right_pointer -= 1

    if not movies:
        return []

    result_tuple = max(movies, key=movies.get)
    return [movie_duration[result_tuple[0]], movie_duration[result_tuple[1]]]


def movies_on_flight_alt(movie_duration: List[int], flight_duration: int):
    flight_duration -= 30
    left_pointer = 0
    right_pointer = len(movie_duration) - 1
    max_l_pointer = left_pointer
    max_r_pointer = right_pointer
    max_minutes = 0

    while left_pointer < right_pointer:
        duration_sum = movie_duration[left_pointer] + movie_duration[right_pointer]

        if duration_sum > flight_duration:
            right_pointer -= 1
        else:
            if duration_sum == flight_duration:
                return [movie_duration[left_pointer] + movie_duration[right_pointer]]
            elif duration_sum > max_minutes:
                max_minutes = duration_sum
                max_r_pointer = right_pointer
                max_l_pointer = left_pointer
            left_pointer += 1

    return [movie_duration[max_l_pointer], movie_duration[max_r_pointer]]


movie_duration1 = [90, 85, 75, 60, 120, 150, 125]
flight_duration1 = 250

print(movies_on_flight(movie_duration1, flight_duration1))  # [90, 125]
print(movies_on_flight_alt(movie_duration1, flight_duration1))  # [90, 125]
