## Find the second largest number in an array


def secondLargestNumber(arr):

    if len(arr) < 2:
        return "Please give array with min length of 2"

    largest = second_largest = float('-inf')

    for item in arr:
        if item > largest:
            second_largest = largest
            largest = item
        elif item > second_largest and item != largest:
            second_largest = item
        else:
            continue

    ## if all the number in an array are equal
    if second_largest == float('-inf'):
        return None

    return second_largest



if __name__ == "__main__":
    arr = [0,18 ,-4, -5, 89]
    result = secondLargestNumber(arr)
    print(f"Second largest number : {result}")
