import csv
import os
import Army as a
import Battle as b
import Warrior as w


def logging(obj1, obj2):
    if isinstance(obj1, w.Warrior) and isinstance(obj2, w.Warrior):
        with open(f'{obj1.get_class()}_{obj2.get_class()}_fight.csv', 'w', newline = '') as file:
            writer = csv.DictWriter(file, ['Round', 'Type_1', 'Health_1', 'Damage_1', 'Defense/Vampirism_1','Type_2', 'Health_2', 'Damage_2', 'Defense/Vampirism_2'])
            writer.writeheader()     
            b.fight(obj1, obj2, writer)

    elif isinstance(obj1, a.Army) and isinstance(obj2, a.Army):
        os.makedirs(f'{obj1.name}_{obj2.name}',exist_ok = True)
        b.Battle.fight(obj1, obj2, True)

    else:
        with open('ERROR_type.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow({'An error has occurred'})

# additional function to simplify logging of 1vs1 battles
def log_round(logger, figther_1, figther_2, round):
    if logger:  
        # I thougth to use point 8, but in that case (to use headers) this variant looked like the best, in my opinion
        logger.writerow({'Round': round, 
                        'Type_1': figther_1.get_class(),
                        'Health_1': figther_1.health, 
                        'Damage_1': figther_1.attack, 
                        'Defense/Vampirism_1': figther_1.special_char_desc(False),
                        'Type_2': figther_2.get_class(), 
                        'Health_2': figther_2.health, 
                        'Damage_2': figther_2.attack, 
                        'Defense/Vampirism_2': figther_2.special_char_desc(False)})