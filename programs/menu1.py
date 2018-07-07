# Menu driven program allows user to perform actions on queue data
def push(queue, item):
    """Push or insert an item into the queue"""
    queue.append(item)

def pop(queue):
    """Pop / remove first item from queue"""
    value = False  # Indicated the queue is empty
    if len(queue)!=0:
        value = queue[0]
        queue.remove( queue[0] )
    return value

def print_queue(queue):
    """Prints the queue"""
    print(queue)

def my_menu():
    choice = 1
    queue = []
    while choice:
      print("1. Push")
      print("2. Pop")
      print("3. Print")
      print("0. Exit")
      choice = int(input("Enter the choice (0 to 3) : "))

      if choice == 1:
          item = int(input("Enter the item : "))
          push(queue,item)
      elif choice == 2:
          item = pop(queue)
          if item:
              print(f"{item} popped!")
          else:
              print("Queue is empty.....!")
      elif choice == 3:
          print_queue(queue)
      elif choice!=0:
          print("Invalid choice!!! Reenter please")

# menu call
my_menu()
