import unittest
import orderbook

class TestEngine(unittest.TestCase):

    def test_limit(self):
        orders = orderbook.Limit(16000)
        n = 1000
        for i in range(n):
            orders.add_order(orderbook.NewBidOrder(i, 21))
        
        self.assertEqual(n, len(orders.orders))

    def test_order_book(self):
        order_book = orderbook.OrderBook()
        orderA = orderbook.NewOrder(1, True, 10)
        orderB = orderbook.NewOrder(2, True, 200)
        orderC = orderbook.NewOrder(3, True, 2)
        order_book.place_order(18000 ,orderA)
        order_book.place_order(18000 ,orderB)
        order_book.place_order(21000 ,orderC)
        order_book.place_order(11000 ,orderC)


        for i in range(len(order_book.Bids)):
            print(str(order_book.Bids[i]))
    


if __name__ == '__main__':
    unittest.main()
