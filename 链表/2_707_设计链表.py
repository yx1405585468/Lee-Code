class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self, listnode):
        self.listnode = listnode

    def get(self, index):
        temp = self.listnode  # 保存头节点
        i = 0
        result = None
        while self.listnode:
            if i == index:
                result = self.listnode.val
                break
            i += 1
            self.listnode = self.listnode.next
        self.listnode = temp
        self.get_list()  # 打印list
        return result if result else -1

    def addAtHead(self, val):
        head = ListNode(val)
        head.next = self.listnode
        self.listnode = head
        self.get_list()

    def addAtTail(self, val):

        head = self.listnode
        while self.listnode:
            if self.listnode.next is None:
                self.listnode.next = ListNode(val=val)
                break
            else:
                self.listnode = self.listnode.next
        self.listnode = head
        self.get_list()

    def get_list(self):
        head = self.listnode
        result = []
        while self.listnode.next is not None:
            result.append(self.listnode.val)
            self.listnode = self.listnode.next
        result.append(self.listnode.val)
        self.listnode = head
        print(result)

    def addAtIndex(self, index, val):
        head = self.listnode

        n = 0
        while self.listnode:
            if n == index - 1:
                temp = self.listnode.next
                self.listnode.next = ListNode(val=val)
                self.listnode = self.listnode.next
                self.listnode.next = temp
                break
            n = n + 1
            self.listnode = self.listnode.next
        self.listnode = head
        self.get_list()

    def deleteAtIndex(self, index, val):
        head = self.listnode

        n = 0
        while self.listnode:
            if n == index - 1:
                self.listnode.next = self.listnode.next.next
                break
            n = n + 1
            self.listnode = self.listnode.next
        self.listnode = head
        self.get_list()


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 转换成node_list
    ## 创建虚拟头节点
    v_head = ListNode(val=0)
    nums_node = v_head

    # 初始化list到链表
    for i in nums:
        v_head.next = ListNode(val=i)
        v_head = v_head.next

    # 去掉虚拟头节点
    nums_node = nums_node.next
    ml = MyLinkedList(nums_node)
    print(ml.get(index=5))
    ml.addAtHead(-1)
    ml.addAtTail(99)
    ml.addAtIndex(3, 99)
    ml.deleteAtIndex(3, 99)
