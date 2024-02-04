# Database Schema

This document describes the schema of our PostgreSQL database, which includes two tables: character and quest.

## Tables

### Character

The character table stores information about characters. It has the following columns:

- CharacterID: An integer that uniquely identifies each character. This is the primary key of the table.
- Name: A string that stores the name of the character.
- Password: A string that stores the password of the character.
- Class: A string that stores the class of the character.

### Quest

The quest table stores information about quests. It has the following columns:

- QuestID: An integer that uniquely identifies each quest. This is the primary key of the table.
- Title: A string that stores the title of the quest.
- Description: A string that stores the description of the quest.
- Rewards: A string that stores the rewards of the quest.
- Experience: An integer that stores the experience points of the quest.

## Relationships

Each character can have multiple quests. This is represented by a one-to-many relationship from character to quest.

## ER Diagram

The following ER diagram illustrates this schema:

https://www.mermaidchart.com/app/projects/0b40769f-6378-41ce-9e9d-c3aba7ebea19/diagrams/444f8fe7-e50e-4c9a-b6ac-3d8481974412/version/v0.1/edit