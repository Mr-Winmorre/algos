def valid_parentheses(s: str):
    opening = ['[', '{', '(']
    closing = [']', '}', ')']
    b = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    stack = []

    for i in s:
        if i in opening:
            stack.append(i)
        elif len(stack) != 0 and i in closing and b[i] == stack[-1]:
            stack.pop()
        elif i not in opening and i not in closing:
            continue
        else:
            return False

    return len(stack) == 0


def find_median_sorted_array(l: list, k: list):
    j: list = l + k
    o: int = len(j)
    j.sort()
    if o == 0:
        return -1

    if o == 1:
        return j[0]

    if o % 2 == 0:
        h = (o // 2)
        med1 = j[h]
        med2 = j[h - 1]

        result = (med1 + med2) / 2
        return result
    else:
        i = (o // 2)
        result = j[i]
        return result


def ein(l: list):
    max_c = -1
    for i in l:
        v = max(i)
        le = [f for f in i if f == v]
        print(le)
        print(i)
        if len(le) == 1 and v > max_c:
            max_c = v
        else:
            continue
    return max_c

def kom(f):
    result =[]
    stack = []
    for i in f:
        if i not in stack:
            stack.append(i)
        elif i in stack:
            k = stack[-1]+1
            stack.append(k)
            result.append(i)
            result.append(k)

    return result

if __name__ == '__main__':
    # print(ein([[5,7,3,9,4,9,8,3,1],[1,2,2,4,4],[1,2,3]]))

    print(kom([1,2,3,2]))