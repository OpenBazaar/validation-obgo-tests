import jsonschema
import json

with open('./listingSchema.json') as a:
  schema = json.load(a)

with open('./listing.json') as b:
  response = json.load(b)

try:
    # Read in the JSON document
    # pyProfileSchema = json.loads(profileSchema)
    # pyProfile = json.loads(profile)
    # And validate the result
    jsonschema.validate(instance=response, schema=schema)
    print("Validation test passed!")
except jsonschema.exceptions.ValidationError as e:
    print("well-formed but invalid JSON:", e)
except json.decoder.JSONDecodeError as e:
    print("poorly-formed text, not JSON:", e)
