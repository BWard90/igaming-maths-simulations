# iGaming Mathematics & Probability Simulations

Some lightweight Python scripts designed to model applied probability, verify statistical convergence, and simulate core casino game mechanics. 

### Contents
**`basic_3-reel_rtp.py`**
Simulates a classic 3-reel slot game to calculate Hit Frequency and Return to Player (RTP) profiles across 1,000,000 test cycles, including expected values.

**`dice_convergence_tester.py`**
Simulates large-scale iterations (e.g. 1,000,000 rolls) of custom dice setups to observe sample outcome distributions.

**`cleopatra_combos_problem.py`**
I was reading an article about deconstructing Cleopatra (which can be found here: https://wizardofodds.com/games/slots/cleopatra/) whilst learning about slot machines. After the winning combinations tables, the author (Michael Shackleford) writes: "Be warned that the math is tedious and error-prone to calculate these combinations by hand. If you're up to the challenge and you can code, then I recommend coding five nested loops and cycle through all 30^4*41=33,210,000 possible outcomes."

I decided that I wanted to give this a go. The result is my cleopatra_combos_problem script. The aim was to see if I could create a function that would iterate over all of the possible combinations and output a frequency table of all paying lines, similar to the tables presented in the article.

The biggest challenge I faced with this is that I hadn't fully considered the impact of the wilds on the reels, nor did I fully consider the impact of the doubled prizes for lines containing wilds. My first attempt correctly counted the number of winners, but hadn't placed all of the lines in the correct location on my frequency table. After revisiting the problem, I reordered my logic to pick off the highest paying lines first, down to the lowest, taking time to be more precise with my logic to ensure that lines that met the criteria of multiple pay conditions were associated with the correct highest paying option.

After testing, the function worked... however it is rather slow and clunky. I have since reflected on this, and I think one definite improvement would be to set the logic so that an iteration stops after it knows that the remaining reels will not change the outcome. For example, if the first reel is "K" and the second reel is "10", there is no reason to check the remaining reels as this will not appear in the pay table. This would save a lot of time processing as there are 33.21 million combinations, of which nearly approximately 31.8 million do not pay. Definitely something I would look to implement when I return to this problem.
