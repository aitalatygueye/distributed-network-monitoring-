# Système distribué de supervision des noeuds d’un réseau

## Description

Ce projet implémente un système de **monitoring distribué** permettant de collecter des métriques système (CPU, mémoire, disque, uptime) depuis plusieurs machines clientes.

Les données sont envoyées à un serveur central qui les stocke dans une base de données SQLite et peut générer des alertes en cas de dépassement de seuils.

## Technologies utilisées

* Python
* Socket Programming
* SQLite
* GitHub pour la gestion du code

## Architecture du système

Le système est composé de quatre composants principaux :

1. **Client (Agent Supervision)**
   Simule des machines qui envoient leurs métriques système.

2. **Serveur de supervision**
   Reçoit les données des clients et les traite.

3. **Base de données SQLite**
   Stocke les métriques reçues.

4. **Gestionnaire d’alertes**
   Détecte les anomalies comme une forte utilisation CPU.

## Structure du projet

distributed-network-monitoring/

client/ → agents clients

server/ → serveur de supervision

database/ → gestion base de données

config/ → configuration et création DB

README.md → documentation

## Installation

Cloner le dépôt GitHub :

git clone https://github.com/aitalatygueye/distributed-network-monitoring.git

Entrer dans le projet :

cd distributed-network-monitoring

## Création de la base de données

python config/init_db.py

## Lancer le serveur

python -m server.server

## Lancer un client

python client/agent_client.py

## Simulation de plusieurs machines

for i in {1..20}; do python client/agent_client.py & done

## Exemple de données envoyées

{
"node": "node1",
"cpu": 54,
"memory": 6,
"disk": 88,
"uptime": 9689
}

## Auteur

Projet réalisé dans le cadre du Master Systèmes, Réseaux et Infrastructures Virtuelles.
