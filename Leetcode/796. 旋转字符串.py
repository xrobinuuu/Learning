def rotate_string(a, b):
    ind = 0
    ext = len(a)
    while ind < ext:
        a = a[1:] + a[0]
        if a == b:
            return True
        ind += 1
    return False


if __name__ == "__main__":
    s, goal = "abcde", "cdeab"
    x = rotate_string(s, goal)
    print(x)
