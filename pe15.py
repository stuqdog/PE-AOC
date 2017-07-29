# for a in reversed(range(0, half the number plus 1))
# then for b in reversed(range(a + 1, half the number + 2))
#
# and so on
#
# for each step, add +1 to solution

solution = 0

for a in reversed(xrange(0, 21)):
    print solution
    solution += 1
    for b in reversed(xrange(a + 1, 22)):
        if b - a > 1:
            solution += 1
        for c in reversed(xrange(b + 1, 23)):
            if c - b > 1:
                solution += 1
            for d in reversed(xrange(c + 1, 24)):
                if d - c > 1:
                    solution += 1
                for e in reversed(xrange(d + 1, 25)):
                    if e - d > 1:
                        solution += 1
                    for f in reversed(xrange(e + 1, 26)):
                        if f - e > 1:
                            solution += 1
                        for g in reversed(xrange(f + 1, 27)):
                            if g - f > 1:
                                solution += 1
                            for h in reversed(xrange(g + 1, 28)):
                                if h - g > 1:
                                    solution += 1
                                for i in reversed(xrange(h + 1, 29)):
                                    if i - h > 1:
                                        solution += 1
                                    for j in reversed(xrange(i + 1, 30)):
                                        if j - i > 1:
                                            solution += 1
                                        for k in reversed(xrange(j + 1, 31)):
                                            if k - j > 1:
                                                solution += 1
                                            for l in reversed(xrange(k + 1, 32)):
                                                if l - k > 1:
                                                    solution += 1
                                                for m in reversed(xrange(l + 1, 33)):
                                                    if m - l > 1:
                                                        solution += 1
                                                    for n in reversed(xrange(m + 1, 34)):
                                                        if n - m > 1:
                                                            solution += 1
                                                        for o in reversed(xrange(n + 1, 35)):
                                                            if o - n > 1:
                                                                solution += 1
                                                            for p in reversed(xrange(o + 1, 36)):
                                                                if p - o > 1:
                                                                    solution += 1
                                                                for q in reversed(xrange(p + 1, 37)):
                                                                    if q - p > 1:
                                                                        solution += 1
                                                                    for r in reversed(xrange(q + 1, 38)):
                                                                        if r - q > 1:
                                                                            solution += 1
                                                                        for s in reversed(xrange(r + 1, 39)):
                                                                            if s - r > 1:
                                                                                solution += 1
                                                                            for t in reversed(xrange(s + 1, 40)):
                                                                                if t - s > 1:
                                                                                    solution += 1



print solution
