# test_strasen.py
import sys

def main():
    sizes = [2, 4, 8, 16, 32, 64, 128, 256]
    
    for i, d in enumerate(sizes):
        with open(f"test{i}.txt", "w") as file:
            for _ in range(2):
                for j in range(1, (d ** 2) + 1):
                    file.write(f"{j}\n")
                    
main()