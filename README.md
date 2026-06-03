# Superset Devin Automation

Event-driven automation using the Devin API to autonomously remediate engineering issues in Apache Superset.

This project demonstrates how to leverage Devin as a core primitive for real engineering workflows — automatically turning GitHub issues into high-quality Pull Requests.

## Problem Statement
Engineering teams spend significant time on repetitive tasks such as:
- Upgrading outdated dependencies
- Remediating security vulnerabilities
- Fixing code quality and linting issues

This automation makes these workflows fast, consistent, and scalable.

## Solution Overview
- Trigger: GitHub webhook (issues event + devin-remediate label)
- Core Engine: Devin API (/sessions endpoint)
- Orchestrator: Lightweight FastAPI service running in Docker
- Outcome: Devin autonomously analyzes the issue, makes changes, and creates a Pull Request

## Key Features
- Fully event-driven architecture
- Devin API as the main automation engine (not just a helper)
- Simple observability through logs and session tracking
- Dockerized for easy deployment

## Project Structure

```
superset-devin-automation/
├── main.py                 # FastAPI app & trigger logic
├── devin_client.py         # Devin API client
├── webhook_handler.py      # GitHub webhook handler
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## Setup & Run

1. Clone the repository
2. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Fill in your credentials in .env:
   - DEVIN_API_KEY
   - DEVIN_ORG_ID

3. Start the service:
   ```bash
   docker-compose up --build
   ```

4. Expose locally using ngrok:
   ```bash
   ngrok http 8000
   ```

5. Add the ngrok URL (https://xxxx.ngrok-free.app/webhook) as a webhook in your Superset fork (select only "Issues" events).

## How to Use

- Go to your Superset fork
- Add the label `devin-remediate` to any issue
- Devin will automatically start a session and create a PR

## Observability

- Real-time logs showing webhook events and session creation
- Direct Devin session links in logs
- Pull Requests created by devin-ai-integration in the target repository

## Demo

See the Loom video for a full end-to-end demonstration.