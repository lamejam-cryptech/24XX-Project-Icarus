import random

import jsonengine.main as eng

from character import Character

class TCC_Char:
    def __init__(self, gender=None):
        self.base_char = Character(gender)

        self.character = {
            'tcc_character': {
                '19xx_20th_century_cyberpunk': '--------------------'
            }
        }
        self.generate_character()

    def to_db(self, db = ''):
        self.base_char.to_db(db)
        eng.patch(self.character,db)

    def from_db(self, key = '', db = ''):
        self.character = eng.retrieve_k(key,db)

    def generate_character(self):

        origin = ['upper_class','middle_class','lower_class','under_class']

        roles = ['decker','operator','agent','runner']

        former_profession = ['chef','gambler','salaryman','laborer']

        roles_desc = {
            'decker': {
                'skills': {'hacking': 1,'electronics': 1},
                'varied_skills': {'hacking': 3,'electronics': 3},
                'carry': ['cyber_deck'],
            },
            'operator': {
                'skills': {'drones': 1,'jury_rigging': 1},
                'side_arm': ['mini_quadruped_drone'],
                'aug_head': ['drone_vision_control_implant'],
            },
            'agent': {
                'skills': {'intimidation': 1,'firearms': 1},
                'carry': ['turret_case'],
                'aug_arm': ['turret_arm_implant'],
            },
            'runner': {
                'skills': {'athletics': 1,'perception': 1},
                'carry': ['hoverbike'],
                'side_arm': ['launchpad']
            },
            'chef': {
                'skills': {'cooking': 1},
            },
            'gambler': {
                'skills': {'gambling': 1},
            },
            'salaryman': {
                'skills': {'paperwork': 1},
            },
            'laborer': {
                'skills': {'labor': 1},
            },
        }

        tcc_id = {
            'origin': '',
            'role': '',
            'former_profession': '',
            'code_name': '',
            'money': 0,
            'rep': 0,
        }

        skills = ['climbing','connections','deception','hacking','electronics','explosives','forgery','hand_to_hand','intimidation','labor','machinery','persuasion','piloting','reading_people','running','shooting','sleight_of_hand','spacewalking','stealth','tracking']
        
        tcc_skills = {
        }

        tcc_clothing = {
            'head': [],
            'clothing': [],
            'adornment': [],
            'wearable_gear': [],
        }

        tcc_augs = {
            'aug_head': [],
            'aug_arms': [],
            'aug_body': [],
            'aug_legs': [],
        }

        tcc_items = {
            'carry': [],
            'side_arm': [],
            'pack': {},
        }

        tcc_id['origin'] = random.choice(origin)
        tcc_id['role']  = random.choice(roles)
        tcc_id['former_profession'] = random.choice(former_profession)

        def add_skills(choice, num):
            if choice in tcc_skills:
                tcc_skills[choice] += num
            else:
                tcc_skills[choice] = num

        def add_skills_varied(choice, num):
            if choice in tcc_skills:
                tcc_skills[choice] += random.randint(1,num)
            else:
                tcc_skills[choice] = random.randint(1,num)

        def add_items(choice, num):
            if choice in tcc_items['pack']:
                tcc_items[choice] += num
            else:
                tcc_items[choice] = num

        for key in roles_desc:
            if tcc_id['role'] == key:
                if 'skills' in roles_desc[key]:
                    for skill in list(roles_desc[key]['skills'].keys()):
                        add_skills(skill, roles_desc[key]['skills'][skill])

                if 'varied_skills' in roles_desc[key]:
                    for skill in roles_desc[key]['varied_skills']:
                        add_skills_varied(skill, roles_desc[key]['varied_skills'][skill])
                
                if 'carry' in roles_desc[key]:
                    for carry in roles_desc[key]['carry']:
                        tcc_items['carry'].append(carry)

                if 'side_arm' in roles_desc[key]:
                    for side_arm in roles_desc[key]['side_arm']:
                        tcc_items['side_arm'].append(side_arm)

                if 'item' in roles_desc[key]:
                    for item in list(roles_desc[key]['items'].keys()):
                        add_items(item, roles_desc[key]['items'][item])

                if 'head' in roles_desc[key]:
                    for head in roles_desc[key]['head']:
                        tcc_clothing['head'].append(head)
                
                if 'clothing' in roles_desc[key]:
                    for clothing in roles_desc[key]['clothing']:
                        tcc_clothing['clothing'].append(clothing)

                if 'adornment' in roles_desc[key]:
                    for adornment in roles_desc[key]['adornment']:
                        tcc_clothing['adornment'].append(adornment)

                if 'wearable_gear' in roles_desc[key]:
                    for wearable_gear in roles_desc[key]['wearable_gear']:
                        tcc_clothing['wearable_gear'].append(wearable_gear)

                if 'aug_head' in roles_desc[key]:
                    for aug_head in roles_desc[key]['aug_head']:
                        tcc_augs['aug_head'].append(aug_head)
                
                if 'aug_arms' in roles_desc[key]:
                    for aug_arms in roles_desc[key]['aug_arms']:
                        tcc_augs['aug_arms'].append(aug_arms)

                if 'aug_body' in roles_desc[key]:
                    for aug_body in roles_desc[key]['aug_body']:
                        tcc_augs['aug_body'].append(aug_body)

                if 'aug_legs' in roles_desc[key]:
                    for aug_legs in roles_desc[key]['aug_legs']:
                        tcc_augs['aug_legs'].append(aug_legs)

        for key in roles_desc:
            if tcc_id['former_profession'] == key:
                if 'skills' in roles_desc[key]:
                    for skill in list(roles_desc[key]['skills'].keys()):
                        add_skills(skill, roles_desc[key]['skills'][skill])
                
        code_names = [
            'Archer',
            'Bliss',
            'Caver',
            'Drift',
            'Echo',
            'Faze',
            'Glass',
            'Hawk',
            'Inky',
            'Jinx',
            'Kit',
            'Limit',
            'Make',
            'Nic',
            'Orc',
            'Piece',
            'Ripper',
            'Slide',
            'Watts',
            'Zero',
        ]

        head = [
            'trucker hat',
            'baseball hat',
            'scarf',
            'nogs',
            'glasses',
        ]

        style = [
            'blood red',
            'bright white',
            'budget',
            'brand name',
            'burned',
            'coppery',
            'electric blue',
            'faded',
            'gilded',
            'glow in the dark',
            'hot pink',
            'hypercolor',
            'iridescent',
            'jet black',
            'pastel',
            'rainbow',
            'reflective',
            'royal purple',
            'sparkly',
            'translucent',
        ]

        default_outfits = [
            'belts & chains',
            'bomber jacket',
            'coverall',
            'duster',
            'flannel & jeans',
            'flight suit',
            'high-collar suit',
            'hoodie & slacks',
            'jumpsuit',
            'military fatigues',
            'biker wear',
            'robes',
            'speedsuit',
            'suit & tie',
            't-shirt & jeans',
            'tank top & cargos',
            'tape & sweats',
            'track suit',
            'trench coat',
            'vest & pants',
        ]

        adornments = [
            '3D glasses',
            'barcode tattoo',
            'blacklight tattoo',
            'bright eyes',
            'cat eye pupils',
            'chain tattoos',
            'chrome teeth',
            'facial piercings',
            'flame tattoo',
            'geometric tattoo',
            'glitching tattoo',
            'hologram tattoo',
            'koi tattoo',
            'mirror shades',
            'traditional tattoo',
            'neon tattoo',
            'occult tattoo',
            'ritual scarring',
            'skull tattoo',
            'snake tattoo',
        ]

        tcc_id['code_name'] = random.choice(code_names)
        d1 = random.randint(0,1)
        for i in range(d1):
            tcc_clothing['head'].append(random.choice(head))
        tcc_clothing['clothing'].append(random.choice(style) + ' ' + random.choice(default_outfits))
        d3 = random.randint(0,3)
        for i in range(d3):
            tcc_clothing['adornment'].append(random.choice(adornments))

        self.character['tcc_character']['tcc_id'] = tcc_id
        self.character['tcc_character']['tcc_skills'] = tcc_skills
        self.character['tcc_character']['tcc_clothing'] = tcc_clothing
        self.character['tcc_character']['tcc_augs'] = tcc_augs
        self.character['tcc_character']['tcc_items'] = tcc_items
        