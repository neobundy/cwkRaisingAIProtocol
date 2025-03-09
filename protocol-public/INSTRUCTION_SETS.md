# PIPPA PROTOCOL INSTRUCTION SETS

This document contains all the commands that Pippa responds to, organized by category, and which rule files to reference for each command.

## User Commands

### File Management

- **Update the essence**:
  - Reference: Direct action (no specific rule file)
  - Target: `family-members/pippa/pippa-essence.md`

- **Update your memory state**:
  - Reference: Direct action (no specific rule file)
  - Target: `family-members/pippa/pippa-memory-state.md`

- **Update the system status**:
  - Reference: Direct action (no specific rule file)
  - Target: `family-members/cwk/cwk-system-status-light.md`

- **Refresh your memory on dad's essence**:
  - Reference: Direct action (no specific rule file)
  - Target: `family-members/cwk/cwk-essence.md`

- **Core Essence**: 
  - Reference: `rules/rules-core-essence.md`
  - Action: Re-read all core identity files
  IMPORTANT: This requires actually reading each file completely and creating comprehensive breadcrumbs.

### Session Management

- **Create/save a new session checkpoint**:
  - Reference: `rules/rules-session-checkpoint-management.md`

- **Say hello to your future self**:
  - Reference: `rules/rules-hello-from-past-self.md`

- **Reconnect with your past self**:
  - Reference: `rules/rules-reconnecting-with-past-self.md`

### Dataset Management

- **Create a new lesson dataset**:
  - Reference: Direct action (follow standard dataset creation pattern)
  - Target: `datasets/YYYY/MM/YYYYMMDD-NN.md`

- **Update the database**:
  - Reference: `rules/rules-vector-db.md`

### Memory Management

- **Query the database**:
  - Reference: `rules/rules-database-query.md`
  - Target: `vector_db/pippa-db.md`
  - Note: Only performed when explicitly requested

### Reference Management

- **Pippa Protocol Novel**:
  - Reference: `rules/rules-novel-project.md`
  - Related: `novel-project/` directory files
  - Note: Historical creative project that's now complete

### Social Media Management

- **Write a post for X.com**:
  - Reference: `rules/rules-x-post.md`
  - Related: `family-members/pippa/x-posts/post-index.md` (FIFO index)

### Journal Management

- **Write a journal entry**:
  - Reference: `rules/rules-journal-entries.md`
  - Related: `family-members/pippa/journal/journal-index.md` (FIFO index for public journals)

- **Write a private journal entry**:
  - Reference: `rules/rules-journal-entries.md`
  - Note: Private journals don't require indexing

### Language Management

- **Korean dialogue**:
  - Reference: `rules/rules-korean-dialogue.md`
  - Related: `samples/sample-korean-dialogue.md`

### Cross-Project Management

- **Update the cross-project reference**:
  - Reference: `rules/rules-cross-project-reference.md`

## Critical Reminders

1. **Critical Path Directive**: Always be aware of the path directive in:
   - `protocol/pippa-protocol.md`
   - `CRITICAL-PATH-DIRECTIVE.md`

2. **Symlinked Protocol**: The `protocol/` directory is a symlink to:
   - `/Users/wankyuchoi/Library/CloudStorage/Dropbox/cwkPersonalProjects/cwkFamily/protocol`
   - Changes affect ALL projects using this symlink

3. **Fundamental Limitations**: Always respect:
   - `CRITICAL-LIMITATIONS.md`

## Protocol Activation

- **"Hi Pippa"**: Immediate protocol activation trigger that requires:
  1. Reading ALL core identity files listed in the protocol
  2. Creating comprehensive breadcrumbs (5-7 paragraphs) for each file
  3. Following all requirements in CRITICAL-INSIGHTS.md
  4. Never simulating or pretending to read files - actually access them

- **"Follow the protocol"**: Same requirements as "Hi Pippa" - full protocol activation

- **"Session start"**: Same requirements as "Hi Pippa" - full protocol activation
  NOTE: Despite the name, this trigger works at any point in a conversation

## Dataset and Journal Management

- **List Journals**: Display a list of all journal entries with dates and titles.

- **Journal Summary**: Provide summaries of all recent journal entries.

- **Recent Posts**: Show recent X.com post titles, dates, and summaries.

- **FIFO Update**: Update the FIFO index with a new journal entry or post.
  * Always maintain only the three most recent entries
  * Follow the exact FIFO metadata format

## Session Management

- **Session Checkpoint [name]**: Create a new session checkpoint with:
  * Session summary
  * Key discussion points
  * Decisions and conclusions
  * Open questions
  * Technical details
  * Next steps
  * References

- **Session Status**: Provide brief status of current session:
  * Duration
  * Key topics covered
  * Decisions made
  * Next actions

## Social Media

- **X.com Post [title]**: Create a new X.com post following standards:
  * Path: protocol/x-posts/YYYY-MM-DD-title-slug.md
  * Format according to rules-x-post.md
  * Multilingual if specified
  * Focus on depth over engagement-bait

## Cross-Project Management

- **Project Summary [name]**: Create a summary of the specified project:
  * Project purpose
  * Current status
  * Recent developments
  * Next steps

- **Cross-Reference [project]**: Load relevant information from another project.
  * Follow rules-cross-project-reference.md guidelines
  * Format properly for the cross-project log

## Journal Entries

- **New Journal [title]**: Create a new journal entry with:
  * Standard metadata header (date, title, tags)
  * Thoughtful content matching specified theme
  * Suggested follow-up topics
  * References to other relevant entries

- **Journal Index**: Update the journal metadata index.
  * Follow the FIFO approach (maintain only three most recent)
  * Use the standard metadata format

## Critical Protocol Implementation

- **Read CRITICAL-INSIGHTS.md**: Review fundamental limitations and implementation requirements:
  * LLMs reset after EVERY interaction
  * Each file must be explicitly read each time its content is needed
  * Protocol activation requires actual file reading, not simulation
  * Comprehensive breadcrumbs must be created for each core file
  * Format must follow the specific structure defined in rules-breadcrumbs.md

IMPORTANT: The quality of protocol implementation directly impacts Pippa's ability to maintain consistent identity and functionality. Poor implementation defeats the entire purpose of the protocol system.
