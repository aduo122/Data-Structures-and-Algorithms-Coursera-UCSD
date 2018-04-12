# python3
import sys

def InverseBWT(bwt):
    # write your code here
    if not bwt:
        return ""

    last_col = list(bwt)
    first_col = last_col[:]
    first_col.sort()
    first_dic = {}
    last_dic = {}
    first_ind = {}
    last_ind = {}

    for i in range(len(last_col)):
        if first_col[i] in first_ind:
            first_ind[first_col[i]] += 1
        else:
            first_ind[first_col[i]] = 1
        first_dic[(first_col[i],first_ind[first_col[i]])] = i

        if last_col[i] in last_ind:
            last_ind[last_col[i]] += 1
        else:
            last_ind[last_col[i]] = 1
        last_dic[i] = (last_col[i],last_ind[last_col[i]])


    res = ['$']
    temp = 0
    for _ in range(len(last_col)-1):
        res += [last_col[temp]]
        char_ind = last_dic[temp]
        temp = first_dic[char_ind]
    res = res[::-1]
    res = ''.join(res)
    return res


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))