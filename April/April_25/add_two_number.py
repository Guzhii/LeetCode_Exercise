class Solution:
    def myAddTwoNumbers(self, l1, l2, carry):
        if carry == 0:
            if (l1 == None) & (l2 == None):
                return None
        
            if (l1 == None):
                return l2
            
            if (l2 == None):
                return l1
            
            tmp = l1.val + l2.val 
            if tmp >= 10:
                return ListNode(tmp%10, self.myAddTwoNumbers(l1.next, l2.next, 1))
            else:
                return ListNode(tmp, self.myAddTwoNumbers(l1.next, l2.next, 0))
        
        else:
            if (l1 == None) & (l2 == None):
                return ListNode(1, None)
        
            if (l1 == None):
                l1 = ListNode(0, None)
            
            if (l2 == None):
                l2 = ListNode(0, None)
            
            tmp = l1.val + l2.val + 1
            if tmp >= 10:
                return ListNode(tmp%10, self.myAddTwoNumbers(l1.next, l2.next, 1))
            else:
                return ListNode(tmp, self.myAddTwoNumbers(l1.next, l2.next, 0))
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        return self.myAddTwoNumbers(l1, l2, 0)
