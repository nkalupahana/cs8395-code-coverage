def ex6(str1, str2):
    # Create a new string by combining the two string arguments
    combined_str = str1 + str2
    
    # Check if the combined string is longer than 10 characters
    if len(combined_str) > 10:
        # If it is longer than 10 characters, reverse the combined string
        reversed_str = combined_str[::-1]
    else:
        # If it is not longer than 10 characters, make the combined string all uppercase
        reversed_str = combined_str.upper()
        
    # Return the final result
    return reversed_str