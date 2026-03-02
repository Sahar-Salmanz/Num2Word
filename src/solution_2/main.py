from src.solution_2.constant import UNDER_20, TENS, ABOVE_100


def num_to_words(num: int) -> str:
    """
    Convert a non-negative integer to its English words representation.

    :param num: A non-negative integer to be converted to words.
    :return: A string representing the English words of the input number.
    """
    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        remainder = num % 10
        if remainder == 0:
            return TENS[num // 10]
        return TENS[num // 10] + " " + UNDER_20[remainder]
    
    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_words(num // pivot)
    p2 = ABOVE_100[pivot]

    if num % pivot == 0:
        return f'{p1} {p2}'
    return f'{p1} {p2} {num_to_words(num % pivot)}'


# Test cases
if __name__ == "__main__":
    test_cases = [
        (0, "Zero"),
        (5, "Five"),
        (13, "Thirteen"),
        (20, "Twenty"),
        (45, "Forty Five"),
        (100, "One Hundred"),
        (123, "One Hundred Twenty Three"),
        (1000, "One Thousand"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (1000000, "One Million"),
        (1234567891, "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
    ]

    for num, expected in test_cases:
        result = num_to_words(num)
        assert result == expected, f"Test failed for input {num}: expected '{expected}', got '{result}'"
    print("All tests passed!")