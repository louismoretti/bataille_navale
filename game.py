import tkinter




class BatailleNavale():
    def __init__(self, canvas, canvas2, root):
        self.canvas = canvas
        self.canvas2 = canvas2
        self.canvas2_images = []
        self.root = root
        self.ships_been_validated = False
        """
        1 Porte-avions (5 cases) ;
        1 Croiseur (4 cases) ;
        2 Contre-torpilleurs (3 cases) ;
        1 Torpilleur (2 cases).
        """
        
        self.photo_Aircraft_Carrier = tkinter.PhotoImage(file="5.png")
        self.photo_Cruiser = tkinter.PhotoImage(file="4.png")
        self.photo_Destroyer = tkinter.PhotoImage(file="3.png")
        self.photo_Torpedo_Ship = tkinter.PhotoImage(file="2.png")

        self.image_Aircraft_Carrier = self.canvas.create_image(300, 10, image=self.photo_Aircraft_Carrier, anchor="nw")
        self.image_Cruiser = self.canvas.create_image(300, 66, image=self.photo_Cruiser, anchor="nw")
        self.image_Destroyer = self.canvas.create_image(300, 122, image=self.photo_Destroyer, anchor="nw")
        self.image_Destroyer2 = self.canvas.create_image(300, 178, image=self.photo_Destroyer, anchor="nw")
        self.image_Torpedo_Ship = self.canvas.create_image(300, 234, image=self.photo_Torpedo_Ship, anchor="nw")

        self.aircraft_carrier = {
            'id': 'aircraft_carrier',
            'width':5,
            'img':self.image_Aircraft_Carrier,
            'coordinate':{'x':300, 'y':10},
            'box':{'x':int((300-10)/28), 'y':int((10-10)/28)}}
        self.cruiser = {
            'id':'cruiser',
            'width':4,
            'img':self.image_Cruiser,
            'coordinate':{'x':300, 'y':66},
            'box':{'x':int((300-10)/28), 'y':int((66-10)/28)}}
        self.destroyer = {
            'id': 'destroyer',
            'width':3,
            'img':self.image_Destroyer,
            'coordinate':{'x':300, 'y':122},
            'box':{'x':int((300-10)/28), 'y':int((122-10)/28)}}
        self.destroyer2 = {
            'id': 'destroyer2',
            'width':3,
            'img':self.image_Destroyer2,
            'coordinate':{'x':300, 'y':178},
            'box':{'x':int((300-10)/28), 'y':int((178-10)/28)}}
        self.torpedo_ship = {
            'id': 'torpedo_ship',
            'width':2,
            'img':self.image_Torpedo_Ship,
            'coordinate':{'x':300, 'y':234},
            'box':{'x':int((300-10)/28), 'y':int((234-10)/28)}}

        self.ship_list = [self.aircraft_carrier, self.cruiser,
                        self.destroyer, self.destroyer2,
                        self.torpedo_ship]
    
    def confirm_placement(self):
        self.ships_been_validated = True

    def confirm_target(self, click_coordinate:list = [0,0]):
        if self.ships_been_validated == True:
            print(click_coordinate)

    def replay(self):
        self.__init__(self.canvas, self.canvas2, self.root)
        for i in range(len(self.canvas2_images)):
            self.canvas2.delete(f"{i}")