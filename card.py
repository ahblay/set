import arcade


class Card:
    def __init__(self, color, shape, quantity, fill):
        self.color = color
        self.shape = shape
        self.fill = fill
        self.quantity = quantity
        self.location = ()
        self.border = {'color': arcade.color.GRAY, 'width': 1}
        self.overflow = False

    def draw(self, loc_x, loc_y):
        if self.shape == 'squiggle':
            if self.quantity == '3':
                self.squiggle(loc_x - 80, loc_y, self.fill)
                self.squiggle(loc_x, loc_y, self.fill)
                self.squiggle(loc_x + 80, loc_y, self.fill)
            if self.quantity == '2':
                self.squiggle(loc_x - 40, loc_y, self.fill)
                self.squiggle(loc_x + 40, loc_y, self.fill)
            else:
                self.squiggle(loc_x, loc_y, self.fill)

        if self.shape == 'oval':
            if self.quantity == '3':
                self.oval(loc_x - 80, loc_y, self.fill)
                self.oval(loc_x, loc_y, self.fill)
                self.oval(loc_x + 80, loc_y, self.fill)
            if self.quantity == '2':
                self.oval(loc_x - 40, loc_y, self.fill)
                self.oval(loc_x + 40, loc_y, self.fill)
            else:
                self.oval(loc_x, loc_y, self.fill)

        if self.shape == 'diamond':
            if self.quantity == '3':
                self.diamond(loc_x - 80, loc_y, self.fill)
                self.diamond(loc_x, loc_y, self.fill)
                self.diamond(loc_x + 80, loc_y, self.fill)
            if self.quantity == '2':
                self.diamond(loc_x - 40, loc_y, self.fill)
                self.diamond(loc_x + 40, loc_y, self.fill)
            else:
                self.diamond(loc_x, loc_y, self.fill)

    def fill_diamond(self, point_list, color):
        arcade.draw_polygon_filled(point_list, color)

    def fill_oval(self, loc_x, loc_y, color):
        arc_width = 30
        arc_height = 30
        line_height = 65

        top_arc_y = loc_y + line_height / 2
        bottom_arc_y = loc_y - line_height / 2
        left_line_x = loc_x - arc_width
        right_line_x = loc_x + arc_width
        point_list = (
            (left_line_x, top_arc_y),
            (left_line_x, bottom_arc_y),
            (right_line_x, bottom_arc_y),
            (right_line_x, top_arc_y)
        )
        arcade.draw_arc_filled(loc_x,
                               top_arc_y,
                               arc_width,
                               arc_height,
                               color,
                               0, 180)
        arcade.draw_arc_filled(loc_x,
                               bottom_arc_y,
                               arc_width,
                               arc_height,
                               color,
                               180, 360)
        arcade.draw_polygon_filled(point_list,
                                   color)

    def fill_squiggle(self, loc_x, loc_y, color):
        point_list = (
            (loc_x - 25, loc_y + 55),
            (loc_x - 35, loc_y + 50),
            (loc_x - 17, loc_y + 19),
            (loc_x - 23, loc_y),
            (loc_x + 25, loc_y - 55),
            (loc_x + 35, loc_y - 50),
            (loc_x + 21, loc_y - 20),
            (loc_x + 22, loc_y + 1)
        )

        arcade.draw_arc_filled(center_x=loc_x - 16,
                                center_y=loc_y + 19,
                                width=45,
                                height=45,
                                color=color,
                                start_angle=25,
                                end_angle=155,
                                tilt_angle=310)
        arcade.draw_arc_filled(center_x=loc_x + 15,
                                center_y=loc_y - 18,
                                width=45,
                                height=45,
                                color=color,
                                start_angle=25,
                                end_angle=155,
                                tilt_angle=130)
        arcade.draw_arc_filled(center_x=loc_x + 22,
                                center_y=loc_y - 51,
                                width=11,
                                height=15,
                                color=color,
                                start_angle=25,
                                end_angle=140,
                                tilt_angle=265)
        arcade.draw_arc_filled(center_x=loc_x - 23,
                                center_y=loc_y + 52,
                                width=11,
                                height=15,
                                color=color,
                                start_angle=25,
                                end_angle=140,
                                tilt_angle=85)
        arcade.draw_polygon_filled(point_list, color)

    def shade_diamond(self, loc_x, loc_y, color):
        border_width = 4
        point_list = (
            (loc_x - 6, loc_y + 52),
            (loc_x + 6, loc_y + 52),
            (loc_x - 12, loc_y + 39),
            (loc_x + 12, loc_y + 39),
            (loc_x - 19, loc_y + 26),
            (loc_x + 19, loc_y + 26),
            (loc_x - 23, loc_y + 13),
            (loc_x + 23, loc_y + 13),
            (loc_x - 28, loc_y),
            (loc_x + 28, loc_y),
            (loc_x - 6, loc_y - 52),
            (loc_x + 6, loc_y - 52),
            (loc_x - 12, loc_y - 39),
            (loc_x + 12, loc_y - 39),
            (loc_x - 19, loc_y - 26),
            (loc_x + 19, loc_y - 26),
            (loc_x - 23, loc_y - 13),
            (loc_x + 23, loc_y - 13)
        )

        arcade.draw_lines(point_list, color, border_width)

    def shade_oval(self, loc_x, loc_y, color):
        border_width = 4
        point_list = (
            (loc_x - 24, loc_y + 52),
            (loc_x + 24, loc_y + 52),
            (loc_x - 28, loc_y + 39),
            (loc_x + 28, loc_y + 39),
            (loc_x - 28, loc_y + 26),
            (loc_x + 28, loc_y + 26),
            (loc_x - 28, loc_y + 13),
            (loc_x + 28, loc_y + 13),
            (loc_x - 28, loc_y),
            (loc_x + 28, loc_y),
            (loc_x - 24, loc_y - 52),
            (loc_x + 24, loc_y - 52),
            (loc_x - 28, loc_y - 39),
            (loc_x + 28, loc_y - 39),
            (loc_x - 28, loc_y - 26),
            (loc_x + 28, loc_y - 26),
            (loc_x - 28, loc_y - 13),
            (loc_x + 28, loc_y - 13)
        )

        arcade.draw_lines(point_list, color, border_width)

    def shade_squiggle(self, loc_x, loc_y, color):
        border_width = 4
        point_list = (
            (loc_x - 36, loc_y + 52),
            (loc_x + 16, loc_y + 52),
            (loc_x - 29, loc_y + 39),
            (loc_x + 26, loc_y + 39),
            (loc_x - 23, loc_y + 26),
            (loc_x + 28, loc_y + 26),
            (loc_x - 23, loc_y + 13),
            (loc_x + 28, loc_y + 13),
            (loc_x - 28, loc_y),
            (loc_x + 26, loc_y),
            (loc_x - 16, loc_y - 52),
            (loc_x + 35, loc_y - 52),
            (loc_x - 26, loc_y - 39),
            (loc_x + 28, loc_y - 39),
            (loc_x - 29, loc_y - 26),
            (loc_x + 22, loc_y - 26),
            (loc_x - 28, loc_y - 13),
            (loc_x + 22, loc_y - 13)
        )

        arcade.draw_lines(point_list, color, border_width)

    def squiggle(self, loc_x, loc_y, fill=None):
        border_width = 5
        if self.color == 'red':
            color = arcade.color.RED
        elif self.color == 'green':
            color = arcade.color.GO_GREEN
        elif self.color == 'purple':
            color = arcade.color.PURPLE_HEART
        else:
            color = arcade.color.BLACK
        # big curve top
        arcade.draw_arc_outline(center_x=loc_x - 16,
                                center_y=loc_y + 19,
                                width=45,
                                height=45,
                                color=color,
                                start_angle=25,
                                end_angle=155,
                                border_width=border_width,
                                tilt_angle=310)
        # big curve bottom
        arcade.draw_arc_outline(center_x=loc_x + 15,
                                center_y=loc_y - 18,
                                width=45,
                                height=45,
                                color=color,
                                start_angle=25,
                                end_angle=155,
                                border_width=border_width,
                                tilt_angle=130)
        # second curve right
        arcade.draw_arc_outline(center_x=loc_x + 60,
                                center_y=loc_y - 28,
                                width=45,
                                height=30,
                                color=color,
                                start_angle=5,
                                end_angle=80,
                                border_width=border_width,
                                tilt_angle=140)
        # small curve bottom
        arcade.draw_arc_outline(center_x=loc_x + 22,
                                center_y=loc_y - 51,
                                width=11,
                                height=15,
                                color=color,
                                start_angle=25,
                                end_angle=140,
                                border_width=border_width,
                                tilt_angle=265)
        # second curve left
        arcade.draw_arc_outline(center_x=loc_x - 61,
                                center_y=loc_y + 29,
                                width=45,
                                height=30,
                                color=color,
                                start_angle=5,
                                end_angle=80,
                                border_width=border_width,
                                tilt_angle=320)
        # small curve top
        arcade.draw_arc_outline(center_x=loc_x - 23,
                                center_y=loc_y + 52,
                                width=11,
                                height=15,
                                color=color,
                                start_angle=25,
                                end_angle=140,
                                border_width=border_width,
                                tilt_angle=85)

        if fill == 'shaded':
            self.shade_squiggle(loc_x, loc_y, color)

        if fill == 'solid':
            self.fill_squiggle(loc_x, loc_y, color)

    def oval(self, loc_x, loc_y, fill=None):
        arc_width = 30
        arc_height = 30
        line_height = 65
        border_width = 5
        if self.color == 'red':
            color = arcade.color.RED
        elif self.color == 'green':
            color = arcade.color.GO_GREEN
        elif self.color == 'purple':
            color = arcade.color.PURPLE_HEART
        else:
            color = arcade.color.BLACK

        top_arc_y = loc_y + line_height / 2
        bottom_arc_y = loc_y - line_height / 2
        left_line_x = loc_x - arc_width
        right_line_x = loc_x + arc_width
        arcade.draw_arc_outline(loc_x,
                                top_arc_y,
                                arc_width,
                                arc_height,
                                color,
                                0, 180,
                                border_width)
        arcade.draw_arc_outline(loc_x,
                                bottom_arc_y,
                                arc_width,
                                arc_height,
                                color,
                                180, 360,
                                border_width)
        arcade.draw_line(left_line_x,
                         bottom_arc_y,
                         left_line_x,
                         top_arc_y,
                         color,
                         border_width)
        arcade.draw_line(right_line_x,
                         bottom_arc_y,
                         right_line_x,
                         top_arc_y,
                         color,
                         border_width)

        if fill == 'shaded':
            self.shade_oval(loc_x, loc_y, color)

        if fill == 'solid':
            self.fill_oval(loc_x, loc_y, color)

    def diamond(self, loc_x, loc_y, fill=None):
        height = 125
        width = 60
        border_width = 5
        if self.color == 'red':
            color = arcade.color.RED
        elif self.color == 'green':
            color = arcade.color.GO_GREEN
        elif self.color == 'purple':
            color = arcade.color.PURPLE_HEART
        else:
            color = arcade.color.BLACK

        x_1 = loc_x - width / 2
        y_1 = loc_y
        x_2 = loc_x
        y_2 = loc_y + height / 2
        x_3 = loc_x + width / 2
        y_3 = loc_y
        x_4 = loc_x
        y_4 = loc_y - height / 2
        point_list = (
            (x_1, y_1),
            (x_2, y_2),
            (x_3, y_3),
            (x_4, y_4),
            (x_1, y_1)
        )

        arcade.draw_line_strip(point_list, color, border_width)

        if fill == 'shaded':
            self.shade_diamond(loc_x, loc_y, color)

        if fill == 'solid':
            self.fill_diamond(point_list, color)

