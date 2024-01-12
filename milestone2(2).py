import numpy as np
#defining the function to compute the coordinates and llcs
def compute_die_indices_and_llcs(wafer_diameter, die_size, reference_die):
    #die size
    die_size_x, die_size_y = die_size
    #reference die
    reference_die_x, reference_die_y = reference_die

    #number of dies in each direction
    num_dies_x = int(wafer_diameter / die_size_x)
    num_dies_y = int(wafer_diameter / die_size_y)

    die_indices = []
    die_llcs = []

    for i in range(-num_dies_x, num_dies_x + 1):
        for j in range(-num_dies_y, num_dies_y + 1):
            die_index_x = i
            die_index_y = j

            #  wafer coordinates
            die_position_x = i * die_size_x + reference_die_x
            die_position_y = j * die_size_y + reference_die_y

            # partially inside the wafer boundary
            if (
                -wafer_diameter / 2.0 <= die_position_x <= wafer_diameter / 2.0 and
                -wafer_diameter / 2.0 <= die_position_y <= wafer_diameter / 2.0
            ) or (
                abs(die_position_x) == wafer_diameter / 2.0 or
                abs(die_position_y) == wafer_diameter / 2.0
            ):
                # LLC
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
die_size = (2, 2)
reference_die = (-44, -66)
output_file_path = "die_information.txt"

die_indices, die_llcs = compute_die_indices_and_llcs(wafer_diameter, die_size, reference_die)

# Writing die information to a text file
write_die_information_to_file(output_file_path, die_indices, die_llcs)

print(f"Die information written to: {output_file_path}")
