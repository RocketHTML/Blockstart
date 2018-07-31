import os
from shell_tools import *

def get_filenames(folder):
    return os.listdir(folder)

def clean_folder(folder):
    sh(["rm", '-r', folder])
    sh(['mkdir', folder])

def move_file(filename, folder):
    sh(['mv', filename, folder])

def move_folder(folder, new_folder):
    filenames = [folder + l for l in get_filenames(folder)]
    contents = ['mv'] + filenames + [new_folder]
    sh(contents)

def zipper(zipname, folder):
    sh(['bash', 'zipper', zipname, folder])

def unzipper(zipname, folder_to_visit):
    sh(['bash', 'unzipper', zipname, folder_to_visit])
