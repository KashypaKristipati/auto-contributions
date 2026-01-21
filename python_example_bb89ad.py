# Learning Objective:
# This tutorial will teach you how to build a simple text-based adventure game
# in Python. We will focus on handling user input to create branching narratives,
# where the player's choices determine the story's progression.

# --- Game Setup ---

# We'll use a dictionary to store the different "scenes" or locations in our game.
# Each key will be a scene name (string), and its value will be another dictionary
# containing the description of the scene and the available choices.
# This structure helps organize our game world and makes it easy to move between scenes.
game_map = {
    "start": {
        "description": "You stand at a crossroads. To your left, a dark forest. To your right, a shimmering lake.",
        "choices": {
            "forest": "You bravely enter the dark forest.",
            "lake": "You approach the sparkling lake."
        }
    },
    "forest": {
        "description": "The trees are dense, and strange noises echo around you. You see a hidden path ahead.",
        "choices": {
            "path": "You follow the hidden path.",
            "back": "You decide to go back to the crossroads."
        }
    },
    "lake": {
        "description": "The water is crystal clear. A small boat is docked by the shore.",
        "choices": {
            "boat": "You get into the boat and push off from the shore.",
            "back": "You turn back towards the crossroads."
        }
    },
    "path": {
        "description": "The path leads to a clearing with a grumpy old hermit. He looks at you suspiciously.",
        "choices": {
            "talk": "You decide to talk to the hermit.",
            "run": "You quickly turn and run back into the forest."
        }
    },
    "boat": {
        "description": "You row across the lake and find a mysterious island. A treasure chest sits in the sand!",
        "choices": {
            "open": "You eagerly open the treasure chest.",
            "leave": "You decide not to disturb the treasure and row back."
        }
    },
    "talk_hermit": {
        "description": "The hermit grumbles, 'What do you want? I'm busy!' He doesn't seem friendly.",
        "choices": {
            "leave": "You decide to leave the hermit alone.",
            "ask": "You ask the hermit for directions."
        }
    },
    "ask_hermit": {
        "description": "The hermit points vaguely north. 'The lost city is that way,' he mutters.",
        "choices": {
            "north": "You head north, hoping to find the lost city.",
            "back": "You decide to return to the clearing."
        }
    },
    "open_chest": {
        "description": "Inside the chest, you find a glittering amulet! Congratulations, you found the treasure!",
        "choices": {} # No further choices, this is an end state.
    },
    "game_over": {
        "description": "You got lost and never found your way back. Game Over.",
        "choices": {}
    }
}

# --- Game Logic ---

def display_scene(scene_name):
    # This function displays the current scene's description and its available choices.
    scene = game_map[scene_name]
    print("\n" + scene["description"]) # Print the scene's description. \n adds a newline for readability.

    if scene["choices"]: # Check if there are any choices available in this scene.
        print("What do you want to do?")
        # Iterate through the choices and print them clearly for the player.
        for choice_key, choice_text in scene["choices"].items():
            # choice_key is what the player will type (e.g., "forest", "lake").
            # choice_text is the brief summary of the action.
            print(f"- {choice_key.capitalize()}: {choice_text}") # Capitalize the first letter of the choice for better presentation.
    else:
        print("The adventure ends here.") # If no choices, it's an ending scene.

def get_player_input(current_scene_name):
    # This function prompts the player for input and validates it against available choices.
    current_scene = game_map[current_scene_name]
    
    if not current_scene["choices"]:
        return None # If there are no choices, return None to signal the end.

    while True: # Loop until valid input is received.
        player_action = input("Enter your choice: ").lower().strip() # Get input, convert to lowercase, and remove whitespace.
        
        if player_action in current_scene["choices"]:
            return player_action # If the input is a valid choice, return it.
        else:
            print("Invalid choice. Please try again.") # Otherwise, inform the player and ask again.

def play_game():
    # This is the main function that runs the game loop.
    current_scene_name = "start" # Start the game at the "start" scene.

    while True: # The main game loop. It continues until the player reaches an end state.
        display_scene(current_scene_name) # Display the current scene.
        
        # Determine the next scene based on player input.
        # We need to map specific input to scene names.
        # For example, if the player chooses "forest" at "start", they go to the "forest" scene.
        # If the player chooses "talk" at "path", we need to decide where that leads.
        # This logic is embedded in the transition from display_scene to get_player_input
        # and then how we determine the next current_scene_name.

        next_action = get_player_input(current_scene_name) # Get the player's chosen action.

        if next_action is None:
            break # If get_player_input returned None, it means we are at an end scene.

        # Now, we need to determine which scene to transition to.
        # This is where the branching narrative happens.
        # We use a series of if-elif-else statements to map player actions to new scene names.
        
        # For the "start" scene:
        if current_scene_name == "start":
            if next_action == "forest":
                current_scene_name = "forest"
            elif next_action == "lake":
                current_scene_name = "lake"
        
        # For the "forest" scene:
        elif current_scene_name == "forest":
            if next_action == "path":
                current_scene_name = "path"
            elif next_action == "back":
                current_scene_name = "start" # Go back to the start.
        
        # For the "lake" scene:
        elif current_scene_name == "lake":
            if next_action == "boat":
                current_scene_name = "boat"
            elif next_action == "back":
                current_scene_name = "start"

        # For the "path" scene:
        elif current_scene_name == "path":
            if next_action == "talk":
                current_scene_name = "talk_hermit" # Transition to a new scene about talking.
            elif next_action == "run":
                current_scene_name = "forest" # Go back into the forest.
        
        # For the "talk_hermit" scene:
        elif current_scene_name == "talk_hermit":
            if next_action == "leave":
                current_scene_name = "path" # Go back to the clearing.
            elif next_action == "ask":
                current_scene_name = "ask_hermit" # Ask for directions.
        
        # For the "ask_hermit" scene:
        elif current_scene_name == "ask_hermit":
            if next_action == "north":
                current_scene_name = "game_over" # A simplified path to game over for this example.
            elif next_action == "back":
                current_scene_name = "path" # Go back to the clearing.

        # For the "boat" scene:
        elif current_scene_name == "boat":
            if next_action == "open":
                current_scene_name = "open_chest" # The winning scene.
            elif next_action == "leave":
                current_scene_name = "lake" # Go back to the lake shore.
        
        # If we reach an end scene (like "open_chest" or "game_over"),
        # the loop will naturally terminate because display_scene will not find choices.
        if not game_map[current_scene_name]["choices"]:
            display_scene(current_scene_name) # Display the final message.
            break # Exit the game loop.

# --- Example Usage ---

if __name__ == "__main__":
    # This block ensures that play_game() is called only when the script is run directly.
    # It's good practice for making your code reusable.
    print("Welcome to the Text Adventure Game!")
    play_game()
    print("\nThanks for playing!")