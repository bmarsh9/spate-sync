import yaml
import json

y = {'name': 'Workflow_4accde58c2', 'children': [{'name': 'Operator_aa87398d1c', 'children': [{'name': 'Link_417779cb01', 'children': [{'name': 'Operator_b8fd180b02'}]}]}]}
x = {'return_path': '97124d89b4a3ef0b071122e7640710c18faed96f', 'paths': [{'59430a118bcb3b0c381974abd20a4067b1cbf881': [{'name': 'Workflow_4accde58c2'}, {'name': 'Operator_aa87398d1c'}, {'name': 'Link_417779cb01'}, {'name': 'Operator_b8fd180b02'}]}, {'a5cdf5e6b056bfed50368edea0c38c92d509ad6f': [{'name': 'Workflow_4accde58c2'}, {'name': 'Operator_aa87398d1c'}, {'name': 'Link_2d2983bcef'}, {'name': 'Operator_05244bc3cd'}]}]}
x={"a":"b","c":"d"}
#r = json.dumps(y)
#data = yaml.safe_load(r)
r = yaml.dump(x)
print(r)
