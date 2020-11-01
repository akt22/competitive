def check(s):
    for j in range(len(s)):
        if s[j] == T[j] or s[j] == "?":
            if j + 1 == lenT:
                return True
            continue
        else:
            return False
    return False

def main():
    for i in range(1, len(S)+1):
        s = S[-i:]
        if check(s):
            tail = "" if -i + lenT == 0 else S[-i+lenT:]
            tmp = S[:-i] + T + tail
            print(tmp.replace("?", "a"))
            exit()

    print("UNRESTORABLE")

if __name__ == "__main__":
    S = input().strip()
    T = input().strip()
    lenT = len(T)
    main()
