## count the negative numbers present in an array


def countNegativeNumbers(arr):
    counter = 0
    for item in arr:
        if item < 0:
            counter += 1
    return counter


if __name__ == "__main__":
    arr = [-2,9,-78,8,-65,45]
    result = countNegativeNumbers(arr)
    print(f"The count of negative number in array is : {result}")

