import json
from tabulate import tabulate

# Specify the path to your JSON file
input_file = 'response_data.json'

# Read the JSON data from the file
with open(input_file, 'r') as f:
    data = json.load(f)

assignments = data.get('course', {}).get('assignmentsConnection', {}).get('nodes', {})
table_data = []

for item in assignments:
    # Ensure '_id' and 'name' exist in the object

    _id = item.get('_id')
    name = item.get('name')

    print(f" ID: {_id}, Name: {name}")
    
    submissions = item.get('submissionsConnection', {}).get('nodes', {})

    for submission in submissions:
        grade = submission.get('grade')
        user = submission.get('user').get('email')

        rubrics_items = submission.get('rubricAssessmentsConnection', {}).get('nodes', {})

        for assessment in rubrics_items.get('assessmentRatings', []):
            criterion_desc = assessment['criterion']['description']
            points = assessment['points']
            comments = assessment['comments']
            table_data.append([criterion_desc, points, comments])

        # Print the grade and user values for each submission
        if grade is not None and user is not None:
            print(f" Grade: {grade}, User: {user}")

        # Define the table headers
        headers = ["Criterion", "Points", "Comments"]

        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

#       print(json.dumps(rubrics_items, indent=2))