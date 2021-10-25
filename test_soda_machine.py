import unittest
from cans import Cola, OrangeSoda
from soda_machine import SodaMachine
from coins import Coin
from coins import Dime, Penny, Quarter, Nickel





class TestFillRegister(unittest.TestCase):
    """ Tests for instantiating a SodaMachine object, test that its register list has a len of 88 """

    def setUp(self):
        self.soda_machine = SodaMachine()


    def test_register_list(self):
        """ Tests for instantiating a SodaMachine object, test that its register list has a len of 88 """
        length_of_register = len(self.soda_machine.register)
        self.assertEqual(length_of_register, 88)
 

    def test_fill_inventory(self):
        """ Tests for instantiating a SodaMachine object, test that its register list has a len of 30 of inventory """
        length_of_inventory = len(self.soda_machine.inventory)
        self.assertEqual(length_of_inventory, 30)   



class TestCoinFunctions(unittest.TestCase):
    """ Tests for instantiating a SodaMachine object, test that its register list has a len of 88 """

    def setUp(self):
        self.register_coin = SodaMachine()


    def test_return_of_dime_from_register(self):
        """ Tests for the return of dime from the register """
        return_dime = self.register_coin.get_coin_from_register('Dime')
        self.assertEqual(0.10, return_dime.value)


    def test_return_of_nickel_from_register(self):
        """ Tests for the return of nickel from the register """
        return_nickel = self.register_coin.get_coin_from_register('Nickel')
        self.assertEqual(0.05, return_nickel.value)


    def test_return_of_penny_from_register(self):
        """ Tests for the return of penny from the register """
        return_penny = self.register_coin.get_coin_from_register('Penny')
        self.assertEqual(0.01, return_penny.value)


    def test_return_of_quarter_from_register(self):
        """ Tests for the return of quarter from the register """
        return_quarter = self.register_coin.get_coin_from_register('Quarter')
        self.assertEqual(0.25, return_quarter.value)
    

    def test_return_of_none_register(self):
        """ Tests for the return of NONE after passing in string not valid coin name """
        return_of_none_register = self.register_coin.get_coin_from_register('Half-dollar')
        self.assertEqual(None, return_of_none_register)



class TestGetCoin(unittest.TestCase):
    """ Tests for instantiating a SodaMachine object, test that its register list has a len of 88 """

    def setUp(self):
        self.get_coin = SodaMachine()

    def test_dime_return_true(self):
        """ Test that each type of coin will return True """
        dime_return = self.get_coin.register_has_coin('Dime')
        self.assertTrue(dime_return)

    def test_penny_return_true(self):
        """ Test that each type of coin will return True """
        penny_return = self.get_coin.register_has_coin('Penny')
        self.assertTrue(penny_return)

    def test_nickel_return_true(self):
        """ Test that each type of coin will return True """
        nickel_return = self.get_coin.register_has_coin('Nickel')
        self.assertTrue(nickel_return)

    def test_quarter_return_true(self):
        """ Test that each type of coin will return True """
        quarter_return = self.get_coin.register_has_coin('Quarter')
        self.assertTrue(quarter_return)

    def test_quarter_return_false(self):
        """ Test that each type of coin will return True """
        false_return = self.get_coin.register_has_coin('Half-dollar')
        self.assertFalse(false_return)



class TestChangeValue(unittest.TestCase):
    """ Test with total payment higher """

    def setUp(self):
        self.change_value = SodaMachine()

    def test_total_payment_higher(self):
        """ Test with total payment higher """
        payment_higher = self.change_value.determine_change_value(1.50, 0.60)
        self.assertEqual (payment_higher, .90)

    def test_selected_soda_higher(self):
            """ Test with select soda price higher """
            selected_soda_higher = self.change_value.determine_change_value(0.60, 1.50)
            self.assertEqual (selected_soda_higher, -.90)


    def test_soda_equal_value(self):
            """ Test with equal value """
            equal_value = self.change_value.determine_change_value(1.50, 1.50)
            self.assertEqual (equal_value, 0)  



class CalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.dime = Dime()
        self.nickel = Nickel()
        self.quarter = Quarter()
        self.penny = Penny()
        self.list = [self.dime, self.penny, self.quarter, self.nickel]
        self.soda_machine = SodaMachine()




    def test_calculate_coin_value(self):
        test_value = self.soda_machine.calculate_coin_value(self.list)
        self.assertEqual(test_value, .41)

    def test_calculate_coin_value2(self):
        test_value = self.soda_machine.calculate_coin_value([])
        self.assertEqual(test_value, 0)

class GetInventorySoda(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_inventory_soda(self):
        test_value = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(test_value.name, 'Cola')
    
    def test_inventory_soda2(self):
        test_value = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(test_value.name, 'Orange Soda')

    def test_inventory_soda3(self):
        test_value = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(test_value.name, 'Root Beer')

    def test_inventory_soda4(self):
        test_value = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertEqual(test_value, None)

class TestReturnInventory(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()


    def test_return_inventory(self):
        cola = Cola()
        self.soda_machine.return_inventory(cola)
        self.assertEqual(len(self.soda_machine.inventory), 31)

class DepositCoinsRegister(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.list_of_coins = [Quarter(), Dime(), Nickel(), Penny()]


    def test_deposit_coins_register(self):
        self.soda_machine.deposit_coins_into_register(self.list_of_coins)
        self.assertEqual(len(self.soda_machine.register), 92)

    








# def determine_change_value(self, total_payment, selected_soda_price):
#     """Determines amount of change needed by finding difference of payment amount and can price"""
#     return round(total_payment - selected_soda_price, 2)



# 5. determine_change_value – 3 tests
# a.    Test with total payment higher
# b.    Test with select_soda_price higher
# c.    Test with two equal values
# 
# 6. calculate_coin_value - 2 tests
# a.    Instantiate each of the 4 coin types and append them to a list. Pass the list into this
#       function, ensure the returned values is .41
# b.    Pass in an empty list. Ensure the returned value is 0.
# 
# 7. get_inventory_soda - 4 tests
# a.    Pass in each of the 3 soda names, ensure the returned can has the same name
# b.    Pass in “Mountain Dew” and ensure None is returned
# 
# 8. return_inventory - 1 test
# a.    Instantiate a can and pass it into the method. Test that the len of self.inventory is now
#       31
# 
# 9. deposit_coins_into_register - 1 test
# a.    Instantiate each of the 4 coins and append them to a list. Pass the list into the function,
# ensure the len of self.register is 92


if __name__ == '__main__':
    unittest.main()