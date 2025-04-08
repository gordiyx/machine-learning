from collections import Counter
import heapq
import math

# Represents a node in the Huffman tree
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char      # Character stored in the node (only for leaves)
        self.freq = freq      # Frequency of the character(s)
        self.left = None      # Left child
        self.right = None     # Right child

    # Enables priority queue to compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq


# Builds the Huffman tree based on character frequencies
def build_huffman_tree(frequency_dict):
    # Initialize a priority queue (min-heap) with all characters as leaf nodes
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_dict.items()]
    heapq.heapify(priority_queue)

    # Combine the two least frequent nodes until only the root remains
    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(freq=node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]  # Return the root of the Huffman tree


# Recursively generates Huffman codes from the tree
def generate_codes(node, current_code='', codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code  # Leaf node: store the code

    generate_codes(node.left, current_code + '0', codes)
    generate_codes(node.right, current_code + '1', codes)

    return codes


# Encodes the input text using the generated Huffman codes
def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)


# Calculates the total length (in bits) of the encoded message
def calculate_encoded_length(huffman_codes, frequency):
    encoded_length = 0
    for char, freq in frequency.items():
        encoded_length += len(huffman_codes[char]) * freq
    return encoded_length


# Calculates the theoretical entropy of the message
def calculate_theoretical_minimum(frequency, total_chars):
    entropy = 0
    for freq in frequency.values():
        prob = freq / total_chars
        entropy += prob * math.log2(1 / prob)
    return entropy * total_chars


# Main function: combines all steps of Huffman coding
def huffman_coding(text):
    # Step 1: Count character frequencies
    frequency = Counter(text)

    # Step 2: Build the Huffman tree
    huffman_tree = build_huffman_tree(frequency)

    # Step 3: Generate Huffman codes for each character
    huffman_codes = generate_codes(huffman_tree)

    # Step 4: Encode the original text
    encoded_text = huffman_encode(text, huffman_codes)

    return encoded_text, huffman_codes, frequency


# Example usage
text = "ffdehhhe hdhehhe"

# Run Huffman coding
encoded_text, codes, frequency = huffman_coding(text)

# Compute encoded length and entropy
encoded_length = calculate_encoded_length(codes, frequency)
theoretical_minimum = calculate_theoretical_minimum(frequency, len(text))

# Output results
print("Original text:", text)
print("Encoded text:", encoded_text)
print("Huffman codes for each character:", codes)
print(f"Encoded text length: {encoded_length} bits")
print(f"Theoretical minimum (entropy): {theoretical_minimum:.2f} bits")

# Check if Huffman encoding is near optimal
if theoretical_minimum <= encoded_length <= theoretical_minimum + 1:
    print("Huffman code is optimal.")
else:
    print("Huffman code is not optimal.")
