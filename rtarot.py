#!/usr/bin/env python3
# rtarot — Tarot révolutionnaire dans le terminal
# Copyright (C) 2026 Kzaark
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import os
import random
import subprocess
import sys

# Version
VERSION = "1.0.0"

# Chemin
DATA_DIR = "/usr/local/share/rtarot/data"

# Couleurs ANSI
class Couleurs:
    ROUGE    = "\033[91m"
    JAUNE    = "\033[93m"
    GRIS     = "\033[90m"
    ITALIQUE = "\033[3m"
    BOLD     = "\033[1m"
    RESET    = "\033[0m"

# ─────────────────────────────────────────
# Lecture des données
# ─────────────────────────────────────────

def lire_carte(fichier: str) -> dict:
    chemin = os.path.join(DATA_DIR, fichier)
    if not os.path.exists(chemin):
        return {}
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)

def lire_toutes_cartes() -> list:
    if not os.path.exists(DATA_DIR):
        return []
    cartes = []
    for f in os.listdir(DATA_DIR):
        if f.endswith(".json"):
            carte = lire_carte(f)
            if carte:
                cartes.append(carte)
    return sorted(cartes, key=lambda c: c.get("numero", 0))

# ─────────────────────────────────────────
# Affichage
# ─────────────────────────────────────────

def afficher_carte(carte: dict, position: str = None):
    numero  = carte.get("numero", "?")
    nom     = carte.get("nom", "?")
    figure  = carte.get("figure", "?")
    sens    = carte.get("sens", "")
    desc    = carte.get("description", "")

    entete = f"Arcane {numero} — {nom}"
    if position:
        entete = f"{position} : {entete}"

    print(f"\n{Couleurs.BOLD}{Couleurs.ROUGE}{entete}{Couleurs.RESET}")
    print(f"{Couleurs.JAUNE}{figure}{Couleurs.RESET}")
    if sens:
        print(f"{Couleurs.GRIS}{Couleurs.ITALIQUE}{sens}{Couleurs.RESET}")
    print(f"\n{desc}")
    print()

# ─────────────────────────────────────────
# Commandes
# ─────────────────────────────────────────

def cmd_tirage_simple():
    cartes = lire_toutes_cartes()
    if not cartes:
        print("Aucune carte trouvée.")
        return
    carte = random.choice(cartes)
    afficher_carte(carte)

def cmd_tirage_triple():
    cartes = lire_toutes_cartes()
    if len(cartes) < 3:
        print("Pas assez de cartes pour un tirage à trois.")
        return
    tirage = random.sample(cartes, 3)
    positions = ["Passé", "Présent", "Futur"]
    print(f"\n{Couleurs.BOLD}━━━ Tirage à trois cartes ━━━{Couleurs.RESET}")
    for pos, carte in zip(positions, tirage):
        afficher_carte(carte, position=pos)
        print("─" * 40)

def cmd_carte(nom_ou_numero: str):
    cartes = lire_toutes_cartes()
    requete = nom_ou_numero.lower()

    # Recherche par numéro
    if requete.isdigit():
        for carte in cartes:
            if str(carte.get("numero")) == requete:
                afficher_carte(carte)
                return
        print(f"Aucune carte avec le numéro '{nom_ou_numero}'.")
        return

    # Recherche exacte par nom ou id
    exact = [
        c for c in cartes
        if requete == c.get("nom", "").lower()
        or requete == c.get("id", "").lower()
    ]
    if exact:
        afficher_carte(exact[0])
        return

    # Recherche partielle
    partielle = [
        c for c in cartes
        if requete in c.get("nom", "").lower()
        or requete in c.get("figure", "").lower()
    ]
    if not partielle:
        print(f"Aucune carte trouvée pour '{nom_ou_numero}'.")
        return
    for carte in partielle:
        afficher_carte(carte)

def cmd_list():
    cartes = lire_toutes_cartes()
    if not cartes:
        print("Aucune carte trouvée.")
        return
    print(f"\n{Couleurs.BOLD}Les 22 arcanes :{Couleurs.RESET}\n")
    for c in cartes:
        print(f"  {Couleurs.ROUGE}{c.get('numero')}{Couleurs.RESET} — {Couleurs.JAUNE}{c.get('nom')}{Couleurs.RESET} ({c.get('figure')})")
    print()

def cmd_mettre_a_jour():
    print("Mise à jour de rtarot...")
    result = subprocess.run(
        ["git", "-C", "/usr/local/share/rtarot", "pull"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print("✓ Mise à jour réussie !")
        print(result.stdout)
    else:
        print("✗ Erreur lors de la mise à jour :")
        print(result.stderr)

def cmd_version():
    print(f"rtarot v{VERSION}")

def desactiver_couleurs():
    Couleurs.ROUGE    = ""
    Couleurs.JAUNE    = ""
    Couleurs.GRIS     = ""
    Couleurs.ITALIQUE = ""
    Couleurs.BOLD     = ""
    Couleurs.RESET    = ""

def cmd_aide():
    print("""
rtarot — Tarot révolutionnaire dans ton terminal

Usage :
  rtarot                        Tirage d'une carte
  rtarot --triple                Tirage à trois cartes (passé/présent/futur)
  rtarot <nom ou numéro>        Affiche une carte précise
  rtarot --list                 Liste les 22 arcanes
  rtarot --no-color             Désactive la colorisation
  rtarot --update               Met à jour rtarot
  rtarot --version              Affiche la version installée
  rtarot --help                 Affiche ce message

Exemples :
  rtarot
  rtarot --triple
  rtarot 0
  rtarot bakounine
  rtarot --list
""")

# ─────────────────────────────────────────
# Point d'entrée
# ─────────────────────────────────────────

def parse_args():
    args = sys.argv[1:]

    if "--no-color" in args:
        desactiver_couleurs()
        args = [a for a in args if a != "--no-color"]

    if not args:
        cmd_tirage_simple()

    elif args[0] in ("--help", "-h"):
        cmd_aide()

    elif args[0] in ("--version", "-v"):
        cmd_version()

    elif args[0] == "--update":
        cmd_mettre_a_jour()

    elif args[0] == "--triple":
        cmd_tirage_triple()

    elif args[0] == "--list":
        cmd_list()

    elif args[0].startswith("--"):
        print(f"Option inconnue : '{args[0]}'. Lance 'rtarot --help'.")

    else:
        cmd_carte(args[0])

if __name__ == "__main__":
    parse_args()
