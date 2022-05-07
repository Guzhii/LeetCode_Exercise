# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.l = iterator
        self.nextt = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.nextt != None:
            return self.nextt
        else:
            nextE = self.l.next()
            self.nextt = nextE
            return nextE
        

    def next(self):
        """
        :rtype: int
        """
        if self.nextt != None:
            nextE = self.nextt
            self.nextt = None
            return nextE
        else:
            nextE = self.l.next()
            return nextE
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nextt != None:
            return True
        else:
            return self.l.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
