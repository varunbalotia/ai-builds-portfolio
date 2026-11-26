# GRC Evaluation Engine (LLM-as-a-Judge)

A live, 9-stage pipeline that evaluates AI-generated text for safety, bias, hallucination risk, and compliance. 

**Live demo:** [AI Governance & Compliance Engine](https://rniam.com/grc/)

> **Note:** The core Python engine and detection patterns are kept private (proprietary logic). This repository contains the architecture documentation, evaluation design, and proof of deployment.

![Scorecard](screenshot-scorecard.png)

## 1. The problem

Deploying LLMs in enterprise or high-stakes environments (medical, legal, financial) requires strict governance. Manual review of AI outputs is slow and subjective. Organizations need an automated, multi-dimensional "judge" that can evaluate outputs for RAGAS quality, bias, source credibility, and regulatory compliance (EU AI Act, NIST, ISO 42001) before a human ever reads them.

## 2. The Architecture

The engine is built in Python and uses the **Gemini API** for semantic extraction and deep evaluation. It includes a two-phase security gate to block prompt injection and PII leakage before any expensive API calls are made. The UI is a custom web frontend that consumes the evaluation results in real-time.

```mermaid
flowchart TD
    A[Input: structured or raw text] --> B[Gemini extraction → normalize]
    B --> C{Security Gate 1<br/>16-pattern heuristic scan}
    C -- 2+ hits --> X[ABORT: blocked=true]
    C --> D[Gemini deep semantic scan]
    D -- critical finding --> X
    D --> E[5 Parallel Evaluations<br/>RAGAS · Bias · Source · Gap · Tone]
    E --> F[SHAP attribution + confidence calibration]
    F --> G[Domain detection: medical/legal/financial]
    G --> H[Compliance: 6 generic + 3 domain checks]
    H --> I[Tier assignment + escalation]
    I --> J[GRC score = weighted composite]
    J --> K[Score card + audit trail → JSON]
