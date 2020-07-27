import json
import os
import traceback 

pt = print

def read_json_to_dict(json_fullpath):
    """
    Read a json and return a object created from it.
    Args:
        json_fullpath: json fullpath

    Returns: json object.
    """
    try:
        with open(json_fullpath, 'r+') as outfile:
            json_readed = json.load(outfile)
        return json_readed
    except Exception as error:
        raise ValueError(error)

def object_to_json(object, attributes_to_delete=None, **kwargs):
    """
    Convert class to json with properties method.
    Args:
        object: class object
        attributes_to_delete: String set with all attributes' names to delete from properties method
        **kwargs:

    Returns:sort json from class properties.

    """
    try:
        object_dictionary = class_properties(object=object, attributes_to_delete=attributes_to_delete)
        json_string = json.dumps(object, default=lambda m: object_dictionary, sort_keys=True, indent=4)
        json_string = json.dumps(object, default=lambda m: object_dictionary)
    except Exception as e:
        pt(e)
        pt(traceback.print_exc())
        raise ValueError("STOP")
    return json_string

def class_properties(object, attributes_to_delete=None):
    """
    Return a string with actual object features without not necessaries
    :param attributes_to_delete: represent witch attributes set must be deleted.
    :return: A copy of class.__dic__ without deleted attributes
    """
    dict_copy = object.__dict__.copy()  # Need to be a copy to not get original class' attributes.
    # Remove all not necessaries values
    if attributes_to_delete:
        for x in attributes_to_delete:
            del dict_copy[x]
    return dict_copy

def write_string_to_pathfile(string, filepath):
    """
    Write a string to a path file
    :param string: string to write
    :param path: path where write
    """
    try:
        create_directory_from_fullpath(filepath)
        file = open(filepath, 'w+')
        file.write(str(string))
        return 1
    except Exception as error:
        raise ValueError(error)
         

def create_directory_from_fullpath(fullpath):
    """
    Create directory from a fullpath if it not exists.
    """
    directory = os.path.dirname(fullpath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
