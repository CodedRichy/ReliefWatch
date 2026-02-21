# ReliefWatch

**Early-warning signals for humanitarian needs, surfaced from public sources before official reports exist.**

---

## What This Is

ReliefWatch is a public humanitarian early-warning system.

It continuously scans open signals—social media and news—during disasters and answers one question:

> "What kind of help is being urgently talked about, where, and how recently?"

It does **not**:
- Verify ground truth
- Coordinate aid
- Replace official reports

It surfaces signals earlier than formal systems, so humans can decide faster.

---

## How It Works

```
┌──────────────────────────────────────────────────────────────┐
│                     DATA INGESTION                           │
│  Twitter  •  Reddit  •  GDELT  •  News APIs                  │
│  Keywords: flood, cyclone, displacement, medical emergency   │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                   SIGNAL CLASSIFICATION                      │
│  Food  •  Medical  •  Shelter  •  Displacement  •  Infra     │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                   SIGNAL AGGREGATION                         │
│  Group similar mentions  •  Count volume  •  Detect spikes   │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                        OUTPUT                                │
│  Ranked needs  •  Locations  •  Timestamps  •  Source links  │
└──────────────────────────────────────────────────────────────┘
```

---

## What You See

A public page showing:

**Latest Alerts**
> "Food shortage — Barpeta, Assam (↑ spike in last 6h)"

**Map**
- Dots marking locations with active signals

**Transparency**
- Source links for every signal
- Timestamps
- Signal counts

**Disclaimer**
> "These are signals, not verified ground truth."

No login. No friction. Scannable in under 60 seconds.

---

## Example Output

```
ALERT: Food shortage
LOCATION: Barpeta, Assam
LAST 6 HOURS: 47 mentions (↑ 520% vs baseline)
NEED TYPE: Food

SOURCES:
1. @AssamTribune - "Heavy flooding, markets closed in Barpeta..."
   twitter.com/... • 2 hours ago

2. NDTV - "Assam floods: 50,000 affected as Brahmaputra rises"
   ndtv.com/... • 4 hours ago

3. r/india - "Any updates on relief camps in Barpeta district?"
   reddit.com/... • 5 hours ago
```

---

## Current Scope

| Dimension | V1 Coverage |
|-----------|-------------|
| **Region** | India |
| **Languages** | English (Hindi planned) |
| **Crisis types** | Floods, cyclones, disease outbreaks, displacement |
| **Sources** | X/Twitter, Reddit, GDELT, NewsAPI |

Starting narrow is intentional. Expansion follows validation.

---

## Who This Is For

**Crisis analysts and OSINT researchers**
- Early signals before official reports
- Transparent methodology

**Journalists**
- Fast situational awareness
- Quotable, shareable outputs

**NGOs and disaster responders**
- Informal reference during active events
- No vendor lock-in

---

## Who This Is NOT For

- General public seeking news (use news sites)
- Automated decision-making (requires human judgment)
- Legal documentation (signals are unverified)
- Tactical response (latency too high)

---

## Known Limitations

**Signals, not facts**
- Social media contains rumors and misinformation
- No ground verification
- Confidence reflects volume and recency, not truth

**Coverage gaps**
- Internet blackouts create blind spots
- Populations without internet access are invisible
- Urban/English bias

**Technical constraints**
- Platform API changes may disrupt access
- Location extraction relies on text mentions
- Classification is keyword-based (V1)

Users should treat outputs as leads for investigation, not confirmed reports.

---

## License

**Proprietary.** This repository is visible for reference only. No license is granted to use, copy, modify, or distribute this software. See [LICENSE](LICENSE) for details.

---

## Project Status

**Status:** Active Development  
**Version:** Pre-release

---

<sub>Copyright 2025 Rishi Praseeth Krishnan. All rights reserved.</sub>
