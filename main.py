import tkinter
import game


width = 750
height = 370

canvas_size = 300
box_size = (canvas_size-20)/10


def create_grid(canvas):
    for i in range(11):
        canvas.create_line(10, 10+box_size*i, 291, 10+box_size*i)
        canvas.create_line(10+box_size*i, 10, 10+box_size*i, 291)


global clicked_ship
clicked_ship = None

def pressed_button_1(event):
    if not game.ships_been_validated:
        x = event.x
        y = event.y
        global clicked_ship
        clicked_ship = None
        for ship in game.ship_list:
            ship_width = ship['width'] * box_size + 1
            x_begin = ship['coordinate']['x']
            x_end = x_begin + ship_width + 1
            if x == max(min(x_end, x),x_begin):
                y_begin = ship['coordinate']['y']
                y_end = y_begin + box_size
                if y == max(min(y_end, y),y_begin):
                    clicked_ship = ship

def release_button_1(event):
    if not game.ships_been_validated:
        x = event.x
        y = event.y
        coordinate_box_x = (int((x-10)/28)*28)+10
        coordinate_box_y = (int((y-10)/28)*28)+10
        box_x = int((x-10)/28)
        box_y = int((y-10)/28)
        global clicked_ship
        if clicked_ship:
            id = clicked_ship['id']
            width = clicked_ship['width']
            
            x_begin = int((x-10)/28)
            x_end = x_begin + width

            y_begin = int((y-10)/28)
            y_end = y_begin + 0

            valid_coordinate = True
            for cord in [x_begin, x_end, y_begin, y_end]:
                if cord < 0 or cord > 10:
                    valid_coordinate = False


            for i in range(width):
                for other_ship in game.ship_list:
                    other_ship_width = other_ship['width']
                    other_ship_box_x = other_ship['box']['x']
                    other_ship_box_y = other_ship['box']['y']
                    for j in range(other_ship_width):
                        if box_x + i == other_ship_box_x + j:
                            if box_y == other_ship_box_y:
                                if id != other_ship['id']:
                                    valid_coordinate = False


            if valid_coordinate:
                canvas1.coords(clicked_ship['img'], coordinate_box_x, coordinate_box_y)
                clicked_ship['coordinate']['x'] = coordinate_box_x
                clicked_ship['coordinate']['y'] = coordinate_box_y
                clicked_ship['box']['x'] = box_x
                clicked_ship['box']['y'] = box_y
            else:
                canvas1.coords(clicked_ship['img'], clicked_ship['coordinate']['x'], clicked_ship['coordinate']['y'])

def motion_button_1(event):
    x = event.x
    y = event.y
    box_x = (int((x-10)/28)*28)+10
    box_y = (int((y-10)/28)*28)+10
    global clicked_ship
    if clicked_ship and not game.ships_been_validated:
        canvas1.coords(clicked_ship['img'], box_x, box_y)
        # canvas1.coords(clicked_ship['img'], x, y)


def coordinate(event):
    x = event.x
    y = event.y
    box_x = int((x-10)/28)
    box_y = int((y-10)/28)
    return [box_x, box_y]



root = tkinter.Tk()
root.title('Bataille navale')
root.geometry(f"{width}x{height}")


tkinter.Label(root, text="🛡 Zone de placement des bateaux").grid(row=0, column=0, columnspan=2)
tkinter.Label(root, text="🎯 Zone de tir").grid(row=0, column=3, columnspan=2)

# title1 = tkinter.Label(root, text="🛡 Zone de placement des bateaux")
# title1.grid(row=0, column=0, columnspan=2)
# title2 = tkinter.Label(root, text="🎯 Zone de tir")
# title2.grid(row=0, column=3, columnspan=2)




canvas1 = tkinter.Canvas(root, width=450, height=canvas_size)
canvas1.grid(row=1, column=0, columnspan=3)
create_grid(canvas1)

canvas1.bind('<Button-1>', lambda e: pressed_button_1(e))
canvas1.bind('<ButtonRelease-1>', lambda e: release_button_1(e))
canvas1.bind('<B1-Motion>', lambda e: motion_button_1(e))

canvas2 = tkinter.Canvas(root, width=canvas_size, height=canvas_size)
canvas2.grid(row=1, column=3, columnspan=2)
create_grid(canvas2)
canvas2.bind('<Button-1>', lambda e: game.confirm_target(coordinate(e)))


button1 = tkinter.Button(root, text="✔ valider placement", command=lambda: game.confirm_placement())
button1.grid(row=2, column=0, columnspan=2)

button2 = tkinter.Button(root, text="⚔ Rejouer", command=lambda: game.replay())
button2.grid(row=2, column=3, columnspan=2)


game = game.BatailleNavale(canvas1, canvas2, root)










root.mainloop()