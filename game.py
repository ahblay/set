import arcade
from deck import Deck


'''class Game(arcade.Window):
    def __init__(self, card_width, card_height, card_gap, title):
        self.card_width = card_width
        self.card_height = card_height
        self.card_gap = card_gap
        self.window_width = 3 * card_width + 4 * card_gap
        self.window_height = 4 * card_height + 5 * card_gap
        self.title = title
        self.deck = None
        self.play = None
        super().__init__(self.window_width, self.window_height, self.title)

    def open(self, background):
        arcade.open_window(self.window_width, self.window_height, self.title)
        arcade.set_background_color(background)

    def start_render(self):
        arcade.start_render()

    def finish_render(self):
        arcade.finish_render()

    def draw_cards(self):
        for col in range(self.card_gap, self.window_width, self.card_width + self.card_gap):
            for row in range(self.card_gap, self.window_height, self.card_height + self.card_gap):
                arcade.draw_lrtb_rectangle_outline(col,
                                                   self.card_width + col,
                                                   self.card_height + row,
                                                   row,
                                                   arcade.color.GRAY,
                                                   1)

    def init_game(self):
        loc_x = self.card_gap + self.card_width / 2
        loc_y = self.window_height - (self.card_gap + self.card_height / 2)
        counter = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.deal(12)
        self.play = self.deck.play
        for card in self.play:
            print(f"Rendering card: "
                  f"shape = {card.shape}, "
                  f"color = {card.color}, "
                  f"quantity = {card.quantity}, "
                  f"fill = {card.fill}.")
            self.render_card(card, loc_x, loc_y)
            counter += 1
            if counter % 3 == 0:
                loc_x = self.card_gap + self.card_width / 2
                loc_y -= self.card_gap + self.card_height
            else:
                loc_x += self.card_width + card_gap

    def render_card(self, card, loc_x, loc_y):
        if card.shape:
            card.draw(loc_x, loc_y)
        else:
            raise Exception('Card has no shape attribute.')

    def on_mouse_motion(self, x, y, dx, dy):
        print(x)
        print(y)

    def run(self):
        arcade.run()

card_width = 300
card_height = 175
card_gap = 25

window_width = 3 * card_width + 4 * card_gap
window_height = 4 * card_height + 5 * card_gap'''

'''
# big curve top
arcade.draw_arc_outline(center_x=175,
                        center_y=225,
                        width=45,
                        height=45,
                        color=arcade.color.RED,
                        start_angle=25,
                        end_angle=155,
                        border_width=2,
                        tilt_angle=310)
# big curve bottom
arcade.draw_arc_outline(center_x=206,
                        center_y=188,
                        width=45,
                        height=45,
                        color=arcade.color.RED,
                        start_angle=25,
                        end_angle=155,
                        border_width=2,
                        tilt_angle=130)
# second curve right
arcade.draw_arc_outline(center_x=251,
                        center_y=178,
                        width=45,
                        height=30,
                        color=arcade.color.RED,
                        start_angle=5,
                        end_angle=80,
                        border_width=2,
                        tilt_angle=140)
# small curve bottom
arcade.draw_arc_outline(center_x=213,
                        center_y=155,
                        width=11,
                        height=15,
                        color=arcade.color.RED,
                        start_angle=25,
                        end_angle=140,
                        border_width=2,
                        tilt_angle=265)
# second curve left
arcade.draw_arc_outline(center_x=130,
                        center_y=235,
                        width=45,
                        height=30,
                        color=arcade.color.RED,
                        start_angle=5,
                        end_angle=80,
                        border_width=2,
                        tilt_angle=320)
# small curve top
arcade.draw_arc_outline(center_x=168,
                        center_y=258,
                        width=11,
                        height=15,
                        color=arcade.color.RED,
                        start_angle=25,
                        end_angle=140,
                        border_width=2,
                        tilt_angle=85)
'''

'''game = Game(card_width, card_height, card_gap, "SET")
game.open(arcade.color.WHITE)
game.start_render()
game.draw_cards()
game.init_game()
game.finish_render()
game.run()'''


class MyGame(arcade.Window):

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
    game = MyGame(card_width, card_height, card_gap, 'SET')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
