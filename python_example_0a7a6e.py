# Learning Objective: Understand and implement Least Significant Bit (LSB) steganography
# to hide and extract a secret text message within an uncompressed WAV audio file.
# This tutorial will demonstrate how to manipulate the least significant bit of each
# byte in audio data to embed information, a fundamental concept in digital steganography.

import wave # Python's standard library for reading and writing WAV files
import struct # For converting between Python values and C structs (byte packing/unpacking)

# --- Helper Functions for Binary Conversion ---

def text_to_binary(text: str) -> str:
    """
    Converts a string of text into its binary representation.

    Args:
        text (str): The input string message.

    Returns:
        str: A binary string where each character's ASCII value is converted to
             an 8-bit binary string, concatenated together.
             Example: "A" -> "01000001"
    """
    # We first encode the text into bytes using UTF-8, which is a common and flexible encoding.
    # Then, for each byte, we convert it to its 8-bit binary string representation.
    # The '08b' format specifier ensures that each binary string is padded with leading zeros
    # to exactly 8 bits (e.g., 1 becomes '00000001').
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))

def binary_to_text(binary_string: str) -> str:
    """
    Converts a binary string back into readable text.

    Args:
        binary_string (str): The input binary string, assumed to be composed of 8-bit chunks.

    Returns:
        str: The decoded text string. Returns an empty string if conversion fails or input is malformed.
    """
    # We iterate through the binary string in chunks of 8 bits.
    # Each 8-bit chunk represents a byte.
    byte_list = []
    for i in range(0, len(binary_string), 8):
        byte_chunk = binary_string[i:i+8]
        if len(byte_chunk) == 8: # Ensure we have a full 8-bit byte
            # Convert the 8-bit binary string to an integer.
            # Then convert that integer to a byte using `bytes([integer_value])`.
            byte_list.append(int(byte_chunk, 2))
    
    # Finally, decode the list of byte integers back into a string using UTF-8.
    # We use a try-except block to handle potential decoding errors,
    # which can happen if the extracted binary data doesn't form valid UTF-8 characters.
    try:
        return bytes(byte_list).decode('utf-8')
    except UnicodeDecodeError:
        print("Warning: Could not fully decode binary to text (possibly incomplete or corrupt message).")
        return "" # Return empty string on error

# --- Core Steganography Functions ---

def encode_message_in_audio(audio_path: str, message: str, output_path: str):
    """
    Hides a secret message within the least significant bits (LSBs) of an audio file.

    Args:
        audio_path (str): Path to the original WAV audio file.
        message (str): The secret message to hide.
        output_path (str): Path where the new stego audio file will be saved.
    """
    print(f"--- Encoding message into {audio_path} ---")

    # 1. Open the original audio file to read its properties and data.
    # Using 'with' ensures the file is properly closed even if errors occur.
    with wave.open(audio_path, 'rb') as audio_file:
        nframes = audio_file.getnframes() # Number of audio frames
        framerate = audio_file.getframerate() # Sample rate (frames per second)
        sampwidth = audio_file.getsampwidth() # Sample width in bytes (e.g., 1 for 8-bit, 2 for 16-bit)
        nchannels = audio_file.getnchannels() # Number of audio channels (e.g., 1 for mono, 2 for stereo)

        # Read all audio frames as a bytes object.
        # This will contain raw audio data, where each frame consists of (sampwidth * nchannels) bytes.
        original_frames = audio_file.readframes(nframes)

    # 2. Convert the secret message into a binary string.
    # We append a unique terminator sequence to the binary message.
    # This terminator is crucial for the decoder to know where the hidden message ends.
    # We use "0000000000000000" (two null bytes) as a simple terminator.
    binary_message = text_to_binary(message) + "0000000000000000" # Terminator: two null characters

    # Calculate how many LSBs are needed to store the message.
    # Each LSB can hold one bit of the message.
    required_lsbs = len(binary_message)

    # Calculate the total number of LSBs available in the audio file.
    # Each byte in 'original_frames' provides one LSB for hiding data.
    available_lsbs = len(original_frames) * 8 # In bits, not bytes. But we use each byte's LSB.

    print(f"Message length (bits): {required_lsbs}")
    print(f"Available LSBs in audio (bits): {len(original_frames)}") # Each byte has 1 LSB

    # Check if the message can fit into the audio file.
    if required_lsbs > len(original_frames):
        print("Error: Message is too long to hide in this audio file.")
        print(f"Needed LSBs: {required_lsbs}, Available LSBs (bytes): {len(original_frames)}")
        return

    # 3. Create a mutable bytearray to store the modified audio data.
    # 'bytearray' is used because 'bytes' objects are immutable, and we need to change individual bytes.
    modified_frames = bytearray(original_frames)

    # 4. Iterate through the audio data and embed the message bits.
    # We're iterating through each byte of the audio data.
    for i in range(len(binary_message)):
        # Get the current bit from our secret message.
        # 'int(binary_message[i])' converts '0' or '1' character to integer 0 or 1.
        message_bit = int(binary_message[i])

        # Get the current byte from the audio data.
        audio_byte = modified_frames[i]

        # Clear the least significant bit (LSB) of the audio byte.
        # Performing a bitwise AND with `0b11111110` (or 0xFE) sets the LSB to 0,
        # while keeping all other bits unchanged.
        audio_byte_cleared_lsb = audio_byte & 0b11111110

        # Set the LSB of the audio byte with the message bit.
        # Performing a bitwise OR with the 'message_bit' (0 or 1) effectively
        # replaces the cleared LSB with our secret message bit.
        modified_frames[i] = audio_byte_cleared_lsb | message_bit

    print(f"Message successfully embedded into {len(binary_message)} LSBs.")

    # 5. Save the modified audio data to a new WAV file.
    with wave.open(output_path, 'wb') as output_audio_file:
        output_audio_file.setnchannels(nchannels)
        output_audio_file.setsampwidth(sampwidth)
        output_audio_file.setframerate(framerate)
        output_audio_file.writeframes(modified_frames) # Write the modified bytearray (converted to bytes)

    print(f"Stego audio saved to {output_path}")

def decode_message_from_audio(stego_audio_path: str) -> str:
    """
    Extracts a hidden message from the LSBs of a stego audio file.

    Args:
        stego_audio_path (str): Path to the WAV audio file containing the hidden message.

    Returns:
        str: The extracted secret message.
    """
    print(f"--- Decoding message from {stego_audio_path} ---")

    # 1. Open the stego audio file to read its data.
    with wave.open(stego_audio_path, 'rb') as stego_audio_file:
        nframes = stego_audio_file.getnframes()
        # Read all audio frames.
        stego_frames = stego_audio_file.readframes(nframes)

    extracted_binary_message = []
    # Define the terminator sequence used during encoding.
    # This must exactly match the terminator appended in `encode_message_in_audio`.
    TERMINATOR = "0000000000000000" # Binary representation of two null characters

    # 2. Iterate through each byte of the audio data to extract LSBs.
    # We iterate up to the total number of bytes available.
    for i in range(len(stego_frames)):
        # Extract the current byte.
        audio_byte = stego_frames[i]

        # Get the least significant bit (LSB) of the audio byte.
        # Performing a bitwise AND with `0b00000001` (or 0x01) isolates the LSB.
        # This will result in 0 or 1, which is our hidden message bit.
        extracted_bit = audio_byte & 0b00000001

        # Append the extracted bit (as a string '0' or '1') to our list.
        extracted_binary_message.append(str(extracted_bit))

        # Check if we have extracted enough bits to potentially form the terminator.
        # This prevents unnecessary iterations once the message is found.
        if len(extracted_binary_message) >= len(TERMINATOR):
            # Join the last `len(TERMINATOR)` bits and compare with the terminator.
            # If the terminator is found, it means we have extracted the full message.
            if "".join(extracted_binary_message[-len(TERMINATOR):]) == TERMINATOR:
                # Remove the terminator from the extracted binary message before converting to text.
                extracted_binary_message = extracted_binary_message[:-len(TERMINATOR)]
                break # Stop decoding as the message end has been reached.

    # 3. Join the list of binary characters into a single binary string.
    final_binary_string = "".join(extracted_binary_message)

    # 4. Convert the binary string back to human-readable text.
    decoded_message = binary_to_text(final_binary_string)

    print(f"Message successfully extracted. Length: {len(decoded_message)} characters.")
    print(f"Decoded Message: '{decoded_message}'")
    return decoded_message


# --- Example Usage ---

if __name__ == "__main__":
    # To run this example:
    # 1. Make sure you have a .wav audio file in the same directory, e.g., 'input_audio.wav'.
    #    You can use any uncompressed WAV file. For best results, use a file with 16-bit
    #    samples or higher, as 8-bit samples can be more noticeably affected by LSB changes.
    # 2. Replace 'input_audio.wav' with the actual name of your audio file.
    # 3. Choose a secret message.
    # 4. Run the script!

    input_audio_file = 'input_audio.wav' # IMPORTANT: Change this to your WAV file!
    output_stego_file = 'stego_audio.wav'
    secret_message = "Hello, this is a very secret message hidden inside the audio file using LSB steganography! Can you find me? This is a test message to ensure we have enough data to fill the audio frames."

    # Step 1: Encode the message
    # This will create a new WAV file ('stego_audio.wav') with the message embedded.
    encode_message_in_audio(input_audio_file, secret_message, output_stego_file)

    print("\n" + "="*50 + "\n")

    # Step 2: Decode the message
    # This will read the 'stego_audio.wav' file and attempt to extract the message.
    extracted_secret = decode_message_from_audio(output_stego_file)

    print("\n" + "="*50 + "\n")

    # Step 3: Verify the extracted message
    if extracted_secret == secret_message:
        print("Verification Successful: The extracted message matches the original secret message!")
    else:
        print("Verification Failed: The extracted message DOES NOT match the original secret message.")
        print(f"Original: '{secret_message}'")
        print(f"Extracted: '{extracted_secret}'")

    print("\n--- Tutorial Complete ---")
    print("You've learned to hide and extract messages using LSB steganography in audio!")
    print("Listen to 'stego_audio.wav' - can you hear the difference?")
    print("Note: The quality of LSB steganography depends on the audio sample width.")
    print("16-bit audio provides more 'room' for changes than 8-bit without noticeable distortion.")
    print("For very long messages, the audio file needs to be proportionally long too.")