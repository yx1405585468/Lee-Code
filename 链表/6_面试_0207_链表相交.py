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

    # 在每个链表的头部初始化两个指针
    pointerA = headA
    pointerB = headB

    # 遍历两个链表直到指针相交
    while pointerA != pointerB:
        # 将指针向前移动一个节点
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    # 如果相交，指针将位于交点节点，如果没有交点，值为None
    return pointerA


if __name__ == '__main__':
    listA = [4, 1]
    listB = [5, 0, 1]
    listC = [8, 4, 5]

    node_A = build_list(listA)
    node_B = build_list(listB)
    node_C = build_list(listC)

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

    list_node_xiangjiao(node_A, node_B)
