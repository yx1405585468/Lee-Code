# Definition for singly-linked list.
import time


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def ring_list(head):
    # fast = head
    # slow = head
    #
    # while fast.next.next != slow.next:
    #     fast = fast.next.next
    #     slow = slow.next
    # if slow.next:
    #     print("有环")

    # # 不断遍历链表，如果有环，说明有节点被重复走了两次，把每一步的节点存在集合里，
    ## 继续遍历，如果新增的节点在集合里，说明有环，同时也知道了入口
    node_set = set()
    while head:
        if head in node_set:
            print(head.val)
            break
        node_set.add(head)
        head = head.next

    return None


def build_list_ring(list_):
    head_v = ListNode(val=0)
    temp = head_v

    for i in list_:
        if i == 5:
            ring_index = head_v
        head_v.next = ListNode(val=i)
        head_v = head_v.next
    head_v.next = ring_index
    # print(ring_index.val)

    listnode = temp.next
    # print(listnode.val)
    return listnode


def get_list(listnode):
    head = listnode
    while listnode.next is not None:
        print(listnode.val)
        listnode = listnode.next
        time.sleep(1)
    listnode = head
    print(listnode.val)


if __name__ == '__main__':
    # 构造一个环型链表
    a_list = [1, 2, 3, 4, 5, 6, 7]
    n_list = build_list_ring(a_list)
    # get_list(n_list)
    ring_list(n_list)
