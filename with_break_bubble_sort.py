def with_break_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n-2, i-1, -1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swap = True
        if not swap:
            break

if __name__ == "__main__":
    arr = [2,2,5,3,1,3,4,9,6,4,-1,0]
    with_break_bubble_sort(arr)
    print(arr)
