# ReliefWatch

## Overview

ReliefWatch is a public humanitarian early-warning system. It scans open-source signals during disasters, meaning social media and news. The question it answers is what kind of help is being urgently talked about, where, and how recently.

Signals surface here earlier than they do in formal reporting systems. That gives crisis analysts and first responders situational awareness at speed, so they can identify urgent needs for food, medical aid, shelter, and displacement alerts before official data is compiled.

---

## Features

*   **Multimodal Data Ingestion**: Continuous scanning of X (Twitter), Reddit, GDELT, and global news feeds. The keywords are disaster-specific.
*   **Rapid Signal Classification**: Automated tagging of signals into Food, Medical, Shelter, Displacement, and Infrastructure.
*   **Geospatial Extraction**: Locations are pulled out of unstructured text so needs can be mapped accurately. Cities, districts, states.
*   **Signal Aggregation**: Similar mentions are grouped, then counted for volume and velocity. Spikes in humanitarian need show up as they emerge.
*   **Public Accountability**: Every alert carries its source links, timestamps, and cross-source agreement.

---

## Architecture

The architecture is decoupled:

*   **Frontend**: A Next.js dashboard with interactive maps (Leaflet) and ranked alert lists. It is built to be scanned quickly.
*   **API Engine**: A FastAPI backend. It processes signals and serves crisis data through structured endpoints.
*   **Ingestion Workers**: Background workers that call the social and news APIs for real-time data.
*   **Data Store**: A PostgreSQL database holding signals, aggregated events, and geographical metadata through their lifecycle.

### Data Flow
1.  **Ingestion**: Scrapers pull raw text from public platforms when a keyword triggers.
2.  **Processing**: NLP modules classify the "Need Type" and extract location coordinates.
3.  **Aggregation**: Individual signals cluster into "Events" by proximity and timing.
4.  **Delivery**: The API serves those events to the frontend for public display.

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
With the backend running, the interactive API documentation is at:
*   **Swagger UI**: `http://localhost:8000/docs`
*   **ReDoc**: `http://localhost:8000/redoc`

---

## Configuration

Configuration lives in environment variables in `backend/.env`. The key ones:

*   `DATABASE_URL`: PostgreSQL connection string.
*   `TWITTER_BEARER_TOKEN`: For X/Twitter ingestion.
*   `REDDIT_CLIENT_ID / SECRET`: For Reddit ingestion.
*   `NEWS_API_KEY`: For NewsAPI data.

---

## Development

*   **Architecture First**: Read `BLUEPRINT.md` before making structural changes.
*   **Linting**: `black` for Python formatting, `eslint` for frontend code.
*   **Pydantic**: Data validation goes through the Pydantic models in `backend/app/models`.

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

The project is built for cloud-native deployment:

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

This project is proprietary. The source code is visible, and contributions are restricted to invited collaborators. If the project interests you, reach out to the repository owner.

---

## License

**Proprietary.** Copyright (c) 2025 Rishi Praseeth Krishnan. All rights reserved.

Visible for reference only. No license is granted to use, copy, modify, or distribute this software without express written permission. See the [LICENSE](LICENSE) file for the full legal text.
