def length_of_longest_substring(s):
    n = len(s)
    if n <= 1:
        return n

    char_set = set()
    max_length = 0
    left = 0
    right = 0

    while right < n:
        if s[right] not in char_set:
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1

    return max_length
print(length_of_longest_substring("aabb"))
