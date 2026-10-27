def firstNonRepeatedElement(numbers):
    for num in numbers:
        if numbers.index(num) == len(numbers) - 1 - numbers[::-1].index(num):
            return num
    return None