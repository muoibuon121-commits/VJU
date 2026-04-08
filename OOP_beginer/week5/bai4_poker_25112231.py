import random

THU_TU = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CHAT_BAI = ['Bích', 'Cơ', 'Rô', 'Chuồn']
BIEU_TUONG = {'Bích': '♠', 'Cơ': '♥', 'Rô': '♦', 'Chuồn': '♣'}

class Card:
    def __init__(self, rank, suit, face_up=True):
        self.__rank = rank      
        self.__suit = suit        
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
        r1 = THU_TU.index(self.__rank)
        r2 = THU_TU.index(other.__rank)
        if r1 < r2:
            return -1
        elif r1 > r2:
            return 1
        return 0

    def __str__(self):
        if not self.__face_up:
            return "[??]"
        return f"{self.__rank}{BIEU_TUONG[self.__suit]}"

    def __repr__(self):
        return self.__str__()

class Hand:
    def __init__(self):
        self.__cards = []

    def add_card(self, card):
        if len(self.__cards) < 2:
            self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    @property
    def value(self):
        total = 0
        for c in self.__cards:
            idx = THU_TU.index(c.get_rank())
            total += idx + 2
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
            return "[Tay trống]"
        return " ".join(str(c) for c in self.__cards)


class Deck:
    def __init__(self):
        self.__cards = []
        self.reset()

    def reset(self):
        self.__cards = [Card(r, s) for s in CHAT_BAI for r in THU_TU]

    def shuffle(self):
        random.shuffle(self.__cards)

    def deal(self, player):
        player.hand.clear()
        for _ in range(2):
            if self.__cards:
                player.hand.add_card(self.__cards.pop())

    def topCard(self):
        if self.__cards:
            return self.__cards.pop()
        return None

    def cards_left(self):
        return len(self.__cards)

class Player:
    def __init__(self, name, chips=1000):
        self.__name = name
        self.__chips = chips
        self.__bet = 0
        self.__hand = Hand()
        self.__is_in_play = True

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

    def bet_chips(self, amount):
        amount = min(amount, self.__chips)
        self.__chips -= amount
        self.__bet += amount
        return amount

    def check(self):
        print(f"  {self.__name} KIỂM TRA (CHECK).")

    def call(self, current_bet):
        to_call = current_bet - self.__bet
        if to_call <= 0:
            self.check()
            return 0
        paid = self.bet_chips(to_call)
        print(f"  {self.__name} THEO (CALL) {paid} chip.")
        return paid

    def fold(self):
        self.__is_in_play = False
        print(f"  {self.__name} BỎ BÀI (FOLD).")

    def raise_bet(self, amount):
        paid = self.bet_chips(amount)
        print(f"  {self.__name} TỐ THÊM (RAISE) {paid} chip.")
        return paid

    def clear(self):
        self.__bet = 0
        self.__is_in_play = True
        self.__hand.clear()

    def win_pot(self, amount):
        self.__chips += amount

    def __str__(self):
        status = "ĐANG CHƠI" if self.__is_in_play else "ĐÃ BỎ"
        return (f"{self.__name} | Chip: {self.__chips} | "
                f"Cược: {self.__bet} | Tay: {self.__hand} | [{status}]")


class HumanPlayer(Player):
    def __init__(self, name, chips=1000):
        super().__init__(name, chips)

    def make_move(self, current_bet):
        print(f"\n  [{self.name}] Bài trên tay: {self.hand} | Chip hiện có: {self.chips} | Cược hiện tại: {current_bet}")
        while True:
            if current_bet > self.bet:
                print("  Hành động: (1) Theo (Call)  (2) Tố thêm (Raise)  (3) Bỏ bài (Fold)")
                choice = input("  Lựa chọn của bạn: ").strip()
                if choice == '1':
                    return self.call(current_bet)
                elif choice == '2':
                    try:
                        amt = int(input("  Bạn muốn tố thêm bao nhiêu? "))
                        self.call(current_bet)
                        return self.raise_bet(amt)
                    except ValueError:
                        print("  Vui lòng nhập số nguyên hợp lệ!")
                elif choice == '3':
                    self.fold()
                    return 0
                else:
                    print("  Lựa chọn không hợp lệ!")
            else:
                print("  Hành động: (1) Kiểm tra (Check)  (2) Tố thêm (Raise)  (3) Bỏ bài (Fold)")
                choice = input("  Lựa chọn của bạn: ").strip()
                if choice == '1':
                    self.check()
                    return 0
                elif choice == '2':
                    try:
                        amt = int(input("  Bạn muốn tố thêm bao nhiêu? "))
                        return self.raise_bet(amt)
                    except ValueError:
                        print("  Vui lòng nhập số nguyên hợp lệ!")
                elif choice == '3':
                    self.fold()
                    return 0
                else:
                    print("  Lựa chọn không hợp lệ!")

class ComputerPlayer(Player):
    def __init__(self, name, chips=1000, difficulty=1):
        super().__init__(name, chips)
        self.__difficulty = difficulty

    @property
    def difficulty(self):
        return self.__difficulty

    def make_move(self, current_bet):
        hand_val = self.hand.value
        to_call = current_bet - self.bet

        if self.__difficulty == 1:
            if hand_val >= 10:
                return self.call(current_bet)
            else:
                self.fold()
                return 0

        elif self.__difficulty == 2:
            if hand_val >= 22:
                self.call(current_bet)
                return self.raise_bet(50)
            elif hand_val >= 15:
                return self.call(current_bet)
            else:
                self.fold()
                return 0

        else:
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
            raise ValueError("Cần từ 2 đến 8 người chơi!")
        self.__players = players
        self.__current_player = 0
        self.__deck = Deck()
        self.__round = 0

    def __print_separator(self, char="=", length=50):
        print(char * length)

    def __collect_antes(self, ante=10):
        pot = 0
        print(f"\n  [TIỀN SÀN: {ante} chip mỗi người]")
        for p in self.__players:
            paid = p.bet_chips(ante)
            pot += paid
        return pot

    def __deal_hands(self):
        self.__deck.reset()
        self.__deck.shuffle()
        for p in self.__players:
            p.clear()
            self.__deck.deal(p)

    def __betting_round(self, pot, current_bet=0):
        active = [p for p in self.__players if p.isInPlay]
        if len(active) <= 1:
            return pot, current_bet

        for p in active:
            if not p.isInPlay:
                continue
            added = p.make_move(current_bet)
            if p.bet > current_bet:
                current_bet = p.bet
            pot += added
        return pot, current_bet

    def __showdown(self, pot):
        self.__print_separator()
        print("  NGỬA BÀI (SHOWDOWN)!")
        active = [p for p in self.__players if p.isInPlay]

        if len(active) == 1:
            winner = active[0]
            print(f"  Tất cả đã bỏ bài! {winner.name} thắng!")
        else:
            for p in active:
                print(f"  {p.name}: {p.hand} (Giá trị: {p.hand.value})")
            winner = max(active, key=lambda p: p.hand.value)
            print(f"\n  >>> {winner.name} THẮNG ván này! <<<")

        winner.win_pot(pot)
        print(f"  {winner.name} nhận được {pot} chip!")
        return winner

    def play_round(self):
        self.__round += 1
        self.__print_separator()
        print(f"  VÁN THỨ {self.__round}")
        self.__print_separator()

        pot = self.__collect_antes(ante=10)
        self.__deal_hands()

        print("\n  [BÀI ĐÃ CHIA]")
        for p in self.__players:
            if isinstance(p, HumanPlayer):
                print(f"  {p.name}: {p.hand}")
            else:
                print(f"  {p.name}: [?? ??]")

        print("\n--- VÒNG CƯỢC 1 ---")
        pot, current_bet = self.__betting_round(pot, current_bet=10)

        active = [p for p in self.__players if p.isInPlay]
        if len(active) < 2:
            return self.__showdown(pot)

        return self.__showdown(pot)

    def __remove_broke_players(self):
        before = len(self.__players)
        self.__players = [p for p in self.__players if p.chips > 0]
        removed = before - len(self.__players)
        if removed:
            print(f"  [{removed} người chơi hết chip đã bị loại]")

    def start(self):
        self.__print_separator('=', 50)
        print("   CHÀO MỪNG ĐẾN VỚI TRÒ CHƠI POKER!")
        self.__print_separator('=', 50)

        while True:
            self.__remove_broke_players()
            active = [p for p in self.__players if p.chips > 0]
            if len(active) < 2:
                print("\n  Chỉ còn 1 người chơi, trò chơi kết thúc!")
                break

            print("\nTrạng thái người chơi:")
            for p in self.__players:
                print(f"  {p.name}: {p.chips} chip")

            self.play_round()

            tiep = input("\nChơi tiếp ván nữa không? (y/n): ").strip().lower()
            if tiep != 'y':
                print("\n--- KẾT THÚC TRÒ CHƠI ---")
                print("Tổng kết:")
                for p in sorted(self.__players, key=lambda x: x.chips, reverse=True):
                    print(f"  {p.name}: {p.chips} chip")
                break

def main():
    print("=" * 50)
    print("   THIẾT LẬP TRÒ CHƠI POKER")
    print("=" * 50)

    try:
        ten = input("Nhập tên bạn: ").strip() or "Người chơi"
        so_bot = int(input("Số lượng máy chơi cùng (1-3): ") or "2")
        so_bot = max(1, min(3, so_bot))
        do_kho = int(input("Độ khó của máy (1=Dễ, 2=Trung bình, 3=Khó): ") or "1")
        do_kho = max(1, min(3, do_kho))
    except ValueError:
        ten, so_bot, do_kho = "Người chơi", 2, 1

    players = [HumanPlayer(ten, chips=500)]
    for i in range(1, so_bot + 1):
        players.append(ComputerPlayer(f"Máy_{i}", chips=500, difficulty=do_kho))

    game = PokerGame(players)
    game.start()


if __name__ == "__main__":
    main()
