# arr[] = [0, -1, 2, -3, 1], target = -2

# sort
# make two list (negative, positive)
# target = 8
# [1,2,5,6]

# Time = n + n + n + n + ... + n = n * n = n ^ 2 = O(n^2)
# Space = O(1)
def first(arr: list[int], target: int) -> bool:
    for index1 in range(len(arr)):
        for index2 in range(len(arr)):
            if index1 == index2:
                continue
            
            if arr[index1] + arr[index2] == target:
                return True
    return False

# Time = O(n)
# Space = O(n)
def second(arr: list[int], target: int) -> bool:
    s = set()
    for member in arr:
        value = target - member
        if value in s:
            return True
        else:
            s.add(member)
    return False

def main():
    arr = [0, -1, 2, -3, 1]
    target = -2

    result = second(arr, target)
    assert result == True

    arr = [1, -2, 1, 0, 5]
    target = 0

    result = second(arr, target)
    assert result == False

def benchmark() -> tuple:
    n = 1_000_000
    
    import random
    arr = random.sample(range(-1_000_000, 1_000_000), n)
    target = arr[-1] + arr[-2]

    import time
    # print('First Algorithm = O(n^2)')
    start = time.time()
    result = first(arr, target)
    end = time.time()
    # print(f'Execution time = {(end - start) * 1000} ms')
    # assert result == True
    execution1 = end - start

    # print('Second Algorithm = O(n)')
    start = time.time()
    result = second(arr, target)
    end = time.time()
    # print(f'Execution time = {(end - start) * 1000} ms')
    # assert result == True
    execution2 = end - start

    return (execution1, execution2)



if __name__ == '__main__':
    #main()
    sum1, sum2 = 0, 0
    for _ in range(1000):
        result = benchmark()
        sum1 += result[0]
        sum2 += result[1]

    print(f'Execution time first = {(sum1 / 1000) * 1000} ms')
    print(f'Execution time second = {(sum2 / 1000) * 1000} ms')

