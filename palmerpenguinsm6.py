# PalmerPenguinsM6.py
# Devin Dollard
# 10/11/2026
# Use functions to organize Palmer Penguin analysis

import math

# Constants for the penguin species
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"

NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151

species_names = [
    SP_CHINSTRAP,
    SP_GENTOO,
    SP_ADELIE
]

species_counts = [
    NUM_CHINSTRAP,
    NUM_GENTOO,
    NUM_ADELIE
]


def calculate_percentage(count, total):
    return count / total * 100


def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent < 40:
        return "medium"
    else:
        return "large"


def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"


def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(f"{species}: {counts[index]} ({percentages[index]:.2f}%)")


def main():
    # Calculations
    total_species = len(species_names)
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)

    chinstrap_percent = calculate_percentage(species_counts[0], total_penguins)
    gentoo_percent = calculate_percentage(species_counts[1], total_penguins)
    adelie_percent = calculate_percentage(species_counts[2], total_penguins)

    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent
    ]

    largest_count = max(species_counts)
    largest_index = species_counts.index(largest_count)
    largest_species = species_names[largest_index]
    smallest_count = min(species_counts)
    smallest_index = species_counts.index(smallest_count)
    smallest_species = species_names[smallest_index]

    # Print the formatted output
    print("Introducing the Palmer Penguins:")
    print(f"\t{SP_CHINSTRAP}!")
    print(f"\t{SP_GENTOO}!")
    print("and last but not least...")
    print(f"\t{SP_ADELIE}!")
    print(
        f"There are a total of {total_species} penguin species in this dataset.")

    print(f"There are a total of {total_penguins} penguins in the dataset.")
    print(
        f"The average number of penguins per species is {average_penguins:.1f}.")
    print(f"The average rounded up is {average_penguins_rounded_up}.")

    display_species_statistics(
        species_names, species_counts, species_percentages)

    print(
        f"The species with the most observations is {largest_species} with {largest_count} penguins.")
    print(
        f"The species with the fewest observations is {smallest_species} with {smallest_count} penguins.")

    # Add a counter for valid species selections
    valid_selections = 0

    # Ask user for species
    print("\nExplore a species:")
    species_choice = input("Enter Chinstrap, Gentoo, Adelie, or Done: ")

    while species_choice != "Done":
        if species_choice not in species_names:
            print(f"{species_choice} is not one of the species in this dataset.")
        else:
            valid_selections += 1

            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            # Retrieve the Selected Species Data
            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # Classify the Species by Its Percentage
            size_category = classify_species(selected_percent)

            # Determine the Species' Relative Position
            position_description = get_position_description(
                selected_species, largest_species, smallest_species)

            # Compare the Selected Count to the Average
            average_position = "above" if selected_count > average_penguins else "below"

            # Display the Selected Species Statistics
            print(f"\n{selected_species} has {selected_count} observations, "
                  f"representing {selected_percent:.2f}% of the dataset.")
            print(
                f"{selected_species} is classified as a {size_category} species group.")
            print(f"{selected_species} is the {position_description} species group.")
            print(f"Its observation count is {average_position} the dataset average of "
                  f"{average_penguins:.1f}.")

        species_choice = input("\nEnter Chinstrap, Gentoo, Adelie, or Done: ")

    print(f"You explored {valid_selections} valid species selections.")


if __name__ == "__main__":
    main()
