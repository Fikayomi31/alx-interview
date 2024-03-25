#!/usr/bin/python3
""" Method that determines if a given data set
represents a valid UTF-8 encoding
"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Mask to check if a byte is a valid continuation byte
    mask1 = 1 << 7
    mask2 = 1 << 6
    
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
            
            # Invalid UTF-8 start byte
            if num_bytes == 0:
                continue
            
            # A single UTF-8 character can be at most 4 bytes
            if num_bytes > 4 or num_bytes == 1:
                return False
            
        else:
            # Check if the byte is a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        num_bytes -= 1
    
    # If all bytes are processed and no incomplete character is left
    return num_bytes == 0

# Example usage:
data = [197, 130, 1]  # Represents the UTF-8 encoding for 'ç'
print(validUTF8(data))  # Output: True

