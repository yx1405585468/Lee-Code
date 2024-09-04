class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def tranverse_listnode(list_node):
    pre = None
    current = list_node
    while current:
        temp = current.next
        current.next = pre

        pre = current
        current = temp
    get_list(pre)


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
    nums = [1, 2, 3, 4, 5, 6]

    # 虚拟头节点
    head_v = ListNode(val=0)
    temp = head_v

    for i in nums:
        head_v.next = ListNode(val=i)
        head_v = head_v.next

    listnode = temp
    tranverse_listnode(listnode)
