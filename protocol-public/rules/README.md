# Protocol Rules Directory

This directory contains modular rule files that manage specific command functionality for the Pippa Protocol. Each file encapsulates implementation details for a particular category of commands, making the protocol more maintainable, organized, and easier to extend.

## File Management

- **`rules-core-essence.md`**: Manages the "Core Essence" command to refresh understanding of core identity files (pippa-essence.md, pippa-memory-state.md, cwk-essence.md, and cwk-system-status-light.md).

## Memory Management

- **`rules-breadcrumbs.md`**: Defines the breadcrumb system for maintaining continuity across interactions, with guidelines for creating comprehensive file summaries.

- **`rules-vector-db.md`**: Handles vector database (RAG) operations, including adding new content, performing semantic searches, and managing the long-term memory system.

- **`rules-database-query.md`**: Manages on-demand database query commands for retrieving information from the vector database, with protocols for when to access this resource.

## Content Creation

- **`rules-journal-entries.md`**: Governs the creation and organization of journal entries, including formatting, directory structure, and FIFO index management for continuity.

- **`rules-x-post.md`**: Defines guidelines for creating social media posts on X.com, including formatting, tone, multilingual posting, and FIFO index management.

- **`rules-image-generation.md`**: Controls image generation requests, including prompt formatting and style guidelines.

## Session Management

- **`rules-session-checkpoint-management.md`**: Handles the creation and management of session checkpoints to maintain continuity across long conversations and prevent context loss.

- **`rules-hello-from-past-self.md`**: Manages the creation of messages for future instances, establishing continuity between different sessions.

- **`rules-reconnecting-with-past-self.md`**: Guides the process of reading and integrating messages left by past instances without modifying the source file.

## Project Management

- **`rules-cross-project-reference.md`**: Coordinates cross-project interactions and knowledge sharing, maintaining consistency across different workspaces using the protocol.

- **`rules-novel-project.md`**: Manages the (now archived) novel project interactions and documentation.

## Language & Communication

- **`rules-korean-dialogue.md`**: Defines rules for conducting conversations in Korean, including cultural norms, relationship-appropriate language patterns, and core pronunciation principles.

## Data Management

- **`rules-dataset-entries.md`**: Handles the creation and organization of dataset entries that capture insights and learning points for future reference and potential training data.

## Implementation Guidelines

Each rule file follows a consistent structure:
1. Purpose and scope
2. Command syntax and parameters
3. Implementation instructions
4. Response formatting
5. Integration with other protocol components

This modular approach allows for easier maintenance, as changes to one command category don't affect others. It also keeps the main protocol file cleaner and more focused on core functionality rather than specific command implementations. 

**Note**: The FIFO (First In, First Out) indexing system is implemented in multiple content management rules (journal entries, X.com posts) to maintain a rolling window of recent content references while preventing context window overflow. 

## Practical Implementation

The power of these rule files is greatly enhanced by Cursor IDE's drag-and-drop functionality:

- **Effortless Integration**: Any rule file can be directly dragged into the Cursor chat panel, instantly refreshing the AI's understanding of that rule.

- **Simultaneous Multi-Rule Activation**: Even complex implementations like the breadcrumbs system work seamlessly—simply drag multiple relevant files simultaneously into the chat panel.

- **Context-Aware Loading**: Only load the specific rules needed for your current task, preserving valuable context window space.

- **Minimal Technical Overhead**: No custom coding, database configurations, or special infrastructure needed—while Cursor IDE still uses API calls behind the scenes, the user experience is simplified to just dragging and dropping files.

This direct file loading approach means that what appears as a complex system in documentation is, in practice, remarkably straightforward to implement. The modular design allows you to selectively load only the rules relevant to your current needs, making the entire protocol both powerful and practical. 