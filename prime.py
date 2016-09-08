from microbit import *

# Write your code here :-)
display.show('|/-\\|/-\\', 400, wait=False, loop=True, clear=False)


def erPrimtall(n):
    bPrimtall = True
    j = 2
    while (j < n):
        rest = n % j
        if not rest:
            bPrimtall = False
            break
        j = j + 1
    return bPrimtall


def FinnTverrsum(n):
    s = str(n)
    tverrSum = 0
    k = 0
    l = len(s)
    while(k < l):
        tverrSum = tverrSum + int(s[k])
        k = k + 1
    return tverrSum


bBeregn = False
iKorrektTverrsum = 29
iTestTall = 1
bRiktigNummerFunnet = False
while not bRiktigNummerFunnet:
    iTestTall = iTestTall + 1
    if erPrimtall(iTestTall):
        if (FinnTverrsum(iTestTall) == iKorrektTverrsum):
            bRiktigNummerFunnet = True

s = "Koden er: " + str(iTestTall)
display.scroll(s)
