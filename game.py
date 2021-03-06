import arcade
from deck import Deck


class Game(arcade.Window):

    def __init__(self, card_width, card_height, card_gap, title):
        self.card_width = card_width
        self.card_height = card_height
        self.card_gap = card_gap
        self.board_width = 3 * card_width + 4 * card_gap
        self.board_height = 4 * card_height + 5 * card_gap
        self.window_width = 4 * card_width + 5 * card_gap
        self.window_height = 4 * card_height + 5 * card_gap
        self.title = title
        super().__init__(self.window_width, self.window_height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.deck = None
        self.selected = []
        self.num_sets = 0

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()
        coords = []
        for row in range(self.board_height - self.card_gap, 0, -self.card_height - self.card_gap):
            for col in range(self.card_gap, self.board_width, self.card_width + self.card_gap):
                max_x, max_y, min_x, min_y = self.card_width + col, row, col, row - self.card_height
                coords.append((max_x, max_y, min_x, min_y))
        self.deck.deal(12, coords)
        self.num_sets = self.deck.count_sets()

    def draw_cards(self):
        for card in self.deck.play:
            arcade.draw_lrtb_rectangle_outline(card.location[2],
                                               card.location[0],
                                               card.location[1],
                                               card.location[3],
                                               card.border['color'],
                                               card.border['width'])
            loc_x = (card.location[0] + card.location[2]) / 2
            loc_y = (card.location[1] + card.location[3]) / 2
            self.render_card(card, loc_x, loc_y)

    def render_card(self, card, loc_x, loc_y):
        if card.shape:
            card.draw(loc_x, loc_y)
        else:
            raise Exception('Card has no shape attribute.')

    def draw_set_counter(self, n):
        text = f"Possible sets: {n}"
        arcade.draw_text(text,
                         self.board_width,
                         self.window_height - self.card_gap - 15,
                         arcade.color.BLACK,
                         14)

    def draw_cards_remaining(self):
        text = f"Cards remaining: {len(self.deck.deck)}"
        arcade.draw_text(text,
                         self.board_width,
                         self.window_height - self.card_gap - 40,
                         arcade.color.BLACK,
                         14)

    def handle_extra_cards(self):
        counter = 0
        while self.num_sets == 0:
            max_x = 4 * self.card_width + 4 * self.card_gap
            max_y = self.card_height + self.card_gap + counter
            min_x = 3 * self.card_width + 4 * self.card_gap
            min_y = self.card_gap + counter
            self.deck.deal(1, [(max_x, max_y, min_x, min_y)])
            self.deck.play[-1].overflow = True
            self.num_sets = self.deck.count_sets()
            counter += self.card_height + self.card_gap

    def on_draw(self):
        arcade.start_render()

        self.draw_set_counter(self.num_sets)
        self.draw_cards_remaining()
        self.draw_cards()
        self.handle_extra_cards()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        for card in self.deck.play:
            if card.location[2] < x < card.location[0] and card.location[3] < y < card.location[1]:
                if card in self.selected:
                    self.selected.remove(card)
                    card.border['color'] = arcade.color.GRAY
                    card.border['width'] = 1
                else:
                    self.selected.append(card)
                    card.border['color'] = arcade.color.RED
                    card.border['width'] = 3

        if self.deck.is_set(self.selected):
            print('SET FOUND!')
            locations = [card.location for card in self.selected if not card.overflow]
            self.deck.remove(cards=self.selected)
            for card in self.deck.play:
                if card.overflow:
                    card.location = locations.pop(0)
            self.deck.redeal(locations)
            self.selected = []
            self.num_sets = self.deck.count_sets()
        else:
            print('Not a set...')

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    card_width = 300
    card_height = 175
    card_gap = 25
    game = Game(card_width, card_height, card_gap, 'SET')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
