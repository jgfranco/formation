import time
def tictoc(func):

    

    def wrapper(*args, **kwargs):

        t1 = time.time()
        test = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'it took {func.__name__} {t2} seconds to run')
        return test

    return wrapper

@tictoc
def removeDuplicates(array: list[int]) -> list[int]:
    seen = set()
    result = []

    for num in array:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

print(removeDuplicates([]) == [])
print(removeDuplicates([1]) == [1])
print(removeDuplicates([1, 1]) == [1])
print(removeDuplicates([4, 2, 6, 7, 4, 8, 7]) == [4, 2, 6, 7, 8])

@tictoc
def removeDuplicatesConstantSpace(array: list[int]) -> list[int]:
    
    length = len(array)

    for i in range(length):
        for j in range(i+1, length):
            if array[i]!= "" and array[i] == array[j]:
                array[j] = ""
    
    array = [num for num in array if isinstance(num,int)]
    return array
                


print(removeDuplicatesConstantSpace([]) == [])
print(removeDuplicatesConstantSpace([1]) == [1])
print(removeDuplicatesConstantSpace([1, 1]) == [1])
print(removeDuplicatesConstantSpace([4, 2, 6, 7, 4, 8, 7]) == [4, 2, 6, 7, 8])
