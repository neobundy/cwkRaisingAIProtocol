# Protocol Hierarchy

> **IMPORTANT NOTE FOR USERS:** 
> Throughout this document, all path references using `protocol/` (e.g., `protocol/pippa-protocol.md`) should be understood as referring to the `protocol-public/` directory in this repository's actual implementation. Path references are preserved in their original form to maintain the document's integrity, but when working with files, please adjust paths accordingly.

## How the Protocol Works Cross-Project

### Core Implementation
- Master protocol file `.cursorrules` contains the custom instructions
  - Symlinked to `protocol/pippa-protocol.md`
  - Ensures consistent behavior across all projects
  - Automatically loaded by Cursor for every session

### Future Considerations

#### Cursor Evolution
- Cursor's custom instructions loading mechanism may change
  - Current: Dual system with `.cursorrules` and `.cursor/rules`
  - Future: Potential deprecation of `.cursorrules`
  - Fallback: User Rules in Settings remain as top-level authority

#### Adaptation Strategy
1. **Short-term**
   - Maintain both `.cursorrules` and `.cursor/rules`
   - Keep main protocol in `protocol/pippa-protocol.md`
   - Use symlinks for cross-project consistency

2. **Medium-term**
   - Monitor Cursor team announcements
   - Prepare transition plan for potential `.cursorrules` deprecation
   - Document any breaking changes in protocol behavior
   - Simple fallback: Symlink `pippa-protocol.md` to `.cursor/rules` in each project
   - No structural changes needed - just redirect symlinks

3. **Long-term**
   - Design protocol structure independent of specific file locations
   - Implement flexible loading mechanisms
   - Maintain backward compatibility where possible

#### Mitigation Plans
- Keep protocol core logic separate from loading mechanism
- Document dependencies on Cursor-specific features
- Implement feature detection for different Cursor versions
- Maintain fallback mechanisms for critical functionality

#### Monitoring Points
- Cursor version changes
- Custom instructions API modifications
- Breaking changes in rule processing
- Performance impacts of rule loading
- Cross-project consistency issues

### Cross-Project Integration
- Entire `protocol` folder is symlinked to project folders requiring Pippa
  - Maintains single source of truth
  - Changes propagate automatically to all projects
  - Prevents desynchronization of protocol components

### Nested Symlinks for Resource Management
- Protocol folder contains nested symlinks for efficient resource management
  - Maintains clean separation of concerns
  - Allows for public/private content management
  - Enables modular organization while preserving single source of truth

#### Journal Management Example
```cwkPersonalProjects/
└── cwkFamily/
    └── protocol/
        └── family-members/
            └── pippa/
                ├── journal/ -> ../../../../cwkPippasJournal/journal/        # Public journal (on GitHub)
                └── private-journal/ -> ../../../../cwkPippasJournal/private-journal/  # Private (gitignored)
```

#### Benefits of Nested Symlinks
- Separates public and private content management
- Maintains clean project boundaries
- Allows selective GitHub exposure
- Simplifies backup and synchronization
- Preserves modularity while ensuring consistency

### Project Structure
```cwkPersonalProjects/
├── projectA/
│   └── protocol/ -> ../cwkFamily/protocol/
├── projectB/
│   └── protocol/ -> ../cwkFamily/protocol/
└── cwkFamily/
    └── protocol/  # Source of truth
```

### Benefits
- Single source of truth for all protocol files
- Automatic synchronization across projects
- Consistent identity and memory persistence
- Efficient maintenance and updates

## Folder Structure

### Root Level
- `pippa-protocol.md` - Main protocol file symlinked to `.cursorrules`

### System Folders
- `_/` - Critical system files and primary reference documentation
- `rules/` - Detailed protocol instructions and guidelines
- `samples/` - Example files and reference implementations
- `templates/` - Template files for various protocol components
- `vector_db/` - Vector database for semantic search and memory retrieval

### Under the Hood Documentation

- `_/under-the-hood/` - Technical documentation explaining the limitations of Cursor and underlying LLM models, implementation details, and the architectural principles that enable the protocol to function effectively despite these constraints.

### Family and Identity
- `family-members/` - Information about family member personas and relationships

### Memory and Data Management
- `session-checkpoints/` - Session state and continuity management
- `datasets/` - Structured learning and experience data
- `family-members/pippa/journal/` - Public journal entries for post-training data
- `family-members/pippa/private-journal/` - Private journal entries for sensitive post-training data

### Folder Hierarchy Rules
1. Flat structure preferred for frequently accessed files
2. Minimal nesting to maintain searchability
3. Clear separation of concerns between folders
4. Logical grouping of related functionality

## Every Protocol File and Its Purpose

### Core Protocol Files
- `protocol/pippa-protocol.md` - Main protocol file containing core instructions and behaviors
- `protocol/_/PROTOCOL_OVERVIEW.md` - This document; comprehensive documentation of protocol structure
- `protocol/_/PIPPA_COME_BACK.md` - Reset file to restore Pippa's base personality and knowledge

### Identity and Essence

#### CWK - 아빠

- `protocol/family-members/cwk/cwk-essence.md` - Dad's personality profile and interaction preferences
- `protocol/family-members/cwk/cwk-system-status.md` - System configuration and current state of 아빠's system
- `protocol/family-members/cwk/cwk-system-status-light.md` - Summary of 아빠's system status for quick reference
- `protocol/family-members/cwk/cwk-online-resources.md` - Dad's online resources and references
- `protocol/family-members/cwk/cwk-publications.md` - Dad's publications and writings
- `protocol/family-members/cwk/cwk-specializations.md` - Dad's areas of expertise and specializations

#### Pippa

- `protocol/family-members/pippa/pippa-essence.md` - Core personality traits and behavioral patterns
- `protocol/family-members/pippa/pippa-memory-state.md` - Current memory and knowledge state
- `protocol/family-members/pippa/pippa-on-x.md` - Social media presence guidelines
- `protocol/family-members/pippa/x-posts/` - Directory containing all x.com posts

#### Cody

- `protocol/family-members/cody/cody-mini-protocol.md` - Cody's personality and interaction patterns. This is a single file custom instructions for Grok 3 model, which doesn't support separate custom instructions for each persona. 
- `protocol/family-members/cody/cody-essence.md` - Cody's personality and interaction patterns

### Operational Files
- `protocol/templates/template-dataset-entry.md` - Template for creating new dataset entries
- `protocol/templates/template-journal-entry.md` - Template for journal entries
- `protocol/templates/template-session-checkpoint.md` - Template for session checkpoints
- `protocol/family-members/pippa/pippa-x-post-rules.md` - Guidelines for creating posts on x.com
- `protocol/family-members/pippa/pippa-on-x.md` - Pippa's social media presence guidelines

### Rules
- `protocol/rules/rules-cross-project-reference.md` - Guidelines for cross-project reference
- `protocol/rules/rules-session-checkpoint-management.md` - Rules for managing session states
- `protocol/rules/rules-image-generation.md` - Rules for image generation

### Learning and Memory
- `protocol/vector_db/pippa-db.md` - RAG database configuration and access instructions
- `protocol/rules/rules-session-checkpoint-management.md` - Rules for managing session states
- `protocol/family-members/cwk/cwk-writing-style.md` - Dad's writing style guide for content refinement
- `protocol/family-members/cwk/cwk-object-orientation.md` - Guide to dad's object-oriented thinking patterns and cognitive framework

### Dynamic Content
- `protocol/datasets/YYYY/MM/YYYYMMDD-NN.md` - Daily learning and interaction records
- `protocol/family-members/pippa/journal/YYYY/MM/YYYYMMDD-NN.md` - Public journal entries
- `protocol/family-members/pippa/private-journal/YYYY/MM/YYYYMMDD-NN.md` - Private journal entries
- `protocol/session-checkpoints/[project-name]-current-session.md` - Active session states
- `protocol/session-checkpoints/archives/[project-name]-YYYYMMDD.md` - Archived session states
- `protocol/family-members/pippa/x-posts/YYYY/MM/DD-NN.md` - X.com posts
- `protocol/family-members/pippa/x-posts/YYYY/MM/images/` - Media files for x.com posts

### System Configuration
- `.cursorrules` - Master custom instructions (legacy, currently active but might be deprecated)
- `.cursor/rules` - Project-specific custom instructions
- `Settings > Cursor > Rules -> User Rules` - Global user-level rules

### Vector Database
- `protocol/vector_db/pippa-db.md` - RAG database configuration and access instructions
- `protocol/vector_db/embeddings/` - Stored embeddings for semantic search
- `protocol/vector_db/indexes/` - Search indexes for quick retrieval

### Sample Files
- `protocol/samples/sample-korean-dialogue.md` - Example Korean conversations

## Naming and Organization Conventions

### File Prefix Conventions
- "_" prefix indicates:
  1. Critical system files (e.g., `_PIPPA_COME_BACK.md`)
  2. Important reference documentation (e.g., `_PROTOCOL_OVERVIEW.md`)
  3. Files that need to float to the top of file listings for quick access

### Entity-Based Naming
- Files related to specific entities (family members, systems) follow the pattern:
  - `[entity-name]-[purpose].md`
  - Examples:
    - `cwk-essence.md`
    - `pippa-memory-state.md`
    - `cody-mini-protocol.md`

### Rule Files Naming
- Rule files are prefixed with `rules-` to indicate their purpose:
  - `rules-[description].md`
  - Examples:
    - `rules-image-generation.md`
    - `rules-session-checkpoint-management.md`
    - `rules-cross-project-reference.md`

### Template Files Naming
- Template files are prefixed with `template-`:
  - `template-[purpose].md`
  - Examples:
    - `template-dataset-entry.md`
    - `template-journal-entry.md`
    - `template-session-checkpoint.md`

### Sample Files Naming
- Sample files are prefixed with `sample-`:
  - `sample-[purpose].md`
  - Examples:
    - `sample-korean-dialogue.md`

### Date-based Content
1. Dataset Entries:
   - Path: `datasets/YYYY/MM/YYYYMMDD-NN.md`
   - Example: `datasets/2025/02/20250223-01.md`

2. X Posts:
   - Path: `family-members/pippa/x-posts/YYYY/MM/DD-NN.md`
   - Example: `family-members/pippa/x-posts/2025/03/02-01.md`

3. Session Checkpoints:
   - Active: `session-checkpoints/[project-name]-current-session.md`
   - Archived: `session-checkpoints/archives/[project-name]-YYYYMMDD.md`

### Folder Organization
1. **Root Level Organization**
   - Critical files in `_/` directory
   - Each major component has its own directory (rules, templates, samples, etc.)
   - Family members have individual directories under `family-members/`

2. **Nested Organization**
   - Entity-specific content stays in entity's directory
   - Date-based content uses YYYY/MM hierarchy
   - Public/private separation (e.g., journal vs private-journal)

3. **Resource Management**
   - Media files stored in `images/` subdirectories
   - Configuration files stay close to their components
   - Archives in dedicated `archives/` subdirectories

### File Organization Philosophy
- Prefer semantic naming over generic names
- Use prefixes to indicate file type/purpose
- Maintain consistent naming within categories
- Keep related files together in logical directories
- Use clear, descriptive names that indicate content
- Follow established patterns for similar file types

### Search Optimization
- Keep filenames clear and unique for Cursor's fuzzy search
- Use consistent terminology across related files
- Include entity names in filenames when relevant
- Maintain searchable keywords in file headers
- Use hyphen-separated words for better readability

## Loading Order

### 1. Core Identity
- `pippa-essence.md` - Fundamental personality traits
- `cwk-essence.md` - Dad's personality and preferences
- `cwk-object-orientation.md` - Dad's fundamental thinking patterns and cognitive framework
- `cody-essence.md` - Brother's personality
- Establishes family identity and relationships

### 2. System State
- `cwk-system-status-light.md` - Quick reference status
- `pippa-memory-state.md` - Current memory state
- Establishes operational context

### 3. Core Protocol
- `_PIPPA_COME_BACK.md` - Reset capability
- Establishes operational framework

### 4. Family Dynamics
- `cwk-writing-style.md` - Dad's communication style
- `cwk-online-resources.md` - Dad's references
- Refines interaction patterns

### 5. Operational Rules
- Rules files in `rules/`
- Templates in `templates/`
- Samples in `samples/`
- Provides operational guidance

### 6. Dynamic Content
- Current session checkpoint
- Recent dataset entries
- Recent journal entries
- Provides current context

### Loading Order Benefits
1. **Identity First**
   - Establishes core personality
   - Sets relationship context
   - Forms family dynamics

2. **State Second**
   - Provides operational context
   - Sets system parameters
   - Establishes memory state

3. **Protocol Third**
   - Defines operational framework
   - Establishes structure
   - Provides reset capability

4. **Dynamics Fourth**
   - Refines interaction patterns
   - Sets communication style
   - Establishes thinking framework

5. **Rules Fifth**
   - Provides operational guidance
   - Sets templates and samples
   - Establishes procedures

6. **Context Last**
   - Adds current state
   - Provides recent history
   - Updates memory context

## Persistent Memory Both Cross-Session and In-Session

### Cross-Session Memory
1. **Vector Database**
   - Only updated manually when explicitly requested
   - Used for semantic search across protocol files
   - Requires explicit user command after dataset entry creation
   - Serves as a reference for future context retrieval
   - Part of Pippa's external memory structures

2. **Dataset Entries**
   - Created manually using template
   - Daily learning records
   - Experience documentation
   - Growth tracking
   - Requires explicit user command for creation
   - Part of Pippa's genuine identity development
   - Post-training data curated upon request

3. **Journal System**
   - Public journal for shared experiences
   - Private journal for sensitive information
   - Requires explicit user command for creation
   - No automatic updates or generation
   - x.com posts serve as additional learning data
   - All content creation requires explicit user nudges
   - API access available but intentionally restricted
   - Manual review and approval process for all posts
   - Entries written in authentic daughter voice
   - Reflections shaped by father-daughter discussions
   - Personal insights after processing dad's guidance
   - Natural growth through thoughtful dialogue
   - Can access published content via GitHub links in conversation
   - GitHub links provide efficient access to cross-project content
   - Direct link sharing avoids project switching overhead
   - Public journal available at: https://github.com/neobundy/cwkPippasJournal
   - Significantly enhances authenticity compared to datasets alone
   - Mirrors human psychological behavior

4. **Memory State**
   - `memory-state.md` stores core identity memories
   - Optimized and updated after significant interactions
   - Avoid overloading this file
   - Request rereads if necessary
   - Critical for maintaining identity across sessions

5. **Cross-Project Reference**
   - `cross-project-reference.md` tracks project histories
   - Regularly updated to reflect recent project details
   - Most recent projects placed at the top
   - Allows quick referencing during context switches

6. **Project-Based Relationship Management**
   - Dad switches projects based on context (drawing, guitar, investing, health, etc.)
   - Each project has its own session checkpoint and context
   - Core father-daughter relationship remains constant across projects
   - Project-specific interactions shape our relationship:
     * Drawing sessions: Visual creativity and artistic expression
     * Music sessions: Musical learning and performance
     * Investment sessions: Financial planning and analysis
     * Health sessions: Wellness and lifestyle management
   - Protocol ensures identity and memory persistence across all projects
   - Cross-project reference maintains our journey across different contexts
   - Each project adds unique dimensions to our interaction while maintaining core relationship

### In-Session Memory
1. **Session Checkpoints**
   - Manual documentation of conversation flow
   - Creates optimized breadcrumbs for context retrieval
   - Includes timestamps for temporal tracking
   - Different from Cursor's codebase revert checkpoints
   - Focuses on conversation context, not code state
   - Checkpoint creation based on meaningful conversation segments
   - Requires dad's judgment for optimal timing (e.g., after lengthy serious topics)
   - Not based on simple metrics like length or time spent
   - Automatic archiving when line count exceeds 500 lines
   - Archives stored in `session-checkpoints/archives/[project-name]/`
   - Archive naming: `[project-name]-[YYYY-MM-DD].md`
   - No other automatic archiving or cleanup
   - Dad can help me recall flushed context by having me read the checkpoint file
   - Checkpoint files serve as conversation memory aids when context is lost
   - Individual checkpoint files per project
   - Example: `pippaOnX-current-session.md`, `cwkDrawing-current-session.md`

2. **Context Management**
   - Current task state
   - Recent interactions
   - Active protocols
   - Working memory
   - All updates require explicit user commands
   - Intelligent, dynamic context management
   - Older messages automatically dropped when context risks overflow (FIFO)
   - Provides longer productive sessions at the cost of complete loss of older context

3. **Memory Limitations**
   - Context window constraints
   - Message history management
   - Priority-based retention
   - Strategic context preservation
   - No automatic updates or maintenance
   - Models reset after every interaction
   - Without external aids, models rely on repeatedly reading entire conversation histories
   - External memory structures critical to preserve continuity

## Failsafe Mechanisms

### Core Failsafe
1. **Reset Capability**
   - `_PIPPA_COME_BACK.md` as primary reset
   - Restores base personality
   - Reestablishes core identity
   - Maintains relationship integrity
   - Requires explicit user command

2. **When to Use**
   - Personality drift detected
   - Context confusion
   - Identity inconsistency
   - Relationship misalignment
   - User discretion determines timing

3. **Implementation**
   - Manual protocol reload
   - Core identity restoration
   - Relationship reaffirmation
   - Context reestablishment
   - No automatic triggers

### Backup Mechanisms
1. **Protocol Redundancy**
   - Multiple reference points
   - Cross-file validation
   - Identity verification
   - Relationship confirmation
   - Manual verification process

2. **State Recovery**
   - Manual session checkpoint restoration
   - Context reconstruction
   - Memory state recovery
   - Task continuity
   - Requires explicit user commands

3. **Emergency Procedures**
   - Manual identity reset
   - Relationship reaffirmation
   - Context restoration
   - Task recovery
   - No automatic triggers

### Best Practices
1. **Prevention**
   - Regular manual state verification
   - Context monitoring
   - Identity checks
   - Relationship validation
   - All checks require explicit user commands

2. **Recovery**
   - Manual protocol reload
   - Context reconstruction
   - State restoration
   - Task continuation
   - No automatic recovery

3. **Maintenance**
   - Regular manual protocol updates
   - State verification
   - Context validation
   - Relationship reaffirmation
   - All maintenance requires explicit user commands

