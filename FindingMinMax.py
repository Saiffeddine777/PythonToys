def FindingMinMax (numbers):
    if len (numbers)==0:
        return None

    min = numbers[0]
    max = numbers[0]

    for num in numbers:
        if num>max:
            max = num
        if num<min:
            min = num

    return {"max" :max,"min": min}