
# SG4 - Understanding Classes and Objects

## Class Name:
Music

## Class Description:
My class represents the different songs, artists, and genres that are found in streaming services like Spotify.

| Property   | Data Type | Description | Visibility
|---|---|---|---|
| Song Title | String  | It is used to instantly find songs and it also grabs the attention of the customer/listener | Public(+)
|  Artist    | String  | It is the person who wrote/sang/produced/performed the music.  | Public(+)
|  Genre     | String  | It categorizes pieces of music that share traits like musical composition, instruments used, origins, and more. | Public(+)
| Publication Year | Int | The year the song is first distributed to the public. | Private (-)
| is_playing | Boolean | This tells whether a song is currently playing or not. | Private (-)

## Methods:
| Method | Description | 
|---|---|
| playBack(seconds) | Playback is used to rewind the music played/is playing.|
| Skip()    | Skip is used to skip the current song playing.|
| Pause()  | Pause is used to stop the current song playing. |
| get_publication_year()  | This returns the private publication year. |
| set_publication_year(year)| This is used to update the publication year IF it is valid and checked. |

## UML Class Diagram:
[Class Diagram](Pictures/classDiagram.png)

## Short Design Explanation: 

### Why did you choose this class?
I chose this class because it peaked my interest when I first saw it.

### Which property is the most important? Why?
The property that I think is the most important is the song title because it is the first thing people see when they go to Spotify or any music streaming websites. Through the song title, users can get a first impression on what the song is going to be about. 

###  Which method is the most useful? Why?
The method that I think is the most useful is playBack() because in my experience, I like to repeat music and rewind parts that I really like in the song like the bridge and intro.