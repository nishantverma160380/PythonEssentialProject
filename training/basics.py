'''

Created On Jan 5, 2019

'''

def amount_processing(numbers):
    sum=count=0
    min=max=numbers[0]
    for num in numbers:

        count=count+1
        sum+=num

        if num<min:
            min=num

        if num>max:
            max=num

    avg=sum/count
    return {"avg":avg, "sum":sum, "count":count, "min":min, "max":max}
    pass

if __name__ == '__main__':
    print("Welcome to Python Programming")
    word = "Hello World"
    print(word[1:-2])
    print(len(word))
    print(word[-2])
    print(word[2])
    print(word.isupper())
    print(word.islower())

    numbers = [123,423,6546,234,756,789,345]
    results = amount_processing(numbers)

    print("avg   : "+str(results["avg"]))
    print("sum   : "+str(results["sum"]))
    print("count : "+str(results["count"]))
    print("min   : "+str(results["min"]))
    print("max   : "+str(results["max"]))

    sequence = {'p', 'a', 's', 's'}
    for val in sequence:
        print(val)
        pass



    pass