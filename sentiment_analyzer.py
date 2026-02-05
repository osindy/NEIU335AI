"""
Assignment 5: Simple Sentiment Analyzer

Instructions:
1. Modify the `positive_words` and `negative_words` sets below:
   - **Add at least 15 positive words** and **15 negative words** of your choice.
   - Ensure words are lowercased and contain only alphabetic characters.
2. Print positive lexicon & negative lexicon
3. Compute simple sentiment score (hint: positive - negative count)
4. Print the output results
5. Add a short reflection as comments at the bottom:
   - Discuss **strengths** and **limitations** of this lexicon-based approach (2–3 sentences).

Deliverables:
- Completed Python script (`sentiment_analyzer.py`).

"""

# --- Grading Rubric (Total: 50 pts) ---
#
# | Criteria                                                          | Points |
# |:------------------------------------------------------------------|:-------|
# | Lexicon completeness (≥15 positive & ≥15 negative words)           |   15   |
# | Display of positive & negative lexicons                            |    5   |
# | Sentiment score computation & correct labeling                    |   10   |
# | Interactive testing functionality (I/O loop, 'exit' handling)     |   10   |
# | Code readability and comments                                     |    5   |
# | Reflection quality (insightful strengths & limitations)          |    5   |
#
# **Total Points:** 50    

import re

def clean_text(text):
    """
    Lowercase, remove punctuation, and split into tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    tokens = text.split()
    return tokens

# 1. Add 15 positive and 15 negative to your expand the knowledge base

positive_words = {
    'happy'
}
negative_words = {
    'sad'
}

# 2. print positive lexicon & negative lexicon:


# --- Interactive Sentiment Testing ---
print("\nEnter sentences to analyze sentiment (type 'exit' to quit):")
while True:
    text = input('> ').strip()
    if text.lower() in ('exit', 'quit'):
        print("Goodbye!")
        break

    tokens = clean_text(text)
    # TODO: 1. Count the number of positive words and negative words in the token list
    # pos_count = ...
    # neg_count = ...
    
    # 3. Compute simple sentiment score (hint: positive - negative count)
    # score = ...

    # TODO: 2. Determine the sentiment label (Positive, Negative, or Neutral) based on the score
    # if ...
    #     sentiment = ...

# 4. print the output results
    print(f"Tokens: {tokens}")
    print(f"+ matches: {pos_count}, - matches: {neg_count}")
    print(f"Score: {score:.3f} => {sentiment}\n")

# 5. Add a short reflection as comments at the bottom (2–3 sentences)

