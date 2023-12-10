class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def create_linked_list(nodes):
    try:
        nodes = [int(node) for node in nodes]
        nodes.sort()
    except ValueError:
        raise ValueError("Please enter only integers in the list.")
    
    dummy = ListNode()
    current = dummy

    for node_value in nodes:
        current.next = ListNode(node_value)
        current = current.next

    return dummy.next

def print_linked_list(head):
    while head is not None:
        print(head.value, end="")
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print()

try:
    list1_input = list(map(int, input("Enter values for linked list 1 (space-separated integers): ").split()))
    list2_input = list(map(int, input("Enter values for linked list 2 (space-separated integers): ").split()))

    list1 = create_linked_list(list1_input)
    list2 = create_linked_list(list2_input)

    result = merge_sorted_lists(list1, list2)

    print("Merged List:")
    print_linked_list(result)
except ValueError as e:
    print(f"Error: {e}")
