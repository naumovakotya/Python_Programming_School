import Warrior as w
import Knight as k
import Defender as d
import Vampire as v
import Army as a
import Battle as b
import random
import log

# only for testing:
def fill_army(army,number_of_warriors = 10):
    classes = [w.Warrior, k.Knight, d.Defender, v.Vampire]
    list_to_add = []
    for x in range(number_of_warriors):
        list_to_add.append(classes[random.randint(0,3)]()+(random.randint(-10,10)))
    army.add_members(number_of_warriors,*list_to_add)
    

arm1, arm2 = a.Army('arm1'), a.Army('arm2')
fill_army(arm1,100)
fill_army(arm2,50)
log.logging(arm1, arm2)