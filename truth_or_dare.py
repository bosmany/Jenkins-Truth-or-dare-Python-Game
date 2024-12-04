import random

def truth_or_dare():
    truths = [
        "What is your biggest fear?",
        "What is the most embarrassing thing you've ever done?",
        "Who was your first crush?"
    ]
    dares = [
        "Sing a song loudly.",
        "Dance for 30 seconds.",
        "Act like a monkey for 10 seconds."
    ]

    print("Welcome to the Truth or Dare Game!")
    while True:
        choice = input("\nChoose 'truth' or 'dare' (or type 'exit' to quit): ").lower()
        if choice == "truth":
            print(random.choice(truths))
        elif choice == "dare":
            print(random.choice(dares))
        elif choice == "exit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please type 'truth', 'dare', or 'exit'.")

if __name__ == "__main__":
    truth_or_dare()
