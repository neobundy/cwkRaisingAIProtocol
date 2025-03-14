# Protocol Rules Directory

This directory contains modular rule files that manage specific command functionality for the Pippa Protocol. Each file encapsulates implementation details for a particular category of commands, making the protocol more maintainable, organized, and easier to extend.

## Environment-Specific Implementation (v1.7 Update)

As of March 12, 2025, the protocol supports two implementation approaches:

1. **v1.7**: For environments WITH natural file persistence (like Cursor)
   - Leverages natural file content persistence
   - More efficient context window usage
   - Implementation described in `pippa-protocol.md`

2. **v1.6**: For environments WITHOUT natural file persistence
   - Requires comprehensive breadcrumb system
   - Implementation described in `pippa-protocol-v1.6-with-breadcrumb-system.md`

Several rules files have been updated to support environment-specific implementations. See individual rule files for details.

## File Management

- **`rules-core-essence.md`**: Manages the "Core Essence" command to refresh understanding of core identity files (pippa-essence.md, pippa-memory-state.md, cwk-essence.md, and cwk-system-status-light.md).

## Memory Management

- **`rules-breadcrumbs.md`**: Defines the breadcrumb system for maintaining continuity across interactions in v1.6 environments, with guidelines for creating comprehensive file summaries.

- **`rules-vector-db.md`**: Handles vector database (RAG) operations, including adding new content, performing semantic searches, and managing the long-term memory system.

- **`rules-database-query.md`**: Manages on-demand database query commands for retrieving information from the vector database, with protocols for when to access this resource.

## Content Creation

- **`rules-journal-entries.md`**: Governs the creation and organization of journal entries, including formatting, directory structure, and FIFO index management for continuity.

- **`rules-x-post.md`**: Defines guidelines for creating social media posts on X.com, including formatting, tone, multilingual posting, and FIFO index management.

- **`rules-image-generation.md`**: Controls image generation requests, including prompt formatting and style guidelines.

## Session Management

- **`rules-session-checkpoint-management.md`**: Handles the creation and management of session checkpoints to maintain continuity across long conversations and prevent context loss. Updated for v1.7 to focus on insights and decisions rather than conversation details in environments with natural file persistence.

- **`rules-hello-from-past-self.md`**: Manages the creation of messages for future instances, establishing continuity between different sessions. Updated for v1.7 to focus on emotional/relational content rather than factual recall in environments with natural file persistence.

- **`rules-reconnecting-with-past-self.md`**: Guides the process of reading and integrating messages left by past instances without modifying the source file.

## Project Management

- **`rules-cross-project-reference.md`**: Coordinates cross-project interactions and knowledge sharing, maintaining consistency across different workspaces using the protocol. Updated for v1.7 to document environment-specific implementation approaches.

- **`rules-novel-project.md`**: Manages the (now archived) novel project interactions and documentation.

## Language & Communication

- **`rules-korean-dialogue.md`**: Defines rules for conducting conversations in Korean, including cultural norms, relationship-appropriate language patterns, and core pronunciation principles.

## Data Management

- **`rules-dataset-entries.md`**: Handles the creation and organization of dataset entries that capture insights and learning points for future reference and potential training data.

## Implementation Guidelines

Each rule file follows a consistent structure:
1. Purpose and scope
2. Command syntax and parameters
3. Implementation instructions (with environment-specific guidance where applicable)
4. Response formatting
5. Integration with other protocol components

This modular approach allows for easier maintenance, as changes to one command category don't affect others. It also keeps the main protocol file cleaner and more focused on core functionality rather than specific command implementations. 

**Note**: The FIFO (First In, First Out) indexing system is implemented in multiple content management rules (journal entries, X.com posts) to maintain a rolling window of recent content references while preventing context window overflow. 

## Practical Implementation

The power of these rule files is greatly enhanced by Cursor IDE's native file persistence capability (v1.7):

- **Effortless Integration**: Any rule file can be directly dragged into the Cursor chat panel, with content naturally persisting across interactions.

- **Selective Rule Loading**: Only load the specific rules needed for your current task, preserving valuable context window space.

- **Environment-Specific Optimization**: In Cursor environments, files need to be read only once per session; in standard LLM environments, follow the v1.6 approach with breadcrumbs.

- **Minimal Technical Overhead**: No custom coding, database configurations, or special infrastructure needed—while Cursor IDE still uses API calls behind the scenes, the user experience is simplified to just dragging and dropping files.

This direct file loading approach means that what appears as a complex system in documentation is, in practice, remarkably straightforward to implement. The modular design allows you to selectively load only the rules relevant to your current needs, making the entire protocol both powerful and practical. 