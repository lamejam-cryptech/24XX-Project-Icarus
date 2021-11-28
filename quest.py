import random

import jsonengine.main as eng

class Quest:

    place = ['castle','hold','city','town','village','camp']
    residence = ['road','street','avenue','alley','path','circle','square']
    place_desc = ['high','remote','exposed','small','broken','diverse','rough','dark','shadowy','contested','grim','wild','fertile','blocked','ancient','perilous','hidden','occupied','rich','big','savage','defended','withered','mystical','inaccessible','protected','abandoned','wide','foul','dead','ruined','barren','cold','blighted','low','beautiful','abundant','lush','flooded','empty','strange','corrupted','peaceful','forgotten','expansive','settled','dense','civilized','desolate','isolated']
    place_goal = ['outsiders-rejected','dangerous-discovery','dreadful-omens','natural-disaster','old-wounds-reopened','important-object-is-lost','someone-is-captured','mysterious-phenomenon','revolt-against-a-leader','vengeful-outcast','rival-settlement','nature-strikes-back','someone-is-missing','production-halts','mysterious-murders','debt-comes-due','unjust-leadership','disastrous-accident','in-league-with-the-enemy','raiders-prey-on-the-weak','cursed-past','an-innocent-is-accused','corrupted-by-dark-magic','isolated-by-brutal-weather','provisions-are-scarce','sickness-run-amok','allies-become-enemies','attack-is-imminent','lost-caravan','dark-secret-revealed','urgent-expedition','a-leader-falls','families-in-conflict','incompetent-leadership','reckles-warmongering','beast-on-the-hunt','betrayed-from-within','broken-truce','wrathful-haunt','conflict-with-firstborn','trade-route-blocked','in-the-crossfire','stranger-causes-discord','important-event-threatened','dangerous-tradition']

    goal_action = ['scheme','clash','weaken','initiate','create','swear','avenge','guard','defeat','control','break','risk','surrender','inspect','raid','evade','assault','deflect','threaten','attack','leave','preserve','manipulate','remove','eliminate','withdraw','abandon','investigate','hold','focus','uncover','breach','aid','uphold','falter','suppress','hunt','share','destroy','avoid','reject','demand','explore','bolster','seize','mourn','reveal','gather','defy','transform','persevere','serve','begin','move','coordinate','resist','await','impress','take','oppose','capture','overwhelm','challenge','acquire','protect','finish','strengthen','restore','advance','command','refuse','find','deliver','hide','fortify','betray','secure','arrive','affect','change','defend','debate','support','follow','construct','locate','endure','release','lose','reduce','escalate','distract','journey','escort','learn','communicate','depart','search','charge','summon']
    goal_theme = ['risk','ability','price','ally','battle','safety','survival','weapon','wound','shelter','leader','fear','time','duty','secret','innocence','renown','direction','death','honor','labor','solution','tool','balance','love','barrier','creation','decay','trade','bond','hope','superstition','peace','deception','history','world','vow','protection','nature','opinion','burden','vengeance','opportunity','faction','danger','corruption','freedom','debt','hate','possession','stranger','passage','land','creature','disease','advantage','blood','language','rumor','weakness','greed','family','resource','structure','dream','community','war','portent','prize','destiny','momentum','power','memory','ruin','mysticism','rival','problem','idea','revenge','health','fellowship','enemy','religion','spirit','fame','desolation','strength','knowledge','truth','quest','pride','loss','law','path','warning','relationship','wealth','home','strategy','supply']

    char_role = ['criminal','healer','bandit','guide','performer','miner','mercenary','outcast','vagrant','forester','traveler','mystic','priest','sailor','pilgrim','thief','adventurer','forager','leader','guard','artisan','scout','herder','fisher','warrior','hunter','raider','trader','farmer','unusual-role']
    char_goal = ['obtain-an-object','make-an-agreement','build-a-relationship','undermine-a-relationship','seek-a-truth','pay-a-debt','refute-a-falsehood','harm-a-rival','cure-an-ill','find-a-person','find-a-home','seize-power','restore-a-relationship','create-an-item','travel-to-a-place','secure-provisions','rebel-against-power','collect-a-debt','protect-a-secret','spread-faith','enrich-themselves','protect-a-person','protect-the-status-quo','advance-status','defend-a-place','avenge-a-wrong','fulfill-a-duty','gain-knowledge','prove-worthiness','find-redemption','escape-from-something','resolve-a-dispute']

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
        self.generate_quest()
        self.generate_detail()

    def to_db(self, db = ''):
        eng.create({},db)
        eng.patch(self.location,db)
        eng.patch(self.quest,db)
        eng.patch(self.detail,db)

    def from_db(self, db = ''):
        self.id = eng.retrieve_k('location',db)
        self.appearance = eng.retrieve_k('quest',db)
        self.detail = eng.retrieve_k('detail',db)

    def generate_place(self):
        direction = ['north','northeast','east','southeast','south','southwest','west','northwest',]
        
        place_desc = ['high','remote','exposed','broken','diverse','rough','dark','shadowy','contested','grim','wild','fertile','blocked','ancient','perilous','hidden','occupied','rich','big','savage','defended','withered','mystical','inaccessible','protected','abandoned','wide','foul','dead','ruined','barren','cold','blighted','low','beautiful','abundant','lush','flooded','empty','strange','corrupted','peaceful','forgotten','expansive','settled','dense','civilized','desolate','isolated']
        place = ['castle','hold','city','town','village','camp']
        residence = ['road','street','avenue','alley','path','circle','square']
        place_goal = ['outsiders-rejected','dangerous-discovery','dreadful-omens','natural-disaster','old-wounds-reopened','important-object-is-lost','someone-is-captured','mysterious-phenomenon','revolt-against-a-leader','vengeful-outcast','rival-settlement','nature-strikes-back','someone-is-missing','production-halts','mysterious-murders','debt-comes-due','unjust-leadership','disastrous-accident','in-league-with-the-enemy','raiders-prey-on-the-weak','cursed-past','an-innocent-is-accused','corrupted-by-dark-magic','isolated-by-brutal-weather','provisions-are-scarce','sickness-run-amok','allies-become-enemies','attack-is-imminent','lost-caravan','dark-secret-revealed','urgent-expedition','a-leader-falls','families-in-conflict','incompetent-leadership','reckles-warmongering','beast-on-the-hunt','betrayed-from-within','broken-truce','wrathful-haunt','conflict-with-firstborn','trade-route-blocked','in-the-crossfire','stranger-causes-discord','important-event-threatened','dangerous-tradition']

        self.quest['direction'] = random.choice(direction)
        self.quest['world'] = random.choice(['nors','blk','his','stp','svt'])
        self.quest['place_size'] = random.choice(['small','medium','large'])
        self.quest['place_desc'] = random.choice(self.place_desc)
        self.quest['place'] = random.choice(self.place)

    def generate_quest(self):
        self.quest['quest_size'] = random.choice(['small','medium','large'])
        self.quest['quest_goal'] = random.choice(self.place_goal)
        # self.quest['small_event'] = random.choice(self.goal_action)
        # self.quest['small_goal'] = random.choice(self.goal_theme)
        # self.quest['npc'] = random.choice(self.char_role)
        # self.quest['npc_goal'] = random.choice(self.char_goal)
        
        if self.quest['quest_size'] == 'small':
            for i in range(random.randint(1,3)):
                self.quest['stage ' + str(i)] = '---------'
                self.quest['stage action ' + str(i)] = random.choice(self.goal_action)
                self.quest['stage goal ' + str(i)] = random.choice(self.goal_theme)

        elif self.quest['quest_size'] == 'medium':
            for i in range(random.randint(3,5)):
                self.quest['stage ' + str(i)] = '---------'
                self.quest['stage action ' + str(i)] = random.choice(self.goal_action)
                self.quest['stage goal ' + str(i)] = random.choice(self.goal_theme)

        elif self.quest['quest_size'] == 'large':
            for i in range(random.randint(5,9)):
                self.quest['stage ' + str(i)] = '---------'
                self.quest['stage action ' + str(i)] = random.choice(self.goal_action)
                self.quest['stage goal ' + str(i)] = random.choice(self.goal_theme)

    def generate_detail(self):
        self.detail['favorbility'] = random.choice(['focus','favors','disfavors'])
        self.detail['target'] = random.choice(['thread','pc','npc'])
        self.detail['emotion'] = random.choice(['anger','sadness','fear','calm','happiness','courage'])

s = Quest()
s.to_db('quest')
eng.displayfull('quest')