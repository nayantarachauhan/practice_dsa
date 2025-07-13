## Returns the largest number in an array


def largestNoFromArray(arr):
    ## largest = 0 // cannot take 0 or any number as solution might be wrong if array contains all negative numbers.
    largest = arr[0]
    for item in arr:
        if item > largest:
            largest = item
    return largest


if __name__ == "__main__":
    arr = [2, 6, 4, 78, 99, 5, 105, 1]
    result = largestNoFromArray(arr)
    print(f"largest no. : {result}")