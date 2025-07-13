## Given the array of number and one number in the input, if number exists in the array then return
## the no. else return -1



arr = [4,78,3,56,99,134,74]
a = 7
11
def returnIndex(arr, input_number):
    for i, item in enumerate(arr):
        if input_number == item:
            return i
    return -1



if __name__ == "__main__":
    result = returnIndex(arr,a)
    print(f"Index returned for the input number : {a}, Index: {result}")


