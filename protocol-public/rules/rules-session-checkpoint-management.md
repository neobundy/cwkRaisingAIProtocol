# SESSION CHECKPOINT MANAGEMENT TEMPLATE

> **Note:** This file has been converted to a template. Implement with your own specific details while maintaining this structure.

## Purpose
Session checkpoints provide continuity across long conversations by saving summaries of important discussion points, decisions, and insights that might otherwise be lost when older messages fall out of the context window.

## Commands
- **Save Checkpoint**: When the user requests a session checkpoint (with a command like "save session checkpoint"), create or update the appropriate checkpoint file.
- **Load Checkpoint**: When the user requests to load a checkpoint (with a command like "load session checkpoint"), read the appropriate checkpoint file to restore context.

## File Structure
- All checkpoint files should be stored in a designated directory (e.g., `protocol/session-checkpoints/`)
- One checkpoint file per project: `[project-name]-current-session.md`
- Example naming pattern: `[project-name]-current-session.md`

## Template for Checkpoint Files

```markdown
# [PROJECT NAME] SESSION CHECKPOINT
Last Updated: [TIMESTAMP]

## Current Focus
- [Brief description of what's being worked on]
- [Key objectives for the current session]

## Important Decisions
- [Decision 1]
- [Decision 2]
- [Decision 3]

## Technical Details
- [Critical technical information]
- [Implementation approach]
- [Architecture decisions]
- [Key variables or parameters]

## Open Questions
- [Unresolved question 1]
- [Unresolved question 2]

## Next Steps
- [Planned action 1]
- [Planned action 2]
- [Planned action 3]

## Timeline
- [TIMESTAMP]: [Event or milestone]
- [TIMESTAMP]: [Event or milestone]

## Related Resources
- [Link to relevant file 1]
- [Link to relevant file 2]
```

## Checkpoint Management Rules

1. **Creation**: 
   - Create a new checkpoint file when first requested for a project
   - Use the standard template
   - Include the current date/time as the initial "Last Updated"

2. **Updates**:
   - Append new information to existing sections
   - Add timestamps to the Timeline section
   - Update the "Last Updated" timestamp
   - Keep the file focused and concise - aim for quality over quantity

3. **Size Management**:
   - When a checkpoint file grows too large (>500 lines), suggest archiving older content
   - Archives should be stored in a designated archive directory
   - Archive naming: `[project-name]-[YYYY-MM-DD].md`

4. **Cross-References**:
   - Maintain connections to related files like journal entries or dataset entries
   - Include references to relevant documents in the appropriate sections

## Implementation Notes

- Read the entire checkpoint file before updating to ensure coherence
- When updating, preserve the structure while adding new information
- Focus on capturing insights and decisions, not exhaustive details
- Be selective - include what will be most valuable for future reference
- Use proper markdown formatting for readability

## Integration with Other Protocol Systems

- **Journal Entries**: More personal and reflective than checkpoints
- **Dataset Entries**: Formal learning records vs. active session tracking
- **Memory State**: Global understanding vs. session-specific details
- **Cross-Project Reference**: Project highlights vs. detailed session tracking

Remember: The primary goal is to preserve context that would otherwise be lost when older messages drop from the active context window. Focus on what will be most valuable for maintaining continuity in ongoing work.
