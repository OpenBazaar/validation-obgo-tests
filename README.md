# Validating obgo API responses

- **What.** The purpose of this repo is to compile python scripts that validate [openbazaar-go](https://github.com/OpenBazaar/openbazaar-go) API responses.
- **Why.** The QA python suite will test multiple order flow scenarios to ensure that the server can successfully progress. However, it doesn't go any further than that to ensure that the server is returning expected data to a client. Just because an API gives a 200 OK response, doesn't mean it is functioning properly. These tests are mean to alert us when the server is not returning the expected data to a client (i.e. values are of the wrong type, keys are missing, or the JSON schema is malformed).
- **How.** We're using a python 3 module called [jsonschema](https://pypi.org/project/jsonschema/) to validate whether a JSON object adheres to a [JSON schema](https://json-schema.org/). This requires us to first determine the _expected_ schema for our API responses, which we can do using an awesome [online tool](https://jsonschema.net/). Here, we paste in a typical JSON response from the server that we know to be accurate, and the JSON schema tool will infer the schema from the object. Then it's a simple matter of using the `jsonschema` module to validate that the server always adheres to the schema with future code changes.

This repo contains:

1. Example JSON responses from the server for the APIs we want to impose a validation check on
2. The JSON schema for each API response in (1)
3. The python 3 scripts to run the validation (1 script per response to check)

The goal is that this code can be imported, in some way, into our QA tests.

### Example

This is an example of a JSON response to `GET /ob/profile`:

```JSON
{
    "peerID": "QmVCJiuBY5RPw8wWU85AxzJRkpYZsvDpnYRyGe8opLRJX6",
    "handle": "",
    "name": "v5 Seller",
    "location": "",
    "about": "The Dude",
    "shortDescription": "Yo",
    "nsfw": false,
    "vendor": true,
    "moderator": false,
    "stats": {
        "followerCount": 7,
        "followingCount": 0,
        "listingCount": 2,
        "ratingCount": 1,
        "postCount": 0,
        "averageRating": 5
    },
    "bitcoinPubkey": "02657f97b89f6de761fc93c9e61c69d92d2db5fa565bc087476932549d2b103add",
    "lastModified": "2019-10-22T00:56:15.841731088Z",
    "currencies": [
        "BCH",
        "ZEC",
        "LTC",
        "ETH",
        "BTC"
    ]
}
```

Using this [schema inferring tool](https://jsonschema.net/), the corresponding JSON schema is:

```JSON
{
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "peerID",
    "name",
    "nsfw",
    "vendor",
    "moderator",
    "stats",
    "bitcoinPubkey",
    "lastModified",
    "currencies"
  ],
  "properties": {
    "peerID": {
      "$id": "#/properties/peerID",
      "type": "string",
      "title": "The Peerid Schema",
      "default": "",
      "examples": [
        "QmVCJiuBY5RPw8wWU85AxzJRkpYZsvDpnYRyGe8opLRJX6"
      ],
      "pattern": "^(.*)$"
    },
    "handle": {
      "$id": "#/properties/handle",
      "type": "string",
      "title": "The Handle Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "name": {
      "$id": "#/properties/name",
      "type": "string",
      "title": "The Name Schema",
      "default": "",
      "examples": [
        "v5 Seller"
      ],
      "pattern": "^(.*)$"
    },
    "location": {
      "$id": "#/properties/location",
      "type": "string",
      "title": "The Location Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "about": {
      "$id": "#/properties/about",
      "type": "string",
      "title": "The About Schema",
      "default": "",
      "examples": [
        "The Dude"
      ],
      "pattern": "^(.*)$"
    },
    "shortDescription": {
      "$id": "#/properties/shortDescription",
      "type": "string",
      "title": "The Shortdescription Schema",
      "default": "",
      "examples": [
        "Yo"
      ],
      "pattern": "^(.*)$"
    },
    "nsfw": {
      "$id": "#/properties/nsfw",
      "type": "boolean",
      "title": "The Nsfw Schema",
      "default": false,
      "examples": [
        false
      ]
    },
    "vendor": {
      "$id": "#/properties/vendor",
      "type": "boolean",
      "title": "The Vendor Schema",
      "default": false,
      "examples": [
        true
      ]
    },
    "moderator": {
      "$id": "#/properties/moderator",
      "type": "boolean",
      "title": "The Moderator Schema",
      "default": false,
      "examples": [
        false
      ]
    },
    "stats": {
      "$id": "#/properties/stats",
      "type": "object",
      "title": "The Stats Schema",
      "required": [
        "followerCount",
        "followingCount",
        "listingCount",
        "ratingCount",
        "postCount",
        "averageRating"
      ],
      "properties": {
        "followerCount": {
          "$id": "#/properties/stats/properties/followerCount",
          "type": "integer",
          "title": "The Followercount Schema",
          "default": 0,
          "examples": [
            7
          ]
        },
        "followingCount": {
          "$id": "#/properties/stats/properties/followingCount",
          "type": "integer",
          "title": "The Followingcount Schema",
          "default": 0,
          "examples": [
            0
          ]
        },
        "listingCount": {
          "$id": "#/properties/stats/properties/listingCount",
          "type": "integer",
          "title": "The Listingcount Schema",
          "default": 0,
          "examples": [
            2
          ]
        },
        "ratingCount": {
          "$id": "#/properties/stats/properties/ratingCount",
          "type": "integer",
          "title": "The Ratingcount Schema",
          "default": 0,
          "examples": [
            1
          ]
        },
        "postCount": {
          "$id": "#/properties/stats/properties/postCount",
          "type": "integer",
          "title": "The Postcount Schema",
          "default": 0,
          "examples": [
            0
          ]
        },
        "averageRating": {
          "$id": "#/properties/stats/properties/averageRating",
          "type": "integer",
          "title": "The Averagerating Schema",
          "default": 0,
          "examples": [
            5
          ]
        }
      }
    },
    "bitcoinPubkey": {
      "$id": "#/properties/bitcoinPubkey",
      "type": "string",
      "title": "The Bitcoinpubkey Schema",
      "default": "",
      "examples": [
        "02657f97b89f6de761fc93c9e61c69d92d2db5fa565bc087476932549d2b103add"
      ],
      "pattern": "^(.*)$"
    },
    "lastModified": {
      "$id": "#/properties/lastModified",
      "type": "string",
      "title": "The Lastmodified Schema",
      "default": "",
      "examples": [
        "2019-10-22T00:56:15.841731088Z"
      ],
      "pattern": "^(.*)$"
    },
    "currencies": {
      "$id": "#/properties/currencies",
      "type": "array",
      "title": "The Currencies Schema",
      "items": {
        "$id": "#/properties/currencies/items",
        "type": "string",
        "title": "The Items Schema",
        "default": "",
        "examples": [
          "BCH",
          "ZEC",
          "LTC",
          "ETH",
          "BTC"
        ],
        "pattern": "^(.*)$"
      }
    }
  }
}
```

In the python script, we import both JSON objects and run the validation using the `jsonschema` module:

```python
import jsonschema
import json

with open('../schema/profileSchema.json') as a:
  schema = json.load(a)

with open('../responses/profile.json') as b:
  response = json.load(b)

try:
    # And validate the response
    jsonschema.validate(instance=response, schema=schema)
    print("Validation test passed!")
except jsonschema.exceptions.ValidationError as e:
    print("well-formed but invalid JSON:", e)
except json.decoder.JSONDecodeError as e:
    print("poorly-formed text, not JSON:", e)
```

### API responses to validate

Presently, our QA tests are focused on order flows, which means that the following APIs responses should be validated:

- [x] GET /ob/profile
- [ ] GET /ob/cases
- [ ] GET /ob/case
- [ ] POST /ob/releasefunds
- [ ] GET /ob/listings
- [x] GET /ob/listing/ipfs/:listingHash
- [x] GET /ob/listing/ipfs/slug
- [ ] GET /ob/order
- [ ] GET /ob/purchases
- [ ] GET /ob/sales
- [ ] POST /ob/purchase
- [ ] POST /wallet/spend
- [ ] POST /ob/orderspend
- [ ] POST /ob/releaseescrow
- [ ] GET /wallet/balance/:coinType
- [ ] GET /wallet/address/:coinType

### Known issues

1. The inferred JSON schema needs to be reviewed carefully to ensure we don't unnecessarily require certain key:value pairs
2. Some more sophisticated validation may be required for certain responses
    - e.g. format of peerIds and addresses (`jsonschema` may allow regex checks for fields, which we should use)
    - e.g. listing quantity values, which can be anything > -1
3. There is some maintenance penalty to ensure these tests are up to date with any API changes made
