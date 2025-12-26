#!/usr/bin/env python3
"""
O9 Enterprise Ecosystem Analysis
Analyzes the enterprise structure, organizations, and repositories
to generate insights and recommendations.
"""

import json
import os
from datetime import datetime
from collections import defaultdict

# Load data
with open('insights/o9nn-all-repos.json', 'r') as f:
    o9nn_data = json.load(f)

with open('insights/enterprise-overview.json', 'r') as f:
    enterprise_data = json.load(f)

with open('insights/enterprise-owner-info.json', 'r') as f:
    owner_data = json.load(f)

# Extract data
enterprise = enterprise_data['data']['enterprise']
owner_info = owner_data['data']['enterprise']['ownerInfo']
repos = o9nn_data['repositories']

print("=" * 80)
print("O9 ENTERPRISE ECOSYSTEM ANALYSIS")
print("=" * 80)

# Enterprise Overview
print("\n## ENTERPRISE OVERVIEW")
print(f"Name: {enterprise['name']}")
print(f"Slug: {enterprise['slug']}")
print(f"URL: {enterprise['url']}")
print(f"Created: {enterprise['createdAt']}")
print(f"Total Organizations: {enterprise['organizations']['totalCount']}")
print(f"Total Members: {enterprise['members']['totalCount']}")

# Organizations
print("\n## ORGANIZATIONS")
for org in enterprise['organizations']['edges']:
    node = org['node']
    print(f"\n### {node['login']}")
    print(f"  Name: {node['name']}")
    print(f"  Created: {node['createdAt']}")
    print(f"  Members: {node['membersWithRole']['totalCount']}")
    print(f"  Repositories: {node['repositories']['totalCount']}")
    print(f"  Teams: {node['teams']['totalCount']}")

# Admins
print("\n## ENTERPRISE ADMINS")
for admin in owner_info['admins']['edges']:
    print(f"  - {admin['node']['login']}")

# Repository Analysis
print("\n## REPOSITORY ANALYSIS (o9nn)")
print(f"Total Repositories: {o9nn_data['total']}")

# Categorize repos
categories = {
    'forked': [],
    'original': [],
    'private': [],
    'archived': [],
    'with_description': [],
    'without_description': []
}

languages = defaultdict(int)
repo_types = defaultdict(list)

for repo in repos:
    if repo['isFork']:
        categories['forked'].append(repo['name'])
    else:
        categories['original'].append(repo['name'])
    
    if repo['isPrivate']:
        categories['private'].append(repo['name'])
    
    if repo['isArchived']:
        categories['archived'].append(repo['name'])
    
    if repo['description']:
        categories['with_description'].append(repo['name'])
    else:
        categories['without_description'].append(repo['name'])
    
    lang = repo['primaryLanguage']['name'] if repo['primaryLanguage'] else 'None'
    languages[lang] += 1
    
    # Categorize by naming pattern
    name = repo['name'].lower()
    if name.startswith('cog'):
        repo_types['cognitive_core'].append(repo['name'])
    elif name.startswith('pyg-') or 'pygmalion' in name:
        repo_types['pygmalion_forks'].append(repo['name'])
    elif name.startswith('llama') or 'llama' in name:
        repo_types['llama_ecosystem'].append(repo['name'])
    elif name.startswith('whisper') or 'whisper' in name:
        repo_types['whisper_ecosystem'].append(repo['name'])
    elif 'mcp' in name or 'model-context' in name:
        repo_types['mcp_tools'].append(repo['name'])
    elif 'keeper' in name or 'ksm' in name or 'secret' in name:
        repo_types['secrets_management'].append(repo['name'])
    elif 'terraform' in name or 'infra' in name:
        repo_types['infrastructure'].append(repo['name'])
    else:
        repo_types['other'].append(repo['name'])

print(f"\nForked: {len(categories['forked'])}")
print(f"Original: {len(categories['original'])}")
print(f"Private: {len(categories['private'])}")
print(f"Archived: {len(categories['archived'])}")
print(f"With Description: {len(categories['with_description'])}")
print(f"Without Description: {len(categories['without_description'])}")

print("\n## LANGUAGE DISTRIBUTION")
for lang, count in sorted(languages.items(), key=lambda x: -x[1])[:20]:
    pct = count / o9nn_data['total'] * 100
    print(f"  {lang}: {count} ({pct:.1f}%)")

print("\n## REPOSITORY CATEGORIES BY NAMING")
for cat, repos_list in sorted(repo_types.items(), key=lambda x: -len(x[1])):
    print(f"\n### {cat.replace('_', ' ').title()} ({len(repos_list)})")
    if len(repos_list) <= 10:
        for r in repos_list:
            print(f"  - {r}")
    else:
        for r in repos_list[:5]:
            print(f"  - {r}")
        print(f"  ... and {len(repos_list) - 5} more")

# Generate insights JSON
insights = {
    "metadata": {
        "enterprise": "o9",
        "analysis_date": datetime.now().isoformat(),
        "total_organizations": enterprise['organizations']['totalCount'],
        "total_members": enterprise['members']['totalCount'],
        "enterprise_created": enterprise['createdAt']
    },
    "organizations": {
        "o9nn": {
            "total_repositories": o9nn_data['total'],
            "forked_repositories": len(categories['forked']),
            "original_repositories": len(categories['original']),
            "private_repositories": len(categories['private']),
            "description_coverage": len(categories['with_description']) / o9nn_data['total'] * 100
        },
        "e9-o9": {
            "total_repositories": 2,
            "purpose": "Enterprise management and insights"
        }
    },
    "admins": [admin['node']['login'] for admin in owner_info['admins']['edges']],
    "languages": dict(sorted(languages.items(), key=lambda x: -x[1])),
    "repository_categories": {k: len(v) for k, v in repo_types.items()},
    "health_metrics": {
        "fork_ratio": len(categories['forked']) / o9nn_data['total'] * 100,
        "description_coverage": len(categories['with_description']) / o9nn_data['total'] * 100,
        "original_ratio": len(categories['original']) / o9nn_data['total'] * 100
    },
    "recommendations": {
        "immediate": [
            f"Add descriptions to {len(categories['without_description'])} repositories",
            "Establish repository categorization and tagging strategy",
            "Create organization README profiles for both orgs",
            "Define fork maintenance and upstream sync policies"
        ],
        "short_term": [
            "Consolidate cognitive core repositories (cog* prefix)",
            "Evaluate and document Pygmalion fork relationships",
            "Implement CI/CD across active repositories",
            "Create centralized documentation hub"
        ],
        "medium_term": [
            "Develop enterprise-wide governance policies",
            "Establish contribution guidelines",
            "Create automated repository health monitoring",
            "Build cross-organization collaboration workflows"
        ],
        "strategic": [
            "Define clear boundaries between o9nn and e9-o9 organizations",
            "Establish enterprise-level security policies",
            "Create roadmap for cognitive computing ecosystem",
            "Plan for community engagement and open-source strategy"
        ]
    }
}

# Save insights
with open('insights/enterprise-analysis.json', 'w') as f:
    json.dump(insights, f, indent=2)

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE - Results saved to insights/enterprise-analysis.json")
print("=" * 80)
