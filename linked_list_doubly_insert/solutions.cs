public static DoublyLinkedListNode sortedInsert(DoublyLinkedListNode llist, int data)
{
    DoublyLinkedListNode newdata = new DoublyLinkedListNode(data);
    if(llist == null){
        return newdata;
    }
    if(data < llist.data){
        newdata.next = llist;
        llist.prev = newdata;
        return newdata;
    }
    DoublyLinkedListNode current = llist;
    while(current.next != null && current.next.data < data){
        current = current.next;
    }
    newdata.next = current.next;
    newdata.prev = current;
    if(current.next != null){
        current.next.prev = newdata;
    }
    current.next = newdata;
    return llist;
}