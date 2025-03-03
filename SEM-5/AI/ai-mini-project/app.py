import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# function to load knowledge base from json
def load_knowledge_base(file_name):
    try:
        with open(file_name, 'r') as file:
            knowledge_base = json.load(file)
        return knowledge_base
    except FileNotFoundError:
        print(f"{file_name} not found")
        return None

# function to find solution
def find_solution(problem, knowledge_base):
    for issue in knowledge_base['issues']:
        if problem.lower() in issue['problem'].lower():
            return issue['solution']
    return "I'm sorry, I don't have information on that specific issue. Please contact our front desk for assistance."

# Load the knowledge base
knowledge_base = load_knowledge_base('medical_knowledge_base.json')

@app.route('/api/helpdesk', methods=['POST'])
def help_desk_api():
    if knowledge_base is None:
        return jsonify({"error": "Knowledge base not found"}), 500

    data = request.json
    user_problem = data.get('problem', '').strip().lower()
    solution = find_solution(user_problem, knowledge_base)
    return jsonify({"solution": solution})

if __name__ == "__main__":
    app.run(debug=True)
