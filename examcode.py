def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")



greet("Pravin", "Selvaranjan")
greet("John", "Smith")

def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("yoyoyo")

secret_word = "Sparta"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word:
    if guess_count < guess_limit:
       guess = input("Enter guess: ")
       guess_count += 1
else:
    out_of_guesses = True
    if out_of_guesses:
     print("Out of guesses, YOU LOSE!")

else:
    print ("You win!")



print("You win!")