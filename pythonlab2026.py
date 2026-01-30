"""
CS 335 Python Lab 1
This script demonstrates basic Python concepts including variables, data types,
lists, loops, dictionaries, conditionals, and functions.
"""
"""
Instruction:
1. Open Google Colab: Go to Google Colab and sign in with your Google account.
2. Create a New Notebook: Name it CS335_PythonLab1_YourName.
"""

from typing import List, Dict, Union


def run_variables_demo():
    """
    Topic 1: Variables and Data Types
    Task: Task: Modify the variables to reflect your name, age, and 
    enrollment status. Then print a sentence using all three values
    """
    print("\n--- 1. Variables and Data Types ---")
    name: str = "Omeed Adham Sindy"
    age: int = 70
    ai_course: bool = True

    print(f"Name: {name}")
    print(f"Age in 5 years: {age + 5}")
    print(f"Is enrolled in CS 335: {ai_course}")
    
    # TODO: Create a sentence using all three values and print it
    # Hint: Use an f-string, e.g., f"{name} is {age}..."



def run_list_demo():
    """
    Topic 2: Lists and Loops
    Task:
    1) Add two additional AI topics to the list.
    2) Modify the loop to include numbering (e.g., "1. Logic").
    """
    print("\n--- 2. Lists and Loops ---")
    topics: List[str] = ["Logic", "Search", "NLP", "ML", "Bayesian Inference"]
    
    # TODO: Add two additional AI topics
    # Hint: Use the .append() or .extend() method
    

    # TODO: Modify loop to include numbering
    # Hint: Use the enumerate() function: for i, topic in enumerate(topics, start=1):
    print("We will study the following topics:")
    for topic in topics:
        print(topic)


def run_dictionaries_demo():
    """
    Topic 3: Dictionaries and Conditionals
    Task:
    1) Modify the score to test different outputs.
    2) Add a new grade tier for "A+" if the score is 95 or higher.
    """
    print("\n--- 3. Dictionaries and Conditionals ---")
    
    # Test cases to demonstrate the logic
    students: List[Dict[str, Union[str, int]]] = [
        {"name": "Omeed", "score": 85},
        {"name": "Alice", "score": 96},  # High score for A+ test
        {"name": "Bob", "score": 72}
    ]

    for student in students:
        score = student["score"]
        grade = ""
        
        # Task completion: Add "A+" tier and logic
        # TODO: Add logic for "A+" if score is 95 or higher
        # Hint: Check for >= 95 first, before checking for >= 90
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        else:
            grade = "C or below"
            
        print(f"{student['name']} (Score: {score}) received a grade of {grade}.")


def greet_student(name: str) -> str:
    """Helper function to greet a student."""
    return f"Welcome to CS 335, {name}!"


def square_number(num: Union[int, float]) -> Union[int, float]:
    """
    Topic 4 Task: Write a function square_number(num) that takes a number
    and returns its square.
    """
    # TODO: Implement this function
    # Hint: Return num * num or num ** 2
    return 0


def run_functions_demo():
    """
    Topic 4: Functions
    Task: Test square_number with at least two inputs.
    """
    print("\n--- 4. Functions ---")
    
    # Demonstrating the existing function
    print(greet_student("Omeed"))

    # TODO: Test square_number with at least two inputs
    # Hint: Call square_number(5) and print the result
    pass


def main():
    """Main function to run all demos."""
    print("CS 335 Python Lab - Completed Tasks")
    run_variables_demo()
    run_list_demo()
    run_dictionaries_demo()
    run_functions_demo()


if __name__ == "__main__":
    main()