# ReliefWatch

## Overview

ReliefWatch is a public humanitarian early-warning system designed to scan open-source signals—social media and news—during disasters. Its primary goal is to answer the core question: **"What kind of help is being urgently talked about, where, and how recently?"**

By surfacing signals earlier than formal reporting systems, ReliefWatch provides crisis analysts and first responders with high-velocity situational awareness, helping them identify urgent needs for food, medical aid, shelter, and displacement alerts before official data is compiled.

---

## Features

*   **Multimodal Data Ingestion**: Continuous scanning of X (Twitter), Reddit, GDELT, and global news feeds using disaster-specific keywords.
*   **Rapid Signal Classification**: Automated tagging of signals into categories such as Food, Medical, Shelter, Displacement, and Infrastructure.
*   **Geospatial Extraction**: Identifying specific locations (cities, districts, states) from unstructured text to map needs accurately.
*   **Signal Aggregation**: Grouping similar mentions and calculating volume and velocity to detect emergent spikes in humanitarian needs.
*   **Public Accountability**: A transparent platform showing source links, timestamps, and cross-source agreement for every alert.

---

## Architecture

ReliefWatch follows a modern decoupled architecture:

*   **Frontend**: A Next.js application providing a scannable dashboard with interactive maps (Leaflet) and ranked alert lists.
*   **API Engine**: A high-performance FastAPI backend that processes signals and serves crisis data via structured endpoints.
*   **Ingestion Workers**: Background workers that interact with various social and news APIs to pull real-time data.
*   **Data Store**: A PostgreSQL database managing the lifecycle of signals, aggregated events, and geographical metadata.

### Data Flow
1.  **Ingestion**: Scrapers pull raw text from public platforms based on keyword triggers.
2.  **Processing**: NLP modules classify the "Need Type" and extract location coordinates.
3.  **Aggregation**: Individual signals are clustered into "Events" based on proximity and timing.
4.  **Delivery**: The API serves these events to the frontend for public visualization.

---

## Tech Stack

*   **Backend**: Python 3.11, FastAPI, Pydantic, SQLAlchemy, Alembic
*   **Frontend**: Next.js (React), Tailwind CSS, Leaflet.js
*   **NLP/ML**: spaCy (Entity Recognition), Transformers (Classification), PyTorch
*   **Data APIs**: Tweepy (X/Twitter), PRAW (Reddit), GDELT, NewsAPI
*   **Database**: PostgreSQL
*   **Deployment**: Vercel (Frontend), Railway (Backend)

---

## Repository Structure

```
/backend
  /app
    /ingestion    → Platform-specific data scrapers (Twitter, Reddit, etc.)
    /models       → Pydantic schemas and database models
    /nlp          → NLP pipeline for classification and geo-extraction
    /routers      → API endpoint definitions (/alerts, /events, /stats)
    /services     → Signal aggregation and business logic
    main.py       → Main entry point for the FastAPI application
    config.py     → Environment configuration management
/frontend         → Next.js dashboard and mapping interface
/data             → Local data storage for research and static assets
/docs             → Technical documentation and design logs
BLUEPRINT.md      → Internal architecture reference and decision log
LICENSE           → Proprietary license terms
```

---

## Installation

### Prerequisites
*   Python 3.11 or higher
*   Node.js 18+
*   PostgreSQL 14+
*   API Keys: Twitter (X) Developer, Reddit API, NewsAPI

### Backend Setup
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/CodedRichy/ReliefWatch.git
    cd ReliefWatch/backend
    ```
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment**:
    ```bash
    cp .env.example .env
    # Edit .env with your database URL and API credentials
    ```
5.  **Initialize Database**:
    ```bash
    alembic upgrade head
    ```

### Frontend Setup
1.  **Navigate to frontend**:
    ```bash
    cd ../frontend
    ```
2.  **Install dependencies**:
    ```bash
    npm install
    ```

---

## Usage

### Running Locally
*   **Start the Backend**:
    ```bash
    uvicorn app.main:app --reload
    ```
*   **Start the Frontend**:
    ```bash
    npm run dev
    ```

### API Interaction
Once the backend is running, you can access the interactive API documentation at:
*   **Swagger UI**: `http://localhost:8000/docs`
*   **ReDoc**: `http://localhost:8000/redoc`

---

## Configuration

The application is configured primarily through environment variables in `backend/.env`. Key variables include:

*   `DATABASE_URL`: PostgreSQL connection string.
*   `TWITTER_BEARER_TOKEN`: For X/Twitter ingestion.
*   `REDDIT_CLIENT_ID / SECRET`: For Reddit ingestion.
*   `NEWS_API_KEY`: For NewsAPI data.

---

## Development

*   **Architecture First**: Always consult `BLUEPRINT.md` before making structural changes.
*   **Linting**: Use `black` for Python formatting and `eslint` for frontend code.
*   **Pydantic**: All data validation should be handled via Pydantic models in `backend/app/models`.

---

## Testing

ReliefWatch uses `pytest` for backend unit and integration tests.

To run tests:
```bash
cd backend
pytest
```

*(Note: Currently implementing comprehensive test coverage for NLP modules.)*

---

## Deployment

The project is designed for cloud-native deployment:

*   **Production API**: Railway (or any Docker-compliant host).
*   **Production Frontend**: Vercel.
*   **Database**: Managed PostgreSQL (Railway/RDS).

---

## Roadmap

*   [ ] **Database Schema Completion**: Finalize SQLAlchemy models for all signal types.
*   [ ] **ML Classification (V2)**: Move beyond keyword matching to Transformer-based classification.
*   [ ] **India-Wide Scale**: Expand location extraction to support all Indian states.
*   [ ] **Multilingual Support**: Implement Hindi language signal processing.
*   [ ] **Public Dashboard**: Release the first version of the Next.js frontend map.

---

## Contributing

This project is currently **Proprietary**. While the source code is visible, contributions are restricted to invited collaborators. If you are interested in the project, please reach out to the repository owner.

---

## License

**Proprietary.** Copyright (c) 2025 Rishi Praseeth Krishnan. All rights reserved.

Visible for reference only. No license is granted to use, copy, modify, or distribute this software without express written permission. See the [LICENSE](LICENSE) file for the full legal text.
