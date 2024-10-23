def isPalindrome(s: str) -> bool:
    j, k = 0, len(s) - 1
    while j < k:
        if not s[j].isalnum():
            j += 1
        elif not s[k].isalnum():
            k -= 1
        elif s[j].lower() == s[k].lower():
            j += 1
            k -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    nu = "1A man, a plan, a canal: Panama1"
    y = isPalindrome(nu)
    print(y)
