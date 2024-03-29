# test_strasen.py

import matplotlib.pyplot as plt
from scipy.stats import mode
import numpy as np
import cross_over
import strassen
import time
import sys

def findnOpt():
    bestN = []
    Ds = [2, 4, 8, 16, 32, 64, 128, 256]
    nOpts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 32, 50, 100, 150]
    for i, d in enumerate(Ds):
        times = []
        for nOpt in nOpts:
            sys.argv = ["strassen.py", f"{nOpt}", f"{d}", f"test{i}.txt"]
            
            start = time.time()
            strassen.main()
            end = time.time()
            
            times.append(end - start)
        bestN.append(nOpts[times.index(min(times))])
        
        plt.plot(nOpts, times, label=f"Dimension: {d}")
        plt.title("n values as a function of time")
        plt.xlabel("nOpt Values")
        plt.ylabel("Time")
        plt.legend()
    plt.show()

    bestN.sort()
    
    print(f"Average: {np.mean(bestN)}")
    print(f"Mode: {mode(bestN)}")
    print(f"Median: {bestN[(len(bestN) - 1) // 2]}")
    


def findCross():
    Ds = [2, 4, 8, 16, 32]

    sTimes = []
    nTimes = []
    for i, d in enumerate(Ds):
        
        sys.argv = ["strassen.py", "0", f"{d}", f"test{i}.txt"]
        
        start = time.time()
        cross_over.main()
        end = time.time()
        
        sTimes.append(end - start)
        
        start = time.time()
        cross_over.main(False)
        end = time.time()
        
        nTimes.append(end - start)
        
    plt.plot(Ds, sTimes, label="Strassen's algorithm")
    plt.plot(Ds, nTimes, label="Traditional Matrix Mult")
    plt.xlabel("Dimension of Matrix")
    plt.ylabel("Time to Exevute Multiplication")
    plt.title("Strassen vs Traditional Matrix Multiplication")
    plt.legend()
    plt.show()
    
findCross()