class Posterior:

    def __init__(self, string):
        
        self.initial = str(string)
        # TODO: handle if it's not a string. maybe str()?

        self.spokenizer = Spokenizer(Posterior.initial)

        # TODO: rename these three finders to what teammates name their find-highest-variable functions.
        self.master_domain = Domainizer.find_master()
        self.master_emotion = Emotionizer.find_master()
        self.master_sentiment = Sentimentizer.find_master()

        self.predicted_behavior = Behaviorizer(Posterior.master_domain, Posterior.master_emotion, Posterior.master_sentiment)


class Behaviorizer:

    def __init__(self, domain, emotion, sentiment):

        self.behavior_dict = self.import_json()
        self.peram_tuple = (domain, emotion, sentiment)
        self.predicted_behavior = self.find_prediction(str(self.peram_tuple))

        print("this sentence is {0}, {1}, and {2}, so the speaker probably is: {3}".format(self.peram_tuple[0], self.peram_tuple[1], self.peram_tuple[2], self.predicted_behavior))

    def import_json(self):
        '''
        this function imports and parses our lexicon of pre-written behavior predictions.

        arguments: none

        '''
        import json
        from pprint import pprint
        # loads json of potential behaviors (I think).
        with open('Behavior_List.json') as data_file:
            behaviors = json.load(data_file)
            return behaviors['Behaviors']
            # pprint(behaviors)

    def find_prediction(self, master):
        '''
        this function receives a stringified tuple with three items in it,
        finds a match within a dictionary of pre-defined behavior predictions,
        and returns the string value for the matching key.

        arguments: one tuple with three items in it.
        Each item is the string name of the highest-rated value for each of the three Posterior analyzation categories:
        In order: domain, emotion, sentiment.
        example: ('financial', 'sad', 'negative')

        '''
        for key, value in self.behavior_dict.items():
            if master == key:
                return value

        
        # ALTERNATE OPTION although it returns a list.
        # return [value for key, value  in self.behavior_dict.items() if master == key]
        