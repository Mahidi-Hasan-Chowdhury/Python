# ==============================================================================
# FILE NAME: exam5_data_structures.py
# PYTHON FOUNDATIONS EXAM - PART 5 (Data Structures)
# INSTRUCTIONS: Answer the questions below directly in this file using comments (#).
# After you are done, copy the entire content of this file and paste it back
# to me in the chat for grading and feedback.
# ==============================================================================

# 1. What is the key difference between a List and a Tuple in Python?
# YOUR ANSWER: A list is a mutable set of ordered elements. A tuple is immutable set of ordered collections.  


# 2. Look at the dictionary below. How would you write code to print the value of "model"?
# agent_config = {"name": "Bot", "model": "gpt-4", "version": 1}
# YOUR ANSWER: print(agent_config["model"])


# 3. What happens if you try to add duplicate items to a Set in Python?
# YOUR ANSWER: duplicate items will be ignored and only unique items will be stored in the set.


# 4. MINI-CHALLENGE:
# Write a short script that:
# 1. Creates a list of your 3 favorite programming languages.
# 2. Uses a method to add a 4th language to the end of the list.
# 3. Prints the final list.
# YOUR ANSWER:
languages = ['python','c','c++','java']
languages.append('javascript')
print(languages) 