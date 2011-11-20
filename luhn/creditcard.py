import luhn
class CreditCard:
  def __init__(self, card_no):
    self.card_no = card_no

  def is_valid(self):
    length_of_card = len(self.card_no)
    print length_of_card
    return (length_of_card == 14 or length_of_card == 16) and luhn.is_valid(self.card_no)
