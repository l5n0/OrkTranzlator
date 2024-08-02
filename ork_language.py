import re

# Dictionary for Ork language translations
ork_language = {
    'hello': 'ello',
    'yes': 'ya',
    'no': 'nah',
    'good': 'gud',
    'bad': 'bad',
    'fight': 'foight',
    'war': 'waaagh',
    'big': 'big',
    'small': 'snikkit',
    'enemy': 'enemee',
    'friend': 'boy',
    'friends': 'boyz',
    'boys': 'boyz',
    'run': 'leggit',
    'fast': 'zoggin quick',
    'strong': 'stompy',
    'kill': 'krump',
    'dead': 'ded',
    'leader': 'boss',
    'stupid': 'stoopid',
    'smart': 'kunin',
    'crazy': 'mad',
    'attack': 'attak',
    'defend': 'defendz',
    'victory': 'viktory',
    'defeat': 'defeet',
    'win': 'winz',
    'lose': 'looz',
    'me': 'me',
    'you': 'ya',
    'we': 'we',
    'they': 'dey',
    'is': 'iz',
    'are': 'are',
    'the': 'da',
    'a': 'a',
    'an': 'an',
    'to': 'ta',
    'of': 'ov',
    'and': 'an',
    'in': 'in',
    'on': 'on',
    'for': 'fer',
    'with': 'wiv',
    'by': 'by',
    'from': 'frum',
    'as': 'az',
    'at': 'at',
    'about': 'abowt',
    'if': 'if',
    'it': 'it',
    'this': 'dis',
    'that': 'dat',
    'there': 'dere',
    'here': 'here',
    'out': 'owt',
    'up': 'up',
    'down': 'down',
    'left': 'left',
    'right': 'rite',
    'back': 'bak',
    'front': 'frunt',
    'go': 'go',
    'come': 'kum',
    'take': 'tak',
    'make': 'mak',
    'get': 'get',
    'give': 'giv',
    'see': 'see',
    'look': 'look',
    'know': 'no',
    'think': 'fink',
    'say': 'say',
    'speak': 'spik',
    'hear': 'heer',
    'listen': 'lissen',
    'do': 'do',
    'try': 'try',
    'use': 'yoos',
    'need': 'need',
    'want': 'want',
    'like': 'like',
    'love': 'luv',
    'hate': 'hate',
    'fear': 'feer',
    'hope': 'hope',
    'believe': 'beleeve',
    'remember': 'remember',
    'forget': 'forget',
    'live': 'liv',
    'die': 'die',
    'move': 'moov',
    'stop': 'stop',
    'start': 'start',
    'end': 'end',
    'open': 'open',
    'close': 'kloze',
    'light': 'lite',
    'dark': 'dark',
    'day': 'day',
    'night': 'nite',
    'morning': 'mornin',
    'afternoon': 'aftanoon',
    'evening': 'evenin',
    'food': 'grub',
    'drink': 'drank',
    'water': 'wat',
    'fire': 'fiyah',
    'earth': 'urf',
    'wind': 'wind',
    'sky': 'sky',
    'star': 'star',
    'sun': 'sun',
    'moon': 'moon',
    'time': 'time',
    'world': 'wurl',
    'life': 'life',
    'death': 'deth',
    'friend': 'frend',
    'enemy': 'eneme',
    'boy': 'boy',
    'girl': 'girl',
    'man': 'man',
    'woman': 'womun',
    'child': 'kid',
    'beast': 'beest',
    'monster': 'monsta',
    'machine': 'mek',
    'weapon': 'wepon',
    'gun': 'shoota',
    'blade': 'choppa',
    'shield': 'shild',
    'armor': 'armur',
    'clothes': 'cloze',
    'shoe': 'boot',
    'hand': 'hand',
    'foot': 'foot',
    'head': 'hed',
    'body': 'boddy',
    'eye': 'eye',
    'ear': 'ear',
    'mouth': 'mouf',
    'nose': 'noze',
    'hair': 'hair',
    'skin': 'skin',
    'bone': 'bone',
    'blood': 'blud',
    'heart': 'hart',
    'mind': 'mind',
    'soul': 'soul',
    'spirit': 'spirit',
    'thing': 'fing',
    'stuff': 'stuff',
    'ork': 'ork',
    'orks': 'orks',
    'boyz': 'boyz',
    'waaagh': 'waaagh',
    'dinner': 'dinna'
}

# List of exceptions
exceptions = {
    'friend': 'boy',
    'friends': 'boyz',
    'boys': 'boyz',
}

def translate_to_ork(text):
    # Define the replacement rules
    replacements = [
        (r'th', 'd'),  # th -> d
        (r'v', 'w'),   # v -> w
        (r'ph', 'f'),  # ph -> f
        (r'f', 'v'),   # f -> v
        (r's', 'z'),   # s -> z
        (r'c(?!h)', 'k'),  # c -> k, but not ch
    ]

    # Split text into words
    words = text.split()

    # Apply exceptions first
    translated_words = [exceptions.get(word.lower(), word) for word in words]

    # Replace words using the ork_language dictionary
    translated_words = [ork_language.get(word.lower(), word) for word in translated_words]

    # Join the translated words into a single string
    translated_text = ' '.join(translated_words)

    # Apply replacements
    for pattern, repl in replacements:
        translated_text = re.sub(pattern, repl, translated_text)

    # Additional grammar simplifications
    translated_text = re.sub(r'\bis\b', 'iz', translated_text)
    translated_text = re.sub(r'\bare\b', 'are', translated_text)
    translated_text = re.sub(r'\bthe\b', 'da', translated_text)

    return translated_text

# Example usage
if __name__ == '__main__':
    example_text = "Hello friends"
    print(translate_to_ork(example_text))
