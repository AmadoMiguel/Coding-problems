orders = {}
ordId = 100

def itemsAndId(M):
    global orders
    global ordId
    if M > 0:
        order = raw_input("Enter product: ")
        orders[order] = ordId
        ordId += 1
        itemsAndId(M-1)
log = []
def record(order_id):
    global orders
    global log
    if order_id <= orders.values()[-1]:
        log.append(order_id)
        record(order_id+1)
def get_last(i):
    global log
    return log[i-1]

# Ask the user to fill in the cart
nItems = raw_input("How many items you wish to order?: ")
itemsAndId(int(nItems))
# Ask the user to prompt in the number of last records to a log
lastItsToLog = int(raw_input("Last N records to add to log: "))
record( orders.values()[-1]-(lastItsToLog-1) )
print(log)
# Ask the user to promp in the id of the ith last record
lastIthInLog = int(raw_input("Which of the last records id you wish to view?: "))
print( get_last(lastIthInLog) )