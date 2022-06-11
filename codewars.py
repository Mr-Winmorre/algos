def unique_in_orders(a: list):
    c = []
    for i in range(len(a)):
        if len(c) == 0:
            c.append(a[i])
        elif a[i] is not c[-1]:
            c.append(a[i])
    return c


def diamond(f):
    if f % 2 == 0 or f < 0:
        return None
    d = [c for c in range(f + 1) if c % 2 != 0 or c == 1]
    lower = [v for v in d if v < f]
    lower.reverse()
    print(lower)
    for n in lower:
        d.append(n)
    print(d)
    c = ['*' * i for i in d]
    upper = '\n'.join(c).center(f, ' ').rstrip()
    return upper


def replace_at_third_index(s: str):
    v = ''
    for c in range(len(s)):
        if (c + 1) % 3 == 0:
            v += 'X'
        else:
            v += s[c]
    return v


def max_profit(a: list):
    max_p, curr_ma_val = 0, 0
    for i in reversed(a):
        curr_ma_val = max(curr_ma_val, i)
        potential_profit = curr_ma_val - i
        max_p = max(potential_profit, max_p)
    if max_p > 0:
        v = replace_at_third_index(str(max_p) + '6kgwid5e2')

        return v
    else:
        b = replace_at_third_index(str(-1) + '6kgwid5e2')
        return b


def large_factorials(n):
    x = 1
    for i in range(n, 0, -1):
        x = x * i
    return x


def forming_magic_square(s):
    result = 0;
    if s[1][1] != 5:
        s[1][1] = 5
    edges = [s[i][v] for i in range(0, len(s), 2) for v in range(0, len(s[i]), 2)]
    o = [c for c in edges if c % 2 != 0]
    e = [i for i in range(10) if i > 0 and i % 2 == 0 and i not in edges]
    b = [(n, m) for n in edges if n % 2 != 0 for m in range(10) if m > 0 and m % 2 == 0 and m not in edges]
    n = [abs(i - j) for i, j in b]
    result += sum(n)
    print(n)
    print(edges)
    print(b)
    for i in range(0, len(s), 2):
        for k in range(0, len(s[i]), 2):
            for h, g in b:
                if s[i][k] % 2 != 0 and s[i][k] == h:
                    s[i][k] = g

    pd = [s[ii][jj] for ii in range(len(s)) for jj in range(len(s[ii])) if ii == jj]
    rd = [s[ii][jj] for ii in range(len(s)) for jj in range(len(s[ii])) if ii + jj == len(s) - 1]
    md = [s[ii][jj] for ii in range(len(s)) for jj in range(len(s[ii])) if jj == 1]
    hmd = [s[ii][jj] for ii in range(len(s)) for jj in range(len(s[ii])) if ii == 1]

    if sum(md) != 15:
        diff1 = 10 - (md[0] + md[2])
        max_1 = max(md[0], md[2]) + diff1
        min_1 = min(md[0], md[2])
        if max_1 % 2 != 0 and max_1 != min(md[0], md[2]) and max_1 not in hmd:
            result += diff1
            for ij in range(len(s)):
                for ji in range(len(s[ij])):
                    if ji == 1 and s[ij][ji] == max(md[0], md[2]):
                        s[ij][ji] = max_1
    if sum(hmd) != 15:
        max_h = max(hmd[0], hmd[2])
        min_h = min(hmd[0], hmd[2])
        diff_h = 10 - (hmd[0] + hmd[2])
        max_2 = max_h + diff_h
        if max_2 % 2 != 0 and max_2 != min_h and max_2 not in md:
            result += diff_h
            for oj in range(len(s)):
                for dj in range(len(s[oj])):
                    if oj == 1 and s[oj][dj] == max_h:
                        s[oj][dj] = max_2
    if sum(s[2]) != 15:
        dd = abs(10 - (s[2][0] + s[2][2]))
        if s[2][0] != s[2][2]:
            mm = max(s[2][0], s[2][2])
            nn = mm + dd
            for i in range(len(s[2])):
                if s[2][i] == mm and nn not in edges:
                    s[2][i] = nn
                    result += dd
        else:
            jk = s[2][0] + dd
            s[2][0] = jk
            result += dd

    print(s)
    print(result)




if __name__ == "__main__":
    # print(unique_in_orders("AAAABBBCCDAABBB"))

    # print(max_profit([10, 9, 8]))
    # print(large_factorials(25))
    # forming_magic_square([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
    print("l")
