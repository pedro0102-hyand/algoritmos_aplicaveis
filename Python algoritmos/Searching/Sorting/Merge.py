def merge(x):
    if len(x) > 1:
        mid = len(x) // 2
        left_half = x[:mid]
        right_half = x[mid:]
        merge(left_half)
        merge(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                x[k] = left_half[i]
                i += 1
            else:
                x[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            x[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            x[k] = right_half[j]
            j += 1
            k += 1