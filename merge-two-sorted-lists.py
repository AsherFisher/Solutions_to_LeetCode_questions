class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if not list1 and not list2:
            return list1

        if not list1:
            return list2

        if not list2:
            return list1

        head = current = ListNode()

        if list1.val < list2.val:
            head.val = list1.val
            list1 = list1.next
        else:
            head.val = list2.val
            list2 = list2.next

        while list1 is not None and list2 is not None:
            temp = ListNode()

            if list1.val < list2.val:
                temp.val = list1.val
                current.next = temp
                current = current.next
                list1 = list1.next

            else:
                temp.val = list2.val
                current.next = temp
                current = current.next
                list2 = list2.next

        while list1 is not None:
            temp = ListNode()
            temp.val = list1.val
            current.next = temp
            current = current.next
            list1 = list1.next

        while list2 is not None:
            temp = ListNode()
            temp.val = list2.val
            current.next = temp
            current = current.next
            list2 = list2.next

        return head


if __name__ == "__main__":
    ListNode1 = ListNode(1, ListNode(2, ListNode(4, None)))
    ListNode2 = ListNode(1, ListNode(3, ListNode(4, None)))

    res = Solution().mergeTwoLists(ListNode1, ListNode2)

    i = 0
    while res is not None:
        print(res.val)
        res = res.next

