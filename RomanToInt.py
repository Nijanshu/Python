
def RomanToInt(roman):
    
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    # Iterate through the Roman numeral from right to left
    for char in reversed(roman):
        current_value = roman_values[char]
        print(current_value)
        
        # If the current value is less than the previous one, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add it to the total
            total += current_value
            
        prev_value = current_value
    
    print( total)

RomanToInt('XLIX')
