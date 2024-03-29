# test_strasen.py
import sys
  # Import your strassen.py module

def main():
    with open("test7.txt", "w") as file:
        for _ in range(2):
            for i in range(1, 101):
                file.write(f"{i}\n")
                
main()