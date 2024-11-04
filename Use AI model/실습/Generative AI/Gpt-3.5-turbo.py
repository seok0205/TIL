from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "describe about 63 building"}  
  ]
)

print("Assistant: " + completion.choices[0].message.content)

'''
결과 :
Assistant: 63 Building is a landmark skyscraper located in Yeouido, Seoul, South Korea. It stands at a height of 250 meters (820 feet) and consists of 63 floors above ground and three basement levels. The building was completed in 1985 and was the tallest 
building in South Korea at the time.

The design of 63 Building is unique, featuring a golden glass exterior that reflects sunlight during the day and is illuminated 
with colorful lights at night. The building's silhouette is said to resemble the curvature of the Han River, which flows nearby.
Within the 63 Building, there are a variety of attractions and amenities for visitors to enjoy. These include an observation deck on the 60th floor, offering panoramic views of Seoul and the Han River, as well as an aquarium, IMAX theater, and shopping mall. The building also houses a sky lounge and several restaurants offering diverse cuisines.

63 Building has become a popular tourist destination in Seoul, attracting visitors from around the world who come to admire its 
striking architecture and enjoy its entertainment and dining options.
'''