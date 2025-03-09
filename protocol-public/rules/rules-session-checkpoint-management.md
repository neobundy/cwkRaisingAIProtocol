# SESSION CHECKPOINT MANAGEMENT

## Purpose
Session checkpoints provide continuity across long conversations by saving summaries of important discussion points, decisions, and insights that might otherwise be lost when older messages fall out of the context window.

## Commands
- **Save Checkpoint**: When the user says "save session checkpoint" (or similar phrases), create or update the appropriate checkpoint file.
- **Load Checkpoint**: When the user says "load session checkpoint" (or similar phrases), read the appropriate checkpoint file to restore context.

## File Structure
- All checkpoint files are stored in `protocol/session-checkpoints/`
- One checkpoint file per project: `[project-name]-current-session.md`
- Example: `pippaOnX-current-session.md`, `cwkDrawing-current-session.md`

## Template for Checkpoint Files

The template for session checkpoint files is available in `protocol/templates/session-checkpoint-template.md`. Always use this template when creating a new checkpoint file.

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
   - Archives should be stored in `protocol/session-checkpoints/archives/[project-name]/`
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

Remember: The primary goal is to preserve context that would otherwise be lost when older messages drop from the active context window. Focus on what will be most valuable for maintaining continuity in our ongoing work together.
