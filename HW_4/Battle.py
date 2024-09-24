import csv
import log

class Battle:     
    @staticmethod
    def fight(army_1, army_2, is_loging_enabled = False):
        len_a1, len_a2 = len(army_1.members), len(army_2.members)
        ind_1, ind_2 = 0, 0
        while ind_1 < len_a1 and ind_2 < len_a2:
            logger = None
            if is_loging_enabled:
                name_dir = f'{army_1.name}_{army_2.name}'
                file = open(f'{name_dir}/{army_1.members[ind_1].get_class()}_{army_2.members[ind_2].get_class()}_fight_{ind_1+ind_2+1}.csv', 'w', newline = '')
                logger = csv.DictWriter(file, ['Round', 'Type_1', 'Health_1', 'Damage_1', 'Defense/Vampirism_1','Type_2', 'Health_2', 'Damage_2', 'Defense/Vampirism_2'])
                logger.writeheader()
            if fight(army_1.members[ind_1], army_2.members[ind_2], logger):
                ind_2 += 1
            else:
                ind_1 += 1
            if is_loging_enabled: file.close()
        return ind_2 >= len_a2

def fight(figther_1, figther_2, logger = None):
    round = 0
    striker, victim = figther_1, figther_2
    log.log_round(logger, figther_1, figther_2, round)
    while striker.is_alive():
        striker.deal_damage(victim) 
        striker, victim = victim, striker
        round += 1
        log.log_round(logger, figther_1, figther_2, round) 
    return  figther_1.health > figther_2.health 