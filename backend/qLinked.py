class Qnode:
    def __init__(self,data):   #Node for the queue linkedList
        self.data= data 
        self.next= None
    
class QlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return self.head is None
    
    # ex:- queue.enqueue(10)
    def enqueue(self,data): #when this method is called it creates a queue object(self)
        new_node=Qnode(data) #the value assigns when creating the queue object get passed to new node(data)
        if self.tail is None:
            self.head=self.tail=new_node #if the queue is empty the head and tail gets assigned to 1st node
        else:
            self.tail.next=new_node
            self.tail=new_node
        print(f"Task added: {data}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Cannot dequeue.")
            return None
        
        result=self.head.data #store the data to return
        self.head=self.head.next  #move pointer to next pointer

        if self.head is None:
            self.rear = None
        print(f"Dequeued: {result}")

        