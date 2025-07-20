# rock-paper-scissor-sim
Have you ever wondered if rock, paper or scissors was better in the rock, paper scissors simulation game? No? Well I have, and this is what I will try to answer here. 
![this soooo low fps](https://raw.githubusercontent.com/marie-kjelberg/rock-paper-scissors/main/game.gif)

## Game simulation premise
An equal amount of rock, paper and scissor items spawn randomly around the canvas. If one touches another and that item beats the other, then the other item gets converted into the first item's type. The game continues like this until only either rock, paper or scissors remain. 

In my rendition of the game, the canvas is made up of a coordinate system of ``760x600`` pixels where each item is ``32x32`` pixels in size. It runs at approx. 60FPS. In order to run millions of these simulations, I made a version of this game whithout any of the visuals in the file ``pure_sim.py``. There you can decide how many times you want to run the simulation. You can subsequently modify and run the file ``chisquare_finder.py`` in order to summarize your collected data.

I assumed the null hypothesis to be true when working on this. Ie. that rock, paper and scissors are all equally likely to win. This is the hypothesis that I'm going to test here.

## Results & Findings
I ran this simulation a total of 11'100'000 times. After analyzing the data, this are the results:
![Screenshot of results](https://raw.githubusercontent.com/marie-kjelberg/rock-paper-scissors/main/chisquare_finder_21072025.png)
- Total entries: 11'100'000
- Expected results: rock=3700000, paper=3700000, scissors=3700000
- Observed results: rock=3720975, paper=3683973, scissors=3695052
- Percentage deviations: rock=+0.5668918918918918, paper=-0.43316216216216213, scissors=-0.13372972972972974
- Chi^2 value: 194.9454210810811
- P-value: 4.657358575808139e-43

These results would indicate that the null hypothesis is untrue, given the tiny p-value and big chi^2 value. Therefore, given the algorithm in its current form, rock appears to be marginally more suited to win in this simulation. Having said that, the statistical advantage that rock has is miniscule and appears not to serve any practical benefits as of now. 

## Future Curiosities: 

I wonder if changing the ``amounts`` variable does anything to change the results? Probably not, but it is something I want to test at another point. I also wonder if the odds change based on the canvas size. Having said all of that, Computing that for ~10 hours does not sound fun in this blazing summer ¯\_(ツ)_/¯