import random

import jsonengine.main as eng

from character import Character

class IBS_Char:
    def __init__(self, race=None, gender=None):
        self.base_char = Character(race, gender)

        self.character = {
            'isb_character': {
                '2400_inner_system_blues': '--------------------'
            }
        }
        self.generate_character()

    def to_db(self, db = ''):
        self.base_char.to_db(db)
        eng.patch(self.character,db)

    def from_db(self, key = '', db = ''):
        self.character = eng.retrieve_k(key,db)

    def generate_character(self):

        origin = ['human','android']

        roles = ['grifter','hacker','infiltrator','psycher','rigger','scrapper','stitcher','trigger','vidcaster']
        
        roles_desc = {
            'grifter': {
                'skills': {'reading_people': 1,'deception': 1},
                'items': {'extensive_disguise': 1},
            },
            'hacker': {
                'skills': {'hacking': 1,'electronics': 1},
                'carry': ['bullet_proof_console'],
                'items': {'electronic_tools': 1},
            },
            'infiltrator': {
                'skills': {'climbing': 1,'stealth': 1},
                'wearable_gear': ['climbing_gear'],
                'head': ['nvg'],
            },
            'psycher': {
                'items': {'psych_out': 1},
            },
            'rigger': {
                'skills': {'drones': 1,'jury_rigging': 1},
                'items': {'drone': 2, 'machinery_tools': 1, 'electronic_tools': 1},
            },
            'scrapper': {
                'skills': {'intimidation': 1, 'hand_to_hand': 1},
                'items': {'drone': 2, 'machinery_tools': 1, 'electronic_tools': 1},
            },
            'stitcher': {
                'skills': {'medicine': 1, 'electronics': 1},
                'carry': ['cyber_surgery_kit'],
                'items': {'medkit': 2},
            },
            'trigger': {
                'skills': {'shooting': 1, 'explosives': 1},
                'carry': ['rifle'],
                'side_arm': ['pistol'],
            },
            'vidcaster': {
                'skills': {'persuasion': 1, 'connections': 1},
                'wearable_gear': ['body_cam'],
            },
        }

        isb_id = {
            'origin': '',
            'role': '',
            'code_name': '',
            'money': 0,
            'rep': 0,
        }

        skills = ['climbing','connections','deception','hacking','electronics','explosives','forgery','hand_to_hand','intimidation','labor','machinery','persuasion','piloting','reading_people','running','shooting','sleight_of_hand','spacewalking','stealth','tracking']
        
        isb_skills = {
        }

        isb_clothing = {
            'head': [],
            'clothing': [],
            'adornment': [],
            'wearable_gear': [],
        }

        isb_augs = {
            'aug_head': [],
            'aug_arms': [],
            'aug_body': [],
            'aug_legs': [],
        }

        isb_items = {
            'carry': [],
            'side_arm': [],
            'pack': {},
        }

        isb_id['origin'] = random.choice(origin)
        isb_id['role']  = random.choice(roles)

        def add_skills(choice, num):
            if choice in isb_skills:
                isb_skills[choice] += num
            else:
                isb_skills[choice] = num

        def add_skills_varied(choice, num):
            if choice in isb_skills:
                isb_skills[choice] += random.randint(1,num)
            else:
                isb_skills[choice] = random.randint(1,num)

        def add_items(choice, num):
            if choice in isb_items['pack']:
                isb_items[choice] += num
            else:
                isb_items[choice] = num

        if isb_id['origin'] == 'human':
            for i in range(2):
                choice = random.choice(skills)
                add_skills(choice, 1)
            
        if isb_id['origin'] == 'android':
            d2 = random.randint(1,2)
            if d2 == 1:
                isb_augs['aug_body'].append('synth_skin')
            else:
                isb_augs['aug_body'].append('case_armor')

        for key in roles_desc:
            if isb_id['role'] == key:
                if 'skills' in roles_desc[key]:
                    for skill in list(roles_desc[key]['skills'].keys()):
                        add_skills(skill, roles_desc[key]['skills'][skill])

                if 'varied_skills' in roles_desc[key]:
                    for skill in roles_desc[key]['varied_skills']:
                        add_skills_varied(skill, roles_desc[key]['varied_skills'][skill])
                
                if 'carry' in roles_desc[key]:
                    for carry in roles_desc[key]['carry']:
                        isb_items['carry'].append(carry)

                if 'side_arm' in roles_desc[key]:
                    for side_arm in roles_desc[key]['side_arm']:
                        isb_items['side_arm'].append(side_arm)

                if 'item' in roles_desc[key]:
                    for item in list(roles_desc[key]['items'].keys()):
                        add_items(item, roles_desc[key]['items'][item])

                if 'head' in roles_desc[key]:
                    for head in roles_desc[key]['head']:
                        isb_clothing['head'].append(head)
                
                if 'clothing' in roles_desc[key]:
                    for clothing in roles_desc[key]['clothing']:
                        isb_clothing['clothing'].append(clothing)

                if 'adornment' in roles_desc[key]:
                    for adornment in roles_desc[key]['adornment']:
                        isb_clothing['adornment'].append(adornment)

                if 'wearable_gear' in roles_desc[key]:
                    for wearable_gear in roles_desc[key]['wearable_gear']:
                        isb_clothing['wearable_gear'].append(wearable_gear)

                if 'aug_head' in roles_desc[key]:
                    for aug_head in roles_desc[key]['aug_head']:
                        isb_augs['aug_head'].append(aug_head)
                
                if 'aug_arms' in roles_desc[key]:
                    for aug_arms in roles_desc[key]['aug_arms']:
                        isb_augs['aug_arms'].append(aug_arms)

                if 'aug_body' in roles_desc[key]:
                    for aug_body in roles_desc[key]['aug_body']:
                        isb_augs['aug_body'].append(aug_body)

                if 'aug_legs' in roles_desc[key]:
                    for aug_legs in roles_desc[key]['aug_legs']:
                        isb_augs['aug_legs'].append(aug_legs)

        if isb_id['role'] == 'psycher':
            d3 = random.randint(1,3)
            if d3 == 1:
                isb_skills['telepathy'] = 1
                isb_skills['telekinesis'] = 1
            elif d3 == 2:
                isb_skills['telepathy'] = 2
            else:
                isb_skills['telekinesis'] = 2

        if isb_id['role'] == 'scrapper':
            d2 = random.randint(1,2)
            if d2 == 1:
                isb_items['carry'] = 'sword'
            else:
                aug_arms = ['claws','shield','gun','super_strong','grapple']
                choice = random.choice(aug_arms)
                isb_augs['aug_arms'].append(choice)

        if isb_id['role'] == 'vidcaster':
            d4 = random.randint(1,4)
            if d4 == 1:
                isb_items['carry'] = 'guitar',
            elif d4 == 2:
                isb_items['carry'] = 'spray_paint',
            elif d4 == 3:
                isb_items['carry'] = 'broadcast_radio',
            else:
                isb_items['carry'] = 'speaker_phone',

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

        isb_id['code_name'] = random.choice(code_names)
        d1 = random.randint(0,1)
        for i in range(d1):
            isb_clothing['head'].append(random.choice(head))
        isb_clothing['clothing'].append(random.choice(style) + ' ' + random.choice(default_outfits))
        d3 = random.randint(0,3)
        for i in range(d3):
            isb_clothing['adornment'].append(random.choice(adornments))

        self.character['isb_character']['isb_id'] = isb_id
        self.character['isb_character']['isb_skills'] = isb_skills
        self.character['isb_character']['isb_clothing'] = isb_clothing
        self.character['isb_character']['isb_augs'] = isb_augs
        self.character['isb_character']['isb_items'] = isb_items
        