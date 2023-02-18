from sentences import get_determiner,get_noun,get_verb,get_preposition,get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    quantity = 1
    single_determiners = ["a", "one", "the"]


    for _ in range(len(single_determiners) + 1):
        word = get_determiner(quantity)
        assert word in single_determiners

    quantity = 2
    plural_determiners = ["some", "many", "the"]


    for _ in range(len(plural_determiners) + 1):
        word = get_determiner(quantity)
        assert word in plural_determiners

def test_get_noun():
    single_noun= ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    for _ in range(len(single_noun) + 1):
        noun = get_noun(1)
        assert noun in single_noun
    
    plural_noun= ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits","women"]
    for _ in range(len(plural_noun) + 1):
        noun = get_noun(2)
        assert noun in plural_noun


def test_get_verb():
    single_verb=["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(len(single_verb) + 1):
        verb= get_verb(1,"present")
        assert verb in single_verb

    plural_verb= ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(len(plural_verb) + 1):
        verb = get_verb (2,"present")
        assert verb in plural_verb

    future_verb= ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(len(future_verb) + 1):
        verb = get_verb (1,"future")
        assert verb in future_verb

    past_verb= ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(len(past_verb) + 1):
        verb = get_verb (1,"past")
        assert verb in past_verb

def test_get_preposition():
    prepositions=[ "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(len(prepositions) + 1):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():

    prepositions=[ "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    determiners=["a", "one", "the"]  
    nouns= ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]  
    for _ in range(5):
        prepositional_phrase=get_prepositional_phrase(1)
        words = prepositional_phrase.split(' ')
        assert words[0] in prepositions
        assert words[1] in determiners
        assert words[2] in nouns

pytest.main(["-v", "--tb=line", "-rN", __file__])
