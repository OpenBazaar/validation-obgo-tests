import jsonschema
import json

with open('../schema/profileSchema.json') as pS:
  profileSchema = json.load(pS)

with open('../responses/profile.json') as p:
  profile = json.load(p)

try:
    # Read in the JSON document
    # pyProfileSchema = json.loads(profileSchema)
    # pyProfile = json.loads(profile)
    # And validate the result
    jsonschema.validate(instance=profile, schema=profileSchema)
    print("Validation test passed!")
except jsonschema.exceptions.ValidationError as e:
    print("well-formed but invalid JSON:", e)
except json.decoder.JSONDecodeError as e:
    print("poorly-formed text, not JSON:", e)
