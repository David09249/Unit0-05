# Created by: David Wang
# Created on: 18-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-05
# This program displays area and perimeter of a rectangle

import ui

def answer_touch_up_inside(sender):
    view['area_answer_label'].text = 'Area = ' + str(3*5) + ' cm^2'
    view['perimeter_answer_label'].text = 'Perimeter = ' + str(2*(5+3)) + ' cm'

view = ui.load_view()
view.present('full_screen')
