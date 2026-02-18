import json
data = '''
[
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "age": 28
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "age": 32
  },
  {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com",
    "age": 25
  },
  {
    "id": 4,
    "name": "Diana",
    "email": "diana@example.com",
    "age": 30
  }
]
'''
# converting JSON-formatted object to python
py_list = json.loads(data)
for i in range(len(py_list)):
    py_list[i]["place"] = i
print(py_list)

# converting python to json

arr1 = json.dumps(py_list)

# saving python to json file

with open("pytojsonfile.json","w") as wf:
    json.dump(py_list,wf,indent=2)

# reading from json file to python 

with open(r"C:\Users\kalpa\Downloads\PYTHON\PYTHON PRACTICE\jsonfile.json") as rf:
    data = json.load(rf)
    for rec in data:
        print(rec)

data = """
{
  "company": "Tech Solutions Ltd",
  "founded_year": 2010,
  "is_active": true,
  "rating": 4.7,
  "branches": ["New York", "London", "Bangalore"],
  "people": [
    {
      "id": 1,
      "firstname": "Joe",
      "lastname": "Jackson",
      "gender": "M",
      "age": 29,
      "phno": null,
      "licence": true,
      "salary": 55000.50,
      "skills": ["Python", "Django", "Docker"],
      "address": {
        "street": "12th Avenue",
        "city": "New York",
        "zipcode": 10001
      },
      "projects": [],
      "performance_scores": [88, 92, 79]
    },
    {
      "id": 2,
      "firstname": "Emma",
      "lastname": "Watson",
      "gender": "F",
      "age": 34,
      "phno": "123-456-7890",
      "licence": false,
      "salary": 72000,
      "skills": ["Java", "Spring Boot"],
      "address": {
        "street": "Baker Street",
        "city": "London",
        "zipcode": "NW1 6XE"
      },
      "projects": ["Banking API", "Payment Gateway"],
      "performance_scores": [91, 89, 95]
    },
    {
      "id": 3,
      "firstname": "Raj",
      "lastname": "Sharma",
      "gender": "M",
      "age": 26,
      "phno": null,
      "licence": true,
      "salary": 48000,
      "skills": [],
      "address": {
        "street": "MG Road",
        "city": "Bangalore",
        "zipcode": 560001
      },
      "projects": ["AI Chatbot"],
      "performance_scores": [85, 87, 90]
    }
  ],
  "metadata": {
    "total_employees": 3,
    "remote_work_supported": true,
    "departments": ["Engineering", "HR", "Finance"],
    "null_field_example": null
  }
}
"""


import json
py_data1 = json.loads(data)
# Print the company name.
print(py_data1.get("company"))
print()
# Print all branch names.
print(py_data1.get("branches"))
print()
# Print the firstname of the second employee.
for key in py_data1:
    if key=="people":
      for person in py_data1[key]:
          if person["id"]==2:
              print(person.get("firstname"))
print()
# Print Raj's city.
for key in py_data1:
    if key=="people":
      for person in py_data1[key]:
         if person["firstname"]=="Raj":
            print(person["address"]["city"])
print()
# Print Emma's phone number.
for key in py_data1:
    if key=="people":
      for person in py_data1[key]:
         if person["firstname"]=="Emma":
            print(person["phno"])
print()
# Print total number of employees.

for key in py_data1:
    if key=="people":
       print(len(py_data1[key]))
print()
# Print all employee first names.
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         print(emp.get("firstname"))
print()
# Print names of employees whose salary is greater than 50,000.
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         if emp.get("salary")>50000:
            print(emp.get("firstname"))
print()
# Print employees who have no phone number.

for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         if emp.get("phno")==None:
            print(emp.get("firstname"))
print()
# Print employees who have more than 2 performance scores.
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         if len(emp.get("performance_scores"))>2:
            print
            print(emp.get("firstname"))
print()
# Count total number of skills across all employees.
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
        print(f"{emp.get('firstname')} has {len(emp.get('skills'))} skills")
print()
# Print all unique cities where employees live.
unique_cities = []
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
        unique_cities.append(emp.get("address").get("city"))
print(set(unique_cities))
print()
# Print the average age of employees.
ages = []
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         ages.append(emp.get("age"))
avg = sum(ages)/len(ages)
print(avg)

# adding new employee
new_emp = '''{
  "id": 4,
  "firstname": "Sophia",
  "lastname": "Williams",
  "gender": "F",
  "age": 31,
  "phno": "987-654-3210",
  "licence": true,
  "salary": 68000.75,
  "skills": ["React", "Node.js", "AWS"],
  "address": {
    "street": "Sunset Boulevard",
    "city": "Los Angeles",
    "zipcode": 90001
  },
  "projects": ["Cloud Migration", "Frontend Revamp"],
  "performance_scores": [93, 88, 91],
  "experience_years": 7,
  "is_manager": false,
  "certifications": ["AWS Certified Developer", "Scrum Master"],
  "bonus": null
}
'''
new_emp_dict = json.loads(new_emp)
for key in py_data1:
   if key=="people":
      py_data1[key].append(new_emp_dict)
print(py_data1)
print()
# Add a new key "experience_years" to every employee.

for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         emp["experience_years"]=int|None
print(py_data1)
print()
# Increase salary of all employees by 10%.

for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         emp["salary"]=emp["salary"]*1.1
print(py_data1)
print()
# Add a new branch "Tokyo".

for key in py_data1:
   if key=='branches':
      py_data1[key].append("Tokyo")
print(py_data1)
print()
# Remove employees with salary less than 50,000.

for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         if emp["salary"]<60000:
            idx = py_data1[key].index(emp)
            py_data1[key].pop(idx)
print(py_data1)
print()

# print("@@@@@@@@@@@@@@@@@@")
for key in py_data1:
   if key=="people":
      for emp in py_data1[key]:
         if emp["salary"]<60000:
            idx = py_data1[key].index(emp)
            py_data1[key].pop(idx)
print(py_data1)

# Find employee with highest salary.

for key in py_data1:
   sal = []
   if key=='people':
      for emp in py_data1[key]:
         sal.append(emp.get("salary"))
      highest_sal = max(sal)
      for emp in py_data1[key]:
         if emp['salary']==highest_sal:
            print(emp['firstname'])

# best approach for this

max_sal = max(py_data1['people'],key=lambda emp:emp['salary'])
print(max_sal['firstname'])

# in case there are more than one person with highest salary

highest_paid = [
    emp for emp in py_data1["people"]
    if emp["salary"] == max_sal
]

print(highest_paid)

# Find employee with highest average performance score.

high_avg_perf_score = max(py_data1['people'],key= lambda emp:sum(emp['performance_scores'])//len(emp['performance_scores']))
name = high_avg_perf_score['firstname']
print(name)

# converting python object into json 
json_data = json.dumps(py_data1)

# saving python into json file
with open("jsonpractise.json",'w') as wf:
   json.dump(py_data1,wf,indent=5)

# accessing data from json file and modifying it and saving back to json file

with open(r'C:\Users\kalpa\Downloads\PYTHON\PYTHON PRACTICE\jsonpractise.json','r') as rf:
   data = json.load(rf)
print(data)
del data['rating']

with open(r'C:\Users\kalpa\Downloads\PYTHON\PYTHON PRACTICE\jsonpractise1.json','w') as wf:
   json.dump(data,wf,indent=3)
