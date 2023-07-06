import random

aCount = 0
bCount = 0
bothCount = 0
notHigh = 0
norCount = 0
trials = 10000000

for i in range(trials):
    flood = random.random()
    if flood >= 0 and flood <= 0.78:
        flood = "low"
    elif flood > 0.78 and flood <= 0.98:
        flood = "medium"
    else:
        flood = "high"
    
    a = False
    b = False
    if flood == "low":
        if random.random() <= 0.01:
            a = True
            if random.random() <= 0.02:
                b = True
    elif flood == "medium":
        if random.random() <= 0.05:
            a = True
            if random.random() <= 0.15:
                b = True
    else:
        if random.random() <= 0.2:
            a = True
            if random.random() <= 0.5:
                b = True
    if a:
        aCount = aCount + 1
    if b:
        bCount = bCount + 1
    if a and b:
        bothCount = bothCount + 1
    if a and not b:
        norCount = norCount + 1

    if a and not b and flood != "high":
        notHigh = notHigh + 1

print(aCount / trials)
print(bothCount / trials)
print(notHigh / norCount)