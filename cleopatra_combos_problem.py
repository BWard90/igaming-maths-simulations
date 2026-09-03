import random

reel1 = ["eye", "Q", "10", "gold", "J", "A", "crook and flail", "10", "Q", "flower", "9", "10", "Sphinx", "Q", "J", "Cleopatra", "Q", "A", "flower", "K", "scarab", "Q", "eye", "K", "crook and flail", "10", "scarab", "9", "gold", "10"]
reel2 = ["Q", "J", "gold", "Q", "A", "Cleopatra", "Q", "J", "eye", "9", "Q", "gold", "K", "scarab", "J", "flower", "10", "scarab", "9", "Sphinx", "A", "crook and flail", "10", "K", "flower", "J", "Q", "eye", "J", "crook and flail"]
reel3 = ["K", "9", "eye", "10", "gold", "K", "J", "Cleopatra", "Q", "10", "gold", "9", "J", "scarab", "A", "10", "crook and flail", "A", "K", "scarab", "9", "10", "flower", "Q", "9", "crook and flail", "K", "eye", "9", "Sphinx"]
reel4 = ["K", "9", "eye", "A", "flower", "J", "scarab", "10", "crook and flail", "J", "gold", "Q", "eye", "J", "10", "crook and flail", "A", "Q", "Sphinx", "10", "K", "gold", "J", "crook and flail", "9", "A", "flower", "9", "A", "Cleopatra"]
reel5 = ["gold", "10", "J", "flower", "K", "10", "Cleopatra", "K", "9", "scarab", "10", "eye", "A", "J", "Sphinx", "9", "A", "crook and flail", "Q", "A", "crook and flail", "10", "eye", "Q", "gold", "9", "Cleopatra", "J", "flower", "Q", "K", "eye", "J", "10", "gold", "Q", "crook and flail", "9", "scarab", "A", "9"]

len_r1 = len(reel1)
len_r2 = len(reel2)
len_r3 = len(reel3)
len_r4 = len(reel4)
len_r5 = len(reel5)

winning_combos_counter = {"Cleo_5": 0, "Cleo_4": 0, "Cleo_3": 0, "Cleo_2": 0,
                          "scar_5": 0, "scar_4": 0, "scar_3": 0, "scar_2": 0,
                          "flow_5": 0, "flow_4": 0, "flow_3": 0, "flow_2": 0,
                          "gold_5": 0, "gold_4": 0, "gold_3": 0,
                          "c&f_5": 0, "c&f_4": 0, "c&f_3": 0,
                          "eye_5": 0, "eye_4": 0, "eye_3": 0,
                          "A_5": 0, "A_4": 0, "A_3": 0,
                          "K_5": 0, "K_4": 0, "K_3": 0,
                          "Q_5": 0, "Q_4": 0, "Q_3": 0,
                          "J_5": 0, "J_4": 0, "J_3": 0,
                          "10_5": 0, "10_4": 0, "10_3": 0,
                          "9_5": 0, "9_4": 0, "9_3": 0, "9_2": 0}

winning_combos_x2_counter = {"scar_5": 0, "scar_4": 0, "scar_3": 0, "scar_2": 0,
                             "flow_5": 0, "flow_4": 0, "flow_3": 0, "flow_2": 0,
                             "gold_5": 0, "gold_4": 0, "gold_3": 0,
                             "c&f_5": 0, "c&f_4": 0, "c&f_3": 0,
                             "eye_5": 0, "eye_4": 0, "eye_3": 0,
                             "A_5": 0, "A_4": 0, "A_3": 0,
                             "K_5": 0, "K_4": 0, "K_3": 0,
                             "Q_5": 0, "Q_4": 0, "Q_3": 0,
                             "J_5": 0, "J_4": 0, "J_3": 0,
                             "10_5": 0, "10_4": 0, "10_3": 0,
                             "9_5": 0, "9_4": 0, "9_3": 0, "9_2": 0}    

"""

One of the biggest challenges here is that combinations that include wilds are doubled (excluding pure wilds).

To counter this, I initially tried to take out 5 wilds first, then deal with all of the doubles. The issue this caused though was that
although all of the combos were accounted for, they weren't placed in the best location when compared to the payout table.

For example, (Cleo, Cleo, Cleo, scar, scar) could be 3 wilds AND 5 scarabs, and my initial grouping caused it to be placed in with the 3 wilds,
which would then cause problems when later evaluating rtp etc. I also learned that I had to be much more precise with my logic, as I later realised
that (Cleo, Cleo, Cleo, scar, Cleo) would be 5 scarabs too, which was much harder to notice.

Below is a function that works, but it doesn't feel efficient. Having reflected on this, I think one definite improvement would be to set the logic so that
an iteration stops after it knows that the remaining reels will not change the outcome. For example, if the first reel is "K" and the second reel is "10",
there is no reason to check the remaining reels as this will not appear in the pay table. This would save a lot of time processing as there are 33.21 million
combinations, of which nearly approximately 31.8 million do not pay. Definitely something I would look to implement when I return to this problem.

"""

def winning_combos():
    for a in reel1:
        for b in reel2:
            for c in reel3:
                for d in reel4:
                    for e in reel5:
                        spin_outcome = (a, b, c, d, e)

                        # 10000 - 5 Cleopatra
                        if spin_outcome.count("Cleopatra") == 5:
                            winning_combos_counter["Cleo_5"] += 1

                        # 2000 - 4 Cleopatra
                        # Do not need to worry about 5 Cleo's here as they've been counted
                        elif spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_counter["Cleo_4"] += 1

                        # 1500 - 5 scarab / flower (wild)
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("scarab") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["scar_5"] += 1

                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("flower") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["flow_5"] += 1

                        # 800 - 5 gold (wild)
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("gold") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["gold_5"] += 1

                        # 750 - 5 scarab / flower (natural)
                        elif spin_outcome.count("scarab") == 5:
                            winning_combos_counter["scar_5"] += 1

                        elif spin_outcome.count("flower") == 5:
                            winning_combos_counter["flow_5"] += 1

                        # 500 - 5 crook and flail / eye (wild)
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("crook and flail") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["c&f_5"] += 1

                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("eye") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["eye_5"] += 1
                        
                        # 400 - 5 gold (natural)
                        elif spin_outcome.count("gold") == 5:
                            winning_combos_counter["gold_5"] += 1

                        # 250 - 5 A (wild)
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("A") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["A_5"] += 1

                        # 250 - 5 crook and flail / eye (natural)
                        elif spin_outcome.count("crook and flail") == 5:
                            winning_combos_counter["c&f_5"] += 1

                        elif spin_outcome.count("eye") == 5:
                            winning_combos_counter["eye_5"] += 1
                        
                        # 200 - 3 Cleopatra
                        # Since this list is ordered by prize size, any higher paying duplicates of 3 Cleo's have been accounted for
                        # Similar logic is used for all future elif statements in this section
                        elif spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_counter["Cleo_3"] += 1
                        
                        # 200 - 4 scarab / flower (wild)
                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("scarab") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["scar_4"] += 1

                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("flower") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["flow_4"] += 1
                        
                        # 200 - 4 gold (wild)
                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("gold") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["gold_4"] += 1

                        # 200 - 5 K-9 (wild)
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("K") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["K_5"] += 1
                        
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("Q") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["Q_5"] += 1
                        
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("J") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["J_5"] += 1
                        
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("10") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["10_5"] += 1
                        
                        elif spin_outcome.count("Cleopatra") > 0 and spin_outcome.count("9") + spin_outcome.count("Cleopatra") == 5:
                            winning_combos_x2_counter["9_5"] += 1
                        
                        # 150 - 4 crook and flail (wild)
                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("crook and flail") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["c&f_4"] += 1
                        
                        # 125 - 5 A (natural)
                        elif spin_outcome.count("A") == 5:
                            winning_combos_counter["A_5"] += 1
                        
                        # 100 - 4 eye (wild)
                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("eye") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["eye_4"] += 1
                        
                        # 100 - 4 scarab / flower (natural)
                        elif spin_outcome[0:4].count("scarab") == 4:
                            winning_combos_counter["scar_4"] += 1

                        elif spin_outcome[0:4].count("flower") == 4:
                            winning_combos_counter["flow_4"] += 1

                        # 100 - 4 gold (natural)
                        elif spin_outcome[0:4].count("gold") == 4:
                            winning_combos_counter["gold_4"] += 1
                        
                        # 100 - 5 K-9 (natural)
                        elif spin_outcome.count("K") == 5:
                            winning_combos_counter["K_5"] += 1
                        
                        elif spin_outcome.count("Q") == 5:
                            winning_combos_counter["Q_5"] += 1
                        
                        elif spin_outcome.count("J") == 5:
                            winning_combos_counter["J_5"] += 1
                        
                        elif spin_outcome.count("10") == 5:
                            winning_combos_counter["10_5"] += 1
                        
                        elif spin_outcome.count("9") == 5:
                            winning_combos_counter["9_5"] += 1
                        
                        # 100 - 4 A-K (wild)
                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("A") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["A_4"] += 1

                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("K") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["K_4"] += 1

                        # 75 - 4 crook and flail (natural)
                        elif spin_outcome[0:4].count("crook and flail") == 4:
                            winning_combos_counter["c&f_4"] += 1
                        
                        # 50 - 4 eye (natural)
                        elif spin_outcome[0:4].count("eye") == 4:
                            winning_combos_counter["eye_4"] += 1
                        
                        # 50 - 3 scarab / flower (wild)
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("scarab") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["scar_3"] += 1

                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("flower") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["flow_3"] += 1
                        
                        # 50 - 4 A-K (natural)
                        elif spin_outcome[0:4].count("A") == 4:
                            winning_combos_counter["A_4"] += 1

                        elif spin_outcome[0:4].count("K") == 4:
                            winning_combos_counter["K_4"] += 1
                        
                        # 50 - 4 Q-9 (wild)
                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("Q") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["Q_4"] += 1

                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("J") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["J_4"] += 1

                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("10") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["10_4"] += 1

                        elif spin_outcome[0:4].count("Cleopatra") > 0 and spin_outcome[0:4].count("9") + spin_outcome[0:4].count("Cleopatra") == 4:
                            winning_combos_x2_counter["9_4"] += 1
                        
                        # 30 - 3 gold (wild)
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("gold") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["gold_3"] += 1
                        
                        # 25 - 3 scarab / flower (natural)
                        elif spin_outcome[0:3].count("scarab") == 3:
                            winning_combos_counter["scar_3"] += 1

                        elif spin_outcome[0:3].count("flower") == 3:
                            winning_combos_counter["flow_3"] += 1

                        # 25 - 4 Q-9 (natural)
                        elif spin_outcome[0:4].count("Q") == 4:
                            winning_combos_counter["Q_4"] += 1

                        elif spin_outcome[0:4].count("J") == 4:
                            winning_combos_counter["J_4"] += 1

                        elif spin_outcome[0:4].count("10") == 4:
                            winning_combos_counter["10_4"] += 1

                        elif spin_outcome[0:4].count("9") == 4:
                            winning_combos_counter["9_4"] += 1
                        
                        # 20 - 3 crook and flail / eye (wild)
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("crook and flail") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["c&f_3"] += 1
                        
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("eye") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["eye_3"] += 1
                        
                        # 20 - 3 A (wild)
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("A") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["A_3"] += 1
                        
                        # 15 - 3 gold (natural)
                        elif spin_outcome[0:3].count("gold") == 3:
                            winning_combos_counter["gold_3"] += 1

                        # 10 - 3 crook and flail / eye (natural)
                        elif spin_outcome[0:3].count("crook and flail") == 3:
                            winning_combos_counter["c&f_3"] += 1

                        elif spin_outcome[0:3].count("eye") == 3:
                            winning_combos_counter["eye_3"] += 1
                        
                        # 10 - 3 A (natural)
                        elif spin_outcome[0:3].count("A") == 3:
                            winning_combos_counter["A_3"] += 1
                        
                        # 10 - 2 Cleopatra
                        elif spin_outcome[0:2].count("Cleopatra") == 2:
                            winning_combos_counter["Cleo_2"] += 1
                        
                        # 10 - 3 K-9 (wild)
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("K") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["K_3"] += 1
                        
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("Q") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["Q_3"] += 1
                        
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("J") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["J_3"] += 1
                        
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("10") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["10_3"] += 1
                        
                        elif spin_outcome[0:3].count("Cleopatra") > 0 and spin_outcome[0:3].count("9") + spin_outcome[0:3].count("Cleopatra") == 3:
                            winning_combos_x2_counter["9_3"] += 1
                        
                        # 5 - 3 K-9 (natural)
                        elif spin_outcome[0:3].count("K") == 3:
                            winning_combos_counter["K_3"] += 1

                        elif spin_outcome[0:3].count("Q") == 3:
                            winning_combos_counter["Q_3"] += 1

                        elif spin_outcome[0:3].count("J") == 3:
                            winning_combos_counter["J_3"] += 1

                        elif spin_outcome[0:3].count("10") == 3:
                            winning_combos_counter["10_3"] += 1

                        elif spin_outcome[0:3].count("9") == 3:
                            winning_combos_counter["9_3"] += 1
                        
                        # 4 - 2 scarab / flower (wild)
                        elif spin_outcome[0:2].count("Cleopatra") > 0 and spin_outcome[0:2].count("scarab") + spin_outcome[0:2].count("Cleopatra") == 2:
                            winning_combos_x2_counter["scar_2"] += 1

                        elif spin_outcome[0:2].count("Cleopatra") > 0 and spin_outcome[0:2].count("flower") + spin_outcome[0:2].count("Cleopatra") == 2:
                            winning_combos_x2_counter["flow_2"] += 1
                        
                        # 4 - 2 9 (wild)
                        elif spin_outcome[0:2].count("Cleopatra") > 0 and spin_outcome[0:2].count("9") + spin_outcome[0:2].count("Cleopatra") == 2:
                            winning_combos_x2_counter["9_2"] += 1
                        
                        # 2 - 2 scarab / flower (natural)
                        elif spin_outcome[0:2].count("scarab") == 2:
                            winning_combos_counter["scar_2"] += 1

                        elif spin_outcome[0:2].count("flower") == 2:
                            winning_combos_counter["flow_2"] += 1

                        # 2 - 2 9 (natural)
                        elif spin_outcome[0:2].count("9") == 2:
                            winning_combos_counter["9_2"] += 1

    #clean tables to show results
    print('Non-Doubled Line Pay Combinations')
    print(f"{'Symbol':<15} | {'5 in a row':<10} | {'4 in a row':<10} | {'3 in a row':<10} | {'2 in a row':<10}")
    print("-" * 67)
    print(f"{'Cleopatra':<15} | {winning_combos_counter['Cleo_5']:<10} | {winning_combos_counter['Cleo_4']:<10} | {winning_combos_counter['Cleo_3']:<10} | {winning_combos_counter['Cleo_2']:<10}")
    print(f"{'scarab':<15} | {winning_combos_counter['scar_5']:<10} | {winning_combos_counter['scar_4']:<10} | {winning_combos_counter['scar_3']:<10} | {winning_combos_counter['scar_2']:<10}")
    print(f"{'flower':<15} | {winning_combos_counter['flow_5']:<10} | {winning_combos_counter['flow_4']:<10} | {winning_combos_counter['flow_3']:<10} | {winning_combos_counter['flow_2']:<10}")
    print(f"{'gold':<15} | {winning_combos_counter['gold_5']:<10} | {winning_combos_counter['gold_4']:<10} | {winning_combos_counter['gold_3']:<10} | {'    -    ':<10}")
    print(f"{'crook and flail':<15} | {winning_combos_counter['c&f_5']:<10} | {winning_combos_counter['c&f_4']:<10} | {winning_combos_counter['c&f_3']:<10} | {'    -    ':<10}")
    print(f"{'eye':<15} | {winning_combos_counter['eye_5']:<10} | {winning_combos_counter['eye_4']:<10} | {winning_combos_counter['eye_3']:<10} | {'    -    ':<10}")
    print(f"{'A':<15} | {winning_combos_counter['A_5']:<10} | {winning_combos_counter['A_4']:<10} | {winning_combos_counter['A_3']:<10} | {'    -    ':<10}")
    print(f"{'K':<15} | {winning_combos_counter['K_5']:<10} | {winning_combos_counter['K_4']:<10} | {winning_combos_counter['K_3']:<10} | {'    -    ':<10}")
    print(f"{'Q':<15} | {winning_combos_counter['Q_5']:<10} | {winning_combos_counter['Q_4']:<10} | {winning_combos_counter['Q_3']:<10} | {'    -    ':<10}")
    print(f"{'J':<15} | {winning_combos_counter['J_5']:<10} | {winning_combos_counter['J_4']:<10} | {winning_combos_counter['J_3']:<10} | {'    -    ':<10}")
    print(f"{'10':<15} | {winning_combos_counter['10_5']:<10} | {winning_combos_counter['10_4']:<10} | {winning_combos_counter['10_3']:<10} | {'    -    ':<10}")
    print(f"{'9':<15} | {winning_combos_counter['9_5']:<10} | {winning_combos_counter['9_4']:<10} | {winning_combos_counter['9_3']:<10} | {winning_combos_counter['9_2']:<10}")
    print(f"\n Total {sum(winning_combos_counter.values())}")

    print('\nDoubled Line Pay Combinations')
    print(f"{'Symbol':<15} | {'5 in a row':<10} | {'4 in a row':<10} | {'3 in a row':<10} | {'2 in a row':<10}")
    print("-" * 67)
    print(f"{'scarab':<15} | {winning_combos_x2_counter['scar_5']:<10} | {winning_combos_x2_counter['scar_4']:<10} | {winning_combos_x2_counter['scar_3']:<10} | {winning_combos_x2_counter['scar_2']:<10}")
    print(f"{'flower':<15} | {winning_combos_x2_counter['flow_5']:<10} | {winning_combos_x2_counter['flow_4']:<10} | {winning_combos_x2_counter['flow_3']:<10} | {winning_combos_x2_counter['flow_2']:<10}")
    print(f"{'gold':<15} | {winning_combos_x2_counter['gold_5']:<10} | {winning_combos_x2_counter['gold_4']:<10} | {winning_combos_x2_counter['gold_3']:<10} | {'    -    ':<10}")
    print(f"{'crook and flail':<15} | {winning_combos_x2_counter['c&f_5']:<10} | {winning_combos_x2_counter['c&f_4']:<10} | {winning_combos_x2_counter['c&f_3']:<10} | {'    -    ':<10}")
    print(f"{'eye':<15} | {winning_combos_x2_counter['eye_5']:<10} | {winning_combos_x2_counter['eye_4']:<10} | {winning_combos_x2_counter['eye_3']:<10} | {'    -    ':<10}")
    print(f"{'A':<15} | {winning_combos_x2_counter['A_5']:<10} | {winning_combos_x2_counter['A_4']:<10} | {winning_combos_x2_counter['A_3']:<10} | {'    -    ':<10}")
    print(f"{'K':<15} | {winning_combos_x2_counter['K_5']:<10} | {winning_combos_x2_counter['K_4']:<10} | {winning_combos_x2_counter['K_3']:<10} | {'    -    ':<10}")
    print(f"{'Q':<15} | {winning_combos_x2_counter['Q_5']:<10} | {winning_combos_x2_counter['Q_4']:<10} | {winning_combos_x2_counter['Q_3']:<10} | {'    -    ':<10}")
    print(f"{'J':<15} | {winning_combos_x2_counter['J_5']:<10} | {winning_combos_x2_counter['J_4']:<10} | {winning_combos_x2_counter['J_3']:<10} | {'    -    ':<10}")
    print(f"{'10':<15} | {winning_combos_x2_counter['10_5']:<10} | {winning_combos_x2_counter['10_4']:<10} | {winning_combos_x2_counter['10_3']:<10} | {'    -    ':<10}")
    print(f"{'9':<15} | {winning_combos_x2_counter['9_5']:<10} | {winning_combos_x2_counter['9_4']:<10} | {winning_combos_x2_counter['9_3']:<10} | {winning_combos_x2_counter['9_2']:<10}")
    print(f"\n Total {sum(winning_combos_x2_counter.values())}")
    print("\n")

winning_combos()
