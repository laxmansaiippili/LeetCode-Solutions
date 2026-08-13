# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head;
        fast=head;
        while fast and fast.next:
            fast=fast.next.next;
            slow=slow.next;
        prev=None;
        while slow:
            slow.next,prev,slow=prev,slow,slow.next;
        fast=head;
        slow=prev;
        while slow and fast:
            if(slow.val!=fast.val):
                return False;
            slow=slow.next;
            fast=fast.next;
        return True;