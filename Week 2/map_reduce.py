import sys
from itertools import groupby
import wget

# Create a map function
def mapfunc(w):
    # Let us remove all puncuation and spaces.  
    cleanword = ''.join([i for i in w if i.isalpha()])
    return [cleanword,1]

# Create a reduce function
def reducefunc(key, values):
    counts = [x[1] for x in values]
    return [key,sum(counts)]

def main():
    url = "https://www.gutenberg.org/cache/epub/1777/pg1777.txt"
    filename = wget.download(url)
    print(f"Downloaded {filename}")
    with open(filename) as f:
        words = [word for line in f for word in line.split()]
    print("The words is")
    print(words)
    print("")
    map_result = map(mapfunc, words)
    map_result_sorted = sorted(map_result, key = lambda x: x[0])
    for res in map_result_sorted:
        print(res)
    print("")
    reduce_result = []
    for k, g in groupby(map_result_sorted, key = lambda x: x[0]):
        reduce_result.append(reducefunc(k, list(g)))
    print("Reduce Result")
    for res in reduce_result:
        print(res)
    print("")


if __name__ == "__main__":
    main()