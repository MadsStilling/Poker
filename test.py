from cards import Deck, Card
from player import Player

deck = Deck()
deck.shuffle()

p1 = Player([deck.deal() for i in range(2)], [deck.deal() for f in range(5)])
print(p1.cards)
print(p1.community)
print(p1.high_card())
print(p1.build_ranks())
