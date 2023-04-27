#my code
def count_positives_sum_negatives(arr):
    result = []
    count = 0
    s = 0
    if not arr:
        return result
    for i in arr:
        if i < 0:
            count += 1
        if i < 0:
            s += i
    result.append(count)
    result.append(s)
    return result

arr = [1, 2, 3, 0, -1, -2, -3]
print(count_positives_sum_negatives(arr))

# Alternative
# def count_positives_sum_negatives(arr):
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []