#video link: https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=8
#Using a list as a stack
#The propblem with list is, if it reaches the maximum size then it allocates double the size in new location and all the data will be copied to that location. Performance impact.
#The issue with using a list as a stack is that list uses dymanic array internally and when it reaches its capacity it will reallocate a big chunk of memory somewhere else in memory area and copy all the elements. For example in below diagram if a list has a capacity of 10 and we try to insert 11th element, it will not allocate new memory in a different memory region, copy all 10 elements and then insert the 11th element. So overhead here is (1) allocate new memory plus (2) copy all existing elements in new memory area
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

print(s)
print(s.pop())
print(s)
print(s[-1])
print(s)