class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_n_daoshu(head, n):
    head_v = ListNode(val=0)
    head_v.next = head
    head = head_v
    fast1 = head
    slow1 = head
    fast = fast1
    slow = slow1

    for i in range(n):
        fast1 = fast1.next

    while fast1:
        if fast1.next is None:
            slow1.next = slow1.next.next
            break
        fast1 = fast1.next
        slow1 = slow1.next

    get_list(slow.next)


def get_list(listnode):
    head = listnode
    result = []
    while listnode.next is not None:
        result.append(listnode.val)
        listnode = listnode.next
    result.append(listnode.val)
    listnode = head
    print(result)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    n = 8

    # 虚拟头节点
    head_v = ListNode(val=0)
    temp = head_v

    for i in nums:
        head_v.next = ListNode(val=i)
        head_v = head_v.next

    listnode = temp.next

    delete_n_daoshu(listnode, n)
