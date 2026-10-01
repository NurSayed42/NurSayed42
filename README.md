<img src="assets/hero/hero.svg" width="720" alt="Nur Sayed — Lead Engineer @ VecoSoft. AI & RAG Systems, Full-Stack Engineering, Backend Architecture, Automation.">

**Full-stack engineer building reliable products, AI systems and automation.**

<img src="assets/architecture/stack.svg" width="560" alt="Layered system: 01 Frontend (React, Next.js) → 02 Backend (Spring Boot, Django, FastAPI) → 03 Database (PostgreSQL, Redis) → 04 AI (LLMs, RAG, agents) → 05 Automation (workers, queues, workflows)">

I build software products end to end — from interfaces and APIs to data, AI features and the automation around them. At VecoSoft I work across architecture, development and technical decisions, turning product requirements into systems that work reliably in real use.

<img src="assets/divider.svg" width="100%" alt="">

## Core engineering

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/architecture/icon-fullstack.svg" width="40" alt=""><br>
      <sub><b>FULL-STACK</b></sub><br>
      React, Next.js, Django, Spring Boot
    </td>
    <td width="50%" valign="top">
      <img src="assets/architecture/icon-backend.svg" width="40" alt=""><br>
      <sub><b>BACKEND</b></sub><br>
      APIs, PostgreSQL, Redis, queues, system architecture
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/architecture/icon-ai.svg" width="40" alt=""><br>
      <sub><b>AI ENGINEERING</b></sub><br>
      LLMs, RAG, retrieval, citations, AI workflows
    </td>
    <td width="50%" valign="top">
      <img src="assets/architecture/icon-automation.svg" width="40" alt=""><br>
      <sub><b>AUTOMATION</b></sub><br>
      AI agents, workflow automation, integrations
    </td>
  </tr>
</table>

## What I build

**AI systems** — retrieval that finds the right context, and answers that are checked against their sources before they reach the user.

<img src="assets/ai/rag-flow.svg" width="660" alt="RAG pipeline: Documents → Retrieval (hybrid BM25 + vector) → Context (sufficiency check) → LLM (grounded) → Answer (citations verified); failed citations trigger re-generation.">

**Backend systems** — APIs and workers designed so that work survives a failed dependency instead of disappearing.

<img src="assets/architecture/backend-flow.svg" width="660" alt="Backend flow: Request → API (transactional outbox) → Queue (Redis) → Worker (idempotent, with retries and a dead-letter queue) → Database (PostgreSQL).">

**Products** — complete features, from data model and API design through to the interface people use.

## Selected projects

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/projects/accent.svg" width="100%" alt="">
      <h3><a href="https://github.com/NurSayed42/mApML">Multi-Agent Automation Platform</a></h3>
      <p>AI agents plan and execute multi-step business tasks from one instruction, coordinated through a task DAG with an outbox, retries and a dead-letter queue.</p>
      <p><code>FastAPI</code> <code>PostgreSQL</code> <code>Redis</code> <code>LangChain</code> <code>ChromaDB</code> <code>React</code></p>
    </td>
    <td width="50%" valign="top">
      <img src="assets/projects/accent.svg" width="100%" alt="">
      <h3><a href="https://github.com/NurSayed42/legalAi">Bangladesh Legal RAG</a></h3>
      <p>Legal research assistant over Bangladesh case law and statutes, with hybrid BM25 + vector retrieval and a citation verifier for every reference.</p>
      <p><code>Python</code> <code>LangGraph</code> <code>ChromaDB</code> <code>BM25</code> <code>FastAPI</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/projects/accent.svg" width="100%" alt="">
      <h3>E-Commerce Platform</h3>
      <p>Spring Boot REST API and admin dashboard with JWT security, orders and payments, plus a React storefront.</p>
      <p><code>Spring&nbsp;Boot</code> <code>PostgreSQL</code> <code>React</code> <code>Redux&nbsp;Toolkit</code></p>
      <p><a href="https://github.com/NurSayed42/ECommerceBackend">Backend</a> · <a href="https://github.com/NurSayed42/eCommerceFrontend">Frontend</a> · <a href="https://e-commerce-frontend-five-snowy.vercel.app">Live demo</a></p>
    </td>
    <td width="50%" valign="top">
      <img src="assets/projects/accent.svg" width="100%" alt="">
      <h3><a href="https://github.com/NurSayed42/swe-internship-experience">Engineering Case Studies</a></h3>
      <p>Architecture write-ups of systems built in a banking environment: a real-time conference prototype and an automation pipeline with an OCR microservice. Source not public.</p>
      <p><code>Spring&nbsp;Boot</code> <code>Selenium</code> <code>FastAPI</code> <code>PaddleOCR</code></p>
    </td>
  </tr>
</table>

## How I think about engineering

- **Reliability over happy-path demos** — a system is judged by how it behaves with bad input, slow dependencies and partial failure.
- **AI should be grounded and verifiable** — answers trace back to sources, and "not enough information" beats a confident guess.
- **Systems should recover from failure** — retries, idempotent writes and dead-letter handling mean work isn't silently lost.
- **Ship the complete product** — data model, API and interface are designed together, not as isolated features.

## Current focus

AI engineering · RAG systems · Backend architecture · Automation · Production-ready product engineering

## Tech stack

<table>
  <tr>
    <td width="150"><sub><b>LANGUAGES</b></sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=py,java,js,ts&theme=dark">
        <img src="https://skillicons.dev/icons?i=py,java,js,ts&theme=light" height="36" alt="Python, Java, JavaScript, TypeScript">
      </picture>
    </td>
  </tr>
  <tr>
    <td><sub><b>FRONTEND</b></sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=react,nextjs&theme=dark">
        <img src="https://skillicons.dev/icons?i=react,nextjs&theme=light" height="36" alt="React, Next.js">
      </picture>
    </td>
  </tr>
  <tr>
    <td><sub><b>BACKEND</b></sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=spring,django,fastapi&theme=dark">
        <img src="https://skillicons.dev/icons?i=spring,django,fastapi&theme=light" height="36" alt="Spring Boot, Django, FastAPI">
      </picture>
    </td>
  </tr>
  <tr>
    <td><sub><b>DATA / INFRA</b></sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=postgres,redis,docker&theme=dark">
        <img src="https://skillicons.dev/icons?i=postgres,redis,docker&theme=light" height="36" alt="PostgreSQL, Redis, Docker">
      </picture>
    </td>
  </tr>
  <tr>
    <td><sub><b>AI</b></sub></td>
    <td>LLMs · RAG · ChromaDB · LangChain · LangGraph · Gemini &amp; Groq APIs</td>
  </tr>
</table>

## GitHub activity

Recently updated public repositories. The full contribution graph is shown below this README.

<!-- ACTIVITY:START -->
| Repository | Description | Last push |
|---|---|---|
| [swe-internship-experience](https://github.com/NurSayed42/swe-internship-experience) | Architecture and engineering case studies from software systems built in a banking environment. Source code is not public. | Oct 2026 |
| [eCommerceFrontend](https://github.com/NurSayed42/eCommerceFrontend) | React storefront for a Spring Boot e-commerce API using Redux Toolkit, Tailwind CSS and JWT-aware API integration. | Oct 2026 |
| [ECommerceBackend](https://github.com/NurSayed42/ECommerceBackend) | E-commerce REST API and admin dashboard built with Spring Boot, PostgreSQL and JWT-based security. | Oct 2026 |
| [mApML](https://github.com/NurSayed42/mApML) | Multi-agent AI platform that breaks business instructions into tasks executed by specialized agents. FastAPI, PostgreSQL, Redis, LangChain, ChromaDB and React. | Oct 2026 |
<!-- ACTIVITY:END -->

<img src="assets/divider.svg" width="100%" alt="">

## Let's build something useful

[GitHub](https://github.com/NurSayed42) &nbsp;·&nbsp; [VecoSoft](https://vecosoft.com)
