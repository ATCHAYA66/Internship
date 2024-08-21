def find_runner_up(scores):
    # Remove duplicate scores to avoid ties
    unique_scores = list(set(scores))
    
    # Sort the scores in descending order
    unique_scores.sort(reverse=True)
    
    # The runner-up score will be the second item in the sorted list
    if len(unique_scores) > 1:
        return unique_scores[1]
    else:
        return None  # If there's no runner-up (e.g., all scores are the same)

# Example usage
scores = [90, 85, 90, 88, 92, 85, 92]
runner_up_score = find_runner_up(scores)

if runner_up_score is not None:
    print(f"The runner-up score is: {runner_up_score}")
else:
    print("There is no runner-up score.")
