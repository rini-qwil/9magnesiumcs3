# Coding Excercise: Chinese Zodiac Calculator

## Requirements:
- Ask the user to input their birthyear (with a baseline year of 1900)
- Validate that the input is not less than the year 1900. If invalid, display an error message and exit.
- Determine the Chinese Zodiac using a 12-year cycle staring from 1900.

## Python Code ('zodiacMagnesiumPrena.py')
birth_year= int(input("Enter your birth year: "))
if birth_year < 1900:
    print("Invalid year. It should not be earlier than 1900.") 
### Stops program if the year is earlier than 1900 

### List of the Chinese Zodiac signs with their translation 
else: 
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)"
    ]

### Finds the remainder after dividing the year gap by 12
    index = (birth_year - 1900) % 12
### Picks the matching animal from the list
    zodiac_sign = zodiac_signs[index]

    print(f"Your Chinese zodiac sign is: {zodiac_sign}")

