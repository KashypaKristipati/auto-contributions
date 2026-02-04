# Educational Code Tutorial: Creative Story Generator with Simple AI

# Learning Objective:
# This tutorial teaches the fundamental concepts of text generation
# and how to build a simple AI-powered program that writes creative stories.
# We will focus on a basic Markov Chain approach to learn patterns in text
# and generate new text based on those patterns.

import random

class SimpleStoryGenerator:
    """
    A simple text generator that uses a Markov Chain model to create stories.
    A Markov Chain predicts the next word based on the current word(s).
    This is a fundamental concept in many text generation AI models.
    """

    def __init__(self, text_corpus):
        """
        Initializes the generator with a corpus of text.

        Args:
            text_corpus (str): A string containing the text to train the model on.
                               This text will be used to learn word sequences.
        """
        # The training data. We need a good amount of text to find meaningful patterns.
        self.text_corpus = text_corpus.lower() # Convert to lowercase for consistent matching.
        # This dictionary will store our Markov Chain.
        # Keys are words (or tuples of words for longer chains),
        # and values are lists of words that can follow them.
        self.model = {}
        # We'll store the starting words here to begin our stories.
        self.starters = []
        # Build the model when the generator is created.
        self._build_model()

    def _build_model(self):
        """
        Builds the Markov Chain model from the provided text corpus.
        It splits the text into words and creates connections between them.
        """
        # Split the corpus into a list of words.
        # We're using a simple split by whitespace for now.
        words = self.text_corpus.split()

        # Iterate through the words to build the model.
        # We go up to the second-to-last word because we need a "current" word
        # and a "next" word to form a transition.
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i+1]

            # If the current word is not yet in our model, add it as a new entry.
            if current_word not in self.model:
                self.model[current_word] = []

            # Add the next word to the list of possible words that can follow the current word.
            self.model[current_word].append(next_word)

            # Also, identify potential starting words for our stories.
            # We'll consider words that appear at the beginning of sentences (after punctuation)
            # or simply any word that has a successor. For simplicity here, we'll just
            # add any word that has a successor as a potential starter.
            # A more advanced approach would look for sentence start indicators.
            if i == 0 or words[i-1].endswith(('.', '!', '?')): # Simple sentence start detection
                self.starters.append(current_word)

        # Ensure there are always some starters, even if no clear sentence starts are found.
        if not self.starters and words:
            self.starters.append(words[0])

    def generate_story(self, length=50, start_word=None):
        """
        Generates a creative story using the trained Markov Chain model.

        Args:
            length (int): The desired number of words in the story.
            start_word (str, optional): A specific word to start the story with.
                                        If None, a random starting word will be chosen.

        Returns:
            str: The generated story.
        """
        # If no starting word is provided, pick a random one from our identified starters.
        if start_word is None or start_word not in self.model:
            if not self.starters:
                return "Error: No valid starting words found in the corpus."
            current_word = random.choice(self.starters)
        else:
            current_word = start_word.lower()
            if current_word not in self.model:
                return f"Error: '{start_word}' is not a known word in the corpus to start from."

        # Initialize the story with the starting word.
        story = [current_word]

        # Generate the rest of the story word by word.
        for _ in range(length - 1):
            # Check if the current word exists in our model.
            # If it doesn't, it means we've reached a word that has no known successors.
            # We stop generating to avoid errors.
            if current_word not in self.model:
                break

            # Get the list of possible next words for the current word.
            possible_next_words = self.model[current_word]

            # If there are no possible next words (shouldn't happen if current_word is in model,
            # but good for robustness), break.
            if not possible_next_words:
                break

            # Randomly choose the next word from the list of possibilities.
            next_word = random.choice(possible_next_words)

            # Add the chosen next word to our story.
            story.append(next_word)

            # Update the current word to the word we just added, for the next iteration.
            current_word = next_word

        # Join the list of words into a single string to form the complete story.
        return " ".join(story)

# --- Example Usage ---

# A sample text corpus. The more text you provide, the more interesting the stories will be.
# Think of this as the "brain" of your AI story writer.
sample_corpus = """
The old wizard lived in a towering castle on a lonely hill.
He had a long white beard that reached his knees.
One day, a young adventurer named Elara arrived at the castle gates.
Elara was seeking a legendary artifact, a gem said to grant immense power.
The wizard, wise and kind, agreed to help her.
Together, they embarked on a perilous journey through enchanted forests and treacherous mountains.
They faced mythical beasts and solved ancient riddles.
Finally, they found the gem hidden within a dragon's lair.
With the gem in hand, Elara and the wizard returned to the castle, their adventure a success.
The wizard smiled, knowing peace had returned to the land.
"""

# Create an instance of our story generator.
# This trains the model based on the sample_corpus.
story_writer = SimpleStoryGenerator(sample_corpus)

print("--- Generating a random story ---")
# Generate a story with a default length of 50 words.
random_story = story_writer.generate_story()
print(random_story)
print("\n" + "="*30 + "\n") # Separator for clarity

print("--- Generating a story starting with 'Elara' ---")
# Generate a story that must start with the word "Elara".
# If "Elara" is not in the corpus or has no successors, it will show an error.
story_starting_with_elara = story_writer.generate_story(start_word="Elara")
print(story_starting_with_elara)
print("\n" + "="*30 + "\n")

print("--- Generating a shorter story ---")
# Generate a shorter story, say 20 words.
short_story = story_writer.generate_story(length=20)
print(short_story)
print("\n" + "="*30 + "\n")

print("--- Attempting to start with an unknown word ---")
# Demonstrate what happens if we try to start with a word not in the corpus.
invalid_start_story = story_writer.generate_story(start_word="dragonfly")
print(invalid_start_story)