def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        for j in range(n-2, -1, -1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

if __name__ == "__main__":
    arr = [2,2,5,3,1,3,4,9,6,4,-1,0]
    bubble_sort(arr)
    print(arr)
