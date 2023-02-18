import random
def get_quantity():
    quantity =int(input("What quantity? "))
    return quantity

def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    determiner = random.choice(determiners)
    return determiner

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_tense():
    tense=input("What tense would you like? (past, present, future)")
    return tense

def get_verb(quantity,tense):
    verbs=[]
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == "present" and quantity > 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
    elif tense == "present" and quantity == 1:
        verbs=["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    verb = random.choice(verbs)
    return verb

def get_preposition():
    prepositions=[ "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition 

def get_prepositional_phrase(quantity):
    noun=get_noun(quantity)
    determiner=get_determiner(quantity)
    preposition=get_preposition()
    prepositional_phrase=f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def main():
    quantity= get_quantity()
    tense=  get_tense()
    determiner=get_determiner(quantity)
    noun=get_noun(quantity)
    verb=get_verb(quantity, tense)
    prepositional_phrase=get_prepositional_phrase(quantity)
    print(f'{determiner} {noun} {verb} {prepositional_phrase}.'.capitalize())

print(f"__name__ is {__name__}")
# if this file is being run via cmd prompt (i.e. terminal)
if __name__ == "__main__":
    main()
