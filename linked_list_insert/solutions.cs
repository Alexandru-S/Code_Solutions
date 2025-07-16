public static SinglyLinkedListNode insertNodeAtPosition(SinglyLinkedListNode llist, int data, int position)
{
    SinglyLinkedListNode newdata = new SinglyLinkedListNode(data);
    if(position == 0){
        newdata.next = llist;
        return newdata;
    }
    SinglyLinkedListNode curr = llist;
    for(int i = 0; i< position -1 && curr != null; i++){
        curr = curr.next;
    }
    newdata.next = curr.next;
    curr.next = newdata;
    return llist;
}
