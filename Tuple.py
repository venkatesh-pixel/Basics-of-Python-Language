'''In Python, a tuple is an ordered, immutable collection of elements. Tuples are similar to lists, but they have key differences—chiefly, immutability. 
Once a tuple is created, its contents cannot be modified, which makes tuples a useful data structure in scenarios where immutability is required. 
Tuples can hold heterogeneous data types, such as integers, strings, floats, or even other tuples, and they can be nested.

Key Characteristics of Tuples
1) Ordered: Tuples maintain the order of elements. When you create a tuple, the elements retain their positions (indexes).
2) Immutable: Once a tuple is created, you cannot change, add, or remove elements from it.
              This immutability provides benefits in terms of performance, as well as making tuples hashable (which allows them to be used as keys in dictionaries).
3) Heterogeneous: Tuples can store different types of data (e.g., integers, floats, strings, lists, etc.) in the same tuple.
4) Allow Duplicates: Like lists, tuples allow duplicate values. If you create a tuple with duplicate elements, they are retained.
5) Indexing and Slicing: Tuples support indexing and slicing just like lists, which means you can access and manipulate subsets of the tuple.'''

# # tuples are homogenous and hetrogenous data items that are enclosed with a pair of parenthesis ().
# # tuples are immutable in nature
# # tuples can hold duplicate data values
# # tuples are hetrogenous in nature.
# import sys
#
# t = ('steve','charu','vasuki','venkatesh')
# w = list(t)
# f = set(t)
# print(f)  # {'vasuki', 'steve', 'charu', 'venkatesh'}
# f.add('vishnu')
# print(f)  # {'steve', 'vasuki', 'charu', 'vishnu', 'venkatesh'}
# print(w)  # ['steve', 'charu', 'vasuki', 'venkatesh']
# w.append('chitra')
# print(w)   # ['steve', 'charu', 'vasuki', 'venkatesh', 'chitra']
# print(tuple(w))  # ('steve', 'charu', 'vasuki', 'venkatesh', 'chitra')
#
# """note: low priority if we want to modify tuple we have to typecast with modified data types"""
# print(dir(f))
#
# tuple = (('steve',2),('charu',4),('vasuki',6),('venkatesh',1))
#
# a = dict(tuple)
# print(a)  # {'steve': 2, 'charu': 4, 'vasuki': 6, 'venkatesh': 1}
#
#
# t = (2,3,4,4,4,5)
# print(t.count(4))
#
# t = (2,3,4,5,6)
# print(t.index(6))
#
# # ------------------------------------------------------------------------------------------------------------------
# a_list = [1,2,3,4,5]
# a_tuple = (1,2,3,4,5)
#
# print(sys.getsizeof(a_list))
# print(sys.getsizeof(a_tuple))
#
# # ----------------------------------------------------------------------------------------------------------------------
#
