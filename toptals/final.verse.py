import re


def solution(T, R):
    b = list(zip(T, R))
    j = [re.sub('[^0-9]', "", p) for p in T]
    v = [(re.sub('[^0-9]', '', n), m) for n, m in b]
    c = {}
    for i in range(len(v)):
        if v[i][1] == 'Ok':
            h = [k for k in j if k == v[i][0]]
            if len(h) < 2:
                c[v[i][0]] = v[i][1]

    r = (len(c) * 100) / len(list(set(j)))
    print(r)
    print(c)
    print(len(c))

    print(v)


def vavation(A):
    needed = {val: 1 for val in set(A)}
    missing = len(needed)
    print(needed)

    cur_i = result_i = result_j = 0
    for cur_j, num in enumerate(A, 1):
        if needed[num] > 0:
            missing -= 1
        needed[num] -= 1

        if not missing:

            while cur_i < cur_j and needed[A[cur_i]] < 0:
                needed[A[cur_i]] += 1
                cur_i += 1

            if not result_j or cur_j - cur_i <= result_j - result_i:
                result_i, result_j = cur_i, cur_j
    return result_j - result_i


if __name__ == '__main__':
    # solution(['test1a', 'test2', 'test1b', 'test1c', 'test3'], ['Wrong', 'Ok', 'time out', 'Ok', 'Time out'])
    print(vavation([7,3,7,3,1,3,4,1]))