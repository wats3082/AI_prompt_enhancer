# AI_prompt_enhancer

To create a Python script that takes user input questions and converts them into **advanced AI prompts**, while adding specific elements like **"Acting as a [role] engineer"** and ending with **"Give me 2 examples, please."**, we can follow a structured approach:

### Steps:
1. **Input the User's Question**: Accept a user input question.
2. **Add Role**: Add the phrase "Acting as a [role] engineer" based on the type of question, or let the user specify a role.
3. **Make the Prompt Advanced**: Reframe the question to ensure it encourages a more comprehensive or detailed response, based on AI prompt writing principles.
4. **End the Prompt**: Add the phrase **"Give me 2 examples, please"** at the end of the refined prompt.
5. **Output**: Display the final AI prompt to the user.

### Python Script:

```python

```

### How the Script Works:

1. **Add Role**: The `add_role_to_prompt` function adds the specified role (e.g., "software engineer", "data engineer") to the prompt in the format "Acting as a [role] engineer."
   
2. **Refine Question**: The `refine_question` function improves the clarity, conciseness, and open-endedness of the user's input. It ensures the question is well-structured, removes unnecessary politeness, and turns yes/no questions into more expansive ones. It also appends **"Give me 2 examples, please."** to encourage actionable examples.

3. **Prompt Generation**: The `generate_ai_prompt` function combines both the refined question and the role to create the final AI prompt.

4. **User Interaction**: The script asks the user for a question and role, then generates and displays the refined AI prompt.

### Example Interactions:

**Example 1:**

**User Input**:  
`What is deep learning?`  
**Role Input**:  
`machine learning`

**Output**:
```
Your advanced AI prompt is:
Acting as a machine learning engineer, What is deep learning? Could you explain in more detail? Give me 2 examples, please.
```

**Example 2:**

**User Input**:  
`How does blockchain work?`  
**Role Input**:  
`software`

**Output**:
```
Your advanced AI prompt is:
Acting as a software engineer, How does blockchain work? Could you explain in more detail? Give me 2 examples, please.
```

**Example 3:**

**User Input**:  
`Is artificial intelligence the future?`  
**Role Input**:  
`data`

**Output**:
```
Your advanced AI prompt is:
Acting as a data engineer, Could you explain in more detail why artificial intelligence is considered the future? Give me 2 examples, please.
```

### Script Breakdown:

1. **`add_role_to_prompt`**: This function ensures that the prompt starts by framing the user's question in the context of a specific role. For example, asking a data engineer or software engineer to explain something from their expertise.

2. **`refine_question`**: This is the heart of the script where we refine the user’s input:
   - It adds clarity by ensuring the prompt ends with a question mark if it's missing.
   - It removes redundant polite phrases like "please" or "could you" to make the prompt more concise.
   - It converts closed-ended questions (like "Is AI the future?") into open-ended ones by asking for more detailed explanations.
   - Finally, it appends **"Give me 2 examples, please."** to encourage the AI to provide concrete examples in the response.

3. **User Interaction**: The user inputs both the question and the desired role. Based on these inputs, the program generates a more structured, role-specific, and example-oriented AI prompt.

### Enhancements:

1. **Context-Aware Role Detection**: You could enhance the script by automatically detecting the role based on the question content, or offer a list of common roles for the user to choose from.
2. **Natural Language Processing (NLP)**: For more advanced processing, integrating NLP libraries like `spaCy` or `transformers` could help detect more complex question types and refine them accordingly.
3. **Customizable Example Requests**: Instead of just asking for "2 examples", you could allow users to specify how many examples they want.

This script helps generate high-quality AI prompts by following best practices in prompt design, ensuring that questions are clear, detailed, and aligned with the expected role of the responder.
