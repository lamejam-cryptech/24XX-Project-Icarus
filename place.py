import random

import jsonengine.main as eng

class Place:

    world = ['nors','blk','his','stp','svt']
    size = ['tiny','small','medium','large','huge']
    place = ['castle','hold','city','town','village','camp']
    residence = ['road','street','avenue','alley','path','circle','square']
    place_desc = ['high','remote','exposed','small','broken','diverse','rough','dark','shadowy','contested','grim','wild','fertile','blocked','ancient','perilous','hidden','occupied','rich','big','savage','defended','withered','mystical','inaccessible','protected','abandoned','wide','foul','dead','ruined','barren','cold','blighted','low','beautiful','abundant','lush','flooded','empty','strange','corrupted','peaceful','forgotten','expansive','settled','dense','civilized','desolate','isolated']
    
    place_goal = ['outsiders-rejected','dangerous-discovery','dreadful-omens','natural-disaster','old-wounds-reopened','important-object-is-lost','someone-is-captured','mysterious-phenomenon','revolt-against-a-leader','vengeful-outcast','rival-settlement','nature-strikes-back','someone-is-missing','production-halts','mysterious-murders','debt-comes-due','unjust-leadership','disastrous-accident','in-league-with-the-enemy','raiders-prey-on-the-weak','cursed-past','an-innocent-is-accused','corrupted-by-dark-magic','isolated-by-brutal-weather','provisions-are-scarce','sickness-run-amok','allies-become-enemies','attack-is-imminent','lost-caravan','dark-secret-revealed','urgent-expedition','a-leader-falls','families-in-conflict','incompetent-leadership','reckles-warmongering','beast-on-the-hunt','betrayed-from-within','broken-truce','wrathful-haunt','conflict-with-firstborn','trade-route-blocked','in-the-crossfire','stranger-causes-discord','important-event-threatened','dangerous-tradition']

    location = {
        'direction': '',
        'world': '',
        'quest_location': '---------',
        'place_size': '',
        'place_desc': '',
        'place': '',
    }

    quest = {
        'quest': '---------',
        'quest_size': '',
        'quest_goal': '',

        # 'small_event': '',
        # 'small_goal': '',
        # 'npc': '',
        # 'npc_goal': '',
    }

    detail = {
        'detail': '---------',
        'favorbility': '',
        'target': '',
        'emotion': '',
    }

    def __init__(self):
        self.generate_place()

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.location,db)

    def from_db(self, db = ''):
        self.id = eng.retrieve_k('location',db)

    def generate_place(self):
        direction = ['north','northeast','east','southeast','south','southwest','west','northwest',]
        
        place_desc = ['high','remote','exposed','broken','diverse','rough','dark','shadowy','contested','grim','wild','fertile','blocked','ancient','perilous','hidden','occupied','rich','big','savage','defended','withered','mystical','inaccessible','protected','abandoned','wide','foul','dead','ruined','barren','cold','blighted','low','beautiful','abundant','lush','flooded','empty','strange','corrupted','peaceful','forgotten','expansive','settled','dense','civilized','desolate','isolated']
        place = ['castle','hold','city','town','village','camp']
        
        self.quest['direction'] = random.choice(direction)
        self.quest['world'] = random.choice(self.world)
        self.quest['place_size'] = random.choice(self.size)
        self.quest['place_desc'] = random.choice(self.place_desc)
        self.quest['place'] = random.choice(self.place)
