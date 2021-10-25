import unittest
from wallet import Wallet


class TestWalletMoney(unittest.TestCase):
    """ Tests for instantiating a Wallet object, test that its money list has a len of 88"""


    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_length(self):
        """ Testing for instantiating a Wallet object, test that its money list has a len of 88 """
        length = len(self.wallet.money)
        self.assertEqual(length, 88)


if __name__ == '__main__':
    unittest.main()
