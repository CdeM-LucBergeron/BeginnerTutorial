"""
Petit programme qui montre certaines bases dans le langage Python.
Par: Luc Bergeron
Groupe: 406, 407
"""
import random


"""
Le mot clé "import" sert à importer des fonctionnalités qui se trouvent dans un module.
Dans l'exemple ci-haut, le module "random" contient une panoplie de fonctions qui sert à
générer des nombres aléatoires.
"""
"""
Le module "math" contient des fonctions en lien avec les opérations mathématiques autres
que des simples opérations (+, -, *, /, %, etc.). Il contient aussi des constantes telles que PI.
Si l'on ne veut pas importer tout ce que le module contient, il faut le spécifier avec la commande from.
"""
from math import pi

print(f"PI = {pi}")


# Les variables en python
numero_dossier = 12322  # Variable de type int
quantite_argent = 123.54  # Variable de type float
# Une variable de type string est entourée de "" ou de ''
nom_client = "Luc"  # Variable de type str
nom_client2 = 'Antoine'
play_game = True  # Variable de type booléen. Deux valeurs possibles: True ou False


"""
Comment faire pour demander de l'information à l'usager? Par exemple, si vous 
affichez un menu et que vous voulez que l'usager fasse un choix.
Python à une fonction qui se nomme "input". Cette fonction peut recevoir un paramètre
ou pas.
Voici la syntaxe de la fonction:
input(prompt)
Le paramètre 'prompt' doit être de type "string". C'est le message qui sera affiché
avant de faire la saisie. Il est optionel.
À noter que la fonction input retourne une valeur. Celle-ci est TOUJOURS de type string.
Dans l'exemple ci-bas, la variable "nom_usager" va contenir ce que l'usager à tapé au clavier.
"""

nom_usager = input("Quel est ton nom?")
print("Quel est ton nom?")
nom_usager2 = input()

"""
La conversion de type. Python est un language dynamique et le type
peut changer à chaque assignation.
numero_dossier = 111 <- le type est int
Si l'on fait l'assignation suivante:
numero_dossier = "test" <- Python change le type de la variable en str!
Nous allons nous intéresser à 3 types de conversion.
int()
str()
float()
Dans l'exemple ci-bas, la réponse de l'usager sera de type str par défaut.
Mais qu'arrive-t-il si l'on veut demander à l'usager d'entrer un chiffre
et que la variable qui reçoit la réponse soit de type str?
On utilise la fonction de conversion de type pour forcer python à changer
le type.
"""
age_usager = int(input("Quel est ton âge?"))

# On peut d'ailleurs vérifier le type d'une variable à l'aide de la fonction
# type()
print(f"Le type de la variable \"age_usager\" est {type(age_usager)}")
print(f"Le type de la variable \"nom_usager\" est {type(nom_usager)}")


"""
Comment afficher le contenu d'une variable à l'aide de la fonction print?
Suffit de mettre la lettre 'f' (en minuscule) devant le paramètre de la fonction 
print. Ensuite, dans le paramètre, il suffit de mettre le nom de la variable entre {}.
C'est ce que l'on appel les f-string.
https://he-arc.github.io/livre-python/fstrings/index.html
"""
print(f"La réponse de l'usager est {nom_usager}")
print(f"Le client {nom_client} détient {quantite_argent}$")


"""
Les if sont des branchements conditionnels. Ils permettent de valider la valeur d'une
variable et ensuite effectuer un branchement selon le test fait.
Un if est toujours évalué en terme de True ou False.
On combine souvent un if avec un else. Ainsi, si la condition du if est False,
on fait un branchement dans le else.
On peut aussi combiner un if avec un elif (else if). Cette façon de faire permet de
tester plusieurs conditions une après l'autre.

Voici la liste des conditions possibles:
if numero_dossier < 100: Strictement inférieur à
if numero_dossier > 100: Strictement supérieur à
if numero_dossier <= 100: Inférieur ou égal à
if numero_dossier >= 100: Supérieur ou égal à
if numero_dossier == 100: Égal à
if numero_dossier != 100: Pas égal à
"""


# Un seul if...
if numero_dossier == 12322:  # Pour tester si c'est égal
    print("C'est le bon numéro")

# Un if avec un else
if quantite_argent > 100:
    print("Vous avez beaucoup d'argent")
else:
    print("Travaillez plus!")

# Un if avec un elif et un else...
if nom_client == "Luc":
    print("Allo cher professeur!")
elif nom_client == "Antoine":
    print("Bonjour cher collègue!")
else:
    # Le branchement qui se fait ici est seulement fait si le nom_client
    # n'est pas "Luc" ou "Antoine".
    print("Bonjour!")

"""
Comment tester plus d'une condition à la fois dans le même if? Il faut utiliser des opérateurs 
logiques.
Si X And Y -> les deux doivent être True pour faire le branchement.
Si X Or Y -> une des deux doit être True pour faire le branchement.
On peut aussi utiliser l'opérateur not:
    if nom_client not "Luc":
ou
    if not play_game:
Notez ici que l'on ne fait jamais un "if play_game == False". Il faut utiliser 
l'opérateur not.
"""

if nom_client == "Luc" and quantite_argent == 200.00:
    print(f"{nom_client} est riche!")

if not play_game:
    print("not playing")
else:
    print("playing")

"""
Les boucles while.
Elles permettent d'exécuter un bloc d'instruction tant et aussi longtemps que la
condition est True. On peut utiliser deux mots clés dans une boucle: break et continue.
'break' permet de sortir immédiatement de la boucle et continuer l'exécution
du code qui se trouve juste en bas de la boucle.
'continue' permet de sauter le reste des instructions de la boucle et
aller re-tester la condition.
"""


compteur = 0
while compteur < 100:  # compteur <= 100 c'est la condition évaluée
    if compteur == 50:
        compteur += 10
        continue
    print(f"Je compte et je suis rendu à {compteur}")
    compteur += 1
    if compteur == 99:
        break


"""
Les boucles for! Cette boucle est à favoriser si vous savez d'avance
le nombre de fois que vous devez répéter une boucle. Pour ce type de boucle,
vous devez utiliser la fonction range(). La syntaxe de la fonction range est
la suivante:
range(debut, fin, saut)
debut: on commence à compter à partir de quel nombre
fin: on arrête de compter à quel nombre
saut: on fait des bonds de combien?
Donc:
range(0, 10, 2) -> on compte en faisant des bonds de 2
range(0, 10, 5) -> on compte en faisant des bonds de 5
Notez que le "range" commence à zéro.
Dans le premier cas, on compte de 0 à 9 en bond de 2.
On peut aussi seulement spécifier un seul paramètre.
Dans ce cas, range commence à 0 et va jusqu'à fin-1.
"""
for i in range(10):
    print(f"Je compte et je suis rendu à {i}")

for i in range(0, 10, 2):
    print(f"Je compte en faisant des bonds de 2  = {i}")


"""
Les boucles for sont la meilleure façon de parcourir une chaîne de caractères ou une
liste. C'est la meilleure façon puisque Python va connaître la grosseur de la liste ou de la chaîne
de caractères par "magie" et il va stopper la boucle automatique à la fin de la liste ou de la chaîne de caractères.
La syntaxe sera alors :
    for x in liste:
"""
membres_groupe = ["Lars", "James", "Kirk", "Robert"]
for membre in membres_groupe:
    print(f"{membre}")

nom_groupe = "Metallica"
for ch in nom_groupe:
    print(f"{ch}")

"""
Les fonctions.
Une fonction est utile pour éviter de reproduire du code. En effet, si vous avez à
deux ou plus d'endroits différents le même code qui fait la même chose,
c'est un indice que vous devez écrire une fonction. De plus, les fonctions permettent
de mieux organiser son code. Encore mieux, les fonctions permettent également de mieux
débogguer son code et elles permettent également d'avoir un code plus
facile à modifier et faire évoluer.
"""


player_hp = 20


def is_player_alive(player_health):
    """
    Petite fonction qui permet de valider si le joueur est vivant ou pas.
    :param player_health: Le nombre de point de vie.
    :return: True si vivant et False si mort.
    """
    return player_health > 0


if is_player_alive(player_hp):
    print("Alive")
else:
    print("Dead")


def player_potion_use(potion_heal_amount):
    """
    Simple fonction qui permet au joueur de boire une potion de vie.
    :param potion_heal_amount: La quantité de point de vie que la potion contient.
    :return: None
    """
    # Afin de modifier une variable globale dans une fonction, il est
    # important de faire la déclaration ci-bas avant
    # la modification. Ceci permet à l'interpréteur de savoir que la variable "player_hp" a été déclaré
    # au niveau global et non dans la fonction.
    global player_hp
    player_hp += potion_heal_amount


print(f"Le joueur à {player_hp} de point de vie.")
player_potion_use(10)
print(f"Le joueur à maintenant {player_hp} de point de vie.")


def die_roll(die_formula):
    """
    Simulates a die roll.
    Can receive a string containing the die size and quantity of dice to roll:
        - 2d6 will roll two 1d6 and add both.
        - 1d6 will only roll a die...
        - 3d12 would roll 3 12 sided dice and add the roll.
    :param die_formula: How many dice of x side to roll
    :return: the dice sum
    """
    import re

    chiffres = re.split("d", die_formula.lower(), maxsplit=1)
    total = 0
    for nb in range(int(chiffres[0])):
        total += random.randint(1, int(chiffres[1]))
    return total


print(f"La force du joueur est de (1d6) = {die_roll("1d6")}")
print(f"La force du joueur est de (2d6) = {die_roll("2d6")}")
print(f"La force du joueur est de (10d4) = {die_roll("10d4")}")
