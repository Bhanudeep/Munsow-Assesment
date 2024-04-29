# Pre-defined list of interview questions with attributes
questions = [
    {"question": "What is object-oriented programming?", "tags": ["programming", "OOP"], "difficulty_level": "Easy"},
    {"question": "What is the difference between list and tuple in Python?", "tags": ["programming", "Python"], "difficulty_level": "Medium"},
    {"question": "What is SQL injection?", "tags": ["databases", "security"], "difficulty_level": "Hard"},
    {"question": "Explain the difference between HTTP and HTTPS.", "tags": ["web", "security"], "difficulty_level": "Medium"},
    {"question": "What is a closure in JavaScript?", "tags": ["programming", "JavaScript"], "difficulty_level": "Hard"},
    {"question": "What is the importance of version control in software development?", "tags": ["software development", "version control"], "difficulty_level": "Easy"}
]

def recommend_questions(candidate_profile):
    recommended_questions = []
    for question in questions:
        # Check if candidate attributes match question tags or difficulty level
        if any(tag in candidate_profile for tag in question['tags']) or candidate_profile['experience_level'] == question['difficulty_level']:
            recommended_questions.append(question['question'])
    return recommended_questions

# Candidate experience level input
candidate_level=input("Enter you experience: Easy/Medium/Hard\n")
candidate_profile = {
    "role": "Software Engineer",
    "experience_level": candidate_level,
    "skills": ["programming", "Python", "JavaScript"]
}

# Get recommended questions for the candidate
recommended_questions = recommend_questions(candidate_profile)


print("Recommended Interview Questions:")
for idx, question in enumerate(recommended_questions, 1):
    print(f"{idx}. {question}")
