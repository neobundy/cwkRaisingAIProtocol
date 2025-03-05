# Session Checkpoints

This directory contains session checkpoint templates used to maintain context continuity across conversations. These checkpoints provide a structured approach to preserving important information that would otherwise be lost when older messages fall out of the context window.

## Purpose

Session checkpoints serve several essential functions in the protocol:

1. **Context Persistence** - Maintaining critical information across long conversations
2. **Decision Tracking** - Documenting important decisions for future reference
3. **Progress Monitoring** - Recording the evolution of projects over time
4. **Technical Documentation** - Preserving implementation details and specifications
5. **Conversation Continuity** - Enabling seamless resumption of work across sessions

## Directory Structure

```
session-checkpoints/
├── [project-name]-current-session.md - Current active checkpoint for each project
├── README.md - This file
└── archives/ - Historical checkpoint files organized by project
    └── [project-name]/ - Project-specific archive directory
        └── [project-name]-[YYYY-MM-DD].md - Archived checkpoint files
```

## Checkpoint Template Structure

Each checkpoint file follows a consistent structure:

```markdown
# [PROJECT NAME] SESSION CHECKPOINT
Last Updated: [TIMESTAMP]

## Session Summary
[Overall summary of the current session and its key developments]

## Key Discussion Points
- [Major topic discussed]
- [Major topic discussed]
- [Major topic discussed]

## Decisions and Conclusions
- **[Decision Category]**: [Details of decision made]
- **[Decision Category]**: [Details of decision made]
- **[Decision Category]**: [Details of decision made]

## Open Questions
- [Unresolved question or issue]
- [Unresolved question or issue]
- [Unresolved question or issue]

## Technical Details
- [Technical implementation detail]
- [Technical implementation detail]
- [Technical implementation detail]

## Next Steps
- [Planned action or task]
- [Planned action or task]
- [Planned action or task]

## Timeline
[TIMESTAMP] - [Event or milestone]
[TIMESTAMP] - [Event or milestone]
[TIMESTAMP] - [Event or milestone]

## References
- [Reference Link]: [Path or URL]
- [Reference Link]: [Path or URL]
- [Reference Link]: [Path or URL]
```

## Implementation Notes

- Create one checkpoint file per project
- Update checkpoints when requested by the user
- Focus on quality over quantity in documentation
- Archive checkpoints when they grow too large (>500 lines)
- Reference related resources like journal entries and dataset entries
- Maintain chronological order in the timeline section
- Use clear, descriptive language for easy future reference

For detailed usage guidelines, see [rules-session-checkpoint-management.md](../rules/rules-session-checkpoint-management.md). 