def countFrequancies(numbers):
    acc = {}
    for num in numbers:
        if num in acc:
            acc[num]=acc[num] +1

        else :acc[num] = 1

    return acc

print(countFrequancies([4, 7, 2, 7, 4, 9, 4, 1]))    