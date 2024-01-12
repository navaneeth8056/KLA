import numpy as np

def is_die_inside_wafer(die_position_x, die_position_y, wafer_diameter):
    distance_from_center = np.sqrt(die_position_x**2 + die_position_y**2)
    return distance_from_center <= wafer_diameter / 2.0 + max(abs(die_position_x), abs(die_position_y))

def compute_die_indices_and_llcs(wafer_diameter, die_size, reference_die, die_shift_vector, dies_per_reticle, die_street_width_height, reticle_street_width_height):
    die_size_x, die_size_y = die_size
    reference_die_x, reference_die_y = reference_die
    die_shift_vector_x, die_shift_vector_y = die_shift_vector
    dies_per_reticle_rows, dies_per_reticle_columns = map(int, dies_per_reticle.split('x'))
    die_street_width, die_street_height = die_street_width_height
    reticle_street_width, reticle_street_height = reticle_street_width_height
    num_dies_x = dies_per_reticle_rows * 2 - 1
    num_dies_y = dies_per_reticle_columns * 2 - 1

    # Initialize lists to store die indices and LLCs
    die_indices = []
    die_llcs = []

    for i in range(-num_dies_x, num_dies_x + 1):
        for j in range(-num_dies_y, num_dies_y + 1):
            die_index_x = i
            die_index_y = j

            # Calculating die position in wafer coordinates with die shift vector
            die_position_x = i * (die_size_x + die_street_width) + reference_die_x + die_shift_vector_x
            die_position_y = j * (die_size_y + die_street_height) + reference_die_y + die_shift_vector_y

            # Checking if the die is inside or partially inside the wafer boundary
            if is_die_inside_wafer(die_position_x, die_position_y, wafer_diameter):
                # Calculate LLC of the die
                llc_x = die_position_x - die_size_x / 2.0
                llc_y = die_position_y - die_size_y / 2.0

                die_indices.append((die_index_x, die_index_y))
                die_llcs.append((llc_x, llc_y))

    return die_indices, die_llcs

def write_die_information_to_file(output_file_path, die_indices, die_llcs):
    with open(output_file_path, 'w') as file:
        for index, llc in zip(die_indices, die_llcs):
            file.write(f"{index}:{llc}\n")


wafer_diameter = 300
die_size = (5, 5)
reference_die = (43.1, 24.9)
die_shift_vector = (27, 39)
dies_per_reticle = "4x6"
die_street_width_height = (1.8, 1.2)
reticle_street_width_height = (3.2, 4.2)
output_file_path = "die_information_asymmetric.txt"

die_indices, die_llcs = compute_die_indices_and_llcs(wafer_diameter, die_size, reference_die, die_shift_vector, dies_per_reticle, die_street_width_height, reticle_street_width_height)

write_die_information_to_file(output_file_path, die_indices, die_llcs)

print(f"Die information written to: {output_file_path}")

#approach to find the llcs of all the dies and sorting it based on the wafer diameter