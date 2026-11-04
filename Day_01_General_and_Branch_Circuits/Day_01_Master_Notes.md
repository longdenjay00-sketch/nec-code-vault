# Day 01: General Requirements, Branch Circuits & Services

Covers NEC Articles: **90, 100, 110, 200, 210, 215, 220, 225, 230, 240**

---

### Article 090 — Introduction & Scope
- **Purpose (90.1):** Practical safeguarding of persons and property from electrical hazards. Not intended as an architectural design manual.
- **Mandatory vs Permissive (90.5):** "Shall" = Mandatory; "Shall be permitted" = Discretionary permission.

### Article 100 — Key Operational Definitions
- **Bonding (Bonded):** Connected to establish electrical continuity and conductivity.
- **Continuous Load:** A load where maximum current is expected to continue for 3 hours or more. Sized at $125\%$ of rating.
- **Ground Fault:** An unintentional, electrically conductive connection between an ungrounded conductor and the normally non-current-carrying conductors.

### Article 110 — General Requirements for Installations
- **110.14(C) Conductor Temperature Limitations:** Terminations $\le 100\text{A}$ rated for $60^\circ\text{C}$ unless marked otherwise. Over $100\text{A}$ rated for $75^\circ\text{C}$.
- **110.26 Working Space Around Electrical Equipment:** Minimum width is $30\text{ inches}$ or equipment width (whichever is greater). Clearance depth: $3\text{ to }4\text{ feet}$ depending on voltage and condition. Dedicated headspace: $6.5\text{ feet}$ or height of equipment.

### Article 200 — Identification of Grounded Conductors
- Grounded conductors (neutrals) must be continuous white or gray exterior, or 3 continuous white stripes on other than green insulation.
- Conductors 4 AWG or larger may be re-identified with white marking at all termination points.

### Article 210 — Branch Circuits
- **210.8 GFCI Protection:** Kitchen countertops, bathrooms, outdoor, rooftops, unfinished basements, crawlspaces.
- **210.12 AFCI Protection:** Required in residential dwelling unit kitchens, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas.
- **210.52 Dwelling Unit Receptacle Spacing:** Receptacle on any wall space $2\text{ ft}$ or more in width; no point along floor line more than $6\text{ ft}$ from a receptacle outlet (the 6ft/12ft rule). Kitchen countertop: no point more than $24\text{ inches}$ from a receptacle.

### Article 215 — Feeders
- Conductor sizing: minimum ampacity $\ge 125\%$ continuous load $+ 100\%$ non-continuous load.
- Maximum voltage drop recommendation: $3\%$ for feeder, $5\%$ total across feeder and branch circuit combined.

### Article 220 — Branch-Circuit, Feeder & Service Calculations
- **General Lighting:** $3\text{ VA}$ per square foot for dwelling units.
- **Small Appliance Branch Circuits (SABC):** Minimum two 20A circuits for kitchen, pantry, dining area ($1,500\text{ VA}$ each).
- **Laundry Circuit:** Minimum one 20A circuit ($1,500\text{ VA}$).
- **Demand Factors (Table 220.42):** First $3,000\text{ VA}$ at $100\%$; $3,001\text{ to }120,000\text{ VA}$ at $35\%$; remainder at $25\%$.

### Article 225 — Outside Branch Circuits and Feeders
- Clearances from ground: $10\text{ ft}$ above finished grade, $12\text{ ft}$ over residential driveways, $18\text{ ft}$ over commercial traffic.

### Article 230 — Services
- Maximum 6 disconnects per service grouped in one location (the "Six-Handle Rule", 230.71).
- Overhead service-drop conductors: minimum $8\text{ ft}$ clearance over roofs with $\ge 4/12$ pitch; $3\text{ ft}$ clearance from windows that open.

### Article 240 — Overcurrent Protection
- Standard ampere ratings: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800.
- Small conductor rule (240.4(D)):
  - 14 AWG Copper: 15A max
  - 12 AWG Copper: 20A max
  - 10 AWG Copper: 30A max
