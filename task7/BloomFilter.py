from bitarray import bitarray
import sys
import math


class BitArray:
    def __init__(self, size):
        self.array = [0] * size

    def set(self, index):
        self.array[index] = 1

    def read(self, index):
        return self.array[index]


class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = BitArray(size)

    def add(self, line):
        for key in range(self.num_hashes):
            result = hash("-".join([str(key),line])) % self.size
            self.bit_array.set(result)


    def lookup(self, line):
        for key in range(self.num_hashes):
            result = hash("-".join([str(key),line])) % self.size
            if self.bit_array.read(result) == 0:
                return False
        return True


entries = int(sys.argv[1])
bf = BloomFilter(10 * entries, int(math.ceil(10 * math.log(2,math.e)/entries)))



for line in sys.stdin:
    line = line.strip()
    if not bf.lookup(line):
        bf.add(line)
        print line
