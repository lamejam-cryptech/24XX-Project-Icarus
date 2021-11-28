import random

import jsonengine.main as eng

from character import Character

class _24q:
    def __init__(self):
        self.place = {
            'hyp_place': {
                '24xx_hyper_lofi_future': '--------------------'
            }
        }

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.place,db)

    def from_db(self, key = '', db = ''):
        self.rules = eng.retrieve_k(key,db)

    def generate_place(self, db = None):

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

        tcc_people = [
            'shadow budget government agency',
            'directed automated corporation',
            'brainbox hivemind collective',

        ]

        ibs_people = [
            
        ]

        ibs_places = [
            'mega apartment 330-b27',
            'the black swan, docked in low orbit',
            'compound of the church of the hive mind',
            'dockyards shipping containers',
            'earth high command zenith base',
            'fountain in kobayashi park',
            'gambling den run by the martian syndicate',
            'kwok tower (200 floors)',
            'little roswell "family" restaurant',
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
            'food court',
            'ramen stalls',
            'food stalls',
            'main entrance',
            'jorik tables',
            'lavatory and back exits',
            'showboards',
            'holo_screens',
            'elevator hall',
            'the bar',
            'balcony',
            'the kitchen',
            'equipment lockers',
            'storage room',
            'the stage',
            'back booths',
            'proshot tables',
            'info_terminals',
        ]

        rooms_desc = {
            'ramen shop': {
                'services': {'food'},
                'items': {'ramen': 1},
            },
            'main entrance': {
                'services': {'information'},
            },
        }

        hyp_place = {}
        hyp_place['detail'] = random.choice(detail)
        hyp_place['emotion'] = random.choice(emotion)
        hyp_place['people'] = random.choice(people)

        hyp_place['place'] = random.choice(ibs_places)

        hyp_place['rooms'] = []

        for i in range(random.randint(1,3)):
            room = {}
            room['room'] = random.choice(rooms)
            room['services'] = []
            room['items'] = {}

            def add_items(choice, num):
                if choice in room['items']:
                    room['items'][choice] += num
                else:
                    room['items'][choice] = num

            for key in rooms_desc:
                if room['room'] == key:
                    if 'services' in rooms_desc[key]:
                        for service in rooms_desc[key]['services']:
                            print(service)
                            room['services'].append(service)

                    if 'items' in rooms_desc[key]:
                        for item in list(rooms_desc[key]['items'].keys()):
                            add_items(item, rooms_desc[key]['items'][item])

            hyp_place['rooms'].append(room)

        self.place['hyp_place'] = hyp_place

q = _24q()
q.generate_place()
q.to_db('24p')
eng.displayfull('24p')