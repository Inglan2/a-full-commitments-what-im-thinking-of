import os
import time

while True:
    for i range(1, 420):
        os.system('git commit -m "commit" --allow-empty')
    os.system('git push')
    # time.sleep(1)