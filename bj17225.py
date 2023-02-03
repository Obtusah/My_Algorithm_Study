ends = 1                        # time sm ends packing
endj = 1
ts = [0 for i in range(88000)]  # time sm starts packing
tj = [0 for i in range(88000)]

A, B, N = map(int, input().split())

for i in range(N):
    t, c, m = input().split()
    t = int(t)
    m = int(m)

    if c == "B":                # when sm is packing
        if t < ends:            # if sm is not done packing at the start time
            t = ends
        for j in range(m):
            ts[t + A*j] += 1    # record each packet's time that sm started packing
        ends = t + A * m
    else:
        if t < endj:
            t = endj
        for j in range(m):
            tj[t + B*j] += 1
        endj = t + B * m

endt = max(ends - A, endj - B)      # max(start packing time)

sm = []
js = []
p = 1
for time in range(1, endt+1):
    for i in range(ts[time]):
        sm.append(p)
        p += 1
    for i in range(tj[time]):
        js.append(p)
        p += 1

# output
print(len(sm))
for r in sm:
    print(r, end=' ')

print()

print(len(js))
for r in js:
    print(r, end=' ')