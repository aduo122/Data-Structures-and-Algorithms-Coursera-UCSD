# python3
import sys

def BWT(text):
    if not text:
        return ""
    temp = []
    for i in range(len(text)):
        temp.append(text[i:]+text[:i])
    temp.sort()

    res = ""
    for i in temp:
        res += i[-1]
    return res

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))