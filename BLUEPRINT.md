# ReliefWatch — Blueprint

> Internal reference for current architecture, decisions, and implementation state.

---

## Overview

Real-time humanitarian early-warning system for India. Monitors social media, news, and satellite sources to detect emerging crises (floods, cyclones, disease outbreaks, displacement) before official reports.

---

## Current State

| Component | Status | Notes |
|-----------|--------|-------|
| Backend structure | Scaffolded | FastAPI app skeleton in `/backend` |
| Database | Not started | PostgreSQL + TimescaleDB planned |
| Ingestion: Twitter | Not started | — |
| Ingestion: Reddit | Not started | — |
| Ingestion: GDELT | Not started | — |
| Ingestion: NewsAPI | Not started | — |
| NLP pipeline | Not started | spaCy + transformers |
| Severity scoring | Not started | — |
| Frontend | Not started | Next.js + Leaflet planned |
| Deployment | Not started | Vercel (frontend) + Railway (backend) |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      NEXT.JS FRONTEND                       │
│  Full-screen map  •  Alert sidebar  •  Filters  •  Dark UI  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      FASTAPI BACKEND                        │
│  /events  •  /alerts  •  /stats  •  WebSocket (future)      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     POSTGRESQL + TIMESCALE                  │
│  events  •  sources  •  locations  •  time-series trends    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  BACKGROUND WORKERS                         │
│  Twitter ingest  •  News ingest  •  NLP pipeline  •  Scoring │
└─────────────────────────────────────────────────────────────┘
```

---

## Scope

| Dimension | V1 |
|-----------|----|
| **Region** | India |
| **Languages** | English (Hindi planned) |
| **Crisis types** | Floods, cyclones, disease outbreaks, displacement |
| **Sources** | X/Twitter, Reddit, GDELT, NewsAPI |

---

## Data Models

### CrisisEvent

```python
class CrisisEvent:
    id: str
    crisis_type: CrisisType  # flood, cyclone, disease, displacement, etc.
    location: Location       # name, state, lat/lon
    severity: Severity       # low, medium, high, critical
    confidence: float        # 0.0 - 1.0
    signal_count: int        # number of sources
    sources: list[Source]    # linked source records
    first_detected: datetime
    last_updated: datetime
    summary: str
```

### Source

```python
class Source:
    id: str
    platform: str           # twitter, reddit, news, gdelt
    url: str
    author: str | None
    posted_at: datetime
    text: str
    event_id: str           # FK to CrisisEvent
```

### Location

```python
class Location:
    name: str               # "Chennai", "Bihar"
    state: str
    country: str = "India"
    admin_level: int        # 1 = state, 2 = district, 3 = city
    latitude: float | None
    longitude: float | None
```

---

## API Endpoints

### Events

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/events` | List events with filters (type, severity, state) |
| GET | `/events/{id}` | Get single event with sources |
| GET | `/events/stats` | Aggregate stats |

### Alerts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/alerts` | Recent high-severity events |
| GET | `/alerts/recent?hours=24` | Alerts from last N hours |

### Health

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service status |
| GET | `/health` | Health check |

---

## Ingestion Sources

### Twitter/X

- **Method:** Filtered stream or search API
- **Keywords:** `flood india`, `cyclone`, `drought`, `disease outbreak`, state names + crisis terms
- **Rate limits:** Respect API tiers
- **Storage:** Raw tweets → processed events

### Reddit

- **Subreddits:** r/india, r/IndiaSpeaks, state-specific subs
- **Method:** PRAW polling
- **Filter:** Crisis-related keywords in title/body

### GDELT

- **Method:** GDELT 2.0 API
- **Filter:** India + event codes for disasters, conflicts
- **Frequency:** Hourly pulls

### NewsAPI

- **Method:** Everything endpoint
- **Keywords:** Same as Twitter
- **Sources:** Indian news outlets priority

---

## NLP Pipeline

1. **Language detection** — Filter to English (Hindi later)
2. **Crisis classification** — Multi-label: flood, cyclone, disease, displacement, other
3. **Location extraction** — NER for Indian places, normalize to state/district
4. **Severity signals** — Keywords, urgency language, casualty mentions
5. **Deduplication** — Cluster similar reports about same event

---

## Frontend Pages

| Route | Description |
|-------|-------------|
| `/` | Full-screen map with event markers, sidebar with alerts |
| `/event/{id}` | Event detail with sources, timeline |
| `/about` | What this is, limitations, methodology |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14, React, Tailwind, Leaflet |
| Backend | Python 3.11+, FastAPI, Pydantic |
| Database | PostgreSQL 15, TimescaleDB |
| NLP | spaCy, Hugging Face transformers |
| Ingestion | Tweepy, PRAW, httpx |
| Task queue | Celery + Redis (future) |
| Deployment | Vercel (FE), Railway (BE), Supabase (DB option) |

---

## Build Order

1. [x] Project structure and documentation
2. [ ] Database schema + migrations
3. [ ] Twitter ingestion worker
4. [ ] Basic NLP pipeline (classification + location)
5. [ ] API endpoints serving real data
6. [ ] Frontend: map + alert list
7. [ ] Reddit + GDELT + NewsAPI ingestion
8. [ ] Severity scoring algorithm
9. [ ] Polish: dark theme, animations, mobile
10. [ ] Deploy

---

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-21 | Focus on India, not East Africa | Familiarity with geography, language, verification |
| 2026-02-21 | Proprietary license | Not open source |
| 2026-02-21 | Start with ingestion, not frontend | Data pipeline is the hard part; UI without data is useless |

---

## Open Questions

- Twitter API tier needed? (Basic vs Pro)
- Host database on Railway or Supabase?
- Hindi language support timeline?

---

## Monetization

### Target Audiences (in order of priority)

| Audience | Why | Revenue Potential |
|----------|-----|-------------------|
| **Journalists / OSINT researchers** | Will share, give visibility | Low (free tier) |
| **NGOs / Disaster response** | Active users, slow sales | ₹50k–₹2L/year |
| **Insurance companies** | Real money, need accuracy proof | ₹5L–₹50L/year |
| **Government / NDMA** | Large contracts, slow procurement | Variable |
| **Academia** | Credibility, citations | Low |

### Revenue Model

**Phase 1 — Free launch**
- Public dashboard, no login required
- Goal: users, credibility, press coverage

**Phase 2 — Freemium**
- Free: dashboard, basic filters
- Paid: API access, custom alerts, CSV/JSON export, historical data

**Phase 3 — Enterprise**
- Data licensing for insurance/reinsurance
- Custom deployments for government
- SLAs and accuracy guarantees

### Pricing Ideas (validate later)

| Tier | Price | Includes |
|------|-------|----------|
| Free | ₹0 | Dashboard, 7-day history |
| Pro | ₹2,000/mo | API (10k calls), alerts, 1-year history |
| Enterprise | Custom | Unlimited API, SLA, custom filters, raw data |

### Grant Opportunities

- Google.org (humanitarian tech)
- Skoll Foundation
- Omidyar Network India
- USAID Development Innovation Ventures
- Bill & Melinda Gates Foundation (health crises)

---

<sub>Last updated: 2026-02-21</sub>
