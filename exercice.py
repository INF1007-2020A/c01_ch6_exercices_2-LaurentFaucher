#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    dictionaire = {}
    for i in some_list:
        dictionaire[i] = some_list.index(i)

    return dictionaire


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex

    result = [((color, cnames[color])) for color in colors]

    result = []
    for color in colors:
        result.append((color, cnames[color]))

    return result


def odd_integer_for_loop(end: int) -> list:
    odd_list = []
    #for i in range(1, end, 2):
        #odd_list.append(i)

    for i in range(1, end):
        if i % 2 != 0:
            odd_list.append(i)

    return odd_list


def odd_integer_list_comprehension(end: int) -> list:
    #return [n for n in range(1, end, 2)]
    return [i for i in range(1, end) if i % 2 != 0]


def loop_traversal(integers: list) -> None:
    for j in range(len(integers)):
        index = j
        element = integers[j]

    return index, element

def word_dict_for_loop(words) -> dict:
    dico = {}
    for i in words:
        dico[i.capitalize()[0]] = i

    return dico


def word_dict_comprehension(words) -> dict:
    return {i.capitalize()[0] : i for i in words}


def dictionary_traversal(words: dict) -> None:
    return {i.capitalize()[0]: i for i in sorted(words)}

def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_for_loop(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")

    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")
    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initialisation", "ajout", "modification", "suppression", "dictionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")

    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")
    loop_traversal(words_comprehension)


if __name__ == '__main__':
    main()
