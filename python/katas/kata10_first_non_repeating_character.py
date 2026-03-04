def first_non_repeating_letter(s):
    lower_s = s.lower()
    counts = {}
    for char in lower_s:
        counts[char] = counts.get(char, 0) + 1
    for i in range(len(s)):
        if counts[lower_s[i]] == 1:
            return s[i]
    return ""
