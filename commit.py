import os
import time

while True:
    for i in range(1, 4200):
        os.system('git commit -m "commit" --allow-empty')
    os.system('git push')
    # time.sleep(1)