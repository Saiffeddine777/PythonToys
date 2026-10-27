def mostFrequantElement(numbers):
    if not numbers:
        return None
    
    counterDic = {}
    for num in numbers:
        if num in counterDic:
            counterDic[num] += 1
        else:
            counterDic[num] =1
    max_frequacy = 0

    toReturn = 0

    for element in counterDic:
        if counterDic[element] > max_frequacy:
            max_frequacy = counterDic[element]
            toReturn = element
    

        
    return toReturn