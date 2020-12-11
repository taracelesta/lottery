# Colorado Lottery
*co_lotto.csv:* Original
*co_lotto_clean.csv & co_lotto.pkl:* Includes Engineered Columns Developed in Cleaning
*co_lotto_2.pkl & co_lotto_clean_2.csv:* Includes Engineered Columns Developed in EDA
- draw_date, draw_year, draw_month, draw_day:
- winning_numbers, winning_numbers_list: 
- ball_1, ball_2, ball_3, ball_4, ball_5, ball_6:
- ball_1_int, ball_2_int, ball_3_int, ball_4_int, ball_5_int, ball_6_int:
- jackpot, jackpot_cash_value: 
- jackpot_co_winners:
- match_5_prize, match_5_co_winners:  
- match_4_prize, match_4_co_winners:
- match_3_prize, match_3_co_winners: 
- match_5_2x_prize, match_5_2x_winners: 
- match_5_3x_prize, match_5_3x_winners:
- match_5_4x_prize, match_5_4x_winners:
- match_5_5x_prize, match_5_5x_winners: 
- match_4_2x_prize, match_4_2x_winners:
- match_4_3x_prize, match_4_3x_winners: 
- match_4_4x_prize, match_4_4x_winners: 
- match_4_5x_prize, match_4_5x_winners:
- match_3_2x_prize, match_3_2x_winners: 
- match_3_3x_prize, match_3_3x_winners: 
- match_3_4x_prize, match_3_4x_winners:
- match_3_5x_prize, match_3_5x_winners:
- odd_even:
- odd_even_0, odd_even_1, odd_even_2, odd_even_3 ,' odd_even_4, odd_even_5, odd_even_6:
-high_low:
- high_low_0, high_low_1, high_low_2, high_low_3, high_low_4, high_low_5, high_low_6:
- IQR: 
- IQR_0, IQR_1, IQR_2, IQR_3, IQR_4, IQR_5 , IQR_6:
- delta_1, delta_2, delta_3, delta_4, delta_5:
        

*co_lucky_num.csv:* Original 
*co_lucky_num_clean.csv & co_lucky_num.pkl:* Cleaned versions: 
- Index: last_time_drawn: date that ball was last drawn excluding plus games
- times_drawn_excluding_plus: amount of times ball has been drawn since beginning of game, excluding plus   
- times_drawn_in_plus: amount of times ball has been drawn since beginning of game, including plus           
- last_time_drawn_in_plus: date that ball was last drawn in plus game  
- ball_int: drawn ball number                      
- year: year of drawn exclusing plus                              
- month: month of drawn exclusing plus                         
- day: day of last time drawn exclusing plus


*co_lucky_store.csv:* Original 
*co_lucky_stores.pkl & co_lucky_stores_clean.csv:* Cleaned Versions 
- game:
- store:
- address:
- city:
- zip:
- number of winners sold:
- total amount won:


*co_l_s_geocodio.csv:* Original Version made from co_lucky_stores_clean at geocodio.com *
*co_l_s_geo_clean.csv & co_l_s_geo.pkl:* Cleaned Version *
- address:
- city:
- zip:
- latitude:
- longitude:
- number:
- street:
- country:
- county:
- ACS Demographics/Sex/Total/Value: