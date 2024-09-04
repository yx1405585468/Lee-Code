class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def exchange(head):
    if head is None or head.next is None:
        return head
    head_t = head
    while head:
        temp = head.next.next
        a = head.next.val
        head.next.val = head.val
        head.val = a
        head = temp
    get_list(head_t)


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
    nums = [1, 2, 3, 4]

    # 虚拟头节点
    head_v = ListNode(val=0)
    temp = head_v

    for i in nums:
        head_v.next = ListNode(val=i)
        head_v = head_v.next

    listnode = temp.next

    exchange(listnode)
