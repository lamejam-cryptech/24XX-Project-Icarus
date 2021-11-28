import random

import jsonengine.main as eng

from character import Character

class _24r:
    def __init__(self, gender=None):
        self.scars = {
            'hyp_scars': {
                '24xx_hyper_lofi_future': '--------------------'
            }
        }

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.scars,db)

    def from_db(self, key = '', db = ''):
        self.scars = eng.retrieve_k(key,db)

    def generate_scars(self, db = None):
        harm = [
            'rolled with it - no die increase!',
            'cut scratched or bruised',
            'overextended (hinder next action)',
            'momentarily deaf, blind, or stunned',
            'tripped, knocked back, or pinned down',
            'moderately injured (broken bones, concussion)',
            'Disfigured',
            'Severely injured (crushed limb or vital organs)',
            'Critically injured (permanent damage/loss) ',
            'Unconscious until roused by someone',
            'Mortally wounded - will die soon without aid',
            'Killed instantly',
        ]

        fear = [
            'focused - don’t increase die size',
            'chills run down your spine',
            'startled (hinders next action)',
            'jumpy, hindered if you stop to think/observe',
            'dread fills you with doubt',
            'uncontrollable vomiting or dry heaves',
            'hyperventilate',
            'uncontrollable screaming / crying',
            'fear hinders when facing source of stress',
            'pass out until roused by someone',
            'catatonic, unresponsive until treatment',
            'cardiac Arrest',
        ]

        hyp_scars = {}
        hyp_scars['harm'] = random.choice(harm)
        hyp_scars['fear'] = random.choice(fear)

        self.scars['hyp_scars'] = hyp_scars

        eng.create({},db)
        eng.patch(self.scars,db)

r = _24r()
r.generate_scars()
r.to_db('24scars')
eng.displayfull('24scars')


        
        