# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        pass
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_list = list()
        temp = head
        if temp == None:
            return None
        elif temp.next == None:
            return temp

        while temp != None:
            my_list.append(temp)
            temp = temp.next

        head2 = my_list[len(my_list) - 1]
        for i in range(len(my_list)):
            temp2 = my_list[len(my_list) - 1 - i]
            if i == len(my_list) - 1:
                temp2.next = None
                break
            temp2.next = my_list[len(my_list) - 2 - i]
            temp2 = temp2.next
        return head2
