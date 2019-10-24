import jsonschema
import json

with open('../schema/orderSpendSchema.json') as a:
  schema = json.load(a)

with open('../responses/orderSpend.json') as b:
  response = json.load(b)

try:
    # And validate the response
    jsonschema.validate(instance=response, schema=schema)
    print("Validation test passed!")
except jsonschema.exceptions.ValidationError as e:
    print("well-formed but invalid JSON:", e)
except json.decoder.JSONDecodeError as e:
    print("poorly-formed text, not JSON:", e)
