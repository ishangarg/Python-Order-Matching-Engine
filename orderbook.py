from utils import curr_time_milli


class Match():
    ask = None
    bid = None
    price = 0
    fill_size = 0

    def __init__(self, ask, bid):
        if not type(ask) == Order or not type(bid) == Order:
            raise TypeError("ask and bid must be of type Order")
        
        self.ask = ask
        self.bid = bid
        self.price = 0
        self.fill_size = 0

class OrderBook():
    Bids = []
    Asks = []

    BidLimits = {}
    AskLimits = {}

    def __init__(self):
        self.Bids = []
        self.Asks = []
        self.BidLimits = {}
        self.AskLimits = {}

    def place_order(self, price: float, order) -> Match:
        # TODO: Implement the matching logic

        if (order.size > 0):
            self.add_order(price, order)
        
        return None

    def add_order(self, price, order):
        limit = None
        if order.isBid:
            if price in self.BidLimits:
                limit = self.BidLimits[price]
            else:
                limit = Limit(price)
                self.BidLimits[price] = limit
                self.Bids.append(limit)
        else:
            if price in self.AskLimits:
                limit = self.AskLimits[price]
            else:
                limit = Limit(price)
                self.AskLimits[price] = limit
                self.Asks.append(limit)
        limit.add_order(order)

    def SortByBestAsk(self):
        self.Asks.sort(key=lambda x: x.price)

    def SortByBestBid(self):
        self.Bids.sort(key=lambda x: x.price, reverse=True)

class Limit():
    price = 0
    orders = []
    total_volume = 0

    def __init__(self, price):
        self.price = price
        self.orders = []
        self.total_volume = 0

    def add_order(self, order):
        order.limitIndex = len(self.orders)
        order.limit = self
        self.orders.append(order)
        self.total_volume += order.size
        self.sort_by_time()

    def find_order(self, id):
        for order in self.orders:
            if order.id == id:
                return order
        return None

    def delete_order(self, order):
        self.orders.pop(order.limitIndex)
        self.total_volume -= order.size
        for i in range(order.limitIndex, len(self.orders)):
            self.orders[i].limitIndex -= 1
        self.sort_by_time()
    
    def sort_by_time(self):
        self.orders.sort(key=lambda x: x.timestamp)
    
    def __str__(self):
        return "Price: %s | Volume: %s" % (self.price, self.total_volume)

class Order():
    id = None
    timestamp = None
    isBid = None
    size = 0
    limitIndex = None
    limit = None
    
    def __init__(self, id, isBid, size):
        self.id = id
        self.timestamp = curr_time_milli()
        self.isBid = isBid
        self.size = size
    
    def __str__(self): 
        return "ID: %s | Size: %s" % (self.id, self.size) 
    

def NewBidOrder(id, size):
    return Order(id, True, size)

def NewAskOrder(id, size):
    return Order(id, False, size)

def NewOrder(id, isBid, size):
    if isBid:
        return NewBidOrder(id, size)
    return NewAskOrder(id, size)
