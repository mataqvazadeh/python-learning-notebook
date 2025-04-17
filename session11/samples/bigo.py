# 1 = O(1)
def sum(a,b):
    c = a + b
    return c

# 10 = O(1)
def get_first_member(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[0]
    
# 1 +‌ n + 1 + 1 = n +‌ 3 = O(n)
# n +‌ 1
def array_sum(lst):
    result = 0
    for member in lst:
        result = result + member

    return result
