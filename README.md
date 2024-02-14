# AI RPG Quest Creator

Proof of concept project showcasing how AI can create real-time video game quests with contextual uniqueness, avoiding the cookie-cutter phenomena.

## How it Works

The AI RPG Quest Creator utilizes the following process:

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database
    participant OpenAI

    User->>Frontend: Clicks "Create Quest" button
    Frontend->>Backend: API Call /quest with JWT token and 'map'

    activate Backend
    Backend->>Backend: Extracts 'username' from JWT token
    Backend->>Database: Query user's character class using 'username'
    Database-->>Backend: Returns user's character class ('class_')

    Backend->>OpenAI: Request for quest generation
    OpenAI-->>Backend: Generates quest in JSON format
    deactivate Backend

    Backend->>Database: Save generated quest to the database
    Database-->>Backend: Confirmation of successful save

    activate Backend
    Backend-->>Frontend: Returns generated quest JSON
    deactivate Backend

    Frontend->>User: Displays generated quest to the user
