# Write a function which compresses a string "AAACCCBBD" to "A3C3B2D".
# Then write another function to get the original string from the compressed string.


def compress(string: str) -> str:
    output_string: str = ""
    if not string or len(string) is 0:
        return output_string

    string_as_list: List[str] = [char for char in string]
    counter: int = 1

    for index, char in enumerate(string_as_list):
        if (index + 1) is len(string_as_list):
            output_string = output_string + str(counter) + char
            return output_string
        if char is string_as_list[index + 1]:
            counter += 1
        else:
            output_string = output_string + str(counter) + char
            counter = 1

    return output_string


if __name__ == "__main__":
    string = "AAABBCCCCCCAAAAA"
    print(f"Compressing: {string}")
    print(f"Result: {compress(string)}")
