# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Kaan DISLI
#  Prénom Nom: Haya MAMLOUK
import random
import math

def get_team_name():
    return "[ incredibles ]" # à compléter (comme vous voulez)

def eviter_robot(sensors):
    translation = 1 * sensors["sensor_front"]["distance_to_robot"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"]
    return translation, rotation

def eviter_les_murs(sensors):
    translation = 1 * sensors["sensor_front"]["distance_to_wall"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"]
    return translation, rotation

def aller_front_ennemi(sensors):
    translation = 1 * sensors["sensor_front"]["distance_to_robot"]
    rotation = (1) * sensors["sensor_front_left"]["distance_to_robot"] + (-1) * sensors["sensor_front_right"]["distance_to_robot"]
    return translation, rotation	
    
def aller_back_ennemi(sensors):
    translation = -1 * sensors["sensor_back"]["distance_to_robot"]
    rotation = (1) * sensors["sensor_back_left"]["distance_to_robot"] + (-1) * sensors["sensor_back_right"]["distance_to_robot"]
    return translation, rotation

def aleatoire(sensors):
    param=[1, 1, 1, 0, 1, 0, 0, -1] # I used randomsearch.py to find the values of bestParam 

    translation = math.tanh (param[0] + param[1] * sensors["sensor_front_left"]["distance"] + param[2] * sensors["sensor_front"]["distance"] +param[3] * sensors["sensor_front_right"]["distance"] )
    rotation = math.tanh (param[4] + param[5] * sensors["sensor_front_left"]["distance"] + param[6] * sensors["sensor_front"]["distance"] + param[7] * sensors["sensor_front_right"]["distance"] )
    is_robot_front = sensors["sensor_front"]["distance_to_robot"] < 1 or sensors["sensor_front_left"]["distance_to_robot"] < 1 or sensors["sensor_front_right"]["distance_to_robot"] < 1
    is_wall = sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1

    if is_wall:
        return eviter_les_murs(sensors)
    if is_robot_front: 
        return eviter_robot(sensors)
    return translation, rotation

def explore(sensors):
    """
    explore the arena
    Brainteberg condition for evaluation verified
    évite les murs ET évite les robots
    """
    is_robot_front = sensors["sensor_front"]["distance_to_robot"] < 1 or sensors["sensor_front_left"]["distance_to_robot"] < 1 or sensors["sensor_front_right"]["distance_to_robot"] < 1
    is_wall = sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1

    # Default values
    translation = 1 * sensors["sensor_front"]["distance"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    if is_wall:
        return eviter_les_murs(sensors)
    if is_robot_front: 
        return eviter_robot(sensors)
    return translation, rotation

def follow_enemy_front(sensors):
    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        translation = 1
        rotation = 0 
 
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False:
        translation = 1
        rotation = -0.5  # rotation vers la gauche
            
    elif sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False:
        translation = 1
        rotation = 0.5  # rotation vers la droite
    else:
        translation = explore(sensors)[0]
        rotation = explore(sensors)[1]

    return translation, rotation

def follow_enemy_back(sensors):
    if sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
        translation = -1
        rotation = 0
            
    elif sensors["sensor_back_left"]["isRobot"] == True and sensors["sensor_back_left"]["isSameTeam"] == False:
        translation = -1
        rotation = -0.5  # rotation vers la gauche
            
    elif sensors["sensor_back_right"]["isRobot"] == True and sensors["sensor_back_right"]["isSameTeam"] == False:
        translation = -1
        rotation = 0.5  # rotation vers la droite
    else:
        translation = explore(sensors)[0]
        rotation = explore(sensors)[1]

    return translation, rotation

def follow_enemy(sensors):
    """
    FOLLOWS THE ENEMY (subsomption)
    """
    # default values
    translation = 1 * sensors["sensor_front"]["distance"]
    rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

    is_robot_front = sensors["sensor_front"]["distance_to_robot"] < 1 or sensors["sensor_front_left"]["distance_to_robot"] < 1 or sensors["sensor_front_right"]["distance_to_robot"] < 1
    is_robot_back = sensors["sensor_back"]["distance_to_robot"] < 1 or sensors["sensor_back_left"]["distance_to_robot"] < 1 or sensors["sensor_back_right"]["distance_to_robot"] < 1
    is_same_team = sensors["sensor_front"]["isSameTeam"] or sensors["sensor_front_left"]["isSameTeam"] or sensors["sensor_front_right"]["isSameTeam"] or sensors["sensor_back"]["isSameTeam"] or sensors["sensor_back_left"]["isSameTeam"] or sensors["sensor_back_right"]["isSameTeam"]
    is_wall = sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1
    is_teammate = (sensors["sensor_front_left"]["distance_to_robot"] < 1 or sensors["sensor_front"]["distance_to_robot"] < 1 or sensors["sensor_front_right"]["distance_to_robot"] < 1) and is_same_team

   
    if is_robot_front and not is_same_team:
        return follow_enemy_front(sensors)
            
    elif is_robot_back and not is_same_team:
        return follow_enemy_back(sensors) 

    elif is_wall :
        return eviter_les_murs(sensors)

    elif is_teammate :
        return eviter_robot(sensors)
    
    return translation, rotation

def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors
    
def step(robotId, sensors):

    sensors = get_extended_sensors(sensors)
    if robotId == 0 or robotId == 7:
        translation = follow_enemy(sensors)[0]
        rotation = follow_enemy(sensors)[1]
    elif robotId == 1 or robotId == 6:
        translation = aleatoire(sensors)[0]
        rotation = aleatoire(sensors)[1]
    else:
        translation = explore(sensors)[0]
        rotation = explore(sensors)[1]

    return translation, rotation
