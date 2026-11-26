# AI-Built Products Portfolio

I build, deploy, and teach others to build working tools using AI coding
tools. Each project below has a README covering: the problem, a live demo,
the AI tool and prompts that mattered, what I fixed by hand, and how an
instructor could teach it in one session.

> Portfolio note: these projects were built over the past few months and
> assembled into this repo now. Original build timelines and AI-tool
> conversation logs are available on request.

## Projects

| Project | What it does | Live demo | Stack | AI tool |
|---|---|---|---|---|
| [Payment Reconciliation Dashboard](payment-reconciliation/) | Uploads platform + bank CSVs, classifies Duplicate / Timing / Rounding / Orphan gaps, exports a corrected ledger | [Live](#) | HTML/JS, Chart.js, SheetJS, PapaParse | Gemini + Claude |
| [Census 2026 Offline App](census-offline-app/) | 34-field survey form, saves locally, exports CSV — no internet needed | [Live](#) | HTML/JS, localStorage | Gemini + Claude |
| [Bihar Health KPI Dashboard](bihar-health-dashboard/) | District-level RMNCH+A monitoring, filters, target-vs-actual charts | [Live / run steps](#) | Python, Streamlit, Plotly | Gemini + Claude |
| [GRC Evaluation Engine](grc-evaluation-engine/) | 9-stage LLM-output evaluator: security gates, 5 parallel evals, SHAP, compliance scoring | [Live/code private]("https://rniam.com/grc/")  | Python, Gemini API | Gemini + Claude |

## How I work with AI tools

I plan the structure with the AI first, generate a first draft, then hand-fix
the parts it gets wrong — data handling, edge cases, chart rendering. Every
project README names the specific prompts that moved the build forward and
the manual fixes that followed. The planning comments at the top of
`payment-reconciliation/Dashboard.html` and the `THE FIX` note in
`bihar-health-dashboard/Dashboard_Bihar.py` are examples of that loop
preserved in the diff.

## What each project teaches (instructor angle)

- **Reconciliation:** file parsing + discrepancy logic — a one-session build, no backend.
- **Census:** forms + localStorage + CSV export — teaches data-driven UI.
- **Bihar:** mock pandas data → Plotly — teaches filters and dashboard layout.
- **GRC:** how to red-team an LLM evaluator and which gate should catch what.



## Contact

[Varun] — [github.com/varunbalotia](https://github.com/varunbalotia) — [varunbalotia@gmail.com]
