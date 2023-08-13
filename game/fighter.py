character1 = {"name": "Tobi", "speed": "3",  "element":"fire", "moves": "f23a", "damage": 5, 'defense': 2, "health": 50, "attack": 0}
character2 = {"name": "Jess", "speed": "2",  "element":"water", "moves": "123b", "damage": 4, 'defense': 1, "health": 60, "attack": 0}


class Character:
    def __init__(self,name,speed,element,moves,damage,defense,health,attack):
        self.name = name
        self.speed = speed
        self.element = element
        self.moves = moves
        self.damage = damage
        self.defense = defense
        self.health = health
        self.attack = attack
        self.fighting = False
        self.BaseCharacter = {'name': self.name, 'speed': self.speed, 'element': self.element, 'moves': self.moves, 'damage': self.damage, 'defense': self.defense, 'health': self.health, 'attack': self.attack, 'fighting':self.fighting}
        self.ModifiedCharacter = {'name': self.name, 'speed': self.speed, 'element': self.element, 'moves': self.moves, 'damage': self.damage, 'defense': self.defense, 'health': self.health, 'attack': self.attack, 'fighting':self.fighting}
        

def Create_Fight_Session(session):
    # Create a Session or a Record of this fight in particular
    pass

def Create_New_Session_Table(session):
    sessionTable = "Table", str(session)
    return sessionTable
    # Create a Table to record moves and events that is tied to the previous Session.


def Create_New_Session_Key(session):
    # Create a Key that can be tool to tie instances of Characters to this particular fight and match what characters and acrtions are valid for this fight
    sessionKey = str(session),"aslkfsdognfo2ewqbojkasdnfkonqopakwnoqkwndlaksnfinqoinw"
    return sessionKey

def Initialize_Character(character1, character2):
    # Create versions of the Characters (player 1 and player 2). Figure out what advantages and what not the Characters have now that you know who the opponent is and what their element is
    # This might be redundant, this is creating two dictionaries of the same character. First one is the Modified Character, Second is the Player(1/2) instance. And untouched and waiting
    # for experience or spoils is the Base Character sitting in the Table.
    char1 = character1
    char2 = character2
    modchar_1 = char1.ModifiedCharacter
    modchar_2 = char2.ModifiedCharacter
    def Calculate_Elemental_Advantage(modchar1, modchar2):
        # See what the Advantages of elements are
        # change the attack and defense stats on the MODIFIED Character instance, which will be where the Player isntances draw their information, the base character is left alone
        # so these instances can be recreated with different characters and what not.
        if modchar1["element"] == 'earth':
            if modchar2['element'] == 'earth':
                modchar1['defense'] += 1
                modchar2['defense'] += 1
            if modchar2['element'] == 'water':
                modchar1['damage'] += 1
                modchar1['defense'] += 1
            if modchar2['element'] == 'fire':
                modchar1['defense'] += 1
            if modchar2['element'] == 'air':
                modchar2['damage'] += 2
            if modchar2['element'] == 'aether':
                modchar2['damage'] += 1
        if modchar1['element'] == 'water':
            if modchar2['element'] == 'earth':
                modchar2['damage'] += 1
                modchar2['defense'] += 1
            if modchar2['element'] == 'water':
                pass
            if modchar2['element'] == 'fire':
                modchar1['damage'] += 2
            if modchar2['element'] == 'air':
                pass
            if modchar2['element'] == 'aether':
                modchar2['damage'] += 1
        if modchar1['element'] == 'fire':
            if modchar2['element'] == 'earth':
                modchar2['defense'] += 1
            if modchar2['element'] == 'water':
                modchar2['damage'] += 2
            if modchar2['element'] == 'fire':
                pass
            if modchar2['element'] == 'air':
                modchar1['damage'] += 2
            if modchar2['element'] == 'aether':
                modchar2['damage'] += 1
        if modchar1['element'] == 'air':
            if modchar2['element'] == 'earth':
                modchar1['defense'] += 2
            if modchar2['element'] == 'water':
                pass
            if modchar2['element'] == 'fire':
                modchar2['damage'] += 2
            if modchar2['element'] == 'air':
                pass
            if modchar2['element'] == 'aether':
                modchar2['damage'] += 1
        if modchar1['element'] == 'aether':
                modchar1['damage'] += 1
    def initialize_moves(modchar1, modchar2):
        # The moves are saved as strings that will be decoded and create a list of move variables. That way i can save the moves in a database and when fighting, call the variables vs
        # trying to get full strings to be refence correctly
        def character_moves(char):
            moves_list = []
            for number in char['moves']:
                if number == "1":
                    moves_list.append("Perfection")
                if number == "2":
                    moves_list.append("Flame")
                if number == "3":
                    moves_list.append("Slow")
                if number == "4":
                    moves_list.append("Reroll")
                if number == "5":
                    moves_list.append("Go_Pro")
                if number == "6":
                    moves_list.append("Acid")
                if number == "7":
                    moves_list.append("Lone")
                if number == "8":
                    moves_list.append("Stone_Throw")
                if number == "9":
                    moves_list.append("Still")
                if number == "0":
                    moves_list.append("Give_it_Everything")
                if number == "a":
                    moves_list.append("Punch")
                if number == "b":
                    moves_list.append("Resurrection")
                if number == "c":
                    moves_list.append("No_Bad_Buff")
                if number == "d":
                    moves_list.append("Double_Attack")
                if number == "e":
                    moves_list.append("Virtue")
                if number == "f":
                    moves_list.append("Freeze")
                if number == "g":
                    moves_list.append("Tornado")
                if number == "h":
                    moves_list.append("Boulder_Smash")
                if number == "i":
                    moves_list.append("Gluton")
            char['moves'] = moves_list
        character_moves(modchar1)
        character_moves(modchar2)
        return modchar1, modchar2
    Calculate_Elemental_Advantage(modchar_1, modchar_2)
    modchar1, modchar2 = initialize_moves(modchar_1, modchar_2)

    def add_modifying_moves_to_status_list():
        # There will be a list of status effects, there will be default ones that can happen generally, but in casses where special status effects are used base on some attributing 
        # variable, this is where i would add them. Like moves that make you immune to fire attacks or something.
        pass

    return modchar1, modchar2


def Assign_Character_2_Key(modchar1, modchar2, sessionKey):
    # Now with the Modified Characters and all their Advantages, assign these versions of the characters the Session Key to lock in that these versions of the characters are the ones who will be fighting
    modchar1['key'] = sessionKey
    modchar2['key'] = sessionKey

def Faster_Character_Is_Player1(character1, character2):
    # Now with the Assigned Modified Characters, Player 1 will be who now has the highest Speed Stat
    if character1['speed'] > character2['speed']:
        player1 = character1
        player2 = character2
    else:
        player1 = character2
        player2 = character1
    return player1, player2

def fight_init(session, character1, character2):
    sesTable = Create_New_Session_Table(session)
    sesKey = Create_New_Session_Key(session)
    modchar1, modchar2 = Initialize_Character(character1, character2)
    Assign_Character_2_Key(modchar1, modchar2, sesKey)
    player1 , player2 = Faster_Character_Is_Player1(modchar1, modchar2)
    return player1, player2
    

def fight_round(Attacker, Opponent):
    # Create a while loop that the fight happens in
    def show_Stats(attacker, opponent):
        spaces = " "*15
        full_space = int((len(attacker['name'])) + int(len(opponent['name'])) + 15)
        healthspace = (' '*(full_space - (len(str(attacker['health'])) + len(str(opponent['health'])))))
        print(f"\nIts {attacker['name']}'s Turn\n\n")
        print(f"{attacker['name']}{spaces}{opponent['name']}\n")
        print(f"{attacker['health']}{healthspace}{opponent['health']}\n")
    def player_turn(attacker, opponent):
        def player_move_choice():
            for index, move in enumerate(attacker["moves"]):
                print(index+1,"-",move)
            choice = int(input('pick a move! (Number)'))
            decision = attacker["moves"][choice-1]
            print(decision)
            return decision
        def player_attack_inst():
            move_choice = player_move_choice()
            damage = 5
            print(f"{attacker['name']} used {move_choice}")
            print(f"It did {damage} points of Damage!")
            block = opponent['defense']
            if damage < block:
                damage = 0
            opponent['health'] -= damage
        def status_effect():
            pass
        player_attack_inst()
        status_effect()
    show_Stats(Attacker, Opponent)
    player_turn(Attacker, Opponent)

def WEBattack_inst(attacker, opponent, att_choice):
    move_choice = att_choice
    damage = 25
    print(f"{attacker['name']} used {move_choice}")
    print(f"It did {damage} points of Damage!")
    block = opponent['defense']
    opponent['fighting'] = True
    if damage < block:
        damage = 0
    opponent['health'] -= damage

def death_check(modchar1, modchar2):
    # check to make sure the dead character is dead
    alive = True
    if modchar1['health'] <= 0:
        print(modchar1['health'])
        alive = False
    if modchar2['health'] <= 0:
        print(modchar2['health'])
        alive = False
    return alive

def victory_sequence():
    # pretty self explanitory
    pass

def session_close():
    #add win/lose stats to main database
    pass

def fightLoop(char1, char2, session):
    # print(f"session: {session}")
    player1, player2 = fight_init(session, char1, char2)
    check = death_check(player1, player2)
    # print(check)
    while check:
        fight_round(player1, player2)
        check = (death_check(player1, player2))
        fight_round(player2, player1)
        check = (death_check(player1, player2))
    if death_check == False:
        victory_sequence()
        session_close()

def WEB_fightLoop(char1, char2, session):
    # print(f"session: {session}")
    player1, player2 = fight_init(session, char1, char2)
    # print(check)
    return player1, player2

def WEBfightround_attack(attacker, opponent, att_choice):
    WEBattack_inst(attacker, opponent, att_choice)
    check = (death_check(attacker, opponent))
    return attacker, opponent, check

def WEBdeath_check(death_check):
    if death_check == False:
        victory_sequence()
        session_close()
        return False
    return True

tobi = Character(character1["name"],character1["speed"],character1["element"],character1["moves"],character1["damage"],character1["defense"],character1["health"],character1["attack"])
jess = Character(character2["name"],character2["speed"],character2["element"],character2["moves"],character2["damage"],character2["defense"],character2["health"],character2["attack"])


# fightLoop(tobi, jess, 123456)