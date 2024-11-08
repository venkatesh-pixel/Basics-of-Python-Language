'''In Python, a set is an unordered collection of unique elements. 
Sets are very useful when you need to store multiple items but don't care about the order or need to eliminate duplicates from a collection. 
Sets are one of the built-in data types in Python, and they are part of the collection module.

Key Characteristics of a Set:
1) Unordered: The items in a set have no specific order, meaning that the elements are not indexed, and the order in which items are stored or displayed is not guaranteed to be the same.
2) Unique Elements: A set cannot have duplicate elements. If you try to add a duplicate item to a set, it will automatically be ignored.
3) Mutable: A set is mutable, meaning that you can add or remove elements from it after creation. However, the elements themselves must be immutable (e.g., numbers, strings, and tuples).

No Indexing: Unlike lists and tuples, sets do not support indexing or slicing. You can't access elements by their position.'''

# from collections import defaultdict
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# c = a.difference(b)
# print(c)  # removes the common value and display's the remaining value of the 1st element
#
# c = a.union(b)
# print(c)  # combines 2 set and removes duplicate values
#
# print(a.intersection(b))   # prints only common values in the 2 sets
#
# print(a.isdisjoint(b)) # prints "TRUE" if 2 sets have different values and prints "FALSE" if two sets have common values
#
#
# d = {1,2}
# e = {1,2,3,4}
# print(d.issubset(e)) # prints TRUE if the value of 1st set present in the 2nd set
#
# charu = {1,2,3,4,5,6}
# names = {1,2,3,4}
# print(charu.issuperset(names))  # prints TRUE if the value of 2nd set is present in 2nd set
#
# data ={1,2,3,4}
# data.remove(2)
# print(data) # removes the exact value given by the user
#
# data.discard(3)
# print(data)
#
# datas = {1,2,4}
# datas.add('charu') # add the value given by the user
# print(datas)
#
# datas.pop()
# print(datas)   # removes the value unordered
#
#
# datas.clear()
# print(datas)
#
#
# # set is an unordered collection data type
# # set is a mutable data type
# # where the values in the values are hashable
# # duplicate values
#
# sentence = "hello world welcome to python hello hi hello hello"
# word_count = defaultdict(int)
# words = sentence.split()
# for word in words:
#     word_count[word] += 1
# print(word_count)
#
# s = 'abracadabraca'
# chr_count = defaultdict(int)
# for c in s:
#     chr_count[c] += 1
# print(chr_count)
