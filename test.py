
from character import Character
from place import Place
from quest import Quest
from _2400IBS_char import IBS_Char
from _19xx_char import TCC_Char
from _24c import _24c

import jsonengine.main as eng

character1 = Character(gender='m')
character2 = Character(gender='f')
character3 = Character(gender='m')

place = Place()
quest = Quest()

character1.to_db('char1')
character2.to_db('char2')
character3.to_db('char3')

quest.to_db('quest')
quest.to_db('place')


ibs_char1 = IBS_Char(gender='f')
ibs_char2 = IBS_Char(gender='f')
ibs_char3 = IBS_Char(gender='f')

tcc_char1 = TCC_Char(gender='m')

ibs_char1.to_db('char1')
ibs_char2.to_db('char2')
ibs_char3.to_db('char3')
tcc_char1.to_db('tc1')

hyp = _24c()
hyp.to_db('hyp')
eng.displayfull('hyp')





