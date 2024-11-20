import wincurloc as wcl
import time

wcl.hide_cursor()
wcl.clear()

c = 65
while c: # Ctrl+c to stop
    for x in range(wcl.W):
        for y in range(wcl.H):
            if 10 < y < 14:
                if 29 < x < 47:
                    continue
            wcl.locate_c(x, y, chr(c))
    wcl.locate(32, 12)
    print("Hello, World!")
    time.sleep(0.1)
    c += 1
    if c > 90:
        c = 65
