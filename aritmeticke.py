from decimal import Decimal, getcontext  # High-precision arithmetic
from collections import Counter          # Efficient frequency counting

# Set high precision for Decimal calculations to avoid rounding errors
getcontext().prec = 10


def calculate_probabilities(data):
    """
    Calculates symbol probabilities and assigns each symbol a cumulative probability interval [0, 1).
    
    Args:
        data (str): Input string to analyze.

    Returns:
        dict: Mapping of each symbol to its (low, high) interval.
    """
    frequency = Counter(data)
    total = len(data)
    probabilities = {}
    cumulative = Decimal(0)

    for symbol in sorted(frequency.keys()):
        probability = Decimal(frequency[symbol]) / Decimal(total)
        probabilities[symbol] = (cumulative, cumulative + probability)
        cumulative += probability

    return probabilities


def arithmetic_encoding(data, probabilities):
    """
    Encodes the input string into a single decimal value using arithmetic coding.

    Args:
        data (str): Input string to encode.
        probabilities (dict): Symbol intervals as (low, high) from `calculate_probabilities`.

    Returns:
        tuple: (encoded_value, low, high) — any value in this interval represents the input.
    """
    low = Decimal(0)
    high = Decimal(1)

    for symbol in data:
        range_width = high - low
        symbol_low, symbol_high = probabilities[symbol]
        low = low + range_width * symbol_low
        high = low + range_width * (symbol_high - symbol_low)

    # Return the midpoint of the final interval as the encoded value
    encoded_value = (low + high) / 2
    return encoded_value, low, high


def arithmetic_decoding(encoded_value, data_length, probabilities):
    """
    Decodes the encoded decimal value back into the original string.

    Args:
        encoded_value (Decimal): Encoded value to decode.
        data_length (int): Length of the original string.
        probabilities (dict): Symbol intervals used for encoding.

    Returns:
        str: The decoded string.
    """
    low = Decimal(0)
    high = Decimal(1)
    decoded_output = []

    for _ in range(data_length):
        range_width = high - low
        target = (encoded_value - low) / range_width

        # Find the symbol whose interval contains the target value
        for symbol, (symbol_low, symbol_high) in probabilities.items():
            if symbol_low <= target < symbol_high:
                decoded_output.append(symbol)
                low = low + range_width * symbol_low
                high = low + range_width * (symbol_high - symbol_low)
                break

    return ''.join(decoded_output)


# Example usage
data = "barbara"

# Step 1: Calculate symbol probabilities and intervals
probabilities = calculate_probabilities(data)

# Step 2: Encode the string
encoded_value, low, high = arithmetic_encoding(data, probabilities)

# Step 3: Decode the encoded value
decoded_data = arithmetic_decoding(encoded_value, len(data), probabilities)

# Output results
print("Original data:", data)
print("Encoded value:", encoded_value)
print("Interval for encoded value:", (low, high))
print("Decoded data:", decoded_data)

# Sanity check
assert decoded_data == data, "Decoding failed!"
print("Decoding successful.")
