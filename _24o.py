import random

import jsonengine.main as eng

from character import Character

class _24r:
    def __init__(self, race=None, gender=None):
        self.planner = {
            'hyp_planner': {
                '24xx_hyper_lofi_future': '--------------------'
            }
        }

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.planner,db)

    def from_db(self, key = '', db = ''):
        self.planner = eng.retrieve_k(key,db)

    def generate_planner(self, db = None):

        # relax = [
        #     'day off',
        #     'visit the doctor',
        #     'visit by family',
        #     'visit by friends',
        #     'goes on date',
        # ]

        # campaign = random.randint(1,6)

        # if campaign != 6:
        #     hyp_relax = {}
        #     hyp_relax['relax'] = random.choice(relax)
        #     self.planner['hyp_planner'] = hyp_relax
        #     eng.create({},db)
        #     eng.patch(self.planner,db)
        #     return
        
        objectives = [
            'rescue VIP',
            'deliver the package',
            'retrieve the prototype',
            'secure the evidence',
            'escort the VIP',
            'kidnap the target',
            'scout the area',
            'plant the bomb',
            'upload the virus',
            'kill the target',
        ]

        hostiles_faction = [
            'syndicate gangsters',
            'corporate goons',
            'insurgent fighters',
            'state military',
            'state police',
        ]

        hostiles_type = [
            'isolate soldiers',
            'squad w/ technical',
            'sniper team',
            'squad w/ observer',
            'drone team',
            'armored vehicle',
            'squad w/ armored vehicle',
            'spec ops fireteam',
            'armored tracked vehicle',
            'squad w/ armored tracked vehicle'
        ]

        strength = ['-2_2easy','-1_4average','0_6average','1_8journeyman','2_10veteran','3_12master','4_20peak_human','5_super_human']

        hyp_planner = {}
        hyp_planner['objective'] = random.choice(objectives)
        hyp_planner['hostiles_faction'] = random.choice(hostiles_faction)
        hyp_planner['hostiles_type'] = random.choice(hostiles_type)
        hyp_planner['enemy_strength'] = random.choice(strength)
        hyp_planner['agl'] = random.randint(-2,4)
        hyp_planner['reward'] = random.randint(1,3)

        self.planner['hyp_planner'] = hyp_planner

        eng.create({},db)
        eng.patch(self.planner,db)

r = _24r()
r.generate_planner()
r.to_db('test')
eng.displayfull('test')


        
        