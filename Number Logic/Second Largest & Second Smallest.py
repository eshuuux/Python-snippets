def getSecondOrderElements():
    a = [2, 5, 30, 1, 50, 60]

    # Find smallest and largest
    smallest = a[0]
    largest = a[0]

    for i in range(len(a)):
        if a[i] < smallest:
            smallest = a[i]
        if a[i] > largest:
            largest = a[i]

    # Find second smallest
    second_smallest = largest
    for i in range(len(a)):
        if a[i] > smallest and a[i] < second_smallest:
            second_smallest = a[i]

    # Find second largest
    second_largest = smallest
    for i in range(len(a)):
        if a[i] < largest and a[i] > second_largest:
            second_largest = a[i]

    print("Second Smallest:", second_smallest)
    print("Second Largest:", second_largest)

getSecondOrderElements()
