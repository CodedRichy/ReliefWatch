# ReliefWatch - Project Planning

**Status:** Concept  
**Created:** 2026-02-21  
**Priority:** High

---

## Summary

Real-time humanitarian early-warning system that aggregates crisis data (social media, news, satellite imagery) to provide intelligence for humanitarian response.

---

## Problem

Humanitarian orgs react slowly to emerging crises. Information is scattered across Twitter/X, news sites, government reports, and satellite feeds. No unified, real-time view exists for rapid decision-making.

---

## Solution

A live crisis tracker that:
- Aggregates signals from social media, news APIs, and open satellite data
- Uses NLP/ML to detect emerging crises before they hit mainstream news
- Provides a dashboard for humanitarian orgs to monitor and prioritize

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python (FastAPI) |
| NLP | spaCy, Hugging Face Transformers |
| Data Sources | X/Twitter API, Reddit API, GDELT, NewsAPI, Sentinel |
| Frontend | React / Next.js |
| Database | PostgreSQL / TimescaleDB |
| Mapping | Leaflet / Mapbox |

---

## Features

- [ ] Real-time social media crisis detection
- [ ] News aggregation and summarization
- [ ] Geographic crisis mapping
- [ ] Severity scoring algorithm
- [ ] Public dashboard / API
- [ ] Alert system for emerging crises
- [ ] Historical crisis data archive

---

## 2-Week MVP Roadmap

### Week 1 — Foundation
- [ ] Set up repo structure
- [ ] Twitter/X API integration for keyword monitoring
- [ ] Basic NLP pipeline for crisis keywords
- [ ] Simple severity scoring
- [ ] Database schema for events

### Week 2 — MVP
- [ ] News API integration
- [ ] Basic frontend dashboard
- [ ] Geographic mapping (Leaflet/Mapbox)
- [ ] Deploy MVP (Vercel/Railway)
- [ ] Write launch post

---

## Post-MVP

1. Public live crisis tracker — real-time global dashboard
2. Humanitarian OSINT engine — deeper intelligence gathering
3. Early-warning system — predictive alerts before crises escalate
4. Crisis index — quantified, citable crisis severity scores

---

## Notes

- Start small: one region, one crisis type
- Ship fast, iterate based on feedback
- Document everything for credibility
- Biggest risk: scope creep (adding too many data sources too fast)
