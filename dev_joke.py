import random

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people: those who understand binary and those who don't.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why do Java developers wear glasses? Because they don't C#.",
    "It works on my machine. Then we'll ship your machine.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "I would tell you a UDP joke, but you might not get it.",
    "99 little bugs in the code. Take one down, patch it around... 127 little bugs in the code.",
    "Debugging: being the detective in a crime movie where you're also the murderer.",
    "Why did the developer go broke? Because he used up all his cache.",
]

if __name__ == "__main__":
    print(random.choice(JOKES))
