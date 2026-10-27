def findDuplicates (numbers):
    seen = set()
    duplicate = set()
    for num in numbers:
        if seen.__contains__(num):
            duplicate.add(num)
        else:
            seen.add(num)    

    return list(duplicate)

print(findDuplicates([4, 7, 2, 7, 4, 9, 4, 1]))