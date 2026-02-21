# ReliefWatch — Blueprint

> Internal reference for architecture, decisions, and implementation state.

---

## What This Is

ReliefWatch is a **public humanitarian early-warning system**.

It continuously scans open, public signals (social media + news) during disasters and answers one core question:

> "What kind of help is being urgently talked about, where, and how recently?"

**It does not:**
- Verify ground truth
- Coordinate aid
- Replace official reports

**It surfaces signals earlier than formal systems, so humans can decide faster.**

Think of it as:
- Google Trends, but for humanitarian needs
- OSINT, but focused on food, shelter, medical aid, displacement

---

## What the System Does

### 1. Data Ingestion
- Pulls recent posts/articles using disaster-specific keywords
- Light geo-bias (place names, regions, hashtags)
- Time-bounded (last X hours)

### 2. Signal Classification
Each post/article is tagged into:
- Food
- Medical
- Shelter
- Displacement
- Infrastructure
- Unknown / noise

No black-box magic. Keep it interpretable.

### 3. Signal Aggregation
The system:
- Groups similar mentions
- Counts volume + velocity (spikes)
- Weights by recency and cross-source agreement

### 4. Output
Produces a ranked list of needs:
- What is needed
- Where
- How recent
- How many sources

This output is publicly visible.

---

## What the User Sees

A public page showing:

**Latest Alerts**
> "Food shortage — Aluva (↑ spike in last 6h)"

**Simple Map**
- Dots marking locations

**Transparency**
- Source links
- Timestamps
- Counts

**Disclaimer**
> "Signals, not verified ground truth"

No login. No interaction friction. Designed to be scannable in under 60 seconds.

---

## Audience

### Primary (Build for these)

**1. Crisis Analysts / OSINT Community**
- Track conflicts and disasters
- Care about early signals, not dashboards
- Will respect clean methodology

**2. Journalists**
- Need fast situational awareness
- Love quotable tools
- Value transparency over accuracy claims

*These people amplify you.*

### Secondary (Validation, not growth)

**3. NGOs (Small–Mid)**
- Local disaster response orgs
- Use outputs informally
- Won't pay yet, but might reference you

### Tertiary (Silent but critical)

**4. Recruiters / Engineers / Seniors**
- Asking: "Can this person design a real system under constraints?"
- ReliefWatch answers yes.

---

## Why No Monetization (Yet)

Monetization right now would:
- Distort design decisions
- Force NGO sales
- Slow you down
- Make you overpromise

**You don't have leverage yet.**

Current currency is:
- Visibility
- Credibility
- Public proof of skill

Trying to monetize early is how projects die quietly.

### When Monetization Becomes Legit

Only after:
- People cite or share it
- Someone asks "can we get alerts for X?"
- An org uses it during a real event

Then monetization becomes pull-based, not push-based.

Possible future paths:
- Custom regional deployments
- Private alert feeds
- Crisis-specific reports
- Grants / fellowships

**None of this is V1.**

---

## Current State

| Component | Status | Notes |
|-----------|--------|-------|
| Backend structure | Scaffolded | FastAPI skeleton in `/backend` |
| Database | Not started | PostgreSQL planned |
| Ingestion: Twitter | Not started | — |
| Ingestion: Reddit | Not started | — |
| Ingestion: GDELT | Not started | — |
| Ingestion: NewsAPI | Not started | — |
| NLP pipeline | Not started | Classification + location extraction |
| Signal aggregation | Not started | — |
| Frontend | Not started | Next.js + Leaflet |
| Deployment | Not started | Vercel (FE) + Railway (BE) |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      NEXT.JS FRONTEND                       │
│  Map  •  Alert list  •  Filters  •  Source links  •  Dark   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      FASTAPI BACKEND                        │
│  /alerts  •  /events  •  /stats                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       POSTGRESQL                            │
│  events  •  sources  •  locations                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   BACKGROUND WORKERS                        │
│  Ingest (Twitter, Reddit, News)  •  Classify  •  Aggregate  │
└─────────────────────────────────────────────────────────────┘
```

---

## Scope (V1)

| Dimension | Coverage |
|-----------|----------|
| **Region** | India |
| **Languages** | English (Hindi later) |
| **Crisis types** | Floods, cyclones, disease outbreaks, displacement |
| **Sources** | X/Twitter, Reddit, GDELT, NewsAPI |

---

## Data Models

### Signal (raw input)

```python
class Signal:
    id: str
    platform: str           # twitter, reddit, news
    url: str
    text: str
    author: str | None
    posted_at: datetime
    location_raw: str | None  # extracted from text
```

### Event (aggregated output)

```python
class Event:
    id: str
    need_type: NeedType     # food, medical, shelter, displacement, infrastructure
    location: Location
    signal_count: int
    velocity: float         # spike indicator
    first_seen: datetime
    last_seen: datetime
    sources: list[Signal]
```

### Location

```python
class Location:
    name: str               # "Chennai", "Barpeta"
    state: str              # "Tamil Nadu", "Assam"
    latitude: float | None
    longitude: float | None
```

### NeedType

```python
class NeedType(Enum):
    FOOD = "food"
    MEDICAL = "medical"
    SHELTER = "shelter"
    DISPLACEMENT = "displacement"
    INFRASTRUCTURE = "infrastructure"
    UNKNOWN = "unknown"
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/alerts` | Ranked list of current needs |
| GET | `/alerts?state=assam` | Filter by state |
| GET | `/alerts?type=flood` | Filter by need type |
| GET | `/events/{id}` | Single event with sources |
| GET | `/health` | Health check |

---

## Frontend

**Single page. No routing complexity.**

| Section | Content |
|---------|---------|
| Header | "ReliefWatch" + last updated timestamp |
| Map | Leaflet, dots for locations, click for details |
| Alert List | Ranked needs, expandable for sources |
| Filters | State, need type, time range |
| Footer | Disclaimer, methodology link, source attribution |

**Design:**
- Dark theme
- Scannable in 60 seconds
- No login
- Mobile-friendly

---

## Build Order

1. [x] Project structure and documentation
2. [ ] Database schema
3. [ ] Twitter ingestion (keywords: flood, cyclone, disaster + India regions)
4. [ ] Basic classification (keyword-based first, ML later)
5. [ ] Location extraction (regex + gazetteer)
6. [ ] Aggregation logic (group, count, spike detection)
7. [ ] API endpoints
8. [ ] Frontend: map + alert list
9. [ ] Add Reddit, GDELT, NewsAPI
10. [ ] Polish and deploy

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js, React, Tailwind, Leaflet |
| Backend | Python 3.11+, FastAPI, Pydantic |
| Database | PostgreSQL |
| NLP | Keyword matching (V1), spaCy (V2) |
| Ingestion | Tweepy, PRAW, httpx |
| Deployment | Vercel (FE), Railway (BE) |

---

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-21 | India focus | Familiarity, verification ability |
| 2026-02-21 | Proprietary license | Not open source |
| 2026-02-21 | No monetization in V1 | Build credibility first |
| 2026-02-21 | Keyword classification first | Interpretable, ship fast, ML later |
| 2026-02-21 | Single-page frontend | Scannable, no friction |

---

## What This Project Says About You

Without saying a word, ReliefWatch signals:
- You understand systems, not just models
- You care about real-world constraints
- You can ship public, usable tools
- You think beyond coursework

---

<sub>Last updated: 2026-02-21</sub>
