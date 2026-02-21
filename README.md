# ReliefWatch

**Early-warning signals for humanitarian needs, extracted from open sources before official reports exist.**

---

## Problem

Humanitarian crises unfold faster than institutions can document them.

Formal situation reports from UN agencies, governments, and NGOs typically lag 24–72 hours behind real events. In rapidly evolving emergencies—displacement surges, disease outbreaks, supply chain collapses—this delay costs lives. By the time a report is published, needs have already shifted.

Meanwhile, fragments of ground truth surface continuously in real time: local news, social media posts, community radio transcriptions, government bulletins. This information exists but remains scattered, unstructured, and inaccessible to responders who need it most.

Crisis analysts currently rely on manual monitoring, keyword alerts, and institutional sitreps. This workflow is reactive by design. It waits for confirmation rather than identifying emerging patterns.

---

## What ReliefWatch Does

ReliefWatch aggregates real-time crisis data from social media, news, and open satellite sources to provide early-warning intelligence for humanitarian response.

Specifically, it:

- Ingests posts from social media platforms (X/Twitter, Reddit), news APIs (GDELT, NewsAPI), and open satellite imagery
- Uses NLP to detect emerging crises and classify need categories: **food insecurity**, **medical emergencies**, **shelter/displacement**, **water/sanitation**
- Extracts geographic references and maps them to administrative boundaries
- Assigns severity scores and tracks signal frequency over time
- Provides a public dashboard for monitoring and prioritization
- Outputs structured alerts with source links, timestamps, and confidence indicators

ReliefWatch does not replace verified reporting. It surfaces *candidates* for further investigation—signals that may warrant analyst attention before formal confirmation arrives.

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                             │
│  X/Twitter  •  Reddit  •  GDELT  •  NewsAPI  •  Sentinel        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      INGESTION LAYER                            │
│  Rate-limited collection  •  Deduplication  •  Language detect  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NLP PIPELINE                                 │
│  Crisis detection (spaCy, transformers)  •  Location extraction │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     SIGNAL AGGREGATION                          │
│  Clustering  •  Severity scoring  •  Geographic mapping         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         OUTPUT                                  │
│  Dashboard  •  Public API  •  Alerts  •  JSON export            │
└─────────────────────────────────────────────────────────────────┘
```

All outputs include direct links to source material. Nothing is synthesized without attribution.

---

## Features

- [ ] Real-time social media crisis detection
- [ ] News aggregation and summarization
- [ ] Geographic crisis mapping
- [ ] Severity scoring algorithm
- [ ] Public dashboard and API
- [ ] Alert system for emerging crises
- [ ] Historical crisis data archive

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python (FastAPI) |
| **NLP** | spaCy, Hugging Face Transformers |
| **Data Sources** | X/Twitter API, Reddit API, GDELT, NewsAPI, Sentinel (satellite) |
| **Frontend** | React / Next.js |
| **Database** | PostgreSQL / TimescaleDB |
| **Mapping** | Leaflet / Mapbox |

---

## Current Scope

ReliefWatch starts narrow and expands based on validated performance:

| Dimension | V1 Coverage |
|-----------|-------------|
| **Regions** | Single region (configurable—default: East Africa) |
| **Languages** | English (additional languages planned) |
| **Crisis types** | Food insecurity, displacement, disease outbreaks |
| **Data sources** | X/Twitter, Reddit, GDELT, NewsAPI |
| **Update frequency** | Near real-time ingestion, configurable aggregation |

Starting small is intentional. Scope creep is the main risk for projects like this. Expansion proceeds only where output quality can be verified.

---

## Example Output

```
ALERT #2847
Generated: 2026-02-21 14:32 UTC

CRISIS TYPE:    Food insecurity
LOCATION:       North Darfur, Sudan (Admin Level 1)
COORDINATES:    15.7833° N, 32.5500° E (centroid)
SEVERITY:       High (0.78)
CONFIDENCE:     Medium (0.67)

SIGNAL SUMMARY:
- 23 social media posts in past 6 hours referencing food shortages
- 4 news articles mentioning market closures in El Fasher
- Spike detected: 340% above 7-day baseline for this region

TOP SOURCES:
1. [X/Twitter] @SudanTribune - "Reports of empty markets in El Fasher..."
   Posted: 2026-02-21 12:15 UTC
   Link: https://twitter.com/...

2. [News] Reuters - "Food supplies disrupted in North Darfur amid conflict"
   Published: 2026-02-21 09:00 UTC
   Link: https://reuters.com/...

3. [GDELT] Event detected - Food security, Sudan
   Logged: 2026-02-21 11:47 UTC

LIMITATIONS:
- No ground verification available
- Location extracted from text, not geotagged
- Source accounts not independently verified

RECOMMENDED ACTION:
- Cross-reference with OCHA Sudan updates
- Monitor WFP food security bulletins
- Flag for analyst review
```

---

## Why This Matters

Crisis response operates on the edge of available information. Decisions about resource pre-positioning, evacuation routes, and supply chain activation often cannot wait for confirmed reports.

Early signals—even imperfect ones—allow responders to:

- Begin logistical planning before official confirmation
- Identify geographic hotspots that may be underreported
- Detect emerging needs that fall outside standard monitoring categories
- Track how conditions change between formal reporting cycles

A verified sitrep arriving 48 hours after an event is valuable for documentation. A probabilistic signal arriving 6 hours before that sitrep is valuable for *action*.

ReliefWatch does not claim to replace institutional reporting. It claims to fill the gap before institutional reporting begins.

---

## Known Limitations

**Data quality:**
- Social media posts may contain rumors, misinformation, or deliberate disinformation
- Geographic extraction relies on text mentions; coordinates are estimated centroids, not precise locations
- Language models make errors in classification and extraction, particularly for informal Arabic dialects

**Coverage gaps:**
- Internet blackouts and communication disruptions create blind spots precisely when crises escalate
- Populations without internet access are structurally invisible to this system
- Signals skew toward urban areas and literate populations

**Verification:**
- ReliefWatch outputs are *unverified signals*, not confirmed facts
- Confidence scores reflect statistical patterns, not ground truth
- No automated system can replace human judgment or field verification

**Ethical considerations:**
- Publicizing location data during active conflict may endanger affected populations
- Source accounts may face retaliation if their posts are amplified
- Aggregated data could be misused by malicious actors

**Operational constraints:**
- Platform API changes may disrupt data access without warning
- Processing delays during high-volume events
- Model drift requires ongoing calibration

Users should treat ReliefWatch outputs as *leads for investigation*, not as reportable facts.

---

## Roadmap

**Week 1 — Foundation:**
- [ ] Repository structure and development environment
- [ ] X/Twitter API integration for keyword monitoring
- [ ] Basic NLP pipeline for crisis keyword detection
- [ ] Simple severity scoring algorithm
- [ ] Database schema for events

**Week 2 — MVP:**
- [ ] News API integration (GDELT, NewsAPI)
- [ ] Basic frontend dashboard
- [ ] Geographic mapping (Leaflet/Mapbox)
- [ ] Deploy MVP (Vercel/Railway)
- [ ] Documentation and launch

**Post-MVP:**
- [ ] Historical crisis data archive
- [ ] Alert system for emerging crises
- [ ] Source credibility scoring
- [ ] Additional language support
- [ ] Satellite imagery integration (Sentinel)

Development priorities are driven by feedback from users. Ship fast, iterate publicly, document everything.

---

## Who Should Use This

**This tool is designed for:**

- **Crisis analysts** tracking emerging situations
- **OSINT researchers** investigating conflict and displacement patterns
- **Journalists** seeking early leads on underreported emergencies
- **NGO operations teams** planning resource deployment
- **Academic researchers** studying humanitarian early warning systems

**This tool is NOT designed for:**

- General public seeking news updates (use established news sources)
- Automated decision-making without human review
- Legal or evidentiary documentation (outputs are unverified)
- Real-time tactical response (latency too high, verification insufficient)
- Monitoring outside current geographic scope (outputs will be unreliable)

---

## Contributing

ReliefWatch is open source. Contributions are welcome in:

- Language model evaluation for under-resourced languages
- Geographic normalization for additional regions
- Integration with humanitarian data standards
- Documentation and translation

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Project Status

**Status:** Active Development  
**Version:** Pre-release (MVP in progress)

This project is under active development. Core functionality is being built. Contributions and feedback welcome.

---

<sub>Last updated: February 2026</sub>
