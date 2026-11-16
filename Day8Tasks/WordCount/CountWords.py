"""5. Word Counter Program
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results."""
try:
    with open("article.txt", "r") as file:
        text = file.read()
        
        lines = text.splitlines()
        words = text.split()
        characters = len(text)
        
        print("--- Article Statistics ---")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")

except FileNotFoundError:
    print("Error: article.txt was not found.")
