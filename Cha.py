questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Mark Twain", "D) Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["A) 50°C", "B) 75°C", "C) 90°C", "D) 100°C"],
        "answer": "D"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {q['answer']}.\n")

print(f"Quiz Over! Your final score is {score} out of {len(questions)}.")
