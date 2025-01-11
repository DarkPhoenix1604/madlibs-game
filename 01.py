def madlibs_game():
    print("Welcome to the Mad Libs game!\n")

    # Collecting user input for different parts of speech
    noun1 = input("Enter a noun (person, place, or thing): ")
    verb1 = input("Enter a verb (action word): ")
    adjective1 = input("Enter an adjective (describing word): ")
    adverb1 = input("Enter an adverb (how something is done): ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    adjective2 = input("Enter another adjective: ")

    # Creating the Mad Libs story
    story = f"Once upon a time, a {adjective1} {noun1} decided to {verb1} in a {adjective2} forest. " \
            f"Along the way, they met a {noun2} who was {adverb1} {verb2} in the woods. " \
            "They became best friends and lived happily ever after."

    # Output the Mad Libs story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Run the game
madlibs_game()
