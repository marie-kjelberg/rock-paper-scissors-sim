from scipy.stats import chisquare

# all data files
data_files = ["./output100000.txt", "./output1000000.txt", "output10000000.txt"]
#["output.txt"]#


observed = [0, 0, 0] # [rock, paper, scissors]
expected = [0, 0, 0]
total = 0

list_indices = {"rock": 0, "paper": 1, "scissors": 2}

# read the all the results
# should probably use something faster idk
for file in data_files:
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            if not line in list_indices:
                continue
            observed[list_indices[line]] += 1 
            total += 1

for i in range(3):
    expected[i] = total / 3

chi2_stat, p = chisquare(observed, f_exp=expected)
percentages = [(o - expected[i]) / expected[i] * 100 for i, o in enumerate(observed)]

print(f"\nTotal entries: {total}")
print("List order: [rock, paper, scissors]")
print(f"Expected: {expected} \t Observed: {observed}")
print(f"Percentage deviations: {percentages}")
print(f"Chi2: {chi2_stat}, p-value: {p}\n")