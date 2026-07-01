# `rtarot`

Affiche des tirages de tarot révolutionnaire dans le terminal — inspiré des symboles et archétypes des mouvements sociaux, politiques et spirituels.

![Langue](https://img.shields.io/badge/Langue-Français-blue.svg)
![Licence](https://img.shields.io/badge/licence-GPL--3.0-red?style=flat-square)
![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey?style=flat-square&logo=linux)
![Terminal](https://img.shields.io/badge/terminal-bash%20%7C%20zsh%20%7C%20fish-black?style=flat-square)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)

---

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple de sortie](#exemple-de-sortie)
- [Mise à jour](#mise-à-jour)
- [Désinstallation](#désinstallation)
- [Licence](#licence)

---

## Prérequis

- Python 3.x
- Git

---
## Installation

```bash
git clone https://github.com/Kzaark/rtarot.git
cd rtarot/
chmod +x install.sh
sudo ./install.sh
```

---
## Utilisation

```bash
rtarot                        → Tirage d'une carte
rtarot --triple               → Tirage à trois cartes (passé/présent/futur)
rtarot <nom ou numéro>        → Affiche une carte précise
rtarot --list                 → Liste les 22 arcanes
rtarot --no-color             → Désactive la colorisation
rtarot --update               → Met à jour rtarot
rtarot --version              → Affiche la version installée
rtarot --help                 → Affiche l'aide
```

### Exemples

```bash
rtarot
rtarot --triple
rtarot 0
rtarot bakounine
rtarot --list
```

---
## Exemple de sortie

```bash
$ rtarot

Arcane 0 — Le Mat
Louis-Auguste Blanqui
L'insurrection perpétuelle, l'homme hors système

Le Mat avance sans regarder où il pose le pied, indifférent aux conventions. Blanqui incarne cet archétype : 33 ans de sa vie passés en prison pour avoir organisé insurrection sur insurrection, sans jamais renoncer. Théoricien du putsch et de l'organisation clandestine, il refuse tout compromis avec l'ordre établi. Sa vie est une suite ininterrompue de complots, d'évasions, de retours en prison — l'image même du révolutionnaire qui ne s'arrête jamais, quoi qu'il en coûte.
```

---
## Mise à jour

```bash
rtarot --update
```

---
## Désinstallation

```bash
sudo ./uninstall.sh
```
---
## Licence
[GNU GPL-3.0](https://github.com/Kzaark/tarot-revolutionnaire/blob/main/LICENCE)
