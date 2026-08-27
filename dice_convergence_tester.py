import random
import math

def run_dice_simulation(num_dice, dice_sides, total_rolls):
    print(f"DICE SIMULATION ENGINE")
    print(f"Configuration: Rolling {num_dice} x {dice_sides}-sided dice")
    print(f"Total Iterations: {total_rolls:,}\n")
    
    # Theoretical mean & variance for a single fair die
    single_mean = (dice_sides + 1) / 2
    single_variance = (dice_sides ** 2 - 1) / 12
    
    # Combined theoretical metrics for n dice
    theoretical_mean = num_dice * single_mean
    theoretical_variance = num_dice * single_variance
    theoretical_std_dev = math.sqrt(theoretical_variance)
    
    # Dictionary to keep track of how many times each sum occurs
    results_frequency = {}
    total_sum_of_all_rolls = 0
    
    # Run the simulation loop
    for i in range(total_rolls):
        roll_sum = 0

        # Generate random outcomes for the given number of dice
        for j in range(num_dice):
            roll_sum += random.randint(1, dice_sides)
        
        # Log frequency of the sum
        results_frequency[roll_sum] = results_frequency.get(roll_sum, 0) + 1
        total_sum_of_all_rolls += roll_sum

    # SAMPLE STATS CALCULATION
    # Sample Mean
    sample_mean = total_sum_of_all_rolls / total_rolls
    
    # Sample Variance (Average of squared deviations from the mean)
    squared_deviations_sum = 0
    for outcome, frequency in results_frequency.items():
        deviation = outcome - sample_mean
        squared_deviations_sum += frequency * deviation ** 2
        
    sample_variance = squared_deviations_sum / total_rolls
    sample_std_dev = math.sqrt(sample_variance)

    # CONVERGENCE REPORT TABLE
    print(f"Statistical Convergence Report")
    print(f"{'Metric':<20} | {'Theoretical':<15} | {'Sample':<15} | {'Delta (Error)':<15}")
    print("-" * 74)
    print(f"{'Expected Mean':<20} | {theoretical_mean:<15.4f} | {sample_mean:<15.4f} | {abs(theoretical_mean - sample_mean):<15.6f}")
    print(f"{'Variance':<20} | {theoretical_variance:<15.4f} | {sample_variance:<15.4f} | {abs(theoretical_variance - sample_variance):<15.6f}")
    print(f"{'Standard Deviation':<20} | {theoretical_std_dev:<15.4f} | {sample_std_dev:<15.4f} | {abs(theoretical_std_dev - sample_std_dev):<15.6f}")
    
    # SAMPLE FREQUENCY DISTRIBUTION (to show the bell curve / distribution)
    print("\nSample Distribution (Simulated Hit Frequencies)")
    min_possible = num_dice
    max_possible = num_dice * dice_sides
    
    # Show results for a snapshot of outcomes to keep print clean
    for outcome in range(min_possible, max_possible + 1):
        count = results_frequency.get(outcome, 0)
        percentage = (count / total_rolls) * 100

        # Draw a basic visual text bar to show the distribution curve shape
        bar = "]" * int(percentage * 2) 
        print(f"Sum {outcome:<3}: {percentage:>5.2f}% {bar}")

# Run simulation: 3 standard 6-sided dice, rolled 1 million times
run_dice_simulation(num_dice=3, dice_sides=6, total_rolls=1000000)