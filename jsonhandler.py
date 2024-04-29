import json

def filter_questions(data, difficulty=None, tags=None):
    filtered_questions = []
    for question in data:
        if (difficulty is None or question['difficulty_level'] == difficulty):
            filtered_questions.append(question['question'])
            filtered_questions.append(question['difficulty_level'])
    return filtered_questions

# Load data from JSON file
try:
    with open('example.json', 'r') as file:
        questions_data = json.load(file)
except:
    print("No such json file found")
    exit()
filtered_questions=[]
# Example usage: Filter questions by difficulty level "Easy" and tags ["Geography", "Countries"]
filtered_questions.append(filter_questions(questions_data, difficulty="Easy"))

# Example usage: Filter questions by difficulty level "Medium" and tags ["Geography", "Countries"]
filtered_questions.append(filter_questions(questions_data, difficulty="Medium"))

# Example usage: Filter questions by difficulty level "Hard" and tags ["Geography", "Countries"]
filtered_questions.append(filter_questions(questions_data, difficulty="Hard"))

print("Filtered Questions:")
for question in filtered_questions:
    print(question)

output_file = 'extracted_questions.json'
with open(output_file, 'w') as file:
    json.dump(filtered_questions, file, indent=4)


