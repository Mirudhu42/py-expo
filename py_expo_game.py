import random
import streamlit as st


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    
    player_choice = st.radio("Choose rock, paper, or scissors:", choices)
    
    
    computer_choice = random.choice(choices)
    st.write(f"Computer chose: {computer_choice}")
    
    
    if player_choice == computer_choice:
        st.write("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        st.write("You win!")
    else:
        st.write("Computer wins!")


def guess_the_number():
    number = random.randint(1, 10)
    attempts = 3
    st.write("Guess the number between 1 and 10. You have 3 attempts.")
    
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
    
    if st.button("Submit Guess"):
        if guess == number:
            st.write("Congratulations! You guessed it right.")
        elif guess < number:
            st.write("Too low!")
        else:
            st.write("Too high!")
        
        
        st.write(f"Sorry, the correct number was {number}.")


def main():
    st.title("Random Game Selection")

    
    game_choice = st.selectbox("Select a game to play:", ["Rock Paper Scissors", "Guess the Number"])
    
    if game_choice == "Rock Paper Scissors":
        rock_paper_scissors()
    elif game_choice == "Guess the Number":
        guess_the_number()


main()
