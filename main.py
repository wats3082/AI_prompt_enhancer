import re

# Function to add "Acting as a [role] engineer"
def add_role_to_prompt(question: str, role: str) -> str:
    """Add 'Acting as a [role] engineer' to the prompt."""
    return f"Acting as a {role} engineer, {question}"

# Function to make the question more advanced (clear, open-ended, actionable)
def refine_question(question: str) -> str:
    """Refine the user question by making it more advanced, clear, and actionable."""
    # Add clarity by making sure it ends with a question mark
    if not question.endswith('?'):
        question += "?"
    
    # Improve conciseness: remove unnecessary words like "please"
    question = re.sub(r'\b(please|kindly|could you|can you)\b', '', question, flags=re.IGNORECASE)
    
    # Encourage open-endedness: If it's a yes/no question, rephrase it
    if re.search(r'\b(yes|no)\b', question, re.IGNORECASE):
        question = re.sub(r'\b(yes|no)\b', '', question, flags=re.IGNORECASE)
        question += " Could you explain in more detail?"
    
    # Make it actionable: Ask for examples or further elaboration
    question += " Give me 2 examples, please."

    return question.strip()

# Function to generate a complete AI prompt
def generate_ai_prompt(user_input: str, role: str) -> str:
    """Create an AI prompt by adding role and refining the question."""
    # Refine the user's question to make it more detailed
    refined_question = refine_question(user_input)
    
    # Add the role to the prompt
    ai_prompt = add_role_to_prompt(refined_question, role)
    
    return ai_prompt

# Main function to interact with the user and generate the prompt
def main():
    print("Welcome to the Advanced AI Prompt Generator!\n")
    
    # Take user input for the question and the role
    user_input = input("Please enter your question: ")
    role = input("Please enter the role (e.g., software, data, machine learning): ")
    
    # Generate the final AI prompt
    ai_prompt = generate_ai_prompt(user_input, role)
    
    # Display the generated prompt
    print("\nYour advanced AI prompt is:")
    print(ai_prompt)

# Run the program
if __name__ == "__main__":
    main()
