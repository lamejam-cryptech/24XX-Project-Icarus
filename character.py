import random

import jsonengine.main as eng

class Character:
    personality_pos = ['confident','brave','laid_back','kind','bright','cheerful','energetic','charismatic','flirty','creative','humble','pragmatic','wise','determined']
    personality_neg = ['shy','anxious','reserved','grumpy','selfish','ditzy','sad','sleepy','awkward','prudish','simple','smug','prissy','brash','lazy']

    def __init__(self, gender=None):
        self.id = {
            'gender': '',
            'name': '',
        }

        self.clothing = {
            'clothing':'---------',
            'hat': ''
            'necklace'
            'ring'
            'innerwear'
            'outerwear'
            'legwear'
            'shoes'
        }

        self.attributes = {
            'atr': '---------',
            'hth': 0,
            'str': 0,
            'dex': 0,
            'agl': 0,
            'int': 0,
            'cha': 0,
        }

        self.generate_id(gender)
        self.generate_attribute()

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.id,db)
        eng.patch(self.attributes,db)

    def from_db(self, db = ''):
        self.id = eng.retrieve_k('id',db)
        self.attributes = eng.retrieve_k('attributes',db)

    def generate_id(self, gender):
        if gender == None:
            self.id['gender'] = random.choice(['m','f'])
        self.id['personality'] = random.choice(self.personality_pos + self.personality_neg)

    def generate_attribute(self):
        # self.attributes['hth'] = random.choice([1,2,3,4,5,6,7,8,9,10])
        # self.attributes['str'] = random.choice([1,2,3,4,5,6,7,8,9,10])
        # self.attributes['dex'] = random.choice([1,2,3,4,5,6,7,8,9,10])
        # self.attributes['agl'] = random.choice([1,2,3,4,5,6,7,8,9,10])
        # self.attributes['int'] = random.choice([1,2,3,4,5,6,7,8,9,10])
        # self.attributes['cha'] = random.choice([1,2,3,4,5,6,7,8,9,10])
        # 1,2,3,4,5 ,6 ,7 ,8 ,9 ,10
        # 2,4,6,8,10,12,20,40,80,100
        # self.attributes['hth'] = random.choice([3,4,5,6,7,8])
        # self.attributes['str'] = random.choice([3,4,5,6,7,8])
        # self.attributes['dex'] = random.choice([3,4,5,6,7,8])
        # self.attributes['agl'] = random.choice([3,4,5,6,7,8])
        # self.attributes['int'] = random.choice([3,4,5,6,7,8])
        # self.attributes['cha'] = random.choice([3,4,5,6,7,8])
        # nxtub-tocci scale
        # d2,d4,d6,d8,d10,d12,d20,d100
        # -2,-1,00,01,002,003,004,0005
        self.attributes['hth'] = random.choice([0,1,2,3,4])
        self.attributes['str'] = random.choice([0,1,2,3,4])
        self.attributes['dex'] = random.choice([0,1,2,3,4])
        self.attributes['agl'] = random.choice([0,1,2,3,4])
        self.attributes['int'] = random.choice([0,1,2,3,4])
        self.attributes['cha'] = random.choice([0,1,2,3,4])
        