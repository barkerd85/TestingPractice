import unittest
from customer import Customer
from cans import Cola, OrangeSoda, RootBeer

class TestGetWalletCoin(unittest.TestCase):
    """ Tests for the return of each type of coin from the wallet """


    def setUp(self):
        self.customer = Customer()


    def test_return_of_dime_from_wallet(self):
        """ Tests for the return of dime from the wallet """
        returned_dime = self.customer.get_wallet_coin('Dime')
        self.assertEqual(0.10, returned_dime.value)


    def test_return_of_nickel_from_wallet(self):
        """ Tests for the return of nickel from the wallet """
        returned_nickel = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(0.05, returned_nickel.value)


    def test_return_of_penny_from_wallet(self):
        """ Tests for the return of penny from the wallet """
        returned_penny = self.customer.get_wallet_coin('Penny')
        self.assertEqual(0.01, returned_penny.value)


    def test_return_of_quarter_from_wallet(self):
        """ Tests for the return of quarter from the wallet """
        returned_quarter = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(0.25, returned_quarter.value)
    

    def test_return_of_none(self):
        """ Tests for the return of NONE after passing in string not valid coin name """
        return_of_none = self.customer.add_coins_to_wallet('Half-dollar')
        self.assertEqual(None, return_of_none)





class TestAddCoinsToWallet(unittest.TestCase):
    """ Tests passing in coins to the wallet """


    def setUp(self):
        self.customer = Customer()


    def test_add_coins_to_wallet(self):
        """ Tests for passing in a list of 3 coins, test that the length of the customer’s wallet’s money list went up by that number """
        length_of_wallet = len(self.customer.wallet.money)
        list_of_coins = ['Dime', 'Quarter', 'Nickel']
        self.customer.add_coins_to_wallet(list_of_coins)
        self.assertEqual(len(self.customer.wallet.money), length_of_wallet + 3)

    def test_empty_list_to_wallet(self):
        """ Tests for pass in an empty list, test that the len of money list remained the same """
        length_of_wallet = len(self.customer.wallet.money)
        empty_list = []
        self.customer.add_coins_to_wallet(empty_list)
        self.assertEqual(len(self.customer.wallet.money), length_of_wallet)




class TestAddCanToBackpack(unittest.TestCase):
    """ Tests passing in cola object to test length of backpack """


    def setUp(self):
        self.customer = Customer()


    def test_add_can_to_backpack(self):
        """ Tests passing in cola object to test length of backpack """
        cola = Cola()
        length_of_backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(cola)
        self.assertEqual(len(self.customer.backpack.purchased_cans), length_of_backpack +1)
    
    
    def test_add_can_to_backpack(self):
        """ Tests passing in orange soda object to test length of backpack """
        orangesoda = OrangeSoda()
        length_of_backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(orangesoda)
        self.assertEqual(len(self.customer.backpack.purchased_cans), length_of_backpack +1)


    def test_add_can_to_backpack(self):
        """ Tests passing in root beer object to test length of backpack """
        rootbeer = RootBeer()
        length_of_backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(rootbeer)
        self.assertEqual(len(self.customer.backpack.purchased_cans), length_of_backpack +1)        


if __name__ == '__main__':
    unittest.main()
