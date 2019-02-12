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

    def setup(self):
        self.deck = Deck()
        self.deck.shuffle()
        coords = []
        for row in range(self.board_height - self.card_gap, 0, -self.card_height - self.card_gap):
            for col in range(self.card_gap, self.board_width, self.card_width + self.card_gap):
                max_x, max_y, min_x, min_y = self.card_width + col, row, col, row - self.card_height
                coords.append((max_x, max_y, min_x, min_y))
        self.deck.deal(12, coords)

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

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.draw_cards()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
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
            locations = [card.location for card in self.selected]
            print(locations)
            self.deck.remove(locations, cards=self.selected)
            self.selected = []
        else:
            print('Not a set...')


    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    card_width = 300
    card_height = 175
    card_gap = 25
    game = Game(card_width, card_height, card_gap, 'SET')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
