def sumAndAvg (numbers):
    if numbers is None or len(numbers)==0:
        return {"sum": 0 , "avg":None }
    sum = 0
    for num in  numbers:
        sum += num

    avg = sum /len(numbers)

    return {"sum" : sum , "avg" :avg}