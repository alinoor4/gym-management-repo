# Gym Management Program

A lightweight, Python-based utility designed to manage gym membership records. This program operates exclusively as a Command Line Interface (CLI) tool, allowing users to perform essential CRUD (Create, Read, Update, Delete) operations on member data during a runtime session.

### Main Features
#### Member Management:
- ***Add Members:*** Captures member Name, Age, and Membership Tier (Basic, Premium, VIP) with auto-incrementing IDs.
- ***View Directory:*** Lists all currently registered members with their details.
- ***Update Records:*** Allows modification of specific fields (Name, Age, or Type) for existing members using their unique ID.
- ***Delete Members:*** Removes specific member records from the system.
- ***Menu-Driven Interface:*** Simple, looped navigation for continuous operation until exit.
- ***Input Validation:*** Basic error handling for non-numeric inputs and invalid selection choices.

#### Technical Implementation
- ***Language:*** Python 3.x
- ***Storage:*** In-memory dictionary data structure (Data is non-persistent and resets upon program exit).
- ***Interface:*** Standard I/O (Console-based).
