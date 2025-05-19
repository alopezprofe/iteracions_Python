## Disseny d'Aplicacions Web - by Alexis López Riera

Document fet amb: Editor.md

![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)

![](https://img.shields.io/github/stars/alopezprofe/iteracions_Python.svg) ![](https://img.shields.io/github/forks/alopezprofe/iteracions_Python.svg) ![](https://img.shields.io/github/tag/alopezprofe/iteracions_Python.svg) ![](https://img.shields.io/github/release/alopezprofe/iteracions_Python.svg) ![](https://img.shields.io/github/issues/alopezprofe/iteracions_Python.svg)

[Curs de Moodle del mòdul 0487: Entorns de Desenvolupament](https://educaciodigital.cat/inslacetania/moodle/course/view.php?id=17871)

**Table of Contents**

Diagrama de classes:

```mermaid
---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

### Funcions de mostra <a name="punt1"></a>
```Python
def recorrer_dic(d):
  for clau in d:
    print(clau, d[clau]
```

### Testing a Python <a name="punt2"></a>
```Python
def recorrer_dic(l):
  """
  Funció que recorre una llista i mostra els seus valors
  >>> recorrer_dic(["groc", "vermell", "blau"])
  [ 'groc', 'vermell', 'blau' ] 
  """
  for element in l:
    print(element)
```
