# 链表结构
class ListNode(object):
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkList(object):
    def __init__(self):
        self.head = None  # 指向链表头元素的指针

    # 在链表末尾插入新结点
    def add_to_tail(self, value):
        """
        :param value: 新插入的值
        :return: None
        """
        newnode = ListNode()
        newnode.value = value
        newnode.next = None
        if self.head is None:  # 空链表
            self.head = newnode
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = newnode

    # 找到第一个含有某值的结点并删除
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
        else:
            node = self.head
            while node.next is not None and node.next.value != value:
                node = node.next
            if node.next is not None and node.next.value == value:
                node.next = node.next.next

    # 从头到尾打印链表
    def print_linklist(self):
        """
        比如 输入链表[1,2,3,4]表头指针，输出字符串 1 -> 2 -> 3 -> 40
        """
        string = ""
        if self.head is not None:
            node = self.head
            while node.next is not None:
                string += str(node.value) + " -> "
                node = node.next
            string += str(node.value)
        print(string)

    # 从尾到头打印链表（栈，循环）
    def rprint_linklist(self):
        if self.head is None:
            return
        stack = []
        node = self.head
        while node is not None:
            stack.append(node)
            node = node.next
        while stack:
            node = stack.pop()
            print(node.value)

    # 从尾到头打印链表（递归）
    def rprint_linklist_recursively(self, phead=None):
        node = phead if phead else self.head
        if node:
            if node.next:
                self.rprint_linklist_recursively(node.next)
            print(node.value)

    # 删除有序链表中的重复结点
    def delete_duplication(self):
        if self.head is None:
            return

        pre_node = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            delete = False
            if next_node and cur_node.value == next_node.value:
                delete = True

            if not delete:
                pre_node = cur_node
                cur_node = cur_node.next
            else:
                value = cur_node.value
                while cur_node and cur_node.value == value:
                    cur_node = cur_node.next

                if not pre_node:
                    self.head = cur_node
                else:
                    pre_node.next = cur_node

    # 找到倒数第K个结点
    def find_kth_tail(self, k):
        if not self.head or k <= 0:
            return

        ahead = self.head
        behind = None

        for i in range(1, k):
            if ahead.next:
                ahead = ahead.next
            else:
                return

        behind = self.head
        while ahead.next:
            ahead = ahead.next
            behind = behind.next

        return behind


# 删除链表中的一个结点，要求O(1)时间，假设结点在链表中
def delete_node(list_head, node):
    if not list_head or not node:
        return

    if node.next is not None:  # 要删除的结点不是尾结点
        node.value = node.next.value
        node.next = node.next.next
    elif list_head == node: # 链表中只有一个结点
        list_head = None
    else:  # 链表中有多个结点，删除尾结点
        current_node = list_head
        while current_node.next != node:
            current_node = current_node.next
        current_node.next = None


# 反转链表
def reverser_list(head):
    if head is None:
        return

    reversed_head = None
    pre_node = None
    cur_node = head

    while cur_node:
        next_node = cur_node.next
        if next_node is None:
            reversed_head = cur_node

        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node

    return reversed_head


# 合并两个排序链表
def merge_list(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    merged_head = None

    if head1.value < head2.value:
        merged_head = head1
        merged_head.next = merge_list(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = merge_list(head1, head2.next)

    return merged_head


if __name__ == '__main__':
    linklist = LinkList()
    linklist.add_to_tail(1)
    linklist.add_to_tail(2)
    linklist.add_to_tail(3)
    node = linklist.find_kth_tail(4)
    # linklist.print_linklist()
    # linklist.delete(2)
    # linklist.rprint_linklist()
    print(node)
