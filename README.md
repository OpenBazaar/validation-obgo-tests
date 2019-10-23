# Validating obgo API responses

- **What.** The purpose of this repo is to compile python scripts that validate [openbazaar-go](https://github.com/OpenBazaar/openbazaar-go) API responses.
- **Why.** The QA python suite will test multiple order flow scenarios to ensure that the server can successfully progress. However, it doesn't go any further than that to ensure that the server is returning expected data to a client. Just because an API gives a 200 OK response, doesn't mean it is functioning properly. These tests are mean to alert us when the server is not returning the expected data to a client (i.e. values are of the wrong type, keys are missing, or the JSON schema is malformed).
- **How.** We're using a python 3 module called [jsonschema](https://pypi.org/project/jsonschema/) to validate whether a JSON object adheres to a [JSON schema](https://json-schema.org/). This requires us to first determine the _expected_ schema for our API responses, which we can do using an awesome [online tool](https://jsonschema.net/). Here, we paste in a typical JSON response from the server that we know to be accurate, and the JSON schema tool will infer the schema from the object. Then it's a simple matter of using the `jsonschema` module to validate that the server always adheres to the schema with future code changes.

This repo contains:

1. Example JSON responses from the server for the APIs we want to impose a validation check on
2. The JSON schema for each API response in (1)
3. The python 3 scripts to run the validation (1 script per response to check)

The goal is that this code can be imported, in some way, into our QA tests.

**Known issues**

1. The inferred JSON schema needs to be reviewed carefully to ensure we don't unnecessarily require certain key:value pairs
2. Some more sophisticated validation (outside of the `jsonschema` module) may be required for certain responses (e.g. format of peerIds and addresses, quantity values can be anything > -1 etc)
3. There is some maintenance penalty to ensure these tests are up to date with any API changes made

**API responses to validate**

Presently, our QA tests are focused on order flows, which means that the following APIs responses should be validated:

- [x] GET /ob/profile
- [ ] GET /ob/cases
- [ ] GET /ob/case
- [ ] POST /ob/release funds
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

