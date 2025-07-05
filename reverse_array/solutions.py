def reverse(llist):    
    previous_node = None
    while (llist):
        next_node = llist.next
        llist.next = previous_node
        previous_node = llist
        llist = next_node
    return previous_node