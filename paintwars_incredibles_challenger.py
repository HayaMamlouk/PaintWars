# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Kaan DISLI
#  Prénom Nom: Haya MAMLOUk

def get_team_name():
    return "[ team with no name ]" # à compléter (comme vous voulez)

def aller_tout_droit(sensors):
    translation = 1 * sensors["sensor_front"]["distance"] 
    rotation = (0) * sensors["sensor_front_left"]["distance"] + (0) * sensors["sensor_front_right"]["distance"]
    return translation, rotation
    
def eviter_les_murs(sensors):
    translation = 1 * sensors["sensor_front"]["distance_to_wall"] 
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"]
    return translation, rotation
    
def explore(sensors):
    """
    explore the arena
    Brainteberg condition for evaluation verified
    évite les murs ET évite les robots
    """
    translation = 1 * sensors["sensor_front"]["distance"]
    rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]
    return translation, rotation

def follow_enemy(sensors):
    """
    follows  the closest enemy detected front and back
    Architecture de subsomption verified
    foncer vers robot ET eviter mur
    """
    if sensors["sensor_front"]["distance_to_robot"]!=1 or sensors["sensor_front_left"]["distance_to_robot"]!=1 or sensors["sensor_front_right"]["distance_to_robot"]!=1 :
        if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
            translation = aller_vers_robot(sensors)[0]
            rotation = aller_vers_robot(sensors)[1]
    else:
        if sensors["sensor_front"]["distance_to_wall"]!=1 or sensors["sensor_front_left"]["distance_to_wall"]!=1 or sensors["sensor_front_right"]["distance_to_wall"]!=1 :
            translation = eviter_les_murs(sensors)[0]
            rotation = eviter_les_murs(sensors)[1]
        else :
            translation = explore(sensors)[0]
            rotation = explore(sensors)[1]

def step(robotId, sensors):

    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        rotation = 0.5  # rotation vers la droite
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.5  # rotation vers la gauche

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)

    return translation, rotation
