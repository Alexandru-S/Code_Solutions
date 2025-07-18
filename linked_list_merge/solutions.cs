static SinglyLinkedListNode mergeLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
    if(head2 == null && head1 == null){
        return null;
    }
    if(head1 ==null){
        return head2;
    }
    if(head2 == null){
        return head1;
    }
    SinglyLinkedListNode dummy = new SinglyLinkedListNode(0);
    SinglyLinkedListNode node = dummy;
    while(head1 != null && head2 != null){
        if(head1.data <= head2.data){
            node.next = head1;
            head1 = head1.next;
            
        }else{
            node.next = head2;
            head2 = head2.next;
        }
        node = node.next;
    }
    if(head1 == null){
        node.next = head2;
    }else{
        node.next = head1;
    }
    return dummy.next;
}
