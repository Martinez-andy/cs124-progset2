# test_strasen.py
import sys
from strassen import main  # Import your strassen.py module

def test():
    file = "strassen.py"

    # Set sys.argv with script name, flag, dimension, and filename
    sys.argv = [file, "0", "2", "test1.txt"]
    main()

    # Set sys.argv for the second test
    sys.argv = [file, "0", "3", "test2.txt"]
    main()

test()
