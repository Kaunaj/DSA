class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        currentNode = self.head

        while (currentNode):
            print("Node", currentNode.data)
            currentNode = currentNode.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    sampleLinkedList = LinkedList()

    sampleLinkedList.head = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)

    sampleLinkedList.head.next = secondNode
    secondNode.next = thirdNode

    sampleLinkedList.printLinkedList()
