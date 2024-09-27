

#Bubble sort function
def BubbleSort(Array, start, end, Key):
    i = end
    sorted = False
    while i > start and not sorted:
        sorted = True
        for j in range(start + 1, i):
            value1 = Array[j - 1][Key]
            value2 = Array[j][Key]
            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                if value1 > value2:
                    temp = Array[j - 1]
                    Array[j - 1] = Array[j]
                    Array[j] = temp
                    sorted = False
            else:
                if str(value1) > str(value2):
                    temp = Array[j - 1]
                    Array[j - 1] = Array[j]
                    Array[j] = temp
                    sorted = False
        i = i - 1
    return Array

# insertion sort
def InsertionSort(Array, start, end, Key):
    for i in range(start + 1, end):
        Temp = Array[i][Key]
        Temp1 = Array[i]
        j = i - 1

        while j >= start:
            value1 = Array[j][Key]
            if (isinstance(Temp, (int, float)) and isinstance(value1, (int, float))) or (isinstance(Temp, str) and isinstance(value1, str)):
                if Temp < value1:
                    Array[j + 1] = Array[j]
                    j -= 1
                else:
                    break
            else:
                if str(Temp) < str(value1):
                    Array[j + 1] = Array[j]
                    j -= 1
                else:
                    break
        
        Array[j + 1] = Temp1
    
    return Array[start:end]


    
#Selection sort function
def SelectionSort(Array, start, end, Key):
    for key in range(start, end):
        min_idx = key

        for i in range(key, end):
            value1 = Array[i][Key]
            value2 = Array[min_idx][Key]
            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                if value1 < value2:
                    min_idx = i
            else:
                if str(value1) < str(value2):
                    min_idx = i

        Array[key], Array[min_idx] = Array[min_idx], Array[key]

    return Array

#Merge sort    
def MergeSort(Array, start, end, Key):
    if start != end:
        q = (start + end) // 2
        MergeSort(Array, start, q, Key)
        MergeSort(Array, q + 1, end, Key)
        return Merge(Array, start, end, q, Key)


def Merge(Array, p, r, q, Key):
    leftcopy = Array[p:q + 1]
    rightcopy = Array[q + 1:r + 1]

    leftcopyindex = 0
    rightcopyindex = 0
    sortedindex = p

    while leftcopyindex < len(leftcopy) and rightcopyindex < len(rightcopy):
        value1 = leftcopy[leftcopyindex][Key]
        value2 = rightcopy[rightcopyindex][Key]

        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            if value1 <= value2:
                Array[sortedindex] = leftcopy[leftcopyindex]
                leftcopyindex += 1
            else:
                Array[sortedindex] = rightcopy[rightcopyindex]
                rightcopyindex += 1
        else:
            if str(value1) <= str(value2):
                Array[sortedindex] = leftcopy[leftcopyindex]
                leftcopyindex += 1
            else:
                Array[sortedindex] = rightcopy[rightcopyindex]
                rightcopyindex += 1

        sortedindex += 1

    while leftcopyindex < len(leftcopy):
        Array[sortedindex] = leftcopy[leftcopyindex]
        leftcopyindex += 1
        sortedindex += 1

    while rightcopyindex < len(rightcopy):
        Array[sortedindex] = rightcopy[rightcopyindex]
        rightcopyindex += 1
        sortedindex += 1

    return Array

#quick sort
def partition(Array, low, high, Key):
    pivot = Array[high][Key]
    i = low - 1
    for j in range(low, high):
        value1 = Array[j][Key]
        pivot_value = pivot

        if (
            (isinstance(value1, (int, float)) and isinstance(pivot_value, (int, float)))
            or (isinstance(value1, str) and isinstance(pivot_value, str))
        ):
           if value1 <= pivot_value:
                i += 1
                Array[i], Array[j] = Array[j], Array[i]
        else:
            if str(value1) <= str(pivot_value):
                i += 1
                Array[i], Array[j] = Array[j], Array[i]

    Array[i + 1], Array[high] = Array[high], Array[i + 1]
    return i + 1

def QuickSort(Array, Start, End, Key):
    if Start >= End:
        return

    p = partition(Array, Start, End, Key)
    QuickSort(Array, Start, p - 1, Key)
    QuickSort(Array, p + 1, End, Key)
    return Array


# Counting Sort
def CountingSort(Array, Key):
    size = len(Array)
    Temp = [None] * size
    max_value = 0
    for i in range(size):
        item = Array[i][Key]
        if isinstance(item, (int, float)):
            max_value = max(max_value, item)
        elif isinstance(item, str):
            max_value = max(max_value, len(item))
    max_value = int(max_value) + 1

    count = [0] * max_value

    # Count the occurrences of each value
    for i in range(size):
        item = Array[i][Key]
        if isinstance(item, (int, float)):
            count[int(item)] += 1
        elif isinstance(item, str):
            count[len(item)] += 1

    for i in range(1, max_value):
        count[i] += count[i - 1]

    j = size - 1
    while j >= 0:
        item = Array[j][Key]
        if isinstance(item, (int, float)):
            count_value = int(item)
        elif isinstance(item, str):
            count_value = len(item)

        Temp[count[count_value] - 1] = Array[j]
        count[count_value] -= 1
        j -= 1

    for j in range(0, size):
        Array[j] = Temp[j]

    return Array


#Radix Sort
def RadixSort(Array, Key):
    def counting_sort(array, exp):
        n = len(array)
        output = [None] * n

        count = [0] * 256 

        for i in range(n):
            item = array[i][Key]
            char = ord(item[exp]) if exp < len(item) else 0
            count[char] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            item = array[i][Key]
            char = ord(item[exp]) if exp < len(item) else 0
            output[count[char] - 1] = array[i]
            count[char] -= 1
            i -= 1

        for i in range(n):
            array[i] = output[i]
    max_length = max(len(item[Key]) if isinstance(item[Key], str) else 0 for item in Array)

    for exp in range(max_length - 1, -1, -1):
        counting_sort(Array, exp)

    return Array



#Searching Algorithms
def LinearSearchthatcontain(Array,Key,text):
    Temp=[]
    for j in range(0, len(Array)):
        if str(Array[j][Key]).find(text)!=-1:
            Temp.append(Array[j])
    return Temp


def LinearSearchthatStarts(Array,Key,text):
    Temp=[]
    for j in range(0, len(Array)):
        if str(Array[j][Key]).startswith(text)==True:
            Temp.append(Array[j])
    return Temp

def LinearSearchthatEnds(Array,Key,text):
    Temp=[]
    for j in range(0, len(Array)):
        if str(Array[j][Key]).endswith(text)==True and str(Array[j][Key]).find(text)!=-1:
            Temp.append(Array[j])
    return Temp



