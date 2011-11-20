import unittest
import luhn.creditcard as creditcard

class CreditCardTest(unittest.TestCase):
  def test_knows_a_valid_16_digit_card(self):
    card_no = "2626262626262626"
    credit_card = creditcard.CreditCard(card_no)
    self.assertTrue(credit_card.is_valid())

  def test_16_digit_cards_are_valid_only_if_they_pass_luhn(self):
    card_no = "2626262626262626"
    credit_card = creditcard.CreditCard(card_no)
    self.assertTrue(credit_card.is_valid())

  def test_16_digit_cards_that_do_not_pass_are_not_valid(self):
    card_no = "3636363636363636"
    credit_card = creditcard.CreditCard(card_no)
    self.assertFalse(credit_card.is_valid())


if __name__ == "__main__":
  unittest.main()
