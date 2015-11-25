class Elem(object):
    _slots_ = ["value", "next"]

    def _repr_(self):
        return "({}, {})".format(self.value, self.next)

def new_elem(value):
    elem = Elem()
    elem.value = value
    elem.next = None
    return elem

def append(head, value):
    end = head
    while end.next is not None:
        end = end.next
    end.next = new_elem(value)
    return head

def insert(head, index, value):
    if index == 0:
        new = new_elem(value)
        new.next = head
        return new


def insert(head, index, value):
    prev = head
    i = 0
    while i < index-1:
        prev = prev.next

    new = new_elem(value)
    new.next = prev.next
    prev.next = new

    return prev

def remove(head,index):
      if index==0:
          head=head.next
          return head

      prev=head
      i=0
      while i<index-1:
          prev=prev.next
          i+=1

      prev.next=prev.next.next
      return head
