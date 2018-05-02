# Build a game representation from ascii art defined by user.
import itertools

class AsciiMapException(Exception):
    pass

class ObjectInfoException(Exception):
    pass

def build_game(ascii_art, objs_info):
    """
    Create the game object from ascii art and objects_information by
    creating difference layers, and pass it to the initilizer.

    Args:
        ascii_art (list of strings)
            The art for the game, must be in rectangle
            (meaning that the lenth of inside list shoud be the same)
            where, the empty string means nothing and the labeled characters
            are representing the object in game.

        objects_information (dictionary)
            We map the characters to prefab object, so that we can easily
            define their colors or behavior.

    Return:
        game (Game object) - Game object created by game class.

    Raises:
        ValueError - When the map is not a rectangle.
        AttributeError - object information isn't contain some
            characters from ascii_art.

    Example:
        Ascii Art

        ['########'
        ,'#      #'
        ,'#      #'
        ,'#   P  #'
        ,'#      #'
        ,'#      #'
        ,'#      #'
        ,'########']

        Object information
        {'P': Player(), '#': Wall()}

    """

    # Testing for the property of the map

    if not all(len(r) == len(ascii_art[0]) for r in ascii_art):
        raise AsciiMapException("The map is not consistent.")

    if ascii_art == []:
        raise AsciiMapException("The map is empty.")

    if not bool(objs_info):
        raise ObjectInfoException("The object information is empty.")

    # Get all the objects
    all_obs = list(set(itertools.chain.from_iterable(ascii_art)))
    all_obs = [o for o in all_obs if not o == ' ']

    if len(all_obs) < len(objs_info.keys()):
        raise ObjectInfoException("Some of the objects are not in the map.")

    if not all(o in objs_info for o in all_obs):
        raise ObjectInfoException("There is no information for the object.")
