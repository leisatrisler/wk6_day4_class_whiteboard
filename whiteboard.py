#Given a string return True if the string can be rearranged to make a palindrome
#a palindrome can be spelled the same forwards and backwards

# Input
s1="aabbcc"
# Output
# True

# Input
s2="aabebcc"
# Output
# True

# Input
s3="racecar"
# Output
# True

# Input
s4="abcd"
# Output
# False

# Input
s5="aaabbbcc"
# Output
# False

def solution(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    num_odd = 0
    for count in letter_count.values():
        if count % 2 == 1:
            num_odd += 1
            if num_odd == 2:
                return False
    return True