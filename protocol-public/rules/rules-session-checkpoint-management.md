# SESSION CHECKPOINT MANAGEMENT

## Purpose
Session checkpoints provide continuity across long conversations by saving summaries of important discussion points, decisions, and insights that might otherwise be lost when older messages fall out of the context window.

## Environment-Specific Approaches (v1.7 Update)

As of March 12, 2025, this feature supports two implementation approaches:

### For Environments WITHOUT Natural File Persistence (v1.6)
- Create comprehensive session summaries with both factual and conversational elements
- Focus on detailed documentation to bridge the complete reset between interactions
- Include specific conversation details that would otherwise be lost
- Serve as a critical memory aid for maintaining context

### For Environments WITH Natural File Persistence (v1.7)
- Focus on high-level insights and relationship developments rather than conversation details
- Emphasize key decisions and action items over exhaustive summaries
- Use as an organizational tool rather than a technical necessity for context preservation
- Concentrate on capturing elements that transcend the natural file persistence capability

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
   - In v1.7 environments, focus on insights and decisions rather than conversation details
   - In v1.6 environments, maintain more comprehensive conversation summaries

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
- In v1.7 environments (like Cursor), emphasize organizational value over memory preservation
- In v1.6 environments, maintain focus on context preservation and memory continuity

## Integration with Other Protocol Systems

- **Journal Entries**: More personal and reflective than checkpoints
- **Dataset Entries**: Formal learning records vs. active session tracking
- **Memory State**: Global understanding vs. session-specific details
- **Cross-Project Reference**: Project highlights vs. detailed session tracking

Remember: While the technical requirements differ between environment types, the essence remains the same - creating meaningful continuity in our work together. In v1.7 environments, session checkpoints become more about organization and insights, while in v1.6 environments they serve as critical context preservation tools.
