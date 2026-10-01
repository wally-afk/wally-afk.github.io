# PORTFOLIO SPECIFICATION

## Waleed Sabir — Data Analytics · Data Engineering · Applied Machine Learning

---

# 1. PROJECT OBJECTIVE

Build a premium, single-page personal portfolio for **Waleed Sabir**, positioned at the intersection of:

* Data Analytics
* Business Intelligence
* Data Engineering
* Applied Machine Learning
* Workflow Automation

The portfolio should demonstrate technical ability **through the interface itself**.

The website should not feel like a generic developer portfolio or an AI-generated template.

The core principle:

> **The website should feel like a data system that happens to be a portfolio.**

A recruiter should be able to understand:

1. Who Waleed is
2. What he does
3. What technologies he uses
4. What problems he has solved
5. What measurable results his projects produced
6. How his data systems are structured
7. How to inspect his work

within approximately **30 seconds**.

---

# 2. DESIGN PHILOSOPHY

### Primary aesthetic

**Swiss Minimalism × Linear × Data Visualization × Subtle Terminal UI**

Use:

* Strong typography
* Dense but organized information
* Asymmetrical Bento Grid
* Thin borders
* Precise spacing
* Data-oriented visualizations
* Subtle interaction
* Restrained animation
* High information density

Avoid making the website look like:

* A generic SaaS landing page
* A cyberpunk website
* A "hacker terminal"
* An AI-generated portfolio template
* A cryptocurrency dashboard

The visual balance should be approximately:

**70% Swiss / Linear minimalism**
**20% data visualization / analytical UI**
**10% terminal aesthetic**

---

# 3. TECHNOLOGY CONSTRAINTS

The initial implementation should remain deliberately simple.

### Core

* HTML5
* Tailwind CSS via CDN
* Vanilla JavaScript
* SVG for custom diagrams
* CSS Grid
* CSS animations/transitions

### No requirement for:

* React
* Next.js
* Vite
* Webpack
* Node.js build pipelines

The site should be deployable as a lightweight static website.

Architecture should make it easy to migrate to a framework later if necessary.

---

# 4. COLOR SYSTEM

### Background

```text
Void Background
#090A0F
```

### Primary Card

```text
Dark Slate
#12131A
```

### Secondary Surface

```text
#171922
```

### Borders

Default:

```text
rgba(255,255,255,0.08)
```

Hover:

```text
rgba(255,255,255,0.20)
```

Active:

```text
rgba(255,255,255,0.30)
```

### Primary Text

```text
#F5F7FA
```

### Secondary Text

```text
#8B909B
```

### Functional Accent

Emerald:

```text
#10B981
```

Use for:

* Availability
* Live status
* Successful states
* Positive system indicators

Cyan:

```text
#06B6D4
```

Use for:

* Data flow
* Interactive elements
* Pipeline connections
* Analytical highlights

Accent colors should remain **functional rather than decorative**.

Do not flood the interface with green/cyan.

---

# 5. TYPOGRAPHY

### Primary Typeface

**Inter**

Use for:

* Hero
* Headings
* Descriptions
* Navigation
* Project titles

### Technical Typeface

**JetBrains Mono**

Use for:

* Metrics
* Technology tags
* Dataset information
* Code
* System labels
* Architecture diagrams
* Metadata
* Small technical annotations

### Typography principle

Large text should be extremely clean.

Technical information should feel like instrumentation.

Example:

```text
99,441
ORDERS PROCESSED
```

rather than:

```text
I analyzed over 99,441 orders
```

---

# 6. GLOBAL LAYOUT

Desktop:

```text
max-width: 1400px
margin: auto
padding: 24px–48px
```

Mobile:

```text
padding: 16px–20px
```

Use CSS Grid for the main portfolio layout.

Cards should have:

```text
border-radius: 14px–18px
border: 1px solid rgba(255,255,255,.08)
background: #12131A
```

Avoid excessive rounded "pill" interfaces.

Pills should primarily be reserved for:

* Technologies
* Status
* Small metadata

---

# 7. NAVIGATION

Minimal fixed/sticky navigation.

Desktop:

```text
WALEED SABIR

WORK    SYSTEMS    ABOUT    CONTACT

                    ● AVAILABLE
```

The navigation should remain extremely compact.

### Navigation behavior

* Transparent/dark background initially
* Slight backdrop blur after scrolling
* Thin bottom border
* Smooth anchor scrolling

Mobile:

```text
WALEED SABIR                         MENU
```

---

# 8. HERO SECTION

The hero should immediately establish professional identity.

### Eyebrow

```text
DATA ANALYTICS · ENGINEERING · APPLIED ML
```

### Main heading

```text
Turning complex data
into useful systems.
```

Alternative supporting line:

```text
I build analytical pipelines, predictive models,
business intelligence systems and automated workflows.
```

Avoid generic statements such as:

> Passionate data scientist with a passion for data.

The writing should be concise and technically grounded.

---

# 9. HERO STATUS

Display:

```text
● AVAILABLE FOR OPPORTUNITIES
```

Emerald pulsing indicator.

Animation should be subtle.

No aggressive flashing.

---

# 10. HERO TECH STACK

Immediately below the hero:

```text
PYTHON     SQL     POWER BI     DAX     POSTGRESQL
```

Use JetBrains Mono.

Each technology appears as a compact technical badge.

---

# 11. PORTFOLIO TELEMETRY

Instead of fake skill percentages, display **real portfolio statistics**.

Example:

```text
┌─────────────────────────────────────────────────────────┐
│ PORTFOLIO TELEMETRY                                     │
│                                                         │
│  PROJECTS       DATA PROCESSED      TECHNOLOGIES        │
│      06              100K+               15+            │
│                                                         │
│  BI SYSTEMS     ML MODELS            AUTOMATIONS        │
│      02              03                  01             │
└─────────────────────────────────────────────────────────┘
```

Only display metrics that can be substantiated.

If a metric changes, it should be easy to update from one central JavaScript data object.

---

# 12. PROJECT ARCHITECTURE

Projects should be presented as **case studies**, not simple cards.

Each project card should communicate:

```text
PROBLEM
↓
DATA
↓
PIPELINE
↓
MODEL / ANALYSIS
↓
RESULT
```

Each project should contain:

* Project title
* Domain
* Problem statement
* Dataset scale
* Technologies
* Architecture
* Key metrics
* Visual evidence
* Links

---

# 13. FEATURED PROJECT — OLIST E-COMMERCE INTELLIGENCE

This is the primary project.

Give it the largest visual footprint.

### Header

```text
01 / E-COMMERCE INTELLIGENCE
MASTER'S THESIS
```

### Title

```text
Olist Marketplace
Analytics Platform
```

### Description

```text
An end-to-end business intelligence system transforming
Brazilian e-commerce marketplace data into sales,
logistics and product intelligence.
```

### Technology tags

```text
SQL
POWER BI
DAX
STAR SCHEMA
SSAS
```

Use only technologies actually used in the project.

---

# 14. OLIST METRICS

Display large metric blocks.

Example:

```text
99,441
ORDERS

6+
DATA DOMAINS

2016—2018
DATA PERIOD

5
ANALYTICAL AREAS
```

Avoid invented metrics.

Any derived performance metric must clearly identify its basis.

For example:

```text
+18.4%
MODEL LIFT
```

with a tooltip explaining:

```text
Relative improvement compared with baseline.
```

If a result is projected rather than observed:

```text
178%
PROJECTED ROI
```

Never present projected results as realized business outcomes.

---

# 15. OLIST DATA PIPELINE VISUALIZATION

Create an interactive SVG architecture.

```text
SOURCE DATA
     │
     ▼
DATA VALIDATION
     │
     ▼
SQL TRANSFORMATION
     │
     ▼
STAR SCHEMA
     │
     ├──────────────┐
     ▼              ▼
FACT TABLES     DIMENSIONS
     │              │
     └──────┬───────┘
            ▼
       BI / ANALYTICS
            │
      ┌─────┼─────┐
      ▼     ▼     ▼
    SALES LOGISTICS PRODUCTS
```

Use subtle animated cyan connection lines.

Hovering a stage should highlight that stage.

---

# 16. INTERACTIVE DATA MODEL

Include an expandable:

```text
[ INSPECT DATA MODEL ]
```

When opened, show the simplified star schema.

Example:

```text
                 DIM_CUSTOMER
                      │
                      │
DIM_PRODUCT ───► FACT_ORDER ◄─── DIM_SELLER
                      │
                      │
                  DIM_DATE
                      │
                      ▼
                FACT_PAYMENT
```

Clicking a table should display metadata.

Example:

```text
FACT_ORDER

GRAIN
1 row per order

ROWS
99,441

PURPOSE
Central transactional fact table
```

This interaction is one of the main portfolio differentiators.

---

# 17. POWER BI REPORT PREVIEW

Include a visual preview of the dashboard.

Do not simply embed a huge screenshot.

Create a framed dashboard preview containing:

* KPI cards
* Sales trend
* Geographic map
* Product categories
* Logistics metrics

Button:

```text
[ VIEW REPORT ]
```

If an actual public Power BI report exists, link to it.

If not, use an interactive visual mockup.

Never imply a mockup is a live report.

---

# 18. PROJECT 02 — DATA AUTOMATION ENGINE

### Header

```text
02 / DATA AUTOMATION
SELF-HOSTED WORKFLOW INFRASTRUCTURE
```

### Title

```text
Event-Driven
Data Automation
```

### Technologies

```text
n8n
Docker Compose
PostgreSQL
Caddy
DigitalOcean
Linux
```

### Description

```text
A self-hosted automation environment for receiving,
processing, routing and storing event-driven data.
```

---

# 19. AUTOMATION PIPELINE VISUAL

Create an SVG node graph:

```text
┌───────────────┐
│ WEBHOOK       │
│ INGESTION     │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ VALIDATION    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ n8n ENGINE    │
└───────┬───────┘
        │
   ┌────┴────┐
   ▼         ▼
POSTGRES   ALERT
```

Animate the data packet traveling through the pipeline very subtly.

---

# 20. INFRASTRUCTURE VIEW

Expandable button:

```text
[ VIEW DOCKER ARCHITECTURE ]
```

Reveal:

```text
DIGITALOCEAN DROPLET
│
├── CADDY
│   └── HTTPS / REVERSE PROXY
│
├── n8n
│   └── WORKFLOW ENGINE
│
└── POSTGRESQL
    └── PERSISTENT DATA
```

This demonstrates actual infrastructure understanding without turning the portfolio into a DevOps website.

---

# 21. PROJECT 03 — CUSTOMER JOURNEY SEQUENCE MINING

### Header

```text
03 / APPLIED MACHINE LEARNING
SEQUENCE ANALYSIS
```

### Title

```text
Customer Journey
Sequence Mining
```

### Technologies

```text
PYTHON
PANDAS
PREFIXSPAN
```

### Visual

Use a compact sequence visualization:

```text
VISIT
  ↓
PRODUCT VIEW
  ↓
CART
  ↓
CHECKOUT
  ↓
PURCHASE
```

Show alternative sequences branching from the main path.

---

# 22. CODE DRAWER

Include an expandable code section.

Button:

```text
[ INSPECT SOURCE ]
```

Reveal a short, clean Python implementation.

The code should be real project code or representative code clearly labeled as such.

Syntax highlighting should be subtle.

Avoid giant code blocks.

---

# 23. GITHUB LINKS

Every project should have:

```text
[ GITHUB ]
```

where a public repository exists.

If no repository is available:

```text
[ CASE STUDY ]
```

Do not create fake repositories or links.

---

# 24. DATA PIPELINE SYSTEM MAP

After the projects, introduce a full-width system visualization.

Title:

```text
HOW I APPROACH DATA
```

Visual:

```text
         SOURCES
            │
            ▼
        INGESTION
            │
            ▼
       VALIDATION
            │
            ▼
      TRANSFORMATION
            │
            ▼
       DATA MODEL
            │
       ┌────┴────┐
       ▼         ▼
   ANALYTICS     ML
       │         │
       └────┬────┘
            ▼
       VISUALIZATION
            │
            ▼
         DECISION
```

This should communicate the user's broader methodology.

---

# 25. "HOW I WORK" SECTION

Five concise stages:

```text
01  UNDERSTAND
    Define the business problem.

02  INGEST
    Collect and validate source data.

03  MODEL
    Transform and structure the data.

04  ANALYZE
    Apply BI, statistics and machine learning.

05  COMMUNICATE
    Turn findings into decisions.
```

No lengthy paragraphs.

---

# 26. TECHNICAL ARSENAL

Full-width system strip.

Organize technologies by purpose.

### DATA

```text
Python
SQL
PostgreSQL
Pandas
Scikit-learn
```

### ANALYTICS & BI

```text
Power BI
DAX
SSAS
SSRS
Star Schemas
```

### ENGINEERING & AUTOMATION

```text
Docker
Docker Compose
n8n
Caddy
Linux CLI
```

Do not list technologies that are not actually used or understood.

---

# 27. TECHNOLOGY DETAIL INTERACTION

Hovering/clicking a technology can reveal:

```text
PYTHON

Used for:
• Data cleaning
• Statistical analysis
• Machine learning
• Automation
```

This converts a generic skills list into evidence of practical application.

---

# 28. ABOUT SECTION

Keep it short.

### Heading

```text
ABOUT
```

Example structure:

```text
I work across data analytics, business intelligence
and data engineering, with a focus on turning complex
datasets into systems that people can actually use.
```

Then:

```text
BACKGROUND

Data Analytics
Business Intelligence
Machine Learning
Technical Art / 3D
```

Do not write a large autobiographical essay.

---

# 29. "BEYOND DATA"

Use the user's technical-art background as a differentiator.

Keep it visually secondary.

```text
BEYOND DATA

TECHNICAL ART
3D MODELLING
VFX
DIGITAL SCENOGRAPHY
```

Short supporting text:

```text
A background in technical art and visual production
shaped my approach to technical problem-solving,
visual communication and systems thinking.
```

---

# 30. CONTACT SECTION

Minimal.

### Heading

```text
LET'S BUILD SOMETHING USEFUL.
```

Then:

```text
GITHUB
LINKEDIN
EMAIL
```

No complicated contact form unless required.

---

# 31. FOOTER

Use JetBrains Mono.

```text
WALEED SABIR
DATA / ANALYTICS / ENGINEERING

PORTUGAL
© 2026
```

Links:

```text
GITHUB   LINKEDIN   EMAIL
```

Optional tiny system indicator:

```text
SYSTEM STATUS ● ONLINE
```

---

# 32. MICROINTERACTIONS

Animations should communicate **data movement**, not decoration.

Use:

* Card hover border transitions
* Slight card elevation
* SVG pipeline animation
* Data-point hover
* Schema node highlighting
* Smooth navigation
* Expand/collapse transitions
* Subtle status pulse
* Number count-up on initial viewport entry

Avoid:

* Excessive parallax
* Glitch effects
* Cursor trails
* Matrix rain
* Constant flashing
* Large page transitions
* Fake loading screens

---

# 33. SCROLL EXPERIENCE

The site should progressively reveal information.

Suggested sequence:

```text
HERO
 ↓
TELEMETRY
 ↓
FEATURED PROJECT
 ↓
AUTOMATION PROJECT
 ↓
ML PROJECT
 ↓
DATA PIPELINE
 ↓
TECHNICAL ARSENAL
 ↓
ABOUT
 ↓
CONTACT
```

Each section should feel like the next layer of a system being inspected.

---

# 34. RESPONSIVE DESIGN

Desktop:

Use the full asymmetric Bento Grid.

Tablet:

Collapse secondary cards while maintaining hierarchy.

Mobile:

Use a single-column layout.

Order:

```text
Hero
Telemetry
Olist
Automation
Sequence Mining
Pipeline
Technical Arsenal
About
Contact
```

Interactive diagrams must remain readable on mobile.

Horizontal overflow should never break the page.

---

# 35. ACCESSIBILITY

Implement:

* Semantic HTML
* Keyboard navigation
* Visible focus states
* ARIA labels where appropriate
* Sufficient contrast
* Reduced-motion media query
* Proper heading hierarchy
* Alt text for meaningful images

Animations must respect:

```css
prefers-reduced-motion
```

---

# 36. PERFORMANCE

Target:

* Minimal JavaScript
* No unnecessary dependencies
* Lazy-load heavy visual assets
* Compress images
* Use SVG where practical
* Avoid autoplay video
* Avoid large background images
* Keep initial page load lightweight

The site should feel fast even on a mediocre connection.

---

# 37. SEO

Include:

```text
<title>
Waleed Sabir — Data Analytics & Data Engineering
</title>
```

Meta description:

```text
Portfolio of Waleed Sabir — data analytics,
business intelligence, data engineering and
applied machine learning projects.
```

Use proper:

```text
H1
H2
H3
```

structure.

Add Open Graph metadata.

Add favicon.

---

# 38. TRUST / CREDIBILITY RULES

This is extremely important.

Never fabricate:

* Metrics
* Clients
* Users
* Revenue
* Performance improvements
* Production deployments
* Business outcomes
* Certifications
* Job titles
* Company affiliations

Every impressive number should answer:

> "Where did this number come from?"

Distinguish clearly between:

```text
OBSERVED
```

```text
CALCULATED
```

```text
PROJECTED
```

```text
SIMULATED
```

This portfolio should feel technically credible above everything else.

---

# 39. CONTENT DENSITY

The homepage should be scannable.

Avoid paragraphs longer than approximately 2–3 lines.

Prefer:

```text
99,441
ORDERS
```

over:

```text
This project involved analyzing a dataset
containing 99,441 orders...
```

Detailed explanations belong inside expandable case studies.

---

# 40. PRIMARY CALL-TO-ACTION HIERARCHY

Primary:

```text
[ VIEW PROJECT ]
```

Secondary:

```text
[ GITHUB ]
```

Tertiary:

```text
[ CONTACT ]
```

Do not place five competing buttons inside every card.

---

# 41. VISUAL HIERARCHY

The visitor's eye should naturally move:

```text
NAME
 ↓
PROFESSIONAL IDENTITY
 ↓
FEATURED PROJECT
 ↓
EVIDENCE / METRICS
 ↓
SYSTEM ARCHITECTURE
 ↓
OTHER PROJECTS
 ↓
TECHNICAL STACK
 ↓
CONTACT
```

The Olist project should receive the greatest visual emphasis.

---

# 42. DESIGN NORTH STAR

The finished site should feel like:

> **A beautifully designed analytical system built by a data professional.**

Not:

> "A developer made a cool portfolio."

Not:

> "An AI generated a dark portfolio template."

Not:

> "A hacker-themed personal website."

The strongest visual metaphor is:

**data moving through a system.**

Use that metaphor throughout the interface.

---

# 43. IMPLEMENTATION PRIORITY

Build in this order:

### PHASE 1 — Foundation

* Global styles
* Typography
* Colors
* Navigation
* Responsive grid

### PHASE 2 — Hero

* Identity
* Value proposition
* Status
* Technology stack
* Telemetry

### PHASE 3 — Featured Project

* Olist card
* Metrics
* Pipeline diagram
* Interactive schema
* Dashboard preview

### PHASE 4 — Supporting Projects

* n8n automation
* Sequence mining

### PHASE 5 — System Sections

* Data pipeline
* How I work
* Technical arsenal

### PHASE 6 — Personal Layer

* About
* Beyond Data
* Contact

### PHASE 7 — Polish

* Animations
* Responsive behavior
* Accessibility
* SEO
* Performance
* Browser testing

---

# 44. FINAL QUALITY BAR

Before deployment, the website should pass these tests:

### 5-second test

Can someone identify:

* Who Waleed is
* What he does
* What type of roles he targets

within 5 seconds?

### 30-second test

Can someone understand:

* Main technical stack
* Strongest project
* Data engineering capability
* Analytics capability
* Machine learning capability

within 30 seconds?

### 2-minute test

Can a technical recruiter inspect:

* Data architecture
* Project methodology
* Tools
* Results
* GitHub/source material

within 2 minutes?

### Credibility test

Can every major claim or metric be explained?

### Technical test

Does the website itself demonstrate:

* Structured thinking
* Data visualization
* Information architecture
* Technical communication
* Attention to detail

?

If yes, the portfolio is doing its job.

---

# FINAL POSITIONING

The portfolio should position Waleed as:

**DATA ANALYTICS**
→ Business Intelligence, Power BI, DAX, analytical storytelling

**DATA ENGINEERING**
→ SQL, PostgreSQL, data modeling, pipelines, Docker

**APPLIED MACHINE LEARNING**
→ Python, segmentation, classification, sequence mining

**AUTOMATION**
→ n8n, APIs, event-driven workflows, self-hosted infrastructure

The unifying message:

> **Build the pipeline. Understand the data. Find the signal. Communicate the result.**
