import duolingo

SPANISH_ENDINGS = ['ar','er','ir']
LANGUAGE_LIST= ['Spanish','French','German', 'Italian']


class Duo:
    '''
    TODO: updates coming
    right now the tooling I am doing is closely aligned with spanish as it is the only language I have been learning
    I will soon example this to past , present , future, and irregular verbs but for now I just am trying to do the basics.
    once I do that I will start adding different languages
    '''
    def __init__(self, username, password):
        self.duo = duolingo.Duolingo(username,password)

    def get_learned_verbs(self, language):
        '''
        :param language: string from the Language LIST
        :return: a dictionary of verbs and all the conjugations the person has learned so far
        '''
        abbr = self.duo.get_abbreviation_of(language)
        word_list = self.duo.get_vocabulary(language_abbr=abbr)
        verb_dict = {}
        for word in word_list['vocab_overview']:
             if word['pos'] == 'Verb':
                 infinitive = word['infinitive']
                 if word['normalized_string'][-2:] not in SPANISH_ENDINGS:
                     if infinitive not in verb_dict:
                         verb_dict[infinitive] = [word['normalized_string']]
                     else:
                         verb_dict[infinitive].append(word['normalized_string'])
        return verb_dict
