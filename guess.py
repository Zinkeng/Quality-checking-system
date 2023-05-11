secret_number = 10
guess_count = 0
guess_limit = 3

print("You have three trials to guess a number")
while guess_count < guess_limit:
    
    guess = int(input("Guess a number: "))
    guess_count +=1
    if guess == secret_number:
        print("You won!")
        break
        
else:
        print("You loose")
    
    
    