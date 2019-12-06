import string
import numpy as np

# increases number by 1
def increment(x):
    return(x + 1)


def min_max_scaler(x):
    """Returns numpy array with original values scaled"""
    return (x - x.min()) / (x.max() - x.min())

# takes punctuation out of text
def strip_punctuation(text):
    """ Takes punctiation out of text """
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)

# takes punctuation out again
def bag_of_words(text):
    """ New and improved punctiation taker-outer """
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return words
