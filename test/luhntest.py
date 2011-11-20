import unittest
import luhn.luhn as luhn
class LuhnTest(unittest.TestCase):

  def test_passes_luhn_test(self):
    card_no = "2626262626262626"
    assertTrue(luhn.is_valid_card(card_no))


  def test_does_not_pass_luhn_test(self):
    card_no = "3636363636363636"
    assertFalse(luhn.is_valid_card(card_no))

  if __name__ == "__main__":
    unittest.main()

