class Player(object):
    """ Holds all the attributes and moves of a player.
    """
    def __init__(self, hole, community):
        """This creates the variables of a player.
        """
        self.cards = hole
        self.community = community
        self.combination = hole + community
        self.best_hand = None

    def high_card(self):
        ranks = [rank.get_value() for rank in self.cards]
        if ranks[0] > ranks[1]:
            return ranks[0]
        else:
            return ranks[1]

    def build_ranks(self):
       pairs = {}
       for item in self.combination:
           item_count = 1
           find_rank = item.get_rank()
           if find_rank not in pairs:
               pairs[find_rank] = item_count

           else:
               item_count += 1
               pairs[find_rank]= item_count
       return pairs
