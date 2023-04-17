# Hackathon des tortues

# [callysto.github.io/hackathon/tortue](https://callysto.github.io/hackathon/tortue)

## Introduction

[Graphiques de tortue](https://en.wikipedia.org/wiki/Turtle_graphics) ont été utilisés pour apprendre la programmation et la pensée computationnelle. Nous les utiliserons pour en savoir plus sur la programmation Python et les notebooks Jupyter.

---

## Commandes des tortues

Le code que vous devez exécuter importera la [bibliothèque de code de dessin de tortue](https://github.com/callysto/tortuemobile) puis créez une nouvelle toile de dessin de tortue.

```
import tortuemobile
t = tortuemobile.Tortue()
```

Votre tortue s'appelle maintenant `t`, voici les commandes possibles que vous pouvez utiliser.

|Commande|Description|Exemple|
|-|-|-|
|`t.vitesse(entier)`|la vitesse de votre tortue, de 1 à 10|`t.vitesse(10)`|
|`t.droite(degrés)`|tourner votre tortue vers la droite d'un certain nombre de degrés|`t.droite(90)`|
|`t.gauche(degrés)`|tourner la tortue vers la gauche d'un certain nombre de degrés|`t.gauche(45)`|
|`t.avant(pixels)`|faire avancer la tortue d'un certain nombre de pixels|`t.avant(100)`|
|`t.recule(pixels)`|faire reculer la tortue d'un certain nombre de pixels|`t.retraite(20)`|
|`t.cercle(rayon, degrés)`|faire dessiner à la tortue un morceau de cercle de rayon égal à un certain nombre de degrés|`t.cercle(40, 360)`|
|`t.styloenhaut()`|ta tortue peut maintenant se déplacer sans tracer des lignes|`t.styloenhaut()`|
|`t.styloenbas()`|ta tortue trace à nouveau des lignes|`t.styloenbas()`|
|`t.couleurstylo('color')`|couleur de la ligne de votre tortue en utilisant un [nom de couleur](https://www.w3schools.com/colors/colors_names.asp)|`t.couleurstylo('blue')`|
|`t.couleurstylo('rgb(R, V, B)')`|couleur de la ligne de votre tortue en utilisant valeurs de rouge, vert, et bleu de 0 à 255|`t.pencolor('rgb(0, 255, 100)')`|
|`t.origine()`|remettre la tortue au centre de l'écran|`t.origine()`|
|`t.position(x, y)`|déplacer la tortue à une position spécifique, (0,0) est en haut à gauche et (400, 400) est en bas à droite|`t.position(100, 250)`|
|`t.cap(degrés)`|fixer le cap de la tortue à un certain nombre de degrés|`t.cap(90)`|

---

## Défis du hackathon

Ces défis n'ont pas besoin d'être complétés dans un ordre particulier. Dites à un enseignant lorsque vous en avez accompli un, il vous donnera des points pour cela.

Travailler sur les défis sur [le Hub Callysto](https://2i2c.callysto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fhackathon&branch=master&subPath=HackathonNotebooks/Tortue/tortue.ipynb&depth=1).

### Beginner

Ces défis valent 2 points chacun.

1. dessine un rectangle rouge
1. dessine un triangle vert
1. dessine un cercle bleu
1. dessine un pentagone violet
1. dessine une étoile jaune
1. dessine une flèche cyan
1. dessine un parallélogramme orange
1. dessine un hexagone magenta
1. dessine un visage
1. dessine le symbole π

### Intermediate

Ces défis valent 5 points chacun.

1. dessine un coeur rose
1. dessine un diagramme de Venn
1. dessine un triangle rectangle avec la couleur RVB `(205, 133, 63)`
1. dessine un triangle équilatéral avec un périmètre de 90 pixels
1. dessine un demi-cercle avec deux couleurs différentes
1. dessine un croissant d'argent
1. dessine [Pac-Man](https://en.wikipedia.org/wiki/Pac-Man)
1. dessine une [maison](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-house.png)
1. dessine une maison avec une porte, une fenêtre, et une cheminée
1. dessine une [simple fleur noire](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-simple-black-flower.png)
1. dessine une [fleur noire](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-black-flower.png)
1. utilise [boucles](https://www.w3schools.com/python/python_for_loops.asp) dans un dessin
1. utilise [boucles imbriquées](https://www.w3schools.com/python/gloss_python_for_nested.asp) dans un dessin
1. utilise [fonctions](https://www.w3schools.com/python/python_functions.asp) dans un dessin
1. dessine un emoji

### Advanced

Ces défis valent 15 points chacun.

1. dessine une [fleur colorée pointue](https://raw.githubusercontent.com/callysto/hackathon/master/HackathonNotebooks/Turtles/images/turtle-pointy-flower.png)
1. dessiner une [feuille d'érable](https://github.com/callysto/TMTeachingTurtles/blob/jupyter-turtles-art-contest/turtles-cool-art-demo.ipynb) entière
1. dessiner une scène de paysage avec beaucoup de couleurs
1. écrive votre nom ou surnom avec une tortue
1. dessine un clavier de piano d'une octave
1. dessine votre Pokémon assigné
1. utilise un [dataframe pour créer un dessin de tortue](https://github.com/callysto/TMTeachingTurtles/blob/master/TMDataTurtles/turtles-and-data-student.ipynb)
1. crée une fonction qui accepte un paramètre entier et dessine une forme avec autant de côtés
1. crée une vidéo de 15 secondes présentant les tortues Python aux personnes de votre âge
1. écrive un ou deux paragraphes descriptifs sur vos expériences d'aujourd'hui à partager avec vos adultes ou vos amis

## Submit

Utilise [ce formulaire](https://forms.gle/fUwREoMutHLWdwb47) pour sumettre votre :

* Nom de votre équipe
* Membres de votre équipe
* Réponses aux questions de réflexion :
    1. Quelles sont les deux choses que vous avez apprises jusqu'à présent ?
    1. Quelle a été votre partie préférée de cette activité ?
    1. Y a-t-il d'autres choses que vous aimeriez créer avec les tortues Python ?
    
**Si vous ne soumettez pas de réponses aux questions de réflexion, votre équipe ne sera pas considérée pour les prix.**
