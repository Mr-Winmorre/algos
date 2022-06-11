import queue


def find_strobogrammatic(n):
    if not n:
        return []

    sys_pair1 = {'8': '8', '6': '9', '9': '6', '1': '1', '0': '0'}
    sys_pair2 = {'8': '8', '6': '9', '9': '6', '1': '1'}
    sys_pair3 = {'8': '8', '1': '1', '0': '0'}

    root = ['']*n
    q = queue.Queue()
    q.put((root,0,n-1))
    print(q.get())

def equilibrium_index(ar: list):
    equi_ar = []
    if not ar:
        return equi_ar

    # create cumulative array
    cum_ar = [ar[0]]
    for i in range(1, len(ar)):
        cum_ar.append(cum_ar[-1] + ar[i])

    # first left element
    sum_left = 0
    sum_right = cum_ar[-1] - cum_ar[0]
    if sum_right == sum_left:
        equi_ar.append(0)

    # in between elements
    for i in range(1, len(ar) - 1):
        sum_left = cum_ar[i - 1]
        sum_right = cum_ar[-1] - cum_ar[i]
        if sum_right == sum_left:
            equi_ar.append(i)

    # last but one element
    # the last element in the list is not considered because it does not satisfy the condition
    if cum_ar[-2] == 0:
        equi_ar.append(len(ar) - 1)

    return equi_ar


def array_operation(string: str, operations) -> str:
    def decrement_str(s: str):
        for i in range(len(s.split())):
            if s[i] == 'a':
                s[i] = 'z'
            else:
                s[i] -= 1

    def increment_str(s: str):
        for i in range(len(s.split())):
            if s[i] == 'z':
                s[i] = 'a'
            else:
                s[i] += 1

    string_sub = ""
    for j in range(len(operations)):
        ith_op = operations[j]
        i1 = ith_op[0] - '0'
        i2 = ith_op[1] - '0'
        if i1 == i2:
            string_sub = string[i1]
            string_sub = str(string[0] + i1, string[0] + i2 + 1)


if __name__ == "__main__":
    # print(equilibrium_index([-1, 3, -4, 5, 1, -6, 2, 1]))
    find_strobogrammatic(13)
