# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_node = l1
        num2_node = l2

        num1 = ""
        num2 = ""

        while num1_node or num2_node:
            if num1_node:
                num1 += str(num1_node.val)
                num1_node = num1_node.next
            if num2_node:
                num2 += str(num2_node.val)
                num2_node = num2_node.next
        print(f"{num1[::-1]}, {num2[::-1]}")
        result = int(num1[::-1]) + int(num2[::-1])

        result_str = reversed(str(result))
        result_node = None
        current_node = None
        for char in result_str:
            if not result_node:
                result_node = ListNode(int(char), None)
                current_node = result_node
            else:
                current_node.next = ListNode(int(char), None)
                current_node = current_node.next
        return result_node
