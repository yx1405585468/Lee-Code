class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(list_):
    head_v = ListNode(val=0)
    temp = head_v

    for i in list_:
        head_v.next = ListNode(val=i)
        head_v = head_v.next

    listnode = temp.next
    return listnode


def get_list(listnode):
    head = listnode
    result = []
    while listnode.next is not None:
        result.append(listnode.val)
        listnode = listnode.next
    result.append(listnode.val)
    listnode = head
    print(result)


def list_node_xiangjiao(headA, headB):
    # 处理边缘情况
    if not headA or not headB:
        return None
    # 保存头指针
    headA_ = headA
    headB_ = headB
    # 计算headA 的长度
    n = 1
    while headA:
        if headA.next is None:
            break
        headA = headA.next
        n += 1

    # 计算headB 的长度
    m = 1
    while headB:
        if headB.next is None:
            break
        headB = headB.next
        m += 1
    if m > n:
        for i in range(m - n):
            headB_ = headB_.next
    elif m < n:
        for i in range(n - m):
            headA_ = headA_.next
    m = min(m, n)

    for i in range(m):
        if headB_ == headA_:
            print(headB_.val)
            break
        headB_ = headB_.next
        headA_ = headA_.next
    return headB_


if __name__ == '__main__':
    # 原数据
    listA = [4, 1]
    listB = [5, 0, 1]
    listC = [8, 4, 5]

    # 构造链表
    node_A = build_list(listA)
    node_B = build_list(listB)
    node_C = build_list(listC)

    # 保存头指针
    head_A = node_A
    head_B = node_B

    while node_A:
        if node_A.next is None:
            node_A.next = node_C
            break
        node_A = node_A.next

    while node_B:
        if node_B.next is None:
            node_B.next = node_C
            break
        node_B = node_B.next
    #

    list_node_xiangjiao(head_A, head_B)
