class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head, val):
    pre = head
    while pre.next is not None:
        if pre.next.val == val:
            pre.next = pre.next.next
        else:
            pre = pre.next
    result = []
    head = head.next
    while head.next is not None:
        result.append(head.val)
        head = head.next
        result.append(head.val)
    print(list(set(result)))


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    val = 1

    # list转链表
    ## 新建虚拟head
    v_head = ListNode(val=0)
    pre = v_head

    # 转换列表
    for n in nums:
        pre.next = ListNode(val=n)
        pre = pre.next
    pre = v_head

    # 删除元素
    remove_elements(pre, val)
