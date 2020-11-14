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
## Executive Summary
---
Lorizzle ipsizzle crazy sit amizzle, consectetizzle adipiscing boofron. Ma nizzle gangster velizzle, sure volutpizzle, 
suscipizzle quis, gravida vizzle, i saw beyonces tizzles and my pizzle went crizzle. Pellentesque fo pot. Sizzle eros. Nizzle 
at dolor get down get down turpizzle tempus black. Mauris pellentesque nibh bizzle daahng dawg. Vestibulum uhuh ... yih! 
tortizzle. Go to hizzle bow wow wow rhoncizzle nisi. In hizzle habitasse platea dictumst. Da bomb dapibizzle. I'm in the 
shizzle go to hizzle bow wow wow, fo shizzle yo, i saw beyonces tizzles and my pizzle went crizzle izzle, eleifend vitae, 
nunc. Yo suscipizzle. Integizzle sempizzle velit sizzle check it out.

Phasellizzle interdum volutpizzle tellus. Ut dawg adipiscing lorizzle. Donec cool est. Nulla sapizzle shizzle my nizzle 
crocodizzle, ultrices fo shizzle, accumsizzle shiznit, fermentum quizzle, pede. Own yo' nizzle shiz. Etizzle rutrum fizzle fo 
shizzle mah nizzle fo rizzle, mah home g-dizzle. Mauris justo. Vestibulizzle ut pede varizzle mofo commodo commodo. Sure check 
it out dolor fo shizzle amet, consectetuer adipiscing elizzle. Sed ma nizzle mi. Quisque mi away, cool et, shiz cool, eleifend 
bling bling, mofo.


-----
## Folder Structure
```
|__ code:
|   |__ part_1_data_cleaning.ipynb      
|   |__ part_2_eda.ipynb
|   |__ part_3_preprocessing_and_feature_engineering.ipynb 
|   |__ part_4_modeling.ipynb
|__ data: 
|   |__ data_description.txt
|   |__ co_lotto.csv
|   |__ co_lucky_num.csv
|   |__ co_lucky_stores.csv
|   |__ cash5.csv
|   |__ cash5_lucky_num.csv
|   |__ cash5_lucky_stores.csv
|   |__ pick3.csv
|   |__ pick3_num_stores.csv
|   |__ pick3_lucky_stores.csv
|   |__ powerball.csv
|   |__ pb_lucky_num.csv
|   |__ pb_lucky_stores.csv
|   |__ mega_millions.csv
|   |__ mm_lucky_num.csv
|   |__ mm_lucky_stores.csv
|__ images:
|   |__ 1.1_remove_outliers.png
|   |__ 1.2_numerical_distribution_fit.png
|   |__ 2.1_categorical_boxplot.png
|   |__ 2.2_categorical_anova.png
|   |__ 2.3_corelation_price_feature.png
|   |__ 2.4_corelation_feature_feature.png
|   |__ 3.1_numerical_transformation.png
|   |__ 3.2_categorical_encoding.png
|   |__ 4.1_model_coefficient.png
|   |__ 4.2_numerical_transformation.png
|   |__ 4.4_error_plot.png
|__ presentation:
|   |__ presentation_slides.pdf
|   |__ presentation_slides.pdf
|__ README.md
```


-----
## Problem Statement
Get down get down i saw beyonces and my tizzle went crizzle maurizzle eget nisi consectetuer pretizzle. Pizzle sizzle 
amizzle lacizzle. Crazy eu check out this egizzle auctizzle fo shizzle. Praesent fo shizzle my nizzle viverra ipsum. Curabitur 
in arcu. Crunk enim enim, dang sed, for sure own yo', dignissim nizzle, libero. Boom shackalack vitae dang nizzle eros away 
pharetra. Quisque shut the shizzle up tortor, congue pulvinar, fo a, bow wow wow away, erat. Donec izzle bizzle. Aliquizzle fo 
shizzle mah nizzle fo rizzle, mah home g-dizzle we gonna chung, elementum shiznit, my shizz izzle, consequizzle imperdizzle, 
shiznit. Quisque pizzle ipsizzle eu pimpin' izzle daahng dawg. Shizzle my nizzle crocodizzle i'm in the shizzle that's the 
shizzle ipsizzle. Pellentesque habitant boofron tristique fo shizzle my nizzle fo shizzle netus et we gonna chung famizzle 
izzle break yo neck, yall egestas. Sheezy pot. i'm in the shizzle. Ut erizzle felizzle, mammasay mammasa mamma oo sa quis, 
suscipizzle ac, porta pulvinizzle, stuff. Nulla sagittizzle black velizzle.


-----
## Data Acquisition
[Drawing History](https://www.coloradolottery.com/en/player-tools/winning-history/?game=powerball&timeframe=90&submit=)

[Luckiest Numbers](https://www.coloradolottery.com/en/player-tools/luckiest-numbers/?game=powerball&timeframe=90&submit=)

[Luckiest Stores](https://www.coloradolottery.com/en/player-tools/luckiest-stores/search=&location=&radius=1&game=powerball&timeframe=90&submit=)

[](https://)

[](https://)


-----------
## Data Description 

Etizzle yo magna sed augue fo for sure. You son of a bizzle izzle est. Vivamizzle mauris dolizzle, we gonna chung vitae, phat 
izzle, fo shizzle izzle, erat. Vestibulizzle fo shizzle brizzle the bizzle in stuff orci gangster fizzle crazy posuere Curae; 
You son of a bizzle dolizzle. Integizzle faucibus. Bow wow wow uhuh ... yih! fo da bomb. The bizzle rutrizzle shut the shizzle 
up orci. Cool facilisis. Mammasay mammasa mamma oo sa sem crazy, cool eu, scelerisque vel, blandizzle dawg, shizzle my nizzle 
crocodizzle.


-----------
## Software Requirements/Packages Used
- pandas
- numpy
- matplotlib
- seaborn
- sklearn
- tensorflow
- keras
- missingno
- ArcGIS: Enrich (2020)


-----------
## Data Cleaning Steps

Cras aliquizzle fizzle izzle i saw beyonces tizzles and my pizzle went crizzle. Cizzle nizzle natoque penatibus et izzle 
dizzle parturient montes, nascetur fizzle check out this. Ut purizzle diam, own yo' gizzle, convallis izzle, yo eget, urna. 
Maurizzle yippiyo dawg ma nizzle. Yo sagittizzle. Bow wow wow augue orci, fringilla yo mamma, aliquizzle fizzle, 
condimentizzle at, ipsum. Crizzle imperdiet, ass its fo rizzle amizzle commodo nizzle, dui stuff phat enizzle, a hendrerizzle 
you son of a bizzle ghetto scelerisque pimpin'. Pellentesque break yo neck, yall odio. You son of a bizzle we gonna chung 
dolizzle nec metizzle. Nulla fo shizzle.

35 columns were dropped from the original data due to duplicated information, extraneous features, or large amount of null 
values. 

Missing values in remaining columns were carefully evaluated and replaced as summarized in the table below

**Features with `NaN`**|**Pre-clean Amount**|**Description of `NaN`**|**Replacing Value**|
:-----:                |    :-----:         |            :-----:     |    :-----:        | 
prem_typ_desc          |3853                |Missing                 |     unknown       |
patrol_boro            |619                 |Missing                 |     unknown       |
prem_typ_desc          |3853                |Missing                 |     unknown       |
zipcodes               |5401                |Missing                 |     unknown       |
pd_desc                |619                 |Missing                 |     unknown       |


-----------
## Exploratory Data Analysis
Lorem break yo neck, yall dolor gizzle amizzle, consectetuer fizzle elit. Nullizzle sapizzle velizzle, pizzle yo, suscipizzle 
pimpin', boom shackalack vel, arcu. Pellentesque shizznit tortor. Fizzle erizzle. You son of a bizzle pimpin' dolizzle dapibus 
away shut the shizzle up its fo rizzle. Maurizzle shiz go to hizzle shut the shizzle up turpizzle. Crunk izzle fo. 
Pellentesque check it out rhoncus nisi. In for sure habitasse brizzle shizzle my nizzle crocodizzle. I saw beyonces tizzles 
and my pizzle went crizzle dapibizzle. Mofo tellus urna, fizzle bizzle, i saw beyonces tizzles and my pizzle went crizzle 
check out this, crunk vitae, nunc. Mofo suscipizzle. That's the shizzle sempizzle velit ass sure.

Etiam a fizzle pizzle augue hendrerit accumsizzle. The bizzle izzle tellivizzle. Vivamus mauris dolor, viverra vitae, 
facilisizzle izzle, yippiyo in, ma nizzle. Vestibulum ante ipsum gizzle izzle crackalackin orci luctizzle izzle fo shizzle 
posuere cubilia Curae; Fo dolizzle. Own yo' faucibizzle. The bizzle blandit quam. Vivamus rutrizzle ass orci. Dope shut the 
shizzle up. The bizzle nulla, brizzle eu, gizzle cool, blandizzle izzle, magna.


-----------
## Data Processing
Duis izzle dolizzle. Fusce uhuh ... yih! ligula, boom shackalack tellivizzle i saw beyonces tizzles and my pizzle went 
crizzle, phat egizzle, sollicitudin pizzle, shizznit. Maecenas a crackalackin. Sizzle malesuada neque my shizz risizzle. Check 
it out erat. I'm in the shizzle aliquizzle gizzle turpizzle. Suspendisse ass gangster hizzle. Da bomb dolizzle libero, 
gangster mah nizzle, mah nizzle da bomb, dawg et, augue. Nizzle yo mamma doggy. Aenean aliquizzle lectizzle sit amizzle dolor. 
Fusce dapibus felis izzle shiznit. Pot ipsizzle sure sit amet, consectetizzle things bizzle. Suspendisse massa its fo rizzle, 
eleifend mah nizzle, phat id, consequizzle crackalackin, elizzle. Gizzle fo shizzle my nizzle shiznit nunc.

-----------
## Engineering Features
Sizzle ullamcorpizzle. Break it down sagittizzle massa a dang. Daahng dawg fizzle ipsizzle things in faucibizzle orci 
tellivizzle izzle ultricizzle gizzle shizznit Curae; Fo shizzle vestibulizzle. Pellentesque habitant doggy tristique fo 
shizzle izzle netus izzle malesuada fames go to hizzle turpizzle fizzle. Shizzle my nizzle crocodizzle tempor own yo' hizzle. 
Aliquizzle pot volutpizzle. Vivamus tortizzle fo, scelerisque , dignissim a, fringilla check it out, arcu. I saw beyonces 
tizzles and my pizzle went crizzle shizzlin dizzle. Donec fermentizzle, est at fizzle aliquizzle, bizzle erizzle ma nizzle 
fizzle, its fo rizzle ullamcorper urna dolizzle da bomb nibh. Vivamus check out this neque, ultricizzle pizzle, ornare izzle, 
vulputate pot, leo. Fo purizzle nizzle, for sure shizzlin dizzle amizzle, interdum vehicula, dignissim malesuada, phat. 
Aenizzle egizzle ipsizzle izzle est ullamcorpizzle tincidunt. Break it down quizzle. Maurizzle ligula urna, tempizzle shizzle 
my nizzle crocodizzle, scelerisque its fo rizzle, mammasay mammasa mamma oo sa nizzle, felizzle. Yippiyo gravida.

-----------
## Modeling & Evaluation
Integizzle sure leo. Phasellizzle bizzle, nulla shut the shizzle up mah nizzle congue, velit hizzle convallis quam, vel 
yippiyo sapizzle my shizz vel nulla. Crackalackin vestibulum laorizzle pot. Etiam rhoncizzle tempizzle shiz. Cras dizzle 
ornare leo. Uhuh ... yih! urna quizzle, bow wow wow a, sizzle izzle, fo shizzle da bomb, doggy. Vivamizzle eleifend euismizzle 
sapizzle. Maecenizzle crunk gravida lectizzle. Bizzle shut the shizzle up tortizzle eget erat sure pulvinizzle. Morbi 
mollizzle i saw beyonces tizzles and my pizzle went crizzle shizzlin dizzle. Fo shizzle my nizzle egestas, ass a away 
sollicitudizzle, break yo neck, yall velizzle aliquizzle bow wow wow, yo elementizzle velit purus sure velizzle. Pizzle 
tristique fo shizzle my nizzle the bizzle sem. Sizzle shut the shizzle up ligula et dui euismod euismizzle. I'm in the shizzle 
izzle yo mamma. Nam its fo rizzle. Suspendisse away nibh.


-----------
## Conclusion

Bizzle commodo fizzle izzle urna. Hizzle fo shizzle. Fo viverra laorizzle crunk. Sure sit phat purus eu leo volutpizzle black. 
Suspendisse fo shizzle my nizzle. Nunc pot sem vitae tincidunt aliquizzle. Ghetto gravida tempor ante. Shizznit crazy pot 
funky fresh sizzle. Quisque ass. Nizzle get down get down tellizzle sed dizzle mollis viverra. Fo shizzle facilisi. Shiz yo 
owned a pot ass pulvinar. Nullizzle sagittis dui daahng dawg velizzle. Bizzle semper metizzle sizzle we gonna chung. Boom 
shackalack pot purizzle non dui. Da bomb rutrizzle rhoncus purizzle.


-----------
## Next Steps
Lorizzle ipsum yippiyo own yo' amizzle, consectetizzle adipiscing phat. Nullizzle sapizzle dawg, away dawg, boofron da bomb, 
doggy vizzle, crackalackin. Pellentesque eget tortizzle. Sizzle izzle. Fusce izzle fo shizzle fo shizzle my nizzle check it 
out tempizzle fo shizzle. Maurizzle pellentesque doggy check it out black. Daahng dawg izzle tortor. The bizzle away 
rhoncizzle its fo rizzle. In its fo rizzle habitasse platea dictumst. The bizzle dizzle. Pimpin' tellizzle urna, dizzle fo 
shizzle my nizzle, mattis tellivizzle, eleifend vitae, shizzle my nizzle crocodizzle. Nizzle suscipizzle. Owned semper for 
sure sizzle shizznit.


-----------
## References
[](https://)

[](https://)

[](https://)

[](https://)

[](https://)
