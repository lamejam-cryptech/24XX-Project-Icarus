import random

import jsonengine.main as eng

from character import Character

class _24s:
    def __init__(self, gender=None):
        self.safe = {
            'hyp_safe': {
                '24xx_hyper_lofi_future': '--------------------'
            }
        }

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.safe,db)

    def from_db(self, key = '', db = ''):
        self.rules = eng.retrieve_k(key,db)

    def generate_safe(self, db = None):

        detail = [
            'focus npc',
            'focus pc',
            'focus thread',
            'favors npc',
            'favors pc',
            'favors thread',
            'disfavors npc',
            'disfavors pc',
            'disfavors thread',
        ]

        emotion = [
            'anger',
            'sadness',
            'fear',
            'calm',
            'happiness',
            'courage',
        ]

        people = [
            'lower class civilians',
            'middle class civilians',
            'upper class civilians',
            'salarymen',
            'laborer',
            'civilian merchants',
            'arm merchants',
            'mercenary',
            'criminal',
            'military',
        ]

        places = [
            'mega apartment 330-b27',
            'the black swan, docked in low orbit',
            'compound of the church of the hive mind',
            'dockyards shipping containers',
            'earth high command zenith base',
            'fountain in kobayashi park',
            'gambling den run by the martian syndicate',
            'kwok tower (200 floors)',
            'little roswell family restaurant',
            'mag_lev railway yard',
            'main street level 12',
            'metro tunnels',
            'mirror gardens',
            'old cyber_parts plant',
            'plaza del diablo',
            'st. paul memorial hospital',
            'space elevator',
            'trailer hitched to a moving truck',
            'underground rave hosted by mas destructo',
            'warehouse row',
        ]

        rooms = [
            'ramen shop',
            'ramen stalls',
            'holo theater',
            'showboard gambling den',
            'bbq shop',
            'street food stall',
            'jorik tables',
            'upper class bar',
            'lower class bar',
            'balcony bar',
            'soup kitchen',
            'black market',
            'proshot tables',
            'info_terminals',
        ]

        rooms_desc = {
            'ramen shop': {
                'services': {'hacking': 1,'electronics': 1},
                'item': ['cyber_deck'],
            },
        }

        services = [
            
            'food',
            'drinks',
            'drinks',
            'drinks',
            'drinks',
            'weapons',
            'drugs',
            'clothing',
            'electronics',
            
            
            'medical care',
            'cyberware repair',
            'medical care',
            'cyberware repair',
            'medical care',
            'cyberware repair',
            'medical care',
            'cyberware repair',

            'hookers',
            'information',
            'games',
            'gambling',
        ]

        hyp_place = {}
        hyp_place['detail'] = random.choice(detail)
        hyp_place['emotion'] = random.choice(emotion)
        hyp_place['people'] = random.choice(people)
        hyp_place['place'] = random.choice(places)

        hyp_place['rooms'] = []
        for i in range(random.randint(1,3)):
            hyp_place['rooms'].append(random.choice(rooms))

        hyp_place['service'] = []
        for i in range(random.randint(1,5)):
            hyp_place['service'].append(random.choice(services))

        self.safe['hyp_safe'] = hyp_place

s = _24s()
s.generate_safe()
s.to_db('24s')
eng.displayfull('24s')
