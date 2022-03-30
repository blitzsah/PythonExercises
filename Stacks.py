# A Stack is a LIFO system - Last In First Out

browsing_session = []
browsing_session.append(1)  # add an item to the stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()  # remove the top item in the stack
print(last)
if not browsing_session:   # Check to see if there is anything in the stack
    top_item = browsing_session[-1]  # returns the top item in the stack
