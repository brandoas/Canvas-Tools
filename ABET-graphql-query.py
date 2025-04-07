import requests
import json


ACCESS_TOKEN = "..."
COURSE_ID = "..."  # Replace with your course ID
API_URL = "..."

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
            }
          }
        }
      }
    }
  }
}
"""

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}



# Make the request
response = requests.post(API_URL, json={'query': query}, headers=headers)

# Raise an exception for bad responses
response.raise_for_status()
data = response.json()

# Dump the response JSON to a file
output_file = 'response_data_unpaged.json'

with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)

#Canvas paged this we need to fix that.