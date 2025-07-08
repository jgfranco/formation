"""

Given a string s return the index of the first unique character (not repeating)

"""


def firstUniqChar(s: str) -> int:
    from collections import Counter

    counts = Counter(s)

    for idx, ch in enumerate(s):
        if counts[ch] == 1:
            return idx
    
    return -1

def run_tests():
    cases = [
        ("leetcode", 0),                 # first character is unique
        ("loveleetcode", 2),            # unique character inside the string
        ("aabb", -1),                   # no unique characters
        ("", -1),                       # empty string
        ("z", 0),                       # single-character string
        ("abcabcd", 6),               # unique character near the end
        ("aaabcccdeeef", 3)            # multiple repeating groups, one unique
    ]
    for s, expected in cases:
        result = firstUniqChar(s)
        assert result == expected, f"Failed for {s}: expected {expected}, got {result}"
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
    