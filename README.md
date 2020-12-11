# Capstone Project 
## Lottery Number Predictions
-----------
### Table of Contents
[Executive Summary](https://git.generalassemb.ly/taracelesta/capstone_tcb/#executive-summary)

[Folder Structure](https://git.generalassemb.ly/taracelesta/capstone_tcb/#folder-structure)

[Problem Statement](https://git.generalassemb.ly/taracelesta/capstone_tcb/#problem-statement)

[Data Acquisition](https://git.generalassemb.ly/taracelesta/capstone_tcb/#data-acquisition)

[Data Description](https://git.generalassemb.ly/taracelesta/capstone_tcb/#data-description)

[Software Requirements](https://git.generalassemb.ly/taracelesta/capstone_tcb/#software-requirements)

[Data Cleaning Steps](https://git.generalassemb.ly/taracelesta/capstone_tcb/#data-cleaning-steps)

[Exploratory Data Analysis](https://git.generalassemb.ly/taracelesta/capstone_tcb/#exploratory-data-analysis)

[Data Processing](https://git.generalassemb.ly/taracelesta/capstone_tcb/#data-processing)

[Engineer Features](https://git.generalassemb.ly/taracelesta/capstone_tcb/#engineer-features)

[Modeling](https://git.generalassemb.ly/taracelesta/capstone_tcb/#modeling)

[Evaluation](https://git.generalassemb.ly/taracelesta/capstone_tcb/#evaluation)

[Conclusion](https://git.generalassemb.ly/taracelesta/capstone_tcb/#conclusion)

[Next Steps](https://git.generalassemb.ly/taracelesta/capstone_tcb/#next-steps)

-----------

## Folder Structure
```
|__ code:
|   |__ part_1_data_cleaning.ipynb      
|   |__ part_2_eda.ipynb 
|   |__ part_3_modeling.ipynb
|   |__ app.py
|__ data: 
|   |__ data_description.txt
|   |__ co_lotto.csv
|   |   |__ co_lotto_clean.csv
|   |   |__ co_lotto_clean_2.csv
|   |   |__ co_lotto.pkl
|   |   |__ co_lotto_2.pkl
|   |__ co_l_s_geocodio.csv
|   |   |__ co_l_s_geo_clean.csv
|   |   |__ co_l_s_geo.pkl
|   |__ co_lucky_num.csv
|   |   |__ co_lucky_num_clean.csv
|   |   |__ co_lucky_num.pkl
|   |__ co_lucky_stores.csv
|   |   |__ co_lucky_stores_clean.csv
|   |   |__ co_lucky_stores.pkl
|   |   |__ pb_lucky_stores.csv
|   |__ generate_numbers_data.pkl
|__ images:
|   |__ b123_pred.png
|   |__ b345_pred.png
|   |__ denver_metro_lucky_locations.png
|   |__ denver_metro_winners_per_zip.png
|   |__ high_low.png
|   |__ hot_cold.png
|   |__ hot_cold_time.png
|   |__ IQR.png
|   |__ jackpot_value.png
|   |__ lottery.jpg
|   |__ lucky_locations_$.png
|   |__ lucky_locations_ticket#.png
|   |__ num_winners.png
|   |__ odd_even.png
|   |__ sum_ball.png
|   |__ top_5_locations.png
|__ presentation:
|   |__ presentation_slides.pdf
|__ README.md
```

-----
## Problem Statement
Jackpot lottery games remain to be one of the most profitable gambling experiences. This is also why the odds of winning are not in the player's favor. The Colorado Lottery has been active since 1982 and has seen anywhere from 4-13 jackpot winners a year with a jackpot minimum of 1 million dollars. This game selects 6 lottery balls, from 1 to 40, without replacement. If a player guesses all 6 numbers before the drawing, they win.

Even though the lottery is a game of chance, based on the concept of randomness, I wanted to see if I could find patterns with the winning numbers. Through extensive eda, algorithms, and modeling, I proved that predicting lottery numbers is an impossible task, but a fun one!

-----
## Data Acquisition
[Drawing History](https://www.coloradolottery.com/en/player-tools/winning-history/?game=powerball&timeframe=90&submit=)

[Luckiest Numbers](https://www.coloradolottery.com/en/player-tools/luckiest-numbers/?game=powerball&timeframe=90&submit=)

[Luckiest Stores](https://www.coloradolottery.com/en/player-tools/luckiest-stores/search=&location=&radius=1&game=powerball&timeframe=90&submit=)

[Geo Codes](https://www.geocod.io/)

-----------
## Data Description 

Description of data can be found within the data folder labeled [data_description.txt](https://git.generalassemb.ly/taracelesta/capstone_tcb/blob/master/data/data_description.mdwn)

-----------
## Data Cleaning Steps
### co_lotto.csv:
- No record of jackpot amount or winners previous of 6/27/03
    - jackpot winners: impute to 0
    - jackpot amount: impute with mean of known jackpot amounts
- Change in Game on 3/23/2020
    - Match 5/4/3 x2/3/4/5 and Plus drawings began, replacing Match 5/4/3
    - Match 5/4/3 recorded from 6/27/03 - 3/19/2020: impute to 0
    - Match 5/4/3 x2/3/4/5 and Plus drawings recorded from 1/21/1989 - 3/23/20: impute to 0
- Removed Columns
    - 51 'Plus Drawing' columns were dropped from the original data due to extraneous features 
### co_lucky_num.csv:
 - Made date as column index
### co_l_s_geocodio.csv:
- Removed Columns
    - 35 columns were dropped from the original data due to duplicated information, extraneous features, or large amount of null values
- Population Count null values: imput with mean of population count by city

-----------
## Data Processing & Engineering Features
 - Split winning numbers into seperate columns:
     - ball_1: string type
     - ball_1_int: integer type
 - Winning numbers as different data types
     - winning_number_list: list type
 - Delta numbers as 'delta_1': representing the count between 1st-6th ball drawn
 - Odd_even: representing the count of odd and even numbers in each drawing
     - 'odd_even': 0= all evens, 1= 5 even/1 odd, 2= 4 even/2 odd, 3= 3 even/3 odd, 4= 2 even/4 odd, 5= 1 even/5 odd, 6= 6 odd
     - 'odd_even_1': 1 = odd, 0 = even
 - High low: representing the count of drawn numbers between 1-20 and 21-40
     - 'high/low': 0= all evens, 1= 5 even/1 odd, 2= 4 even/2 odd, 3= 3 even/3 odd, 4= 2 even/4 odd, 5= 1 even/5 odd, 6= 6 odd
     - 'high_low_1': 0 = 1-20, 1 = 21-40
 - IQR: representing the count of drawn numbers between 11-30 and 1-10 & 31-40
     - 'IQR': 0= all OQR(outer quartile range), 1= 5 OQR/1 IQR, 2= 4 OQR/2 IQR, 3= 3 OQR/3 IQR, 4= 2 OQR/4 IQR, 5= 1 OQR/5 IQR, 6= 6 IQR
     - IQR_1': 0 = 11-30, 1 = 1-10 & 31-40
 - Split draw dates into seperate columns:
     - 'draw_month': month of drawing
     - 'draw_year': year of drawing
     - 'draw_day': day of draying

-----------
## Exploratory Data Analysis
### Performed with Python and Tableau
- ![Lucky Locations](https://git.generalassemb.ly/taracelesta/capstone_tcb/blob/master/images/top_5_locations.png?raw=true)
- Hot Cold Numbers
    - Hot numbers are the numbers that have been picked most frequently throughout the drawings. You might consider these "lucky" numbers to pick. 34 is our hottest number!
    - Cold numbers are drawn less frequently overall. A cold number may have been drawn recently, but the overall number of times it has been drawn is below average. You might consider these unlucky numbers. 6 is our coldest number.

- Difference between numbers drawn
    - For a common 6/40 game, the Delta numbers will run between 1 and 10. Delta numbers higher than this can happen, but 90% of the time they don't.

- Number Totals
    - Numbers drawn usually add up to 128

- Determining Overdue numbers
    - Overdue numbers are ones that have not shown up in recent weeks. Maybe it's a hot number that hasn't been drawn recently. You might think it's bound to show up soon.
    - 11 is our most overdue number.

- Number Combinations
    - Odd and even: numbers drawn usually have 3 odd and 3 even numbers
    - High and low: numbers drawn usually have 3 numbers above 20 and 3 numbers below 20
    - IQR: numbers usually have 3 numbers within 11-30 and 3 numbers within 1-10 & 31-40

- Corrilation of Numbers Drawn
    - None found

- Corrilation Over Time
    - None found
- Comparison of Winners
    - Jackpot value predicted to be $338.89 million with a cash value of $155.25 million
    - 8 winners predicted to win in 2021

-----------
## Modeling & Evaluation
- Jackpot
    - Odds of you selecting all lottery number's correctly with a single ticket is 1 in 3838380.
        - The probability of you winning the jackpot is 0.00000026052657631605
    - The odds of you winning the jackpot with 2 tickets is 1 in 1919190
        - The probability of you winning the jackpot with 2 tickets is 0.00000052105315263210
    - The odds of you winning the jackpot with 10 tickets is 1 in 383838
        - The probability of you winning the jackpot with 10 tickets is 0.00000260526576316050
    - The odds of you winning the jackpot with 100 tickets is 1 in 38384
        - The probability of you winning the jackpot with 100 tickets is 0.00002605252188411838
    - The odds of you winning the jackpot with 10000 tickets is 1 in 384
        - The probability of you winning the jackpot with 10000 tickets is 0.00260416666666666652
    - The odds of you winning the jackpot with 1000000 tickets is 1 in 4
        - The probability of you winning the jackpot with 1000000 tickets is 0.25
    - The odds of you winning the jackpot with 6787409 tickets is 1 in 1
        - The probability of you winning the jackpot with 6787409 tickets is 1
- Match 3/4/5
    - The odds of selecting 5 numbers correctly with one ticket is 1 in 18815.58823529412
        - The probability of selecting 5 numbers correctly with one ticket is 0.00005314742156847420
    - The odds of selecting 4 numbers correctly with one ticket is 1 in 456.13547237076654
        - The probability of selecting 4 numbers correctly with one ticket is 0.00219233113969956057
    - The odds of selecting 3 numbers correctly with one ticket is 1 in 32.07202540106952
        - The probability of selecting 3 numbers correctly with one ticket is 0.03117982065350486526
- Jackpot Over Time
    - Probability of a jackpot win buying 1 ticket a week for 50 years is 0.0006771398239313609
- Bensford Law
    - No abnormalities in drawing found
- Time Seriese Predictions:
    - R2 score: .517
    - VAR
        - The test MSE on the diff_ball1 data is: 49.0948
        - The test MSE on the diff_ball2 data is: 71.9387
        - The test MSE on the diff_ball3 data is: 95.2724
        - The test MSE on the diff_ball4 data is: 97.8041
        - The test MSE on the diff_ball5 data is: 86.4677
        - The test MSE on the diff_ball6 data is: 52.6506
    - ![1st - 3rd Balls Drawn](https://git.generalassemb.ly/taracelesta/capstone_tcb/blob/master/images/b123_pred.png?raw=true)
    - ![4th - 6th Balls Drawn](https://git.generalassemb.ly/taracelesta/capstone_tcb/blob/master/images/b456_pred.png?raw=true)
- Naive Bayes Ball 1 Prediction:
    - best score .152
- Multilabel Classification:
    - Accuracy score .133
- Keras:
    - Predicted numbers: 8. 13. 19. 25. 31. 37.

-----------
## Predict and Play Web App
Lottery game web app developed with Streamlit. Pick your own numbers or let the app choose for you. Play the lottery with your numbers or see the probabilitiy of you winning. Code can be found within the code folder labeled [app.py](https://git.generalassemb.ly/taracelesta/capstone_tcb/blob/master/code/app.py)

-----------
## Conclusion

Every lottery ticket purchased has an equal probability of winning for that particular game. Each drawing is independent of the next therefore there is no relation between historical numbers and future numbers

Becasue of this, my goal of predicting the exact numbers from one-time events, comeing out of what is essentially a fully random process, is impossible to achieve.

We can only predict using statistical methods and modeling when the data has some repeating patterns, corrilation or some inherent order.

-----------
## References
https://towardsdatascience.com/understanding-mega-millions-lottery-using-python-simulation-d2b07d30a7cc

https://towardsdatascience.com/the-house-always-wins-monte-carlo-simulation-eb82787da2a3

https://towardsdatascience.com/probability-of-winning-the-lottery-9331080952c4

https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173

http://www.use4.com/prove-it.html  

http://www.flalottery.com/exptkt/pwrball-odds.pdf

https://www.statschat.org.nz/2012/09/05/lotto-and-abstract-theory/ 

https://lotterycodex.com/how-to-win-the-lottery-mathematically/ 

https://en.wikipedia.org/wiki/Lottery_mathematics#:~:text=Lottery%20mathematics%20is%20used%20to,way%20and%20combinations%20without%20replacement.

https://github.com/JeffMv/Lofea 
 
https://github.com/uranusdemilo/LottoProj/blob/master/lotto.py