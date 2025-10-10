def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]  # 1-indexed
        if s < target:
            l += 1
        else:
            r -= 1
    return [-1, -1]  # In LC167 there's guaranteed one solution
