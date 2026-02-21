# AidNeedsAI - Humanitarian Crisis Intelligence

**Status:** 💡 Concept  
**Created:** 2026-02-21  
**Priority:** High  
**Category:** Shippable / Portfolio

## Summary

Open-source OSINT platform that aggregates real-time crisis data (social media, news, satellite imagery) to provide early-warning intelligence and live crisis tracking for humanitarian response.

## Problem

Humanitarian orgs react slowly to emerging crises. Information is scattered across Twitter/X, news sites, government reports, and satellite feeds. No unified, real-time view exists for rapid decision-making.

## Solution

A public, live crisis tracker that:
- Aggregates signals from social media, news APIs, and open satellite data
- Uses NLP/ML to detect emerging crises before they hit mainstream news
- Provides a dashboard for humanitarian orgs to monitor and prioritize
- Open-source so anyone can verify, fork, and contribute

## Tech Stack

- Python (FastAPI / Flask)
- NLP models (spaCy, transformers)
- Social media APIs (Twitter/X, Reddit)
- News APIs (GDELT, NewsAPI)
- Satellite imagery (Sentinel, open sources)
- Frontend (React / Next.js)
- Database (PostgreSQL / TimescaleDB)

## Features

- [ ] Real-time social media crisis detection
- [ ] News aggregation and summarization
- [ ] Geographic crisis mapping
- [ ] Severity scoring algorithm
- [ ] Public dashboard / API
- [ ] Alert system for emerging crises
- [ ] Historical crisis data archive

## Why This Works

| Criteria | AidNeedsAI | Drone Swarms |
|----------|------------|--------------|
| Hardware required | No | Yes ($$$) |
| Permissions needed | No | Military/state |
| Can ship in weeks | Yes | No (years) |
| Stranger can verify | Yes (5 min) | No |
| Open-source adoption | High | Zero |
| Portfolio signal | Strong | Fantasy |

## 2-Week V1 Roadmap

**Week 1:**
- [ ] Set up repo structure
- [ ] Twitter/X API integration for keyword monitoring
- [ ] Basic NLP pipeline for crisis keywords
- [ ] Simple severity scoring
- [ ] Database schema for events

**Week 2:**
- [ ] News API integration
- [ ] Basic frontend dashboard
- [ ] Geographic mapping (Leaflet/Mapbox)
- [ ] Deploy MVP (Vercel/Railway)
- [ ] Write launch post

## Potential Evolution

1. **Public live crisis tracker** — real-time global dashboard
2. **Humanitarian OSINT engine** — deeper intelligence gathering
3. **Early-warning system** — predictive alerts before crises escalate
4. **Crisis index** — quantified, citable crisis severity scores

## Notes

- Start small: one region, one crisis type
- Ship fast, iterate based on feedback
- Document everything for GitHub credibility
- Write a launch post for visibility (Twitter, Reddit, HN)

---

## Stress Test

### Shippability Test
- **Can this be built in weeks?** Yes — APIs exist, tech stack is standard
- **Hardware/permissions needed?** No — pure software, public APIs
- **Stranger can verify in 5 min?** Yes — live dashboard, public repo

### Market/Impact Test
- **Real problem?** Yes — humanitarian orgs struggle with fragmented intel
- **Crowded space?** Partially — but most tools are closed/enterprise
- **Will anyone use it?** Yes — if it works and is free/open-source

### Technical Feasibility
- **Realistic stack?** Yes — Python, React, PostgreSQL, standard NLP
- **Unsolved hard problems?** No — everything here is proven tech
- **MVP possible?** Yes — 2 weeks to basic version

### Red Flags
- None significant. Biggest risk is scope creep (adding too many data sources too fast).

---

## Final Score

| Criteria | Score | Notes |
|----------|-------|-------|
| **Shippability** | 9/10 | Can ship MVP in 2 weeks, no blockers |
| **Impact** | 8/10 | Real need, clear value for humanitarian orgs |
| **Feasibility** | 9/10 | Proven tech, well-scoped MVP |
| **Signal Value** | 9/10 | Strong portfolio piece, media-worthy, recruiter magnet |
| **TOTAL** | **35/40** | |

### Verdict: ✅ BUILD IT

This is the one. Ship fast, iterate publicly, build credibility. Start with Week 1 roadmap immediately.
