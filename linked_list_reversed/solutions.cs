    public static SinglyLinkedListNode reverse(SinglyLinkedListNode llist)
    {
        SinglyLinkedListNode prev = null;
        SinglyLinkedListNode curr = llist;
        
        while(curr !=  null){
            SinglyLinkedListNode tempcurr = curr.next;
            curr.next = prev;
            prev= curr;
            curr = tempcurr;
        }
        return prev;

    }