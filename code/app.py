import time
import streamlit as st
import pickle
import numpy as np
import random
import math
from collections import Counter


with open('data/generate_numbers_data.pkl', 'rb') as pickle_in:
    df2 = pickle.load(pickle_in)

st.title(':crystal_ball: Lottery Crystal Ball :crystal_ball:')
st.title("Pick 6 numbers from 1 to 40")

st.subheader("Do you know the lottery numbers you want to play?")
yes = st.checkbox("Yes, I have my own numbers.")
no = st.checkbox("No, predict my numbers for me.")

numbers_ready = 0
numbers_ready2 = 0

if yes == True:
    guessed_numbers = st.multiselect(
        "Great! Select your six numbers here",
        ('1', '2', '3', '4', '5', '6', '7', '8',
         '9', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22',
         '23', '24', '25', '26', '27', '28', '29',
         '30', '31', '32', '33', '34', '35', '36',
         '37', '38', '39', '40'))
    if len(guessed_numbers) < 6:
        st.write(f'Please select {6-len(guessed_numbers)} more numbers.')
    else:
        st.write(
            "Perfect, My magic ball told me you would pick those numbers. \n Are you ready to play?")
        numbers_ready2 += 1


if no == True:
    st.subheader("My crystal ball tells me your lucky numbers are...")

    balls = df2.iloc[:, 1:7].values
    X_balls = np.zeros((balls.shape[0], 40))
     
    N = balls.shape[0]
    d = 40
    num_selected = []
    numbers_of_rewards_1 = [0] * d
    numbers_of_rewards_0 = [0] * d

    for n in range(N):
        max_random = 0
        num = 0
        for i in range(d):
            random_beta = random.betavariate(numbers_of_rewards_1[i]+1,
                                             numbers_of_rewards_0[i]+1)
            if random_beta > max_random:
                max_random = random_beta
                num = i

        num_selected.append(num)

        if X_balls[n, num] == 1:
            numbers_of_rewards_1[num] += 1
        else:
            numbers_of_rewards_0[num] += 1

    guessed_numbers = [i+1 for i, _ in Counter(num_selected).most_common(6)]

    if len(guessed_numbers) == 6:
        numbers_ready2 += 1

    st.write(f"{guessed_numbers}")

if numbers_ready == 1:
    st.subheader("Perfect, My magic ball told me you would pick those numbers. \n Are you ready to play?")
    play = st.checkbox("Yes I'm feeling lucky!")
    pick_odds = st.checkbox("What are my odds of winning?")

if numbers_ready2 == 1:
    st.subheader("Now that we have your lucky numbers, are you ready to play?")
    play = st.checkbox("Yes I'm feeling lucky!")
    pick_odds = st.checkbox("What are my odds of winning?")

    if play == True:
        ready = st.subheader("Sounds good! Let me cross the paradox and start your lottery:nail_care:")
        with st.spinner("...this might take a sec"):
            time.sleep(2)
        
        generated = []

        while len(generated) < 6:
            random_num = random.randrange(1, 41)
            generated.append(random_num)

        correct_guess = []

        for num in guessed_numbers:
            if num in generated:
             correct_guess.append(num)

        st.write(f'the lottery numbers are ', generated)
        st.write(f'you guessed ', guessed_numbers)
        st.write(f'your correct guesses are', correct_guess)
        
        num_correct = len(correct_guess)
        if num_correct > 1:
            st.write(f"you got {str(num_correct)} numbers right!:trophy:")
        elif num_correct <= 1:
            st.write(
                f":cyclone:You only got 1 number right:cyclone:Better luck next time:cyclone:")
        elif num_correct == 6:
            st.write("JACKPOT WINNER!!!:trophy:")
            st.write('you guess all 6 numbers correct!')

    if pick_odds == True:
    
        numerator = math.factorial(40)
        denominator = math.factorial(6) * math.factorial(40-6)
        odds = numerator / denominator
        total_outcomes = round(odds)
        successful_outcome = 1 / total_outcomes

        st.write(f"Odds of you selecting all lottery number's correctly with a single ticket is 1 in {total_outcomes}!")
        st.write(f"The probability of you winning the jackpot is {successful_outcome:.20f}%!")
