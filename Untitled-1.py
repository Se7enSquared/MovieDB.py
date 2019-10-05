    #Print all of the statistical analyses
    print("Column:", column_to_parse)
    print("\tCount:", len(numbers))
    print("\tValidNum:", 0) #fix later
    print("\tAverage:", sum(numbers)/ len(numbers))
    print("\tMax:", max(numbers))
    print("\tMin:", min(numbers))
    print("\tVariance:", sum(pow(x-mean,2) for numbers in f / len(numbers)))
    print("\tStdDev:", math.sqrt(var))
    print("\tMedian:", median_of_numbers)
 if__name__=="__main__"