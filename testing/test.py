import yaml
import json

y = {'name': 'Workflow_4accde58c2', 'children': [{'name': 'Operator_aa87398d1c', 'children': [{'name': 'Link_417779cb01', 'children': [{'name': 'Operator_b8fd180b02'}]}]}]}
x = {'paths': [{'steps': [{'name': 'Workflow_4accde58c2','imports':'test'}, {'name': 'Operator_aa87398d1c'}, {'name': 'Link_417779cb01'}, {'name': 'Operator_b8fd180b02'}]}, {'steps': [{'name': 'Workflow_4accde58c2'}, {'name': 'Operator_aa87398d1c'}, {'name': 'Link_2d2983bcef'}, {'name': 'Operator_05244bc3cd'}]}]}
#r = json.dumps(y)
#data = yaml.safe_load(r)
r = yaml.dump(x)
print(r)
