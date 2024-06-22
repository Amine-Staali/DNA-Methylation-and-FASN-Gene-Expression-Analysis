def dna_to_bytes(dna_sequence):
    # Define mapping from nucleotides to binary representation
    nucleotide_to_binary = {
        'A': '00',
        'T': '01',
        'C': '10',
        'G': '11'
    }

    # Convert DNA sequence to binary string
    binary_string = ''
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_to_binary:
            binary_string += nucleotide_to_binary[nucleotide]
        else:
            # Log warning for invalid nucleotide and continue
            print(f"Warning: Invalid nucleotide '{nucleotide}' found. Skipping...")
            continue

    # Pad the binary string to ensure it's a multiple of 8
    padded_length = (len(binary_string) + 7) // 8 * 8  # Round up to the nearest multiple of 8
    binary_string = binary_string.ljust(padded_length, '0')

    # Convert binary string to bytes
    bytes_result = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_value = int(byte, 2)  # Convert binary string to integer
        bytes_result.append(byte_value)
    
    return bytes_result
