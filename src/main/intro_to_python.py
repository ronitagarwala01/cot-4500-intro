import numpy as np

if __name__ == "__main__":
    arr = np.zeros((3, 3)) #Create 3x3 matrix with all 0s
    
    #Solution for 1; Prints 1s where row number == column number
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if i==j:
                arr[i][j] = 1
    print(arr)
    print()

    #Solution for 2; Adds 3 to elements where row number != column number
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if i!=j:
                arr[i][j] += 3
    print(arr)
    print()

    #Solution for 3; Deletes last column
    arr = np.delete(arr, obj = 2, axis = 1)
    print(arr)
