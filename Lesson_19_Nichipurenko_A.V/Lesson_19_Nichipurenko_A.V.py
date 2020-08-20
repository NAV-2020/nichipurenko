"""
import struct

ls = [1,3,9,12]
obj = struct.pack('>4i', ls[0], ls[1], ls[2], ls[3])
size = struct.calcsize('>3f')
print('obj:', obj)
print('size', size)
"""

import pickle

#pickle.dump(object, )

my_list = [1,2,3,4,5]

f = open('my_file.bin', 'wd')

pickle.dump(my_list, f)


f.close()