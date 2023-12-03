from customtkinter import *
from PIL import ImageTk, Image

#The package for the window
shop_window = CTk()
shop_window.geometry("600x600")
shop_window.resizable(False, False)
shop_window.title("Fruit Shop")
# shop_window.configure(bg='#0D1117')

#The main list of the cart
shopping_cart = []

class CenteringGrid(CTkFrame):
    def __init__(self, parent, child):
        CTkFrame.__init__(self, parent)
        child.grid(row=0, column=0)
        child.grid_rowconfigure(0, weight = 1)
        child.grid_rowconfigure(1, weight = 1)
        child.grid_rowconfigure(2, weight = 1)
        child.grid_rowconfigure(3, weight = 1)
        child.grid_columnconfigure(0, weight = 1)
        child.grid_columnconfigure(1, weight = 1)
        child.grid_columnconfigure(2, weight = 1)
        child.grid_propagate(False)
       
# Current cart details frame
right_frame = CTkFrame(master=shop_window, width=200, height=600)
right_frame.grid(row=0, column=1)
right_frame.grid_propagate(False)
right_frame.columnconfigure(0, weight=1)

# Adding string variables for each fruit in the cart details
cart_apples = StringVar()
cart_banana = StringVar()
cart_cherry = StringVar()
cart_grapes = StringVar()
cart_lemon = StringVar()
cart_orange = StringVar()
cart_pineapple = StringVar()
cart_strawberry = StringVar()
cart_watermelon = StringVar()

# Class for the backend part
class FruitShop:
    def __init__(self):
        self.apple = 0
        self.banana = 0
        self.cherry = 0
        self.grapes = 0
        self.lemon = 0
        self.orange = 0
        self.pineapple = 0
        self.strawberry = 0
        self.watermelon = 0

    def check_value(self, fruit, add=False, reduce=False):
        if add and (getattr(self, fruit) + 1 > 99): 
            return False
        elif reduce and (getattr(self, fruit) - 1 < 0):
            return False
        return True

        
    def set_label(self, fruit):
        match fruit:
            case "apple": 
                cart_apples.set(f"APPLE X {self.apple}")
            case "banana": 
                cart_banana.set(f"BANANA X {self.banana}")
            case "cherry": 
                cart_cherry.set(f"CHERRY X {self.cherry}")
            case "grapes": 
                cart_grapes.set(f"GRAPES X {self.grapes}")
            case "lemon": 
                cart_lemon.set(f"LEMON X {self.lemon}")
            case "orange": 
                cart_orange.set(f"ORANGE X {self.orange}")
            case "pineapple": 
                cart_pineapple.set(f"PINEAPPLE X {self.pineapple}")
            case "strawberry": 
                cart_strawberry.set(f"STRAWBERRY X {self.strawberry}")
            case "watermelon": 
                cart_watermelon.set(f"WATERMELON X {self.watermelon}")

    def add_to_cart(self, fruit):
        if not self.check_value(fruit, True, False):
            return
        
        match fruit:
            case "apple": 
                self.apple += 1
            case "banana": 
                self.banana += 1
            case "cherry": 
                self.cherry += 1
            case "grapes": 
                self.grapes += 1
            case "lemon": 
                self.lemon += 1
            case "orange": 
                self.orange += 1
            case "pineapple": 
                self.pineapple += 1
            case "strawberry": 
                self.strawberry += 1
            case "watermelon": 
                self.watermelon += 1
        
        self.set_label(fruit)

    def reduce_cart_quantity(self, fruit):
        if not self.check_value(fruit, False, True):
            return
        
        match fruit:
            case "apple": 
                self.apple -= 1
            case "banana": 
                self.banana -= 1
            case "cherry": 
                self.cherry -= 1
            case "grapes": 
                self.grapes -= 1
            case "lemon": 
                self.lemon -= 1
            case "orange": 
                self.orange -= 1
            case "pineapple": 
                self.pineapple -= 1
            case "strawberry": 
                self.strawberry -= 1
            case "watermelon": 
                self.watermelon -= 1
        
        self.set_label(fruit)
        

# Creation of the fruit shop backend side
fruit_shop = FruitShop()

# Setting inital cart details
cart_apples.set(f"APPLE X {fruit_shop.apple}")
cart_banana.set(f"BANANA X {fruit_shop.banana}")
cart_cherry.set(f"CHERRY X {fruit_shop.cherry}")
cart_grapes.set(f"GRAPES X {fruit_shop.grapes}")
cart_lemon.set(f"LEMON X {fruit_shop.lemon}")
cart_orange.set(f"ORANGE X {fruit_shop.orange}")
cart_pineapple.set(f"PINEAPPLE X {fruit_shop.pineapple}")
cart_strawberry.set(f"STRAWBERRY X {fruit_shop.strawberry}")
cart_watermelon.set(f"WATERMELON X {fruit_shop.watermelon}")

left_frame = CTkFrame(master=shop_window, width=400, height=600, fg_color="#C5FFF8")
left_frame.grid(row=0, column=0)
left_frame.grid_propagate(False)

inner_left_frame = CTkFrame(master=left_frame, width=380, height=580, fg_color="#7B66FF")
#Instantiating to center the inner_left_frame
CenteringGrid(left_frame, inner_left_frame)
left_frame.grid_rowconfigure(0, weight=1)
left_frame.grid_columnconfigure(0, weight=1)

# Start of creation of grid cells in the left frame
# Main title
main_label = CTkLabel(master=inner_left_frame, text="CHOOSE FRUIT!", font=("Open Sans Medium", 18, "bold"))
main_label.grid(row=0, column=1, sticky="N", padx=10, pady=10)

apple_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
apple_image = CTkImage(dark_image=Image.open("assets/apple.png"), size=(60, 60))
apple_image_label = CTkLabel(master=apple_frame, image=apple_image, text="")
apple_image_label.grid(row=0, column=0)

# Adding of button 
apple_add_button = CTkButton(apple_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("apple"))
apple_add_button.grid(row=1, column=0, pady=(10, 0),  sticky="E")
apple_remove_button = CTkButton(apple_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("apple"))
apple_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
# Actual Positioning of the frame to inner left frame
apple_frame.grid(row=1, column=0, sticky="NE")

banana_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
banana_image = CTkImage(dark_image=Image.open("assets/banana.png"), size=(60, 60))
banana_image_label = CTkLabel(master=banana_frame, image=banana_image, text="")
banana_image_label.grid(row=0, column=0)
banana_add_button = CTkButton(banana_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("banana"))
banana_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
banana_remove_button = CTkButton(banana_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("banana"))
banana_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
banana_frame.grid(row=1, column=1, sticky="N")

cherry_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
cherry_image = CTkImage(dark_image=Image.open("assets/cherry.png"), size=(60, 60))
cherry_image_label = CTkLabel(master=cherry_frame, image=cherry_image, text="")
cherry_image_label.grid(row=0, column=0)
cherry_add_button = CTkButton(cherry_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("cherry"))
cherry_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
cherry_remove_button = CTkButton(cherry_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("cherry"))
cherry_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
cherry_frame.grid(row=1, column=2, sticky="NW")

grapes_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
grapes_image = CTkImage(dark_image=Image.open("assets/grapes.png"), size=(60, 60))
grapes_image_label = CTkLabel(master=grapes_frame, image=grapes_image, text="")
grapes_image_label.grid(row=0, column=0)
grapes_add_button = CTkButton(grapes_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("grapes"))
grapes_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
grapes_remove_button = CTkButton(grapes_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("grapes"))
grapes_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
grapes_frame.grid(row=2, column=0, sticky="NE")

lemon_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
lemon_image = CTkImage(dark_image=Image.open("assets/lemon.png"), size=(60, 60))
lemon_image_label = CTkLabel(master=lemon_frame, image=lemon_image, text="")
lemon_image_label.grid(row=0, column=0)
lemon_add_button = CTkButton(lemon_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("lemon"))
lemon_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
lemon_remove_button = CTkButton(lemon_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("lemon"))
lemon_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
lemon_frame.grid(row=2, column=1, sticky="N")

orange_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
orange_image = CTkImage(dark_image=Image.open("assets/orange.png"), size=(60, 60))
orange_image_label = CTkLabel(master=orange_frame, image=orange_image, text="")
orange_image_label.grid(row=0, column=0)
orange_add_button = CTkButton(orange_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("orange"))
orange_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
orange_remove_button = CTkButton(orange_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("orange"))
orange_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
orange_frame.grid(row=2, column=2, sticky="NW")

pineapple_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
pineapple_image = CTkImage(dark_image=Image.open("assets/pineapple.png"), size=(60, 60))
pineapple_image_label = CTkLabel(master=pineapple_frame, image=pineapple_image, text="")
pineapple_image_label.grid(row=0, column=0)
pineapple_add_button = CTkButton(pineapple_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("pineapple"))
pineapple_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
pineapple_remove_button = CTkButton(pineapple_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("pineapple"))
pineapple_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
pineapple_frame.grid(row=3, column=0, sticky="NE")

strawberry_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
strawberry_image = CTkImage(dark_image=Image.open("assets/strawberry.png"), size=(60, 60))
strawberry_image_label = CTkLabel(master=strawberry_frame, image=strawberry_image, text="")
strawberry_image_label.grid(row=0, column=0)
strawberry_add_button = CTkButton(strawberry_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("strawberry"))
strawberry_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
strawberry_remove_button = CTkButton(strawberry_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("strawberry"))
strawberry_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
strawberry_frame.grid(row=3, column=1, sticky="N")

watermelon_frame = CTkFrame(master=inner_left_frame, width=100, height=100, fg_color="#7B66FF")
watermelon_image = CTkImage(dark_image=Image.open("assets/watermelon.png"), size=(60, 60))
watermelon_image_label = CTkLabel(master=watermelon_frame, image=watermelon_image, text="")
watermelon_image_label.grid(row=0, column=0)
watermelon_add_button = CTkButton(watermelon_frame, text="ADD", height=30, width=65, command = lambda: fruit_shop.add_to_cart("watermelon"))
watermelon_add_button.grid(row=1, column=0, pady=(10, 0), sticky="E")
watermelon_remove_button = CTkButton(watermelon_frame, text="REMOVE", height=30, width=65, fg_color="#c21a04", command = lambda: fruit_shop.reduce_cart_quantity("watermelon"))
watermelon_remove_button.grid(row=2, column=0, pady=(5, 0), sticky="E")
watermelon_frame.grid(row=3, column=2, sticky="NW")
# End of creation of grid cells in the left frame


# Each label in the current cart details from the right frame
apples_label = CTkLabel(master=right_frame, textvariable=cart_apples, anchor="w", justify="left", font=("Open Sans Medium", 18, "bold"))
apples_label.grid(row=0, column=0, sticky="W", padx=(15, 0), pady=10)
banana_label = CTkLabel(master=right_frame, textvariable=cart_banana, font=("Open Sans Medium", 18, "bold"))
banana_label.grid(row=1, column=0, sticky="W", padx=(15, 0), pady=10)
cherry_label = CTkLabel(master=right_frame, textvariable=cart_cherry, font=("Open Sans Medium", 18, "bold"))
cherry_label.grid(row=2, column=0, sticky="W", padx=(15, 0), pady=10)
grapes_label = CTkLabel(master=right_frame, textvariable=cart_grapes, font=("Open Sans Medium", 18, "bold"))
grapes_label.grid(row=3, column=0, sticky="W", padx=(15, 0), pady=10)
lemon_label = CTkLabel(master=right_frame, textvariable=cart_lemon, font=("Open Sans Medium", 18, "bold"))
lemon_label.grid(row=4, column=0, sticky="W", padx=(15, 0), pady=10)
orange_label = CTkLabel(master=right_frame, textvariable=cart_orange, font=("Open Sans Medium", 18, "bold"))
orange_label.grid(row=5, column=0, sticky="W", padx=(15, 0), pady=10)
pineapple_label = CTkLabel(master=right_frame, textvariable=cart_pineapple, font=("Open Sans Medium", 18, "bold"))
pineapple_label.grid(row=6, column=0, sticky="W", padx=(15, 0), pady=10)
strawberry_label = CTkLabel(master=right_frame, textvariable=cart_strawberry, font=("Open Sans Medium", 18, "bold"))
strawberry_label.grid(row=7, column=0, sticky="W", padx=(15, 0), pady=10)
watermelon_label = CTkLabel(master=right_frame, textvariable=cart_watermelon, font=("Open Sans Medium", 18, "bold"))
watermelon_label.grid(row=8, column=0, sticky="W", padx=(15, 0), pady=10)

shop_window.mainloop()








