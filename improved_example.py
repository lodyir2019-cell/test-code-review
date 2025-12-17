"""Improved version of calculate_average with better performance."""

from typing import List, Union

def calculate_average(numbers: List[Union[int, float]]) -> float:
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numbers to average.
        
    Returns:
        The average of the numbers.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    result = calculate_average([10, 20, 30])
    print(f"Average: {result}")
