import argparse
import quicksort
import Fib
import mergesort
import dictionary

def run_function():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-n', action="store", dest="temp", help="sss")
    args = parser.parse_args()
    if(args.temp == 'quicksort'):
        quicksort.quick_sort_main()
    elif (args.temp == 'mergesort'):
        mergesort.merge_sort_main()
    elif (args.temp == 'fib'):
        Fib.fib_main()
    else:
        dictionary.dictionary_main()
if __name__ == "__main__":
    run_function()