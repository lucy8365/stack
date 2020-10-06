class Stack:
    def __init__(self,size):
        if isinstance(size, int):
            self.size = size
        else:
            self.size = 0
            print("default used")

        self.stack = [None] * size
        self.top = -1
        print("your stack has been created")

    # def create_list(self):
    #     lst = input.split()
    #     return lst

    def isEmpty(self):
        # len looks @ how many values are in the stack this is 0 if its empty
        if self.top == -1:
            #boolean value is returned
            return True
        else:
            #boolean value is returned
            return False

    def isFull(self):
        # checking if the stack is complelty full by looking @ the len
        if self.top == self.size:
            print("the stack is full")
            #boolean value is returned
            return True
        else:
            #boolean value is returned
            return False


    def push(self,stack):
        #validates that the item is a string
        if isinstance(stack, str):
            if not self.isFull():
                self.top += 1
                self.stack[self.top] = stack
                # if the stack is NOT full then item is added
                #append adds to the end
                #sucess is shown to the used
                print("ITEM HAS BEEN ADDED")
            else:
                #if the stack is full then it won't work
                print("error, stack is full!")
        else:
            #shows an error is the item is not a str
            print("ERROR")



    def pop(self):
        # if the stack is empty nothing can be popped so an error will show
        if self.isEmpty():
            print("STACK EMPTY, INVALID REQUEST")
            #else the top value will be popped
        else:
            self.top -= 1
            return self.stack[self.top]
            #the request is valid so it is popped
            #returns it


    def peek(self):
        # if the stack is empty there is nothing to peek so its invalid
        if self.isEmpty():
            print("STACK EMPTY, INVALID REQUEST")
        else:
            # -1 prints the value at the very top of the stack
            print(self.stack[self.top])


# push = .append
# pop = .pop
#TESTING
newStack = Stack(15)
newStack.push("www.dubaicollege.org")
newStack.push("www.misguided.com")
newStack.push("www.urban.com")

newStack.peek()
#
# x = ["www.bbc.co.uk"]
# y = ["www.dubaicollege.org"]
# stack = self.stack.append(x)
# print(stack)
