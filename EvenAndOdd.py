def evenAndOdd (numbers):
    
    if len(numbers)==0:
        return {"odd": 0 , "even": 0}

    even = 0
    odd = 0

      
    for num in numbers:
        if num % 2==0 :
            even +=1

        else:
            odd +=1


    return {"even": even , "odd": odd}