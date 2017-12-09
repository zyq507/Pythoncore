#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import os
from os.path import split, join

def getProjectPath():
    """retourne le chemin absolu du projet quel que soit l'emplacement de d�part"""
    util_path = os.path.realpath(__file__)
    src_path, _ = split(util_path)
    project_path, _ = split(src_path)
    return project_path

def getTestRessourcePath(ressource_name):
    """Les fichier utilis�s par les tests sont stock�s dans un dossier ressource � la maven,
    cette fonction permet d'avoir un acc�s facile � ces fichiers"""
    return join(join(getProjectPath(), "tests_ressources"), ressource_name)
