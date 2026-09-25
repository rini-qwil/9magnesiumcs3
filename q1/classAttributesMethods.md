# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision:


## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| song_title  | String | Public(+) | It stores the song title.|
| artist | String | Public(+) | It stores the artist/s' name.|
| genre | String | Public(+) | It stores the song's genre|
| publication_year | Int | Private(-) | It protects the publicaction year from being modified by outside code. |
| is_playing | Boolean | Private(-) | It tracks wheter the song is currently playing or not. |



## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis:
### Why did you make your chosen attribute private?

I made my chosen attributes "is_playing" and "publication_year" private to avoid changes from outside code, and these are managed by hidden helpers.

### Which method changes the state of your object?
The method that changes the state of my object is "set_publication_year" because it modifies the data stored within the object.

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
My class diagram shows the data types of each object, while the object diagram shows the final values of it.