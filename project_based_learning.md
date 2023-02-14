# Project Based Learning

I think something like computer science and programming are very hard concepts to learn, and it sometimes feels as though there is no way to get it done. So where do you start? How can I accomplish these things. I have "imposter syndrome". I feel like I am faking it.

## Breaking Things Up

These thoughts are valid, and I completely understand how programming and difficult concepts can be incredibly overwhelming, so how do we get over this? Personally, I think we can chunk things up. Do small things to build confidence reinforce the basics. Then, slowly we can advance into true knowledge

## Starting from scratch

if I had to start over learning to program. I would take an approach that allows me to create small programs that allow me to keep advancing. Learn the basics. Then, I personally like to create simple games or things of that nature. 

## Example project

Let's imagine you have done your research, and you decided that you wanted to learn python. You see it's one of the most in demand programming languages. It commands high salaries, but you don't know where to start. You've done the basics. You know what the basic data types are

```python
number = 3 #this is an int
name = "Lucas" #this is a string
people = ["Lucas", "Jamie", "Josh","Dylan"] #this is a list
def hello_world(): #this is a function
    return "hello world"
...
# and so on
```

you just don't feel confident you can create a project. What can you do?

I personally like to gamify my projects, but that is just a peronsal preference, so a recommendation I say to beginners is create a rock paper scissors game. It can be done in about 10-15 minutes.


you start by defining what would a rock paper scissors game need?

Player_choice -> Computer_choice -> check_winner

the player needs to make a choice. Then, we need to make a computer choose, and finally, we need to see who wins.

let's the players choice.
```python
def get_input():
    player = input("Player 1, pick rock, paper, or scissors:").lower()
    return player if player in ["rock", "paper", "scissors"] else get_input()

```
we can see we tell the user to give us rock, paper or scissors, and if they don't we make them choose again until they give something valid. 


so we have a PLAYER_CHOICE 


Then, I would need a the computers choice
```python
from random import choice

def computer_choice():
    return choice(["rock", "paper", "scissors"])
```

we can think, "oh what is this random thing", and we can learn about modules, and how we stand on the shoulders of giants. We can see how we have so many convience functions and to be honest many times being an "expert"... is knowing how and when to use functions from modules someone else wrote. 


so let's revist

we have a player choice, a computer choice, now all we need is to check who won. 

```python
def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice: #if they are the same
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player 1 wins!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player 1 wins!")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player 1 wins!")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Computer wins!")
    else:
        print("Something went wrong!")

```
and that's it... we finished a project. if we put it all together, it might look like this. 
```python
from random import choice

def get_input():
    player = input("Player 1, pick rock, paper, or scissors:").lower()
    return player if player in ["rock", "paper", "scissors"] else get_input()

def computer_choice():
    return choice(["rock", "paper", "scissors"])

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice: #if they are the same
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player 1 wins!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player 1 wins!")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player 1 wins!")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Computer wins!")
    else:
        print("Something went wrong!")

player_choice = get_input()
computer_choice = computer_choice()
check_winner(player_choice, computer_choice)
```
and there you go... you did it. Now, as you progress you may eventually be like well. what if I wanted to play more than once? what if I didn't want to type rock, paper, and scissors every time, and you could extend things more, so I wrote a version that has even more "expert" or at least good code choices in my opinion, so you can see things maybe you haven't seen before.  


```python
from random import choice

def not_valid_input():
    print("Not valid input. Please try again. pick rock, paper, or scissors.")
    return get_input()


def get_input():
    player = input("Player 1, pick rock, paper, or scissors:[r/p/s] ").lower()
    player = "rock" if player == "r" else player
    player = "paper" if player == "p" else player
    player = "scissors" if player == "s" else player
    return player if player in ["rock", "paper", "scissors"] else not_valid_input()



def get_computer_choice():
    return choice(["rock", "paper", "scissors"])

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player 1 wins!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player 1 wins!")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player 1 wins!")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Computer wins!")
    else:
        print("Something went wrong!")

def game_loop():
    while True:
        player_choice = get_input()
        computer_choice = get_computer_choice()
        print(f"{player_choice = }")
        print(f"{computer_choice = }")
        check_winner(player_choice, computer_choice)
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "n":
            break

def main():
    game_loop()

if __name__ == "__main__":
    main()
```
if there is anything you don't understand in the "expert code", just review, and try to make something yourself. You can't watch tutorials. You can watch a tutorial to learn, but then, you have to create a "mini-project" yourself to see if you truly understand. Then, keep going. Learning is hard. You will want to bang your head agains the wall. However, if you work hard, you can do it. I believe in you! 