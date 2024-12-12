def f(array):
    valid_count = 0  # Counter for valid usernames
    
    for name in array:
        # Check length constraint
        if not (4 <= len(name) <= 12):
            continue

        # Initialize flags
        has_lowercase = False
        has_number = False
        has_underscore = False

        # Check each character
        for char in name:
            if char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_number = True
            elif char == "_":
                has_underscore = True

        # If all conditions are met, increment the counter
        if has_lowercase and has_number and has_underscore:
            valid_count += 1

    return valid_count

# Example usage
print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))  # Output: 2

        