"""
Interactive Expert System Simulation.

This script simulates a simple expert system that diagnoses possible medical conditions
based on user-reported symptoms using a rule-based inference engine.
"""

from typing import List, Dict, Union

# Knowledge base: Define rules as a list of dictionaries
KNOWLEDGE_BASE: List[Dict[str, Union[List[str], str]]] = [
    {"if": ["fever", "sore_throat"], "then": "possible_strep_throat"},
    {"if": ["fever", "cough"], "then": "possible_flu"},
    {"if": ["headache"], "then": "possible_migraine"},
    {"if": ["sore_throat"], "then": "possible_common_cold"},
]


def evaluate_symptoms(user_symptoms: List[str], rules: List[Dict]) -> List[str]:
    """
    Evaluate user symptoms against the knowledge base rules to find matches.

    Args:
        user_symptoms: A list of symptoms provided by the user.
        rules: A list of rules defining the knowledge base.

    Returns:
        A list of matched conditions (inferred facts).
    """
    # Create a set for faster lookup
    symptom_set = set(s.strip().lower() for s in user_symptoms)
    inferred_conditions = []

    for rule in rules:
        # Check if all conditions in the rule are present in user's symptoms
        if all(condition in symptom_set for condition in rule["if"]):
            inferred_conditions.append(rule["then"])

    return inferred_conditions


def main():
    """
    Main function to run the expert system simulation.
    """
    print("Welcome to the Expert System Simulation.")
    try:
        user_input = input("Enter your symptoms separated by commas: ")
        if not user_input.strip():
            print("No symptoms entered. Exiting.")
            return

        user_symptoms = user_input.split(',')
        possible_conditions = evaluate_symptoms(user_symptoms, KNOWLEDGE_BASE)

        if possible_conditions:
            print("\nBased on your symptoms, possible conditions include:")
            print(", ".join(possible_conditions))
        else:
            print("\nNo conditions matched your symptoms. Please consult a medical professional.")

    except KeyboardInterrupt:
        print("\nExiting program.")


if __name__ == "__main__":
    main()
