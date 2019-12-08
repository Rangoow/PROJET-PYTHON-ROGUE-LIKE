ESPARSA Noé  -  DUBOIS Thomas

Sujet : Rogue Like Game

Titre : Area 51 RPG

Instalation : nécessite python 3.7 uniquement

Lancement : Il suffit de compiler main.py qui instancie gameArchitecture qui va se charger de gérer tout le jeu.

Commande : Au cours du jeu le joueur n'a besoin que d'appuer sur les touches 1, 2 ou 3 ainsi que ENTREE.

Déroulement du jeu : Le joueur est amené à renseigner un nom ainsi que la calsse avec laquelle il souhaite jouer.
Il arrive en suite directement sur le menu principale du jeu qui lui permet de :
continuer l'aventure / voir ses caractéristiques / quitter le jeu.


Voir ses caractéristiques : Le joueur est en mesure de voir son nom, sa classe, ses HP, son XP, ses gold,
le nombre de potions dont il dispose, ses dégats, son armure, l'XP nécessiare pour monter d'un niveau.

Continuer l'aventure : Le joueur avance pendant 30 niveaux au cours desquel il peut rencontrer des ennemis
dont les stats sont calculés en fonction du niveau dans lequel se trouve le joueurs, au cours d'un comabts celui-ci peut
attaquer grace à une attaque de base ou une attaque magique consomant des MP ( il dispose de 3 attaques magiques différentes).
    1 - attaque qui fait plus de dégats
    2 - Redonne des HP
    3- réduit l'attque de l'ennemi

Il peut aussi utiliser des potions pour récupérer des HP ou des MP.

Pour finir il peut passer son tour (ça sert à rien mais bon) sans rien faire et laisser l'ennemie lui briser la nuque.

A la fin d'un combat soit le joueur est mort comme une ***** et le jeu se termine, soit le joueur triomphe et peut ainsi
gagner de l'XP, des golds et à une chance sur trois de gagner une pièce d'équipement aléatoire dont les stats sont générés
aléatoirement en fonction du niveau dans lequel se situe le joueur. Le joueur à ensuite la possibilité d'échanger
toutes les pièces de son inventaire ave celle qu'il a d'équipée.

A partir du niveau 10 le joueur à la possibilité de tomber sur un shp pour achter des potions en échange de quelques golds.
Puis à partir du niveau 15 il peut aussi avoir la possibilité de se reposer pour retrouver des HP.

Le jeu compte 30 niveaux et se termine par le combat d'un boss ave des stats plus élevés que des mobs normaux,
au cours de l'aventure le joueur à la possibilité de gagner des succès qui seront stockés dans une basse de donnée
tout comme certaines infos relative au joueur.

Les stats des mobs ainsi que des pieces d'équipements sont toutes généré aléatoirement en fonction
du level dans lequel se situe le joueur cependant les valeurs obtenus parfois ne sont pas des plus optimales.

Pour finir nous avons mis en place cette base de donnée avec sqlLite3 et nous utilisons sqlliteviewer afin de visualiser
le contenu de celle ci.

En terme d'amélioration nous souhaiterions revoir le système de stats pour le rendre plus optimale, augmenter le contenu
de notre base de donné et notament ajouter la possibilité de reprendre notre aventure en la sauvegardant à un point précis

