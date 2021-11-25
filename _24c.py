import random

import jsonengine.main as eng

from character import Character

class _24c:
    def __init__(self, race=None, gender=None):
        self.base_char = Character(race, gender)

        self.character = {
            'hyp_character': {
                '24xx_hyper_lofi_future': '--------------------'
            }
        }
        self.generate_character()

    def to_db(self, db = None):
        self.base_char.to_db(db)
        eng.patch(self.character,db)

    def from_db(self, key = None, db = None):
        self.character = eng.retrieve_k(key,db)

    def print_db(self, key = None, db = None):
        eng.display(db)

    def generate_character(self):

        race = ['human','android']

        origin = ['upper_class','middle_class','lower_class','under_class']

        roles = ['decker','operator','agent','runner','grifter','hacker','infiltrator','psycher','rigger','scrapper','stitcher','trigger','vidcaster'
        ,'mma fighter']

        # roles = ['mma fighter']

        former_profession = ['cook','gambler','salaryman','laborer','vidcaster','student','street_sweeper','administrator']

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
                'varied_skills': {'intimidation': 1,'firearms': 4},
                'carry': ['turret_case'],
                'aug_arms': ['turret_arm_implant'],
            },
            'runner': {
                'varied_skills': {'athletics': 3,'perception': 2},
                'carry': ['hoverbike'],
                'side_arm': ['launchpad']
            },
            'cook': {
                'skills': {'cooking': 1},
            },
            'gambler': {
                'varied_skills': {'gambling': 4},
            },
            'salaryman': {
                'varied_skills': {'paperwork': 4},
            },
            'laborer': {
                'skills': {'labor': 1},
            },
            'student': {
                'skills': {'paperwork': 1},
            },
            'street_sweeper': {
                'skills': {'labor': 1},
            },
            'administrator': {
                'skills': {'hacking': 1,'electronics': 1},
            },
            'grifter': {
                'varied_skills': {'reading_people': 1,'deception': 2},
                'items': {'extensive_disguise': 1},
            },
            'hacker': {
                'varied_skills': {'hacking': 2,'electronics': 2},
                'carry': ['bullet_proof_console'],
                'items': {'electronic_tools': 1},
            },
            'infiltrator': {
                'varied_skills': {'climbing': 2,'stealth': 2},
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
                'varied_skills': {'intimidation': 1, 'hand_to_hand': 3},
            },
            'stitcher': {
                'skills': {'medicine': 1, 'electronics': 1},
                'carry': ['cyber_surgery_kit'],
                'items': {'medkit': 2},
            },
            'trigger': {
                'varied_skills': {'shooting': 2, 'explosives': 2},
                'carry': ['rifle'],
                'side_arm': ['pistol'],
            },
            'vidcaster': {
                'skills': {'persuasion': 1, 'connections': 1},
                'wearable_gear': ['body_cam'],
            },
            'mma fighter': {
                'varied_skills': {'striking': 4, 'takedown': 4, 'grapple': 4, 'movement': 4},
            },
            'war veteran': {
                'varied_skills': {'shooting': 2, 'intimidation': 1, 'hand_to_hand': 1, 'explosives': 1},
                'carry': ['old rifle'],
            }
        }

        hyp_id = {
            'race': '',
            'origin': '',
            'role': '',
            'former_profession': '',
            'code_name': '',
            'money': 0,
            'rep': 0,
            'motivation': '',
        }

        skills = ['climbing','connections','deception','hacking','electronics','explosives','forgery','hand_to_hand','intimidation','labor','machinery','persuasion','piloting','reading_people','running','shooting','sleight_of_hand','spacewalking','stealth','tracking']
        
        hyp_skills = {
        }

        hyp_clothing = {
            'head': [],
            'clothing': [],
            'adornment': [],
            'wearable_gear': [],
        }

        hyp_augs = {
            'aug_head': [],
            'aug_arms': [],
            'aug_body': [],
            'aug_legs': [],
        }

        hyp_items = {
            'carry': [],
            'side_arm': [],
            'pack': {},
        }

        hyp_id['origin'] = random.choice(origin)
        hyp_id['race'] = random.choice(race)
        hyp_id['role']  = random.choice(roles)
        hyp_id['former_profession'] = random.choice(former_profession)

        def add_skills(choice, num):
            if choice in hyp_skills:
                hyp_skills[choice] += num
            else:
                hyp_skills[choice] = num

        def add_skills_varied(choice, num):
            number = random.randint(0,num)
            # if number > 0:
            if choice in hyp_skills:
                hyp_skills[choice] += number
            else:
                hyp_skills[choice] = number

        def add_items(choice, num):
            if choice in hyp_items['pack']:
                hyp_items['pack'][choice] += num
            else:
                hyp_items['pack'][choice] = num

        if hyp_id['race'] == 'human':
            for i in range(2):
                choice = random.choice(skills)
                add_skills(choice, 1)
            
        if hyp_id['race'] == 'android':
            d2 = random.randint(1,2)
            if d2 == 1:
                hyp_augs['aug_body'].append('synth_skin')
            else:
                hyp_augs['aug_body'].append('case_armor')

        for key in roles_desc:
            if hyp_id['role'] == key:
                if 'skills' in roles_desc[key]:
                    for skill in list(roles_desc[key]['skills'].keys()):
                        add_skills(skill, roles_desc[key]['skills'][skill])

                if 'varied_skills' in roles_desc[key]:
                    for skill in roles_desc[key]['varied_skills']:
                        add_skills_varied(skill, roles_desc[key]['varied_skills'][skill])
                
                if 'carry' in roles_desc[key]:
                    for carry in roles_desc[key]['carry']:
                        hyp_items['carry'].append(carry)

                if 'side_arm' in roles_desc[key]:
                    for side_arm in roles_desc[key]['side_arm']:
                        hyp_items['side_arm'].append(side_arm)

                if 'items' in roles_desc[key]:
                    for item in list(roles_desc[key]['items'].keys()):
                        add_items(item, roles_desc[key]['items'][item])

                if 'head' in roles_desc[key]:
                    for head in roles_desc[key]['head']:
                        hyp_clothing['head'].append(head)
                
                if 'clothing' in roles_desc[key]:
                    for clothing in roles_desc[key]['clothing']:
                        hyp_clothing['clothing'].append(clothing)

                if 'adornment' in roles_desc[key]:
                    for adornment in roles_desc[key]['adornment']:
                        hyp_clothing['adornment'].append(adornment)

                if 'wearable_gear' in roles_desc[key]:
                    for wearable_gear in roles_desc[key]['wearable_gear']:
                        hyp_clothing['wearable_gear'].append(wearable_gear)

                if 'aug_head' in roles_desc[key]:
                    for aug_head in roles_desc[key]['aug_head']:
                        hyp_augs['aug_head'].append(aug_head)
                
                if 'aug_arms' in roles_desc[key]:
                    for aug_arms in roles_desc[key]['aug_arms']:
                        hyp_augs['aug_arms'].append(aug_arms)

                if 'aug_body' in roles_desc[key]:
                    for aug_body in roles_desc[key]['aug_body']:
                        hyp_augs['aug_body'].append(aug_body)

                if 'aug_legs' in roles_desc[key]:
                    for aug_legs in roles_desc[key]['aug_legs']:
                        hyp_augs['aug_legs'].append(aug_legs)

        for key in roles_desc:
            if hyp_id['former_profession'] == key:
                if 'skills' in roles_desc[key]:
                    for skill in list(roles_desc[key]['skills'].keys()):
                        add_skills(skill, roles_desc[key]['skills'][skill])

        if hyp_id['role'] == 'psycher':
            d3 = random.randint(1,3)
            if d3 == 1:
                hyp_skills['telepathy'] = 1
                hyp_skills['telekinesis'] = 1
            elif d3 == 2:
                hyp_skills['telepathy'] = 2
            else:
                hyp_skills['telekinesis'] = 2

        if hyp_id['role'] == 'scrapper':
            d2 = random.randint(1,2)
            if d2 == 1:
                hyp_items['carry'] = 'sword'
            else:
                aug_arms = ['claws','shield','gun','super_strong','grapple']
                choice = random.choice(aug_arms)
                hyp_augs['aug_arms'].append(choice)

        if hyp_id['role'] == 'vidcaster':
            d4 = random.randint(1,4)
            if d4 == 1:
                hyp_items['carry'] = 'guitar',
            elif d4 == 2:
                hyp_items['carry'] = 'spray_paint',
            elif d4 == 3:
                hyp_items['carry'] = 'broadcast_radio',
            else:
                hyp_items['carry'] = 'speaker_phone',
                
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

        ibs_adornments = [
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

        tcc_decals = [
            'neon strips',
            'windbreaker',
            'logos/stickers',
            'corp tattoos',
            'sunglasses',
            'army boots',
            'jumpsuit',
            'military fatigues',
            'microchips',
            'wires',
        ]

        tcc_motivations = [
            'its work',
            'thrill',
            'protection',
            'blackmail',
            'debt',
            'escape',
            'greed',
            'desperation',
            'revolution',
            'professionalism',
        ]

        side_arms = [
            'pistol',
            'revolver',
            'smg',
            'pocket_pistol',
            'grapple',
            'knife',
            'homemade_explosives',
        ]

        hyp_id['code_name'] = random.choice(code_names)
        hyp_id['motivation'] = random.choice(tcc_motivations)

        d1 = random.randint(0,1)
        for i in range(d1):
            hyp_clothing['head'].append(random.choice(head))
        hyp_clothing['clothing'].append(random.choice(style) + ' ' + random.choice(default_outfits))
        d3 = random.randint(0,3)
        for i in range(d3):
            hyp_clothing['adornment'].append(random.choice(ibs_adornments))
        hyp_clothing['adornment'].append(random.choice(tcc_decals))

        hyp_items['side_arm'] = random.choice(side_arms)

        self.character['hyp_character']['hyp_id'] = hyp_id
        self.character['hyp_character']['hyp_skills'] = hyp_skills
        self.character['hyp_character']['hyp_clothing'] = hyp_clothing
        self.character['hyp_character']['hyp_augs'] = hyp_augs
        self.character['hyp_character']['hyp_items'] = hyp_items
        