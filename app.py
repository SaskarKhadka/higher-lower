import streamlit as st
import random

def start_game():
  if 'game_started' not in st.session_state or st.session_state.game_started is False:
    st.session_state.game_started = True
    st.session_state.random_no = random.randint(1, 100)

def play_again():
  st.session_state.game_started = False
  st.session_state.user_guess = ''
  start_game()

def run_app():
  st.title("Welcome to the Higher Lower Game")  
  st.write("Your objective is to guess the randomly generated number from 1 to 100")
  st.write("For each guess, you are given a hint - higher or lower")
  st.write("You are given **Higher** if your guess is higher than the random number")
  st.write("You are given **Lower** if you guess if lower than the random number")
  st.write("")
  st.write("")
  start_game() 
  st.text_input("Enter Guess", key='user_guess')
  if st.button("Guess"):
    try:
      guess = int(st.session_state.user_guess)
      if guess < 1 or guess > 100:
        raise ValueError()
      if guess == st.session_state.random_no:
        st.write("Congratulations, You Won!!!!")
        st.button("Play Again", on_click=play_again)
      elif guess > st.session_state.random_no:
        st.write("Higher")
      else:
        st.write("Lower")
    except ValueError:
      st.write("Invalid guess, please enter an integer from 1 and 100")

if __name__ == "__main__":
  run_app()
