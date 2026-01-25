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
    
    # Task completion: Sentence using all three values
    enrollment_status = "is enrolled" if ai_course else "is not enrolled"
    print(f"Summary: {name}, aged {age}, {enrollment_status} in the CS 335 AI course.")


def run_list_demo():
    """
    Topic 2: Lists and Loops
    Task:
    1) Add two additional AI topics to the list.
    2) Modify the loop to include numbering (e.g., "1. Logic").
    """
    print("\n--- 2. Lists and Loops ---")
    topics: List[str] = ["Logic", "Search", "NLP", "ML", "Bayesian Inference"]
    
    # Task completion 1: Add two additional AI topics
    topics.extend(["Robotics", "Computer Vision"])

    # Task completion 2: Modify loop to include numbering
    print("We will study the following topics:")
    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic}")


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
        if score >= 95:
            grade = "A+"
        elif score >= 90:
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
    return num * num


def run_functions_demo():
    """
    Topic 4: Functions
    Task: Test square_number with at least two inputs.
    """
    print("\n--- 4. Functions ---")
    
    # Demonstrating the existing function
    print(greet_student("Omeed"))

    # Task completion: Test square_number with inputs
    test_inputs = [5, 12, -3, 2.5]
    print(f"Testing square_number function:")
    for num in test_inputs:
        result = square_number(num)
        print(f"The square of {num} is {result}")


def main():
    """Main function to run all demos."""
    print("CS 335 Python Lab - Completed Tasks")
    run_variables_demo()
    run_list_demo()
    run_dictionaries_demo()
    run_functions_demo()


if __name__ == "__main__":
    main()