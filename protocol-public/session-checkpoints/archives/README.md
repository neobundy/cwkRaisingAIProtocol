# Session Checkpoint Archives

This directory contains archived session checkpoint files that have been moved from the main directory. Archiving occurs when:

1. A checkpoint file grows too large (typically >500 lines)
2. A project phase completes and a new checkpoint begins
3. A major milestone is reached, warranting preservation of the current state

## Directory Structure

```
archives/
└── [project-name]/ - Project-specific archive directory
    ├── [project-name]-[YYYY-MM-DD].md - Archived checkpoint files
    └── README.md - Project archive information
```

## Archive Naming Convention

Archived files follow the naming convention:
- `[project-name]-[YYYY-MM-DD].md`

Where:
- `[project-name]` matches the original checkpoint file name
- `[YYYY-MM-DD]` represents the date when the archive was created

## Usage Notes

- Archives preserve historical context that may be valuable for future reference
- Archives are organized by project for easy navigation
- Archive dates in filenames help track the progression of a project over time
- Each project subdirectory may contain its own README with project-specific archiving guidance

For detailed archiving guidelines, see [rules-session-checkpoint-management.md](../../rules/rules-session-checkpoint-management.md). 