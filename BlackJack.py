import random
class BlackJack:
    def __init__(self):
        self.cards = []
        self.ace_el_count = 0
        self.score = 0
        self.computer_score = 0
        self.cards_in_play = []

    def get_score(self):
        return self.score
    def get_computer_score(self):
        return self.computer_score
    def get_ace_count(self):
        return self.ace_el_count

    def card_compare(self, new_card_string):
        if len(self.cards_in_play) > 0:
            for i in range(len(self.cards_in_play)):
                if self.cards_in_play[i] == new_card_string:
                    return True
        return False

    # player methods
    def add_cards(self, spade_list, club_list, heart_list, diamond_list):
        red_cards = [heart_list, diamond_list]
        black_cards = [spade_list, club_list]
        self.cards = [red_cards, black_cards]

    def draw_2_cards(self):
        #drawing cards logic
        color_1 = random.randint(1, 2) - 1
        suit_1 = random.randint(1, 2) - 1
        num_card_1 = random.randint(1, 13) - 1
        first_draw = self.cards[color_1][suit_1][0][num_card_1]
        draw_1_name = self.cards[color_1][suit_1][1]

        print("Your first draw is the " + str(first_draw) + " of " + draw_1_name)
        self.cards_in_play.append(str(first_draw) + draw_1_name)
        if first_draw >= 10:
            self.score += 10
        elif first_draw == 1:
            score_input = input("Drew an ace, do you want a 1 or 11?\n")
            if int(score_input) == 11 or score_input.lower == 'eleven':
                self.score += 11
                self.ace_el_count += 1
            else:
                self.score += 1
        else:
            self.score += first_draw
        color_2 = random.randint(1, 2) - 1
        suit_2 = random.randint(1, 2) - 1
        num_card_2 = random.randint(1, 13) - 1
        second_draw = self.cards[color_2][suit_2][0][num_card_2]
        draw_2_name = self.cards[color_2][suit_2][1]
        while self.card_compare(str(second_draw) + draw_2_name):
            color_2 = random.randint(1, 2) - 1
            suit_2 = random.randint(1, 2) - 1
            num_card_2 = random.randint(1, 13) - 1
            second_draw = self.cards[color_2][suit_2][0][num_card_2]
            draw_2_name = self.cards[color_2][suit_2][1]
        print("Your second draw is the " + str(second_draw) + " of " + draw_2_name)
        if second_draw >= 10:
            self.score += 10
        elif second_draw == 1:
            score_input = input("Drew an ace, do you want a 1 or 11?\n")
            if int(score_input) == 11 or score_input.lower == 'eleven':
                self.score += 11
                self.ace_el_count += 1
            else:
                self.score += 1

        else:
            self.score += second_draw
        print("Your score is: " + str(self.score))
        if self.score > 21:
            print("Sorry, you busted")
            return
        elif self.score == 21:
            print("You got exactly 21, you win")

    def continue_game(self):
        player_choice = input("Do you wish to draw again? (Y or N)\n")
        while player_choice == 'Y' or player_choice == 'y':
            new_color = random.randint(1, 2) - 1
            new_suit = random.randint(1, 2) - 1
            new_num = random.randint(1, 13) - 1
            new_draw = self.cards[new_color][new_suit][0][new_num]
            new_draw_name = self.cards[new_color][new_suit][1]
            while self.card_compare(str(new_draw) + new_draw_name):
                new_color = random.randint(1, 2) - 1
                new_suit = random.randint(1, 2) - 1
                new_num = random.randint(1, 13) - 1
                new_draw = self.cards[new_color][new_suit][0][new_num]
                new_draw_name = self.cards[new_color][new_suit][1]
            print("You drew the " + str(new_draw) + " of " + new_draw_name)
            if new_draw >= 10:
                self.score += 10
            elif new_draw == 1:
                score_input = input("Drew an ace, do you want a 1 or 11?\n")
                if int(score_input) == 11 or score_input.lower == 'eleven':
                    self.score += 11
                    self.ace_el_count += 1
                else:
                    self.score += 1
            else:
                self.score += new_draw
            if self.score >= 21 and self.ace_el_count > 0:
                self.score -= 10
                self.ace_el_count -= 1
                print("Ace Converted to 1")
            print("Your score is: " + str(self.score))
            if self.score > 21:
                print("Sorry, you busted")
                return
            elif self.score == 21:
                print("You got exactly 21, you win")
            player_choice = input("Do you wish to draw again? (Y or N)\n")
        if player_choice != 'Y' and player_choice != 'y':
            print("Your score was: " + str(self.score))
            pass

    def computer_draw_cards(self):
        computer_color = random.randint(1, 2) - 1
        computer_suit = random.randint(1, 2) - 1
        computer_number = random.randint(1, 13) - 1
        computer_color2 = random.randint(1, 2) - 1
        computer_suit2 = random.randint(1, 2) - 1
        computer_number2 = random.randint(1, 13) - 1
        computer_draw = self.cards[computer_color][computer_suit][0][computer_number]
        computer_draw2 = self.cards[computer_color2][computer_suit2][0][computer_number2]
        if computer_draw >= 10:
            self.computer_score += 10
        else:
            self.computer_score += computer_draw
        if computer_draw2 >= 10:
            self.computer_score += 10
        else:
            self.computer_score += computer_draw2
        computer_color3 = random.randint(1, 2) - 1
        computer_suit3 = random.randint(1, 2) - 1
        computer_number3 = random.randint(1, 2) - 1
        computer_draw3 = self.cards[computer_color3][computer_suit3][0][computer_number3]
        if self.computer_score < self.score:
            self.computer_score += computer_draw3
        print("Here's what the computer drew: " + str(self.computer_score))

    def full_blackjack_game(self):
        self.draw_2_cards()
        if self.score <= 21:
           self.continue_game()
        self.computer_draw_cards()
        # End game logic
        if self.score > self.computer_score and self.score < 21:
            print("You beat the computer! \nYour score was: " + str(self.score))
            print("Computer's score was: " + str(self.computer_score))
        elif self.computer_score > self.score and self.computer_score < 21:
            print("Sorry, the computer beat you.")
            print("Your score was: " + str(self.score))
            print("The computer score was: " + str(self.computer_score))
        elif self.score > 21:
            print("Sorry, you busted")
            print("Your score: " + str(self.score))
            print("Computer's score: " + str(self.computer_score))
        elif self.score == 21:
            print("You got exactly 21, congrats you win!")
        else:
            print("You lost.")

game = BlackJack()
spades = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Spades"]
clubs = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Clubs"]
hearts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Hearts"]
diamonds = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Diamonds"]
game.add_cards(spades, clubs, hearts, diamonds)

game.full_blackjack_game()
