from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime

file_to_test = "re-entry-alert-updated.jinja"  # Change this value to test different files

def to_risk(probability):
    return "Low"

def to_affected_territories(x):
    return "Wales"

def to_time_frame(x):
    return "10:00 - 12:00"

def to_full_country_name(code):
    return "US"

environment = Environment(loader=FileSystemLoader("..\\html"))

environment.filters['to_risk'] = to_risk
environment.filters['to_affected_territories'] = to_affected_territories
environment.filters['to_time_frame'] = to_time_frame
environment.filters['to_full_country_name'] = to_full_country_name

template = environment.get_template(file_to_test)

with open('test_json_data.json', 'r') as file:
    json_string = file.read()

my_dict = json.loads(json_string)

# Convert decay_time to a datetime object if present in the JSON data
if "decay_time" in my_dict:
    my_dict["decay_time"] = datetime.fromisoformat(my_dict["decay_time"])

filename = "test.html"
content = template.render(
    **my_dict
)

with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"Created {filename} in testing-resources folder. Open this file to preview email template")
