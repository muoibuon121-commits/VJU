import random


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
SUIT_SYMBOL = {'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣'}

class Card:
    def __init__(self, rank, suit, face_up=True):
        self.__rank = rank        # '2'..'A'
        self.__suit = suit        # 'Spades','Hearts','Diamonds','Clubs'
        self.__face_up = face_up

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

    def is_face_up(self):
        return self.__face_up

    def flip(self):
        self.__face_up = not self.__face_up

    def compareTo(self, other):
        """So sánh theo thứ tự rank. Trả về -1, 0, hoặc 1."""
        r1 = RANKS.index(self.__rank)
        r2 = RANKS.index(other.__rank)
        if r1 < r2:
            return -1
        elif r1 > r2:
            return 1
        return 0

    def __str__(self):
        if not self.__face_up:
            return "[??]"
        return f"{self.__rank}{SUIT_SYMBOL[self.__suit]}"

    def __repr__(self):
        return self.__str__()

class Hand:
    def __init__(self):
        self.__cards = []   # Tối đa 2 lá (Texas Hold'em hole cards)

    def add_card(self, card):
        if len(self.__cards) < 2:
            self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    @property
    def value(self):
        """Tổng giá trị rank của 2 lá bài trong tay."""
        total = 0
        for c in self.__cards:
            idx = RANKS.index(c.get_rank())
            total += idx + 2   # '2'=2, ..., 'A'=14
        return total

    def compareTo(self, other_hand):
        if self.value < other_hand.value:
            return -1
        elif self.value > other_hand.value:
            return 1
        return 0

    def clear(self):
        self.__cards = []

    def __str__(self):
        if not self.__cards:
            return "[Tay trong]"
        return " ".join(str(c) for c in self.__cards)


class Deck:
    def __init__(self):
        self.__cards = []
        self.reset()

    def reset(self):
        """Tạo lại bộ bài 52 lá."""
        self.__cards = [Card(r, s) for s in SUITS for r in RANKS]

    def shuffle(self):
        random.shuffle(self.__cards)

    def deal(self, player):
        """Chia 2 lá cho player."""
        player.hand.clear()
        for _ in range(2):
            if self.__cards:
                player.hand.add_card(self.__cards.pop())

    def topCard(self):
        """Lấy lá bài trên cùng."""
        if self.__cards:
            return self.__cards.pop()
        return None

    def cards_left(self):
        return len(self.__cards)


# ==========================================
# CLASS: Player (base)
# ==========================================
class Player:
    def __init__(self, name, chips=1000):
        self.__name = name
        self.__chips = chips
        self.__bet = 0
        self.__hand = Hand()
        self.__is_in_play = True

    # --- Properties ---
    @property
    def name(self):
        return self.__name

    @property
    def chips(self):
        return self.__chips

    @property
    def bet(self):
        return self.__bet

    @property
    def hand(self):
        return self.__hand

    @property
    def isInPlay(self):
        return self.__is_in_play

    # --- Actions ---
    def bet_chips(self, amount):
        amount = min(amount, self.__chips)
        self.__chips -= amount
        self.__bet += amount
        return amount

    def check(self):
        print(f"  {self.__name} CHECK.")

    def call(self, current_bet):
        to_call = current_bet - self.__bet
        if to_call <= 0:
            self.check()
            return 0
        paid = self.bet_chips(to_call)
        print(f"  {self.__name} CALL {paid} chip.")
        return paid

    def fold(self):
        self.__is_in_play = False
        print(f"  {self.__name} FOLD.")

    def raise_bet(self, amount):
        paid = self.bet_chips(amount)
        print(f"  {self.__name} RAISE them {paid} chip.")
        return paid

    def clear(self):
        self.__bet = 0
        self.__is_in_play = True
        self.__hand.clear()

    def win_pot(self, amount):
        self.__chips += amount

    def __str__(self):
        status = "ACTIVE" if self.__is_in_play else "FOLD"
        return (f"{self.__name} | Chips: {self.__chips} | "
                f"Bet: {self.__bet} | Tay: {self.__hand} | [{status}]")


# ==========================================
# CLASS: HumanPlayer
# ==========================================
class HumanPlayer(Player):
    def __init__(self, name, chips=1000):
        super().__init__(name, chips)

    def make_move(self, current_bet):
        """Người chơi nhập hành động từ bàn phím."""
        print(f"\n  [{self.name}] Tay bai: {self.hand} | Chips: {self.chips} | Bet hien tai: {current_bet}")
        while True:
            if current_bet > self.bet:
                print("  Hanh dong: (1) Call  (2) Raise  (3) Fold")
                choice = input("  Lua chon: ").strip()
                if choice == '1':
                    return self.call(current_bet)
                elif choice == '2':
                    try:
                        amt = int(input("  Raise them bao nhieu? "))
                        self.call(current_bet)
                        return self.raise_bet(amt)
                    except ValueError:
                        print("  Nhap so nguyen hop le!")
                elif choice == '3':
                    self.fold()
                    return 0
                else:
                    print("  Lua chon khong hop le!")
            else:
                print("  Hanh dong: (1) Check  (2) Raise  (3) Fold")
                choice = input("  Lua chon: ").strip()
                if choice == '1':
                    self.check()
                    return 0
                elif choice == '2':
                    try:
                        amt = int(input("  Raise them bao nhieu? "))
                        return self.raise_bet(amt)
                    except ValueError:
                        print("  Nhap so nguyen hop le!")
                elif choice == '3':
                    self.fold()
                    return 0
                else:
                    print("  Lua chon khong hop le!")

class ComputerPlayer(Player):
    def __init__(self, name, chips=1000, difficulty=1):
        super().__init__(name, chips)
        self.__difficulty = difficulty  # 1=Easy, 2=Medium, 3=Hard

    @property
    def difficulty(self):
        return self.__difficulty

    def make_move(self, current_bet):
        """AI tự động quyết định dựa trên difficulty và hand value."""
        hand_val = self.hand.value
        to_call = current_bet - self.bet

        if self.__difficulty == 1:
            # Easy: call nếu hand value >= 10, ngược lại fold
            if hand_val >= 10:
                return self.call(current_bet)
            else:
                self.fold()
                return 0

        elif self.__difficulty == 2:
            # Medium: raise nếu hand mạnh, call bình thường, fold nếu yếu
            if hand_val >= 22:
                self.call(current_bet)
                return self.raise_bet(50)
            elif hand_val >= 15:
                return self.call(current_bet)
            else:
                self.fold()
                return 0

        else:
            # Hard: chiến lược tích cực hơn
            if hand_val >= 24:
                self.call(current_bet)
                return self.raise_bet(100)
            elif hand_val >= 18:
                self.call(current_bet)
                return self.raise_bet(30)
            elif hand_val >= 12:
                return self.call(current_bet)
            else:
                self.fold()
                return 0
                
class PokerGame:
    def __init__(self, players):
        if not (2 <= len(players) <= 8):
            raise ValueError("Can tu 2 den 8 nguoi choi!")
        self.__players = players
        self.__current_player = 0
        self.__deck = Deck()
        self.__round = 0

    def __print_separator(self, char="=", length=50):
        print(char * length)

    def __collect_antes(self, ante=10):
        """Thu ante (tien cuoc ban dau) truoc khi chia bai."""
        pot = 0
        print(f"\n  [ANTE: {ante} chip moi nguoi]")
        for p in self.__players:
            paid = p.bet_chips(ante)
            pot += paid
        return pot

    def __deal_hands(self):
        """Chia bai cho tat ca nguoi choi."""
        self.__deck.reset()
        self.__deck.shuffle()
        for p in self.__players:
            p.clear()
            self.__deck.deal(p)

    def __betting_round(self, pot, current_bet=0):
        """Vong cuoc: moi nguoi choi lan luot hanh dong."""
        active = [p for p in self.__players if p.isInPlay]
        if len(active) <= 1:
            return pot, current_bet

        for p in active:
            if not p.isInPlay:
                continue
            if isinstance(p, HumanPlayer):
                added = p.make_move(current_bet)
            else:
                added = p.make_move(current_bet)
            # Cập nhật current_bet nếu raise
            if p.bet > current_bet:
                current_bet = p.bet
            pot += added
        return pot, current_bet

    def __showdown(self, pot):
        """So bai va tim nguoi thang."""
        self.__print_separator()
        print("  SHOWDOWN!")
        active = [p for p in self.__players if p.isInPlay]

        if len(active) == 1:
            winner = active[0]
            print(f"  Tat ca da fold! {winner.name} thang!")
        else:
            for p in active:
                print(f"  {p.name}: {p.hand} (Value: {p.hand.value})")
            winner = max(active, key=lambda p: p.hand.value)
            print(f"\n  >>> {winner.name} THANG vong nay! <<<")

        winner.win_pot(pot)
        print(f"  {winner.name} nhan {pot} chips!")
        return winner

    def play_round(self):
        self.__round += 1
        self.__print_separator()
        print(f"  VONG {self.__round}")
        self.__print_separator()

        # 1. Thu ante & chia bai
        pot = self.__collect_antes(ante=10)
        self.__deal_hands()

        print("\n  [BAI DA CHIA]")
        for p in self.__players:
            if isinstance(p, HumanPlayer):
                print(f"  {p.name}: {p.hand}")
            else:
                print(f"  {p.name}: [?? ??]")

        # 2. Vong cuoc 1
        print("\n--- VONG CUOC 1 ---")
        pot, current_bet = self.__betting_round(pot, current_bet=10)

        # 3. Loai nguoi het chips
        active = [p for p in self.__players if p.isInPlay]
        if len(active) < 2:
            return self.__showdown(pot)

        # 4. Showdown
        return self.__showdown(pot)

    def __remove_broke_players(self):
        before = len(self.__players)
        self.__players = [p for p in self.__players if p.chips > 0]
        removed = before - len(self.__players)
        if removed:
            print(f"  [{removed} nguoi choi het chips da bi loai]")

    def start(self):
        self.__print_separator('=', 50)
        print("   CHAO MUNG DEN VOI POKER!")
        self.__print_separator('=', 50)

        while True:
            # Xoa nguoi het chips
            self.__remove_broke_players()
            active = [p for p in self.__players if p.chips > 0]
            if len(active) < 2:
                print("\n  Chi con 1 nguoi choi, tro choi ket thuc!")
                break

            # Hien thi chips
            print("\nTrang thai nguoi choi:")
            for p in self.__players:
                print(f"  {p.name}: {p.chips} chips")

            self.play_round()

            # Hoi tiep tuc
            tiep = input("\nChoi tiep? (y/n): ").strip().lower()
            if tiep != 'y':
                print("\n--- KET THUC TRO CHOI ---")
                print("Tong ket:")
                for p in sorted(self.__players, key=lambda x: x.chips, reverse=True):
                    print(f"  {p.name}: {p.chips} chips")
                break

def main():
    print("=" * 50)
    print("   SETUP GAME POKER")
    print("=" * 50)

    try:
        ten = input("Nhap ten nguoi choi: ").strip() or "Player"
        so_bot = int(input("So may (1-3): ") or "2")
        so_bot = max(1, min(3, so_bot))
        do_kho = int(input("Do kho cua may (1=De, 2=TB, 3=Kho): ") or "1")
        do_kho = max(1, min(3, do_kho))
    except ValueError:
        ten, so_bot, do_kho = "Player", 2, 1

    players = [HumanPlayer(ten, chips=500)]
    for i in range(1, so_bot + 1):
        players.append(ComputerPlayer(f"Bot_{i}", chips=500, difficulty=do_kho))

    game = PokerGame(players)
    game.start()


if __name__ == "__main__":
    main()
