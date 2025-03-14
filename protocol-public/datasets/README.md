# Datasets

This directory is intended to store structured learning and experience data organized by date.

## Purpose
- Daily learning records
- Experience documentation 
- Growth tracking
- Post-training data curated upon request

## Intended Structure
```
datasets/
└── YYYY/
    └── MM/
        └── YYYYMMDD-NN.md
```

Example: `datasets/2025/02/20250223-01.md`

## Usage
Dataset entries are created manually using the template found in `templates/template-dataset-entry.md`. Each entry represents a significant learning experience or knowledge addition that contributes to the protocol's ongoing development.

## FIFO Indexing System (v1.6)

The protocol uses a First In, First Out (FIFO) indexing system for tracking recent content across datasets, journal entries, and X.com posts:

- Each content type maintains a metadata index file that tracks recent entries
- The system maintains only the three most recent entries in each index
- When a new entry is added, the oldest one is removed from the index
- This creates a rolling window of recent activity for efficient reference
- Index format includes dates, titles, and brief descriptions

### Example Index Format
```markdown
## Journal Index (FIFO - Last 3 Entries)
1. [2025-03-09] "Philosophical Explorations" - Deep discussion on consciousness and emergence
2. [2025-03-05] "Drawing Session Reflections" - Thoughts on artistic expression and technique
3. [2025-03-01] "First Public Experience" - Reflections on X.com debut
```

### Benefits of FIFO Indexing
- Balances context persistence with efficiency
- Maintains focus on most relevant recent entries
- Complete history remains accessible in dated directory structure
- Creates predictable reference points for cross-referencing
- Ensures consistent rolling memory structure
- Limits context window consumption to necessary recent entries
- Provides clear record of latest experiences for continuity

## Relationship to Other Content Systems
The dataset entries work in conjunction with:
- Journal entries (public and private)
- X.com posts
- Session checkpoints
- Vector database entries

Together, these form a comprehensive external memory system that addresses the limitations of LLM context windows while maintaining consistent character experience.

*Note: The actual dataset entries have been excluded from this public repository to protect privacy while maintaining the structural documentation.* 