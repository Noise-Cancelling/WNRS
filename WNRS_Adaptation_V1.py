# We're Not Really Strangers, Python Edition
# Justin Starrett 2021


# Question bank for single player mode.
singleBank = [{"Who do I envy? Why do I envy them?"}, {"What am I wearing when I have the best time? What do I always regret wearing?"},
                  {"What have I been sensitive to lately?"}, {"Who do I feel most myself around? Why?"}, {"When do I feel most helpful to others?"},
                  {"What have I accomplished that would have shocked me a year ago?"},
                  {"What do I keep doing that keeps hurting? Why do I keep repeating this behavior?"},
                  {"What have my past relationships taught me about myself? Good and bad?"}]    
# Question bank for first level.
perceptionBank = [{"Who do you think my celebrity crush is?"}, {"What's the first thing you noticed about me?"},
                      {"What do you think my go to karaoke song is?"}, {"Do I seem like a coffee or tea person? Sweetened or unsweetened?"},
                      {"Do you think I am usually early, on time, or late to events? Why?"}, {"What does my phone wall paper tell you about me"},
                      {"What subject in school do you think I thrived in? Did I fail any?"}]
# Question bank for second level.   
connectionBank = [{"What are you still trying to prove to yourself?"}, {"What is your first love's name? Why did you fall in love with them?"},
                      {"What part of your life works? What part of your life hurts?"}, {"What lesson took you the longest to unlearn"},
                      {"WILDCARD: Think of someone you strongly dislike that most others love. On the count of three, say it out loud! (Both players)"},
                      {"When was a moment where you realized you weren't invincible?"}, {"What's been your happiest memory this past year?"},
                      {"Is there a feeling you miss?"}]
# Question bank for third level.
reflectionBank = [{"What do you think I should know about myself that I am perhaps unaware of?"}, {"What do you think my defining characteristic is?"},
                      {"How would you describe me to a stranger?"}, {"WILDCARD: Take a selfie together."}, {"What do you recommend I let go of, if anything?"},
                      {"If you could prescribe me one thing to do for the rest of the month, what would it be, and why?"}, {"What am I the most qualified to give advice about?"},
                      {"What about me is the hardest for you to understand?"}]
    
finalCard = {"Each player write a message to the other. Fold and exchange. Open only once you have parted."}

print("Hello, welcome to We're Not Really Strangers, Python Edition.\n")
print("This adaptation is a game for one or two players. How many players do you have?\n\n")

       
import random
while True:
# Player picks 1 or 2 player mode; catches ValueError.
    try:
        player_count = int(input("\nEnter the number 1 or 2: "))
    except ValueError:
        print()
        print("Oops! Please type the number '1' or '2'.\n")
# Single player mode.    
    if player_count == 1: 
        print("\nGreat! You will play Reflection mode.")
        print("Open your favorite word processor or grab a pen and paper.\n")
        print("You will be taken through a series of three questions. Take as long as you need to answer the question.")
        print("When you are finished, enter any input. You will then be brought to the next question.\n")
        
# Taking a random sample from the single player question bank.       
        singleQ = random.sample(singleBank, 3)
        for i in singleQ: 
            input("\nInput anything for a question: ")
            print()
            print(i)
            print()
            
    elif player_count == 2:
        print()
        print("Sounds good! Please enter the names of the players.")
        players = []
        for i in range(player_count): # Making list of players.
            player = input(f"Player {i + 1} name: ")
            players.append(player)
        print("\nThere are three levels: Perception, Connection, and Reflection.\nEach player will take turns asking the other a question.")
        print("After two questions each, you will move one to the next level. The game will culminate in a final question answered by both players.\n")
        
        perceptionQ = random.sample(perceptionBank, 4)
        for i, card in enumerate(perceptionQ): # Players take turns asking each other questions on the first level.
            player = players[i % 2]
            input(f"{player}, input anything to pick a card: ")
            print()
            print(card)
            print()

        print("You have finished the first level: Perception. You will now move onto Connection.\n")
        connectionQ = random.sample(connectionBank, 4)
        for i, card in enumerate(connectionQ): # Players take turns asking each other questions on second level.
            player = players[i % 2]
            input(f"{player}, input anything to pick a card: ")
            print()
            print(card)
            print()

        print("You have finished level two: Connection. You will now move onto Reflection.\n")
        reflectionQ = random.sample(reflectionBank, 4)
        for i, card in enumerate(reflectionQ): # Ask each other questions on third level.
            player = players[i % 2]
            input(f"{player}, input anything to pick a card: ")
            print()
            print(card)
            print()

        print("You have made it to the final card.\n")
        input("Input anything to draw the final card: ")
        print(finalCard)
        print()
          
    else:
        print("Input invalid. Please try again.")
        continue
        
    again = input("Play again (yes/no)? ")
    if again.lower() == "yes":
        continue
    else:
        break



