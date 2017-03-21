#
# Justin Ethier
#
# Solution to problem #54 of project euler
#
class Poker():
    """
    Class to load a round of poker hands and determine the winner
    """
    def load(self, hands):
        """
        Load a round of given hands into memory
        See Euler #54 for data format.
        """
        self.hands = [self.parse(hands.split(" ")[0:5]),
                      self.parse(hands.split(" ")[5:] )]

    def parse(self, rawhand):
        """
        Process a single hand, massage data, and save into memory
        
          Input: hand of form 5H 5C 6S 7S KD
        Returns: hand in list form
        """

        hand = []
        for card in rawhand:
            hand.append( (self.face2value(card[0]), card[1]) )


        # Sort by suit and then by face value
        hand.sort()
        hand.reverse()
        return hand
    
    def face2value(self, cardFace):
        """
        Convert from card face to discrete value
        """
        faces = {'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
        if cardFace in faces:
            return faces[cardFace]
        return int(cardFace)
    
    def rank(self, ihand):
        """
        Determine numeric rank for a hand

        Returns:
            - Overall score (rank) of the hand
            - Tuple containing a list of individual scores (EG: 2 pair, high card):
               rank
               high card (EG: K for pair of kings or 10 for 10,9,8,7,6 straight)
        """
        return self.calcRank(self.hands[ihand])

    def calcRank(self, h):
        """
        Score the hand by calculating an overall score as well has each sub-rank
        (see above for returns)
        """
        def isFlush(hand):
            for i in range(1, len(hand)):
                if hand[i][1] != hand[0][1]:
                    return False
            return True

        def isStraight(hand):
            for i in range(1, len(hand)):
                if hand[i][0] != hand[i-1][0] - 1:
                    return False
            return True


        def addResult(result, results):
            """
            Add a result to the list such that they are sorted by score (1st) and high-card (2nd).
            Results are of form (score, high-card)
            """
            i = 0
            while i < len(results):
                if results[i][0] < result[0] or (results[i][0] == result[0] and results[i][1] < result[1]):
                    break
                i += 1
            results.insert(i, result)

        hand = h
        if isFlush(hand) and isStraight(hand):
            return 8, [(8, hand[0][0])]
        elif isFlush(hand):
            return 5, [(5, hand[0][0])]
        elif isStraight(hand):
            return 4, [(4, hand[0][0])]
        else:
            # Count how many of each card are in the hand
            cards = {}
            for card in hand:
                if card[0] in cards:
                    cards[card[0]] += 1
                else:
                    cards[card[0]] = 1

            # Reduce the hand by number of each card value (IE, pair, three-of-a-kind, etc)
            result = []
            for card in cards.keys():
                if cards[card] == 4:
                    addResult((7, card), result) # 4-of-a-kind
                elif cards[card] == 3:
                    addResult((3, card), result) # 3-of-a-kind
                elif cards[card] == 2:
                    addResult((1, card), result) # Pair
                else:
                    addResult((0, card), result) # High card

            # Determine the overall score (may be more if 2 pair, full house)
            ranks = {}
            maxRank = 0
            for rank in result:
                if rank[0] in ranks:
                    ranks[rank[0]] += 1
                else:
                    ranks[rank[0]] = 1
                if rank[0] > maxRank:
                    maxRank = rank[0]

            # Handle special cases
            if (1 in ranks and ranks[1] == 2):
                maxRank = 2 # 2 Pair
            elif (3 in ranks and 1 in ranks):
                maxRank = 6 # Full House

            return maxRank, result

    def compare(self):
        """
        Rank all hands and choose one with highest rank (winner)
        
        TODO: hardcoded to only compare 2 hands for now
        """

        def compareHand(h0, h1):
            """
            Compare all cards in hand until we find the winner
            """


            if len(h0) == 0:
                print("unable to find a winner!")
                return None


            if h0[0][0] > h1[0][0]:
                return 0
            elif h0[0][0] < h1[0][0]:
                return 1
            else:
                if h0[0][1] > h1[0][1]:
                    return 0
                elif h0[0][1] < h1[0][1]:
                    return 1
                else:
                    return compareHand(h0[1:], h1[1:])

        # Score each hand    
        hands = []
        for i in range(0, len(self.hands)):
            hands.append( self.rank(i) )

        # Compare top-level score
        if hands[0][0] > hands[1][0]:
            return 0
        elif hands[0][0] < hands[1][0]:
            return 1
        else:
            # Same hand, compare lower-level scores
            return compareHand(hands[0][1], hands[1][1])

p = Poker()
# test code:
#p.load("9S KS 3S 4S 7S 8S TS QS JS 2S")
#print(p.rank(0))
#print(p.rank(1))
#print(p.compare())

p1wins = 0
fp = open("poker.txt", "r")
for line in fp.readlines():
    p.load(line)
    if p.compare() == 0:
        p1wins += 1
fp.close()

print(p1wins)

