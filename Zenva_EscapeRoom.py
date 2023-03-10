#This is a simple text based escape room game. There is only 1 room to explore, be sure to inspect all of the items around you to find the code.

#Game Objects--------------
class GameObject:
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"
    
    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"

#game rooms--------------------
class Room: 
    escape_code = 0
    game_objects = []
    
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return self.escape_code == code
    

    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

#Game Class----------------
class Game:
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(287, objects)
        
    def create_objects(self):
        return[
            GameObject("Sweater", "It's a blue sweater that had the number 123 stitched on it", "You can feel that someone has unstitched everything but the number 2", "It smells of cigarettes."),
            GameObject("Chair", "It's one of those old metal schooldesk chairs, covered in gouges and pen drawings", "You can feel 8 lines gouged into the underside of the chair.","You quickly realize you have no idea who has sat there and regret putting your nose in it."),
            GameObject("Magazine", "It's an old magazine that looks to be about mens health", "Flipping through the pages, you notice page 7 has been ripped out", "You take a moment of meditation to enjoy the cologne samples. Mmmm, Sandlewood."),
            GameObject("Bear", "It is a taxedermied bear, standing about 7 feet tall.", "You find the bear's hair is more stiff than you expected.", "It smells musty, as expected. Maybe look for the Febreeze."),
            GameObject("Vape Pen", "Woah dude! A vape with some fluid left in it! You wonder if it's got any charge left.", "It feels smooth, you twist the cartridge to make sure it's fully seated.", "You proceed to jam the vape pen up your nose and inhale. It takes you a moment to remember that you have no idea how to smoke. Luckily for you the battery is dead."),
            GameObject("Knife", "It's old and rusted but the blade looks to have been crudely sharpened", "It cuts a few layers of your skin. You wonder why you did that.", "It smells like rust"),
            GameObject("Shopping Receipt", "It's very long and a little crumpled but you can read the letters 'CVS' at the top", "It feels like paper", "It smells like gasoline"),
        ]
    
    #retrieve user input and assign it to the self variable
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if selection >= 1 and selection <= 5:
            self.select_object(selection - 1)
            self.take_turn()
        else:
            is_code_correct = self.guess_code(selection)
            if is_code_correct:
                print("You made it out.")
            else:
                if self.attempts == 3:
                    print("You have failed.\nGame Over.")
                elif self.attempts <= 3:
                    print(f"Wrong. {self.attempts} tries used.")
                    self.take_turn()
    
    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}.{name}\n"
            index += 1
        return prompt
        
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)
    
    def get_object_interaction_string(self, name):
        return f"""How do you want to interact with the {name}?\n
            1. Look\n
            2. Touch\n
            3. Smell\n"""

    def interact_with_object(self, object, interaction):
        if interaction == '1':
            return object.look()
        elif interaction == '2':
            return object.touch()
        elif interaction == '3':
            return object.sniff()
        else:
            print("That won't do anything")
        return ""

    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False


#The Game. The bit that does all the stuff.----------------------------------------------------
print("""Do you want to play a game?\nYou have three tries to guess the code.\nGood Luck.\n""")
game = Game()
game.take_turn()



#Unit Testing --------------------------------------
class RoomTests:
    def __init__(self):
        self.room_1 = Room(111, 
                           [GameObject("Sweater", "It's a blue sweater that had the number 123 stitched on it", "You can feel that someone has unstitched everything but the number 2", "It smells of cigarettes."), 
                            GameObject("Shopping Receipt", "It's very long and a little crumpled but you can read the letters 'CVS' at the top", "It feels like paper", "It smells like gasoline")],)
        self.room_2 = Room(222, [])

    def test_check_code(self):
        self.room_1.check_code(111) == True
        self.room_1.check_code(222) == False
    
    def test_get_game_object_names(self):
        print(self.room_1.get_game_object_names() == ['Sweater', 'Chair'])
        print(self.room_2.get_game_object_names() == [])
        

#tests = RoomTests()
#tests.test_check_code
#tests.test_get_game_object_names