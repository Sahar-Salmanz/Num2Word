from src.solution_1.constants import UNDER_20, TENS, ABOVE_100


def num_to_words(num: int) -> str:
    """
     Converts a number to its English word representation.

    :param num: The number to convert.
    :return: The English word representation of the number.
    """
    if num == 0:
        return "Zero"
    
    result = ""
    
    for pivot in sorted(ABOVE_100.keys(), reverse=True):
        if num >= pivot:
            count = num // pivot
            result += num_to_words(count) + " " + ABOVE_100[pivot] + " "
            num %= pivot
    
    if num >= 20:
        tens_place = num // 10
        result += TENS[tens_place] + " "
        num %= 10
    
    if num > 0:
        result += UNDER_20[num - 1] + " "
    
    return result.strip()


# Test cases
if __name__ == "__main__":
    test_numbers = [0, 5, 13, 25, 99, 100, 101, 110, 999, 1000, 1001, 1010, 1100, 9999, 1000000, 1234567890]
    for number in test_numbers:
        assert num_to_words(number) == num_to_words(number), f"Test failed for {number}"
    print("All tests passed!")