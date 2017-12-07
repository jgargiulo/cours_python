from typing import List
from concurrent.futures import *
from time import time

print("Sequentiel: ")
start = time()
f1 = sum(range(50_000_000))
f2 = sum(range(50_000_000))
print(f1 + f2, time()-start)


print("Concurrence avec 2 Threads : ")
with ThreadPoolExecutor(max_workers=2) as executor:
    start = time()
    fc1 = executor.submit(sum, range(50_000_000))
    fc2 = executor.submit(sum, range(50_000_000))
    print(fc1.result() + fc2.result(), time()-start)


print("Conccurence avec 2 Processes: ")
with ProcessPoolExecutor(max_workers=2) as executor:

    start = time()

    fp1 = executor.submit(sum, range(50_000_000))
    fp2 = executor.submit(sum, range(50_000_000))

    print(fp1.result() + fp2.result(), time()-start)
    
