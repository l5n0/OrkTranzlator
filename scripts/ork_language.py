import re
from scripts.ork_dictionary import ork_language

# List of exceptions
exceptions = {
    'friend': 'boy',
    'friends': 'boyz',
    'boys': 'boyz',
}

def translate_to_ork(text):
    # Define the replacement rules
    replacements = [
        (r'\bI am\b|\bI\'m\b|\bIm\b', 'I iz'),  # I am -> I iz, I'm -> I iz, Im -> I iz
        (r'\bWe are\b|\bWe\'re\b', 'We iz'),  # We are -> We iz
        (r'\bYou are\b|\bYou\'re\b', 'You iz'),  # You are -> You iz
        (r'\bThey are\b|\bThey\'re\b', 'Dey iz'),  # They are -> Dey iz
        (r'\bDon\'t\b|\bDidn\'t\b|\bDoesn\'t\b', 'Dunt'),  # Don't -> Dunt
        (r'\bIsn\'t\b|\bHasn\'t\b|\bHadn\'t\b', 'Ent'),  # Isn't -> Ent
        (r'\bWasn\'t\b|\bWeren\'t\b', 'Wunt'),  # Wasn't -> Wunt
        (r'\bHis\b', '\'Iz'),  # His -> 'Iz
        (r'\bHer\b|\bHers\b', '\'Er'),  # Her -> 'Er
        (r'\bTheirs\b', 'Derez'),  # Theirs -> Derez
        (r'\bOurs\b', 'Arrz'),  # Ours -> Arrz
        (r'\bYours\b', 'Yourz'),  # Yours -> Yourz
        (r'\bYour\b', 'Yer'),  # Your -> Yer
        (r'\bThinking\b', 'Finking'),  # Thinking -> Finking
        (r'\bThought\b', 'Fought'),  # Thought -> Fought
        (r'\bThree\b', 'Free'),  # Three -> Free
        (r'\bThanks\b', 'Fanks'),  # Thanks -> Fanks
        (r'\bThunder\b', 'Funda'),  # Thunder -> Funda
        (r'\bOther\b', 'Ovva'),  # Other -> Ovva
        (r'\bFather\b', 'Farva'),  # Father -> Farva
        (r'\bMother\b', 'Muvva'),  # Mother -> Muvva
        (r'\bBrother\b', 'Bruvva'),  # Brother -> Bruvva
        (r'\bBother\b', 'Bovva'),  # Bother -> Bovva
        (r'\bFeather\b', 'Fevva'),  # Feather -> Fevva
        (r'\bSomething\b', 'Sumfing'),  # Something -> Sumfing
        (r'\bNothing\b', 'Nuffing'),  # Nothing -> Nuffing
        (r'\bEverything\b', 'Everyfing'),  # Everything -> Everyfing
        (r'\bDeath\b', 'Deff'),  # Death -> Deff
        (r'\bEarth\b', 'Erf'),  # Earth -> Erf
        (r'\bHealth\b', 'Elff'),  # Health -> Elff
        (r'\bBreath\b', 'Breff'),  # Breath -> Breff
        (r'\bWealth\b', 'Welf'),  # Wealth -> Welf
        (r'\bWorth\b', 'Wurf'),  # Worth -> Wurf
        (r'\bBoth\b', 'Boaf'),  # Both -> Boaf
        (r'\bWith\b', 'Wiv'),  # With -> Wiv
        (r'ng\b', "n'"),  # words ending with ng -> n'
        (r'th', 'd'),  # th -> d
        (r'v', 'w'),   # v -> w
        (r'ph', 'f'),  # ph -> f
        (r'f', 'v'),   # f -> v
        (r's', 'z'),   # s -> z
        (r'c(?!h)', 'k'),  # c -> k, but not ch
        (r'ould', 'ud'),  # should -> shud
        (r'er\b', 'a'),  # er -> a
        (r'er', 'ah'),  # er -> ah
        (r'\bThe\b', 'Da'),  # The -> Da
    ]

    # Split text into words
    words = text.split()

    # Apply exceptions first
    translated_words = [exceptions.get(word.lower(), word) for word in words]

    # Replace words using the ork_language dictionary if not in exceptions
    translated_words = [ork_language.get(word.lower(), word) for word in translated_words]

    # Apply replacements in a case-insensitive manner
    translated_text = ' '.join(translated_words)
    for pattern, repl in replacements:
        translated_text = re.sub(pattern, repl, translated_text, flags=re.IGNORECASE)

    return translated_text

# Example usage
if __name__ == '__main__':
    example_text = "Hello friends"
    print(translate_to_ork(example_text))
