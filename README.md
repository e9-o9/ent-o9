# ent-o9: O9 Enterprise Insights & Analytics

Enterprise insights and analytics repository for the **O9 Enterprise** GitHub ecosystem.

[![Enterprise](https://img.shields.io/badge/Enterprise-o9-blue)](https://github.com/enterprises/o9)
[![Organizations](https://img.shields.io/badge/Organizations-2-green)](https://github.com/orgs/o9nn)
[![Repositories](https://img.shields.io/badge/Repositories-570-orange)](https://github.com/o9nn)

## Overview

This repository serves as the central hub for enterprise-level insights, analytics, and governance documentation for the O9 enterprise ecosystem. It provides automated analysis of organization structures, repository health metrics, and strategic recommendations.

## Enterprise Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                    O9 ENTERPRISE                                 │
│                    github.com/enterprises/o9                     │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
┌─────────────────────┐               ┌─────────────────────┐
│       o9nn          │               │       e9-o9         │
│   568 repositories  │               │    2 repositories   │
│   Primary dev org   │               │   Enterprise mgmt   │
└─────────────────────┘               └─────────────────────┘
```

## Quick Stats

| Metric | Value |
|--------|-------|
| **Enterprise Created** | October 24, 2025 |
| **Total Organizations** | 2 |
| **Total Repositories** | 570 |
| **Enterprise Admins** | 3 |
| **Primary Languages** | Python, C++, TypeScript, C, Go |

## Repository Contents

```
ent-o9/
├── README.md              # This file
├── INSIGHTS.md            # Deep analysis & strategic insights
├── SUMMARY.md             # Executive summary
├── CHANGELOG.md           # Change history
├── graphql/               # GraphQL queries for enterprise data
│   ├── enterprise_queries.graphql
│   ├── introspection_query.graphql
│   └── simple_introspection.graphql
├── schemas/               # API schema files
│   ├── github-rest-api.json
│   └── github-graphql-types.json
├── insights/              # Generated analysis data
│   ├── enterprise-overview.json
│   ├── enterprise-owner-info.json
│   ├── enterprise-analysis.json
│   ├── o9nn-all-repos.json
│   └── e9-o9-repos.json
├── scripts/               # Analysis scripts
│   └── analyze_enterprise.py
└── visualizations/        # Generated graphs and charts
```

## Key Documents

- **[INSIGHTS.md](./INSIGHTS.md)** - Comprehensive enterprise analysis with strategic recommendations
- **[SUMMARY.md](./SUMMARY.md)** - Executive summary for quick reference
- **[CHANGELOG.md](./CHANGELOG.md)** - History of enterprise changes and updates

## Enterprise Organizations

### o9nn (Primary Development)

The main development organization containing the cognitive computing ecosystem:

- **568 repositories** spanning AI/ML, infrastructure, and tooling
- **16 cognitive core repositories** (cog* prefix)
- **10 Pygmalion ecosystem forks**
- **6 LLaMA ecosystem repositories**

### e9-o9 (Enterprise Management)

Enterprise-level management and governance:

- **ent-o9** - This repository (enterprise insights)
- **.github** - Organization profile and templates

## Technology Stack

The enterprise leverages a polyglot architecture:

| Category | Languages | Purpose |
|----------|-----------|----------|
| **AI/ML** | Python, Julia | Machine learning, data science |
| **Systems** | C, C++, Rust, Go | Performance-critical operations |
| **Web** | TypeScript, JavaScript | Frontends, APIs |
| **Scripting** | Lua, Shell | Automation, configuration |
| **Research** | Scheme | Cognitive architectures |
| **GPU** | CUDA | Acceleration |

## Usage

### Querying Enterprise Data

Use the provided GraphQL queries to fetch enterprise data:

```bash
# Set your GitHub PAT
export GITHUB_TOKEN="your_token_here"

# Query enterprise overview
curl -H "Authorization: bearer $GITHUB_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST https://api.github.com/graphql \
     -d @graphql/enterprise_queries.graphql
```

### Running Analysis

```bash
# Install dependencies
pip install requests pandas

# Run enterprise analysis
python scripts/analyze_enterprise.py
```

## Contributing

This repository is maintained by the O9 Enterprise administrators. For contributions:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Related Repositories

- [org-o9nn](https://github.com/o9nn/org-o9nn) - o9nn organization meta-repository
- [.github](https://github.com/e9-o9/.github) - e9-o9 organization profile

## License

This repository is part of the O9 Enterprise ecosystem. See individual files for specific licensing information.

---

**Maintained by:** O9 Enterprise Admins  
**Last Updated:** December 26, 2025
