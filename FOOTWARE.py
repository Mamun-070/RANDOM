import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\x1b[1;31m[!] Checking Update........✔️✔️');time.sleep(0.5)
os.system("git pull")
