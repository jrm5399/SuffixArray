#John Murphy
#CAP 6517

# Take in user input
sequence = input('Insert your string: ')
sub_string = input('Now insert your substring you want to search for: ')

# Helper Functions
def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Step 1: break up the string into segments
def break_apart(text):
    arr = []
    N = len(text)

    for i in range(N):
        arr.append((i, text[i:]))

    return arr


# Step 2: Sort array lexicographically
def string_sort(arr):
    arr.sort(key=lambda x: x[1])
    return arr

# Step 3: Binary search our substring
def bin_search(arr, seq):
    lo = 0
    hi = len(arr)
    ans = []

    while lo < hi:
        mid = (hi + lo) // 2
        if compare(seq[0], arr[mid][1][0]) == 1:
            lo = mid + 1
        else:
            hi = mid

    start = lo
    hi = len(arr)

    while lo < hi:
        mid = (hi + lo) // 2
        if compare(seq[0], arr[mid][1][0]) == -1:
            hi = mid
        else:
            lo = mid + 1

    end = hi

    for i in range(start, end):
        if seq == arr[i][1][0:len(seq)]:
            ans.append(arr[i])

    return ans

arr = break_apart(sequence)
print("String Broken Up: ", *arr, sep='\n')
print("=======================")

sorted_string = string_sort(arr)
print("Sorted By Characters: ", *sorted_string, sep="\n")
print("=======================")

test = bin_search(sorted_string, sub_string)
print(f"--We located {sub_string} in the following indicies--")
[print(x) for x in test]
