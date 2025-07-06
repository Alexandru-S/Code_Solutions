    public static DoublyLinkedListNode reverse(DoublyLinkedListNode llist)
    {
        DoublyLinkedListNode? curr = llist;
        DoublyLinkedListNode? prev = null;
        
        while(curr != null){
            prev = curr.prev;
            curr.prev = curr.next;
            curr.next = prev;
            curr = curr.prev;
        }
        if(prev != null){
            llist = prev.prev;
        }
        return llist;
    }