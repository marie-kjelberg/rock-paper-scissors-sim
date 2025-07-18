# rock-paper-scissor-sim
I was curious to see if one item was better in this simulation game. 

Todo: 
- Make it be able to simulate everything without rendering it (at ~60fps, but random spawnpoints)
- Collect data 
- Run it at least 100k times

## How to simulate without rendering it: (probably)
I imagine I could just update the positions (with the same frequency), but just not render it. Right now I use the inbuilt collision system, but in I will need to change this and make my own algorithm. After this, I imagine I could possibly run these in parallel to achieve 100k runs faster.  

I want to try to find more efficent ways of modeling this. Matrix representation would be the ultimate form of this, but I am terrible at linear algebra. 