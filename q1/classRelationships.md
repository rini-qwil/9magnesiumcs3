# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Music
Description: My class represents the different songs, artists, and genres that are found in streaming services like Spotify.

## New Related Class
Class: Instruments 
Description: They are devices made to make musical sounds.

## Association
Relationship: Music includes instruments.

Explanation: Without instruments, music would become bland and boring because they are crucial tools in creating sound. They bring textures, colors, and emotions to a piece. 

## Multiplicity
Multiplicity: *
Explanation: I chose the multiplicity "many" because there are many different instruments that are used to play music.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis:
### What is the association between your two classes?
The association I used between my two classes is "includes".

### What multiplicity did you choose and why?
The multiplicity I chose was the "Many" multiplicity because like I said earlier, there are many different instruments that are used to play music. There is no single "instrument" used to play music.

### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
A list is appropriate when the relationship uses "many" because they are used to store multiple items in a single variable. 
