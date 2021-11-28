import random

import jsonengine.main as eng

from character import Character

class _24r:
    def __init__(self, gender=None):
        self.rules = {
            'hyp_rules': {
                '24xx_hyper_lofi_future': '--------------------'
            }
        }

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.rules,db)

    def from_db(self, key = '', db = ''):
        self.rules = eng.retrieve_k(key,db)

    def generate_rules(self, db = None):
        self.rules['hyp_rules']['d2'] = random.randint(1,2)
        self.rules['hyp_rules']['d4'] = random.randint(1,4)
        self.rules['hyp_rules']['d6'] = random.randint(1,6)
        self.rules['hyp_rules']['d8'] = random.randint(1,8)
        self.rules['hyp_rules']['d10'] = random.randint(1,10)
        self.rules['hyp_rules']['d12'] = random.randint(1,12)
        self.rules['hyp_rules']['d20'] = random.randint(1,20)

        

        tactic = ['push','hold','maneuver']

        vof_s = ['-','-','S','S','S','X']
        vof_d = ['S','S','S','X','X','X']
        vof_f = ['2S','X','X','X','X','2X']

        vof_response = ['fight','flight','shock']

        hype_tactic = {}

        d3 = random.randint(1,3)
        if d3 == 1:
            hype_tactic['tactic'] = tactic[0]
        elif d3 == 2:
            hype_tactic['tactic'] = tactic[1]
        else:
            hype_tactic['tactic'] = tactic[2]
        
        vof = random.randint(0,5)
        hype_tactic['vof_n'] = vof
        hype_tactic['vof_s'] = vof_s[vof]
        hype_tactic['vof_d'] = vof_d[vof]
        hype_tactic['vof_f'] = vof_f[vof]

        response = random.randint(0,2)
        hype_tactic['response'] = vof_response[response]

        self.rules['hyp_rules']['tactic'] = hype_tactic

        eng.create({},db)
        eng.patch(self.rules,db)

r = _24r()
r.generate_rules()
r.to_db('24r')
eng.displayfull('24r')


        
        