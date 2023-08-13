from flask import Blueprint, render_template, request, redirect, url_for
from .fighter import *

homePage = Blueprint('homePage', __name__)

tobi = Character(character1["name"],character1["speed"],character1["element"],character1["moves"],character1["damage"],character1["defense"],character1["health"],character1["attack"])
jess = Character(character2["name"],character2["speed"],character2["element"],character2["moves"],character2["damage"],character2["defense"],character2["health"],character2["attack"])
game_session = 123456
player1, player2 = WEB_fightLoop(tobi, jess, game_session)

@homePage.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('start_fight') == ('start_fight'):
            content = 'startFight'
            return redirect(url_for('homePage.fight', turn=content))
    return render_template("base.html")

@homePage.route("/endFight")
def endfight():
    return render_template("base.html")

@homePage.route("/fight", methods=['GET', 'POST'])
def fight():
    if request.method == 'POST':
        p1_name = player1["name"]
        p2_name = player2["name"]
        p1_health = player1["health"]
        p2_health = player2["health"]
        p1_moves = player1["moves"]
        p2_moves = player2["moves"]
        p1_fight = player1["fighting"]
        p2_fight = player2["fighting"]
        if request.form.get('start_fight') == 'start_fight':
            whoesturn = 'start_fight'
            quote = f"Lets Fight"
            return render_template("fight.html",WHOSTURN=whoesturn, p1=player1, p1_name=p1_name, p1_health=p1_health, p1_moves=p1_moves, p2_name=p2_name, p2=player2, p2_health=p2_health, p2_moves=p2_moves, p1Fight=p1_fight, p2Fight=p2_fight)
        
        if request.form.get('player') == 'p1' or request.form.get('player') == 'p2':
            while player1["health"] > 0 or player2["health"] > 0:
                if request.form.get('player') == 'p2':
                    if p2_fight != False:
                        choice = request.form.get('choice')
                        attacker, opponent, check = WEBfightround_attack(player2, player1, choice)
                        print(opponent['name'], opponent['health'],"\n",attacker['name'],attacker['health'])
                        p1_health = player1["health"]
                        p2_health = player2["health"]
                        if p1_health <= 0:
                            whoesturn = "start_fight"
                            quote = f"{p1_name} has died"
                            break
                        else:
                            whoesturn = "player1"
                            quote = f'{p2_name} used {choice}'
                        return render_template("fight.html", start_message=quote ,WHOSTURN=whoesturn, p1=player1, p1_name=p1_name, p1_health=p1_health, p1_moves=p1_moves, p2_name=p2_name, p2=player2, p2_health=p2_health, p2_moves=p2_moves)
                if request.form.get('player') == 'p1':
                    choice = request.form.get('choice')
                    attacker, opponent, check = WEBfightround_attack(player1, player2, choice)
                    print(attacker['name'], attacker['health'],"\n",opponent['name'], opponent['health'])
                    p1_health = player1["health"]
                    p2_health = player2["health"]
                    whoesturn = "player2"
                    player1["fighting"] = True
                    player2["fighting"] = True
                    if p1_health <= 0:
                        whoesturn = "start_fight"
                        quote = f"{p2_name} has died"
                        break
                    else:
                        whoesturn = "player2"
                        quote = f'{p1_name} used {choice}'
                    return render_template("fight.html", start_message=quote ,WHOSTURN=whoesturn, p1=player1, p1_name=p1_name, p1_health=p1_health, p1_moves=p1_moves, p2_name=p2_name, p2=player2, p2_health=p2_health, p2_moves=p2_moves)
                whoesturn = 'start_fight'
                quote = f'{p1_name} is first player.' 
                return render_template("fight.html", start_message=quote,  WHOSTURN=whoesturn, p1=player1, p1_name=p1_name, p1_health=p1_health, p1_moves=p1_moves, p2_name=p2_name, p2=player2, p2_health=p2_health, p2_moves=p2_moves)    
    whoesturn = 'start_fight'
    quote = f'Game Over' 
    return render_template("fight.html", start_message=quote,  WHOSTURN=whoesturn, p1=player1, p1_name=p1_name, p1_health=p1_health, p1_moves=p1_moves, p2_name=p2_name, p2=player2, p2_health=p2_health, p2_moves=p2_moves)