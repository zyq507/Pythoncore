#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import os
from os.path import split, join

def getProjectPath():
    """retourne le chemin absolu du projet quel que soit l'emplacement de départ"""
    util_path = os.path.realpath(__file__)
    src_path, _ = split(util_path)
    project_path, _ = split(src_path)
    return project_path

def getTestRessourcePath(ressource_name):
    """Les fichier utilisés par les tests sont stockés dans un dossier ressource à la maven,
    cette fonction permet d'avoir un accès facile à ces fichiers"""
    return join(join(getProjectPath(), "tests_ressources"), ressource_name)
