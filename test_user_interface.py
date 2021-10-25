import unittest
from cans import Cola, OrangeSoda, RootBeer
from coins import Dime, Nickel, Penny, Quarter
import user_interface



class TestUserInterface(unittest.TestCase):
    
    def test_validate_menu(self):
        test_value = user_interface.validate_main_menu(1)
        self.assertEqual(test_value, (True, 1))

    def test_validate_menu2(self):
        test_value = user_interface.validate_main_menu(2)
        self.assertEqual(test_value, (True, 2))

    def test_validate_menu3(self):
        test_value = user_interface.validate_main_menu(3)
        self.assertEqual(test_value, (True, 3))

    def test_validate_menu4(self):
        test_value = user_interface.validate_main_menu(4)
        self.assertEqual(test_value, (True, 4))

    def test_validate_menu5(self):
        test_value = user_interface.validate_main_menu(5)
        self.assertEqual(test_value, (False, None))

    def test_try_parse_int(self):
        test_value = user_interface.try_parse_int(10)
        self.assertEqual(test_value, 10)

    def test_try_parse_int2(self):
        test_value = user_interface.try_parse_int('Hello')
        self.assertEqual(test_value, 0)

    def test_get_unique_can_names(self):
        cola1 = Cola()
        cola2 = Cola()
        cola3 = OrangeSoda()
        cola4 = OrangeSoda()
        cola5 = RootBeer()
        cola6 = RootBeer()
        list_of_cans = [cola1,cola2,cola3,cola4,cola5,cola6]
        test_value = user_interface.get_unique_can_names(list_of_cans)
        self.assertEqual(len(test_value), 3)

    def test_get_unique_can_names2(self):
        test_value = user_interface.get_unique_can_names([])
        self.assertEqual(len(test_value), 0)


    def test_payment_value(self):
        list_of_coins = [Quarter(), Dime(), Nickel(), Penny()]
        test_value = user_interface.display_payment_value(list_of_coins)
        self.assertEqual(test_value, .41)

    def test_payment_value(self):
        
        test_value = user_interface.display_payment_value([])
        self.assertEqual(test_value, 0)


    def test_validate_coin_selection(self):
        test_value = user_interface.validate_coin_selection(1)
        self.assertEqual(test_value, (True, 'Quarter'))

    def test_validate_coin_selection2(self):
        test_value = user_interface.validate_coin_selection(2)
        self.assertEqual(test_value, (True, 'Dime'))

    def test_validate_coin_selection3(self):
        test_value = user_interface.validate_coin_selection(3)
        self.assertEqual(test_value, (True, 'Nickel'))

    def test_validate_coin_selection4(self):
        test_value = user_interface.validate_coin_selection(4)
        self.assertEqual(test_value, (True, 'Penny'))

    def test_validate_coin_selection5(self):
        test_value = user_interface.validate_coin_selection(5)
        self.assertEqual(test_value, (True, 'Done'))

    def test_validate_coin_selection6(self):
        test_value = user_interface.validate_coin_selection(6)
        self.assertEqual(test_value, (False, None))


        





    



if __name__ == '__main__':
    unittest.main()

