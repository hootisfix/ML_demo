def findSubArray(arr, n):
    sum = 0
    maxsize = -1
    startindex = 0
    originalarray= arr.copy()
    for i in range(n):

        # If its an alphabet
        if (arr[i].isalpha()):
            arr[i] = 0


        # Else its a number
        else:
            arr[i] = 1

    # Pick a starting poas i
    for i in range(n - 1):
        if arr[i] == '1':
            sum = 1
        else:
            sum = -1

            # Consider all sub-arrays starting from i
        for j in range(i + 1, n):
            if arr[j] == 0:
                sum -= 1
            else:
                sum += 1

                # If this is a 0 sum sub-array then
            # compare it with maximum size sub-array
            # calculated so far
            if (sum == 0 and maxsize < j - i + 1):
                maxsize = j - i + 1
                startindex = i

                # If no valid sub-array found
    if (maxsize == -1):
        print(maxsize, end=" ")
    else:
        print(startindex, (startindex + maxsize - 1))
        print(originalarray[startindex:(startindex + maxsize)])

    # Driver code


arr = ['A', 'B', '6','6','6','6','6','6','6','6','X', '4', '6', '4', '6','6', 'X', 'a','6','X','6', '6','6','6','6','6','6','6','6','6','a']
size = len(arr)

findSubArray(arr, size)