import requests
import json

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN="..."
API_URL = "..."
COURSE_ID = "..."  # Replace with your course ID

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Define the query with pagination for assignmentsConnection
query = """
{
  course(id: ...) {
    id
    name
    assignmentsConnection {
      nodes {
        name
        _id
        submissionsConnection {
          nodes {
            grade
            user {
              email
            }
            rubricAssessmentsConnection {
              nodes {
                assessmentRatings {
                  comments
                  description
                  points
                  criterion {
                    longDescription
                    points
                    description
                  }
                }
              }
              pageInfo {
                hasNextPage
                endCursor
              }
            }
          }
          pageInfo {
            endCursor
            hasNextPage
          }
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
"""

def fetch_all_data():
    # Use a dictionary to store the data directly under 'course' instead of an array
    all_data = {}

    # Initial request to get the first page of course data with assignmentsConnection
    variables = {}
    query_data = {"query": query}
    
    while True:
        response = requests.post(API_URL, json=query_data, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Update the 'course' data in the dictionary
        course_data = data.get('data', {}).get('course', {})
        all_data['course'] = course_data

        # Extract the assignments and submissions data from the response
        assignments = course_data.get('assignmentsConnection', {}).get('nodes', [])
        
        # Check if there are more pages for assignments
        page_info = course_data.get('assignmentsConnection', {}).get('pageInfo', {})
        if not page_info.get('hasNextPage'):
            break
        
        # If there's a next page, modify the query to include the `endCursor`
        end_cursor = page_info.get('endCursor')
        query_data["query"] = query.replace("first: 100", f"first: 100, after: \"{end_cursor}\"")

    return all_data

# Fetch all the data
all_course_data = fetch_all_data()

# Dump the response JSON to a file
output_file = 'response_data.json'
with open(output_file, 'w') as f:
    json.dump(all_course_data, f, indent=2)

print(f"Data has been fetched and saved to {output_file}")
