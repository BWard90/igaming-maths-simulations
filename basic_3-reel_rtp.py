import random

def run_slot_sim(num_spins):
    print(f'SIMULATION: {num_spins} spins of 3-Reel Single-Line slot machine')

    # Defining reels to be similar to on an actual machine.
    # Here, "blank" is very common, "cherry" and "lemon" are moderate in frequency, and "jackpot" is very rare.
    reel_1 = ["blank", "blank", "blank", "cherry", "cherry", "lemon", "lemon", "jackpot"]
    reel_2 = ["blank", "blank", "blank", "blank", "cherry", "cherry", "lemon", "jackpot"]
    reel_3 = ["blank", "blank", "blank", "blank", "blank", "cherry", "lemon", "jackpot"]

    total_combinations = len(reel_1) * len(reel_2) * len(reel_3)
    print(f'Total number of possible combinations: {total_combinations}')

    # Dictionary with key value pairs to show payout structure
    paytable = {
        ("jackpot", "jackpot", "jackpot"): 50, # Top prize, pays 50x bet
        ("lemon", "lemon", "lemon"): 10, # Pays 10x bet
        ("cherry", "cherry", "cherry"): 8, # Pays 8x bet
    }

    # Other rules:
    # Three mixed fruit to pay 5x bet
    # Any two fruits to pay 1x bet

    total_payout = 0
    winning_spin_counter = 0

    win_type_counter = {"jackpot": 0, "lemon": 0, "cherry": 0, "3_fruits": 0, "2_fruits": 0}

    for i in range(num_spins):
        symbol_1 = random.choice(reel_1)
        symbol_2 = random.choice(reel_2)
        symbol_3 = random.choice(reel_3)

        spin_outcome = (symbol_1, symbol_2, symbol_3)

        if spin_outcome in paytable:
            total_payout += paytable[spin_outcome]
            winning_spin_counter += 1
            win_type_counter[symbol_1] += 1

        elif spin_outcome.count("cherry") + spin_outcome.count("lemon") == 3:
            total_payout += 5
            winning_spin_counter += 1
            win_type_counter["3_fruits"] += 1

        elif spin_outcome.count("cherry") + spin_outcome.count("lemon") == 2:
            total_payout += 1
            winning_spin_counter += 1
            win_type_counter["2_fruits"] += 1

    # For purposes of simulation, 1 spin has a value of 1
    rtp = round((total_payout / num_spins) * 100, 2)
    hit_frequency = round((winning_spin_counter / num_spins) * 100, 2)

    # Calculating expected values for comparison
    jackpot_combos = 1 * 1 * 1
    lemon_combos = 2 * 1 * 1
    cherry_combos = 2 * 2 * 1
    mixed_fruit_3_combos = 4 * 3 * 2 - lemon_combos - cherry_combos
    mixed_fruit_2_combos = (4 * 3 * 6) + (4 * 5 * 2) + (4 * 3 * 2) # sums of combinations of pairs -> first two, outer two, last two
    total_winning_combos = jackpot_combos + lemon_combos + cherry_combos + mixed_fruit_3_combos + mixed_fruit_2_combos
    total_losing_combos = total_combinations - total_winning_combos
    ave_prize = (jackpot_combos * 50 + lemon_combos * 10 + cherry_combos * 8 + mixed_fruit_3_combos * 5 + mixed_fruit_2_combos * 1) / total_winning_combos
    exp_value_per_spin = (jackpot_combos * 50 + lemon_combos * 10 + cherry_combos * 8 + mixed_fruit_3_combos * 5 + mixed_fruit_2_combos * 1 + total_losing_combos * (-1)) / total_combinations

    exp_jackpot_freq = jackpot_combos / total_combinations * num_spins
    exp_lemon_freq = lemon_combos / total_combinations * num_spins
    exp_cherry_freq = cherry_combos / total_combinations * num_spins
    exp_3_fruits_freq = mixed_fruit_3_combos / total_combinations * num_spins
    exp_2_fruits_freq = mixed_fruit_2_combos / total_combinations * num_spins

    exp_rtp = round(ave_prize * total_winning_combos / total_combinations * 100, 2)
    exp_hit_freq = round(total_winning_combos / total_combinations * 100, 2)

    # Data output
    print(f'\n Summary data')
    print(f'Total invested: {num_spins}')
    print(f'Total paid out: {total_payout}')
    print(f'RTP: {rtp}')
    print(f'Hit frequency: {hit_frequency}')

    print(f'\n Outcomes from simulation')
    print(f'3x "jackpot": {win_type_counter["jackpot"]}')
    print(f'3x "lemon": {win_type_counter["lemon"]}')
    print(f'3x "cherry": {win_type_counter["cherry"]}')
    print(f'3x fruit: {win_type_counter["3_fruits"]}')
    print(f'2x fruit: {win_type_counter["2_fruits"]}')

    print('\n Expected outcomes')
    print(f'Expected value per spin: {exp_value_per_spin}')
    print(f'Expected RTP: {exp_rtp}')
    print(f'Expected hit frequency: {exp_hit_freq}')  
    print(f'Expected 3x "jackpot": {exp_jackpot_freq}')
    print(f'Expected 3x "lemon": {exp_lemon_freq}')
    print(f'Expected 3x "cherry": {exp_cherry_freq}')
    print(f'Expected 3x fruit: {exp_3_fruits_freq}')
    print(f'Expected 2x fruit: {exp_2_fruits_freq}')

run_slot_sim(1000000)