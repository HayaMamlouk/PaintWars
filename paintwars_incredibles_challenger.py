# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Kaan DISLI
#  Prénom Nom: Haya MAMLOUK
import random
import math

translation = 1 
rotation = 0


def get_team_name():
    return "[ incredibles ]" # à compléter (comme vous voulez)

def eviter_robot_right(sensors):
    global translation, rotation
    translation = 1 * sensors["sensor_front"]["distance_to_robot"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1.1) * sensors["sensor_front_right"]["distance_to_robot"] * (random.uniform(0.5, 1.5))
    return translation, rotation

def eviter_robot_left(sensors):
    global translation, rotation
    translation = 1 * sensors["sensor_front"]["distance_to_robot"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1.1) * sensors["sensor_front_right"]["distance_to_robot"] * (-(random.uniform(0.5, 1.5)))
    return translation, rotation

def eviter_murs_right(sensors):
    global translation, rotation
    translation = 1 * sensors["sensor_front"]["distance_to_wall"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1.1) * sensors["sensor_front_right"]["distance_to_wall"] * (random.uniform(0.5, 1.5))
    return translation, rotation

def eviter_murs_left(sensors):
    global translation, rotation
    translation = 1 * sensors["sensor_front"]["distance_to_wall"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1.1) * sensors["sensor_front_right"]["distance_to_wall"] * (-(random.uniform(0.5, 1.5)))
    return translation, rotation

def aller_front_ennemi(sensors):
    global translation, rotation
    translation = 1 * sensors["sensor_front"]["distance_to_robot"]
    rotation = (1) * sensors["sensor_front_left"]["distance_to_robot"] + (-1.1) * sensors["sensor_front_right"]["distance_to_robot"]
    return translation, rotation	
    
def aller_back_ennemi(sensors):
    global translation, rotation
    translation = -1 * sensors["sensor_back"]["distance_to_robot"]
    rotation = (1) * sensors["sensor_back_left"]["distance_to_robot"] + (-1.1) * sensors["sensor_front_right"]["distance_to_robot"]
    return translation, rotation

def explore_1(sensors):
    """
    explore the arena
    Brainteberg condition for evaluation verified
    évite les murs ET évite les robots
    """
    global translation, rotation
    is_robot_front = sensors["sensor_front"]["distance_to_robot"] < 1 or sensors["sensor_front_left"]["distance_to_robot"] < 1 or sensors["sensor_front_right"]["distance_to_robot"] < 1
    is_wall = sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1

    if is_wall:
        return eviter_murs_left(sensors)
    if is_robot_front: 
        return eviter_robot_left(sensors)
    return translation, rotation

def explore_2(sensors):
    """
    explore the arena
    Brainteberg condition for evaluation verified
    évite les murs ET évite les robots
    """
    global translation, rotation
    is_robot_front = sensors["sensor_front"]["distance_to_robot"] < 1 or sensors["sensor_front_left"]["distance_to_robot"] < 1 or sensors["sensor_front_right"]["distance_to_robot"] < 1
    is_wall = sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1

   
    if is_wall :
        return eviter_murs_right(sensors)
    if is_robot_front: 
        return eviter_robot_right(sensors)
    return translation, rotation

def follow_enemy_front(sensors):
    global translation, rotation
    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        translation = 1
        rotation = 0 
 
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False:
        translation = 1
        rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"] * (-(random.uniform(0.5, 1.5)))
            
    elif sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False:
        translation = 1
        rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"] * (random.uniform(0.5, 1.5))
    else:
        translation = explore_1(sensors)[0]
        rotation = explore_1(sensors)[1]

    return translation, rotation

def follow_enemy_back(sensors):
    global translation, rotation
    if sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
        translation = -1
        rotation = 0
            
    elif sensors["sensor_back_left"]["isRobot"] == True and sensors["sensor_back_left"]["isSameTeam"] == False:
        translation = -1
        rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"] * (-(random.uniform(0.5, 1.5)))
            
    elif sensors["sensor_back_right"]["isRobot"] == True and sensors["sensor_back_right"]["isSameTeam"] == False:
        translation = -1
        rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"] * (random.uniform(0.5, 1.5))
    else:
        translation = explore_1(sensors)[0]
        rotation = explore_1(sensors)[1]

    return translation, rotation

def follow_enemy(sensors):
    """
    FOLLOWS THE ENEMY (subsomption)
    """
    global translation, rotation
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
        return eviter_murs_right(sensors)

    elif is_teammate :
        return eviter_robot_left(sensors)
    
    return translation, rotation

def explore_maze_left(sensors):
    """
    permet de rentrer dans des couloirs et des labyrinthes en tournant a gauche
    """
    global translation, rotation
    translation = follow_enemy(sensors)[0]
    rotation = follow_enemy(sensors)[1]
    
    if sensors["sensor_front_left"]["distance"] == 1 and sensors["sensor_left"]["distance"] < 1: 
        translation = 1
        rotation = -0.3
        return translation, rotation
      
    return translation, rotation
    
def explore_maze_right(sensors):
    """
    permet de rentrer dans des couloirs et des labyrinthes en tournant a droite
    """
    global translation, rotation
    translation = follow_enemy(sensors)[0]
    rotation = follow_enemy(sensors)[1]
    
    if sensors["sensor_front_right"]["distance"] == 1 and sensors["sensor_right"]["distance"] < 1:
        translation = 1
        rotation = 0.3
        return translation, rotation
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
    global translation, rotation
    sensors = get_extended_sensors(sensors)
    # default values
    translation = 1 
    rotation = 0
    
  
    if robotId == 1:
        translation = explore_maze_left(sensors)[0]
        rotation = explore_maze_left(sensors)[1]
    elif robotId == 5 :
        translation = explore_maze_right(sensors)[0]
        rotation = explore_maze_right(sensors)[1]
    else :
        translation = follow_enemy(sensors)[0]
        rotation = follow_enemy(sensors)[1]

    return translation, rotation
