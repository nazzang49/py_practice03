arr = [5, 9, 3, 8, 60, 20, 1]

for i in range(0, len(arr)-1):
    for n in range(i+1, len(arr)):
        if arr[i] < arr[n]:
            tmp = arr[i]
            arr[i] = arr[n]
            arr[n] = tmp

print(arr)