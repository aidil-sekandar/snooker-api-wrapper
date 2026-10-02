# Snooker Python

> 🚧 **Under Development** — This project is currently in early development and is not yet ready for production use.

A Python wrapper for the [snooker.org](https://snooker.org/) API, designed to provide a simple Python interface for accessing professional snooker data.

## About

This project aims to make snooker.org data easier to access and use in Python without requiring users to manually handle HTTP requests and API responses.

The library is being developed with support for local caching to reduce unnecessary API requests and respect the API's rate limits.

## Current Progress

Currently implemented:

- Retrieve player information by player ID
- Local JSON caching
- Basic HTTP error handling
- Invalid player detection

More endpoints and features will be added as development continues.

## Example

```python
player = get_player(5)

print(player["FirstName"], player["LastName"])
