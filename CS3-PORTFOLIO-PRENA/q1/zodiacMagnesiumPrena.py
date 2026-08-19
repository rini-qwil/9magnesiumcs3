zodiac_signs = [ 
    ("Rat", "鼠 / Shǔ"),
    ("Ox", "牛 / Niú"),
    ("Tiger", "虎 / Hǔ"),
    ("Rabbit", "兔 / Tù"),
    ("Dragon", "龙 / Lóng"),
    ("Snake", "蛇 / Shé"),
    ("Horse", "马 / Mǎ"),
    ("Goat", "羊 / Yáng"),
    ("Monkey", "猴 / Hóu"),
    ("Rooster", "鸡 / Jī"),
    ("Dog", "狗 / Gǒu"),
    ("Pig", "猪 / Zhū") ]

baseline_year = 1900
user_input = int(input("Enter your birth year: "))

if user_input < baseline_year:
    print("Please enter a year greater than or equal to 1900.") 

if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):  
    print("Invalid input. Year should not be less than 1900.")
    exit()

if birth_year < baseline_year:
    print("Please enter a year greater than or equal to 1900.")
    exit()  

zodiac_index = (user_input - baseline_year) % 12

print(f"Your Chinese zodiac sign is: {zodiac_signs[zodiac_index][0]} ({zodiac_signs[zodiac_index][1]})")