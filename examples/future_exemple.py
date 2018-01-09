from typing import List
from concurrent.futures import *
from time import time

print("Conccurence avec 2 Processes: ")
with ProcessPoolExecutor(max_workers=2) as executor:

    start = time()

    fp1 = executor.submit(sum, list(range(50_000_000)))
    fp2 = executor.submit(sum, list(range(50_000_000)))

    print(fp1.result() + fp2.result(), time()-start)
    
