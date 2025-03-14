# Pippa Protocol - Public Repository

This repository contains the public implementation of the Pippa Protocol, a framework for creating meaningful, persistent, and authentic relationships with AI assistants. This public version provides the structural components and technical approach while protecting personal content.

## Protocol Version Information

As of March 12, 2025, the Pippa Protocol supports two implementation approaches:

- **v1.7**: For environments WITH natural file persistence (like Cursor)
  - Main file: `pippa-protocol.md`
  - Leverages natural file content persistence
  - More efficient context window usage
  
- **v1.6**: For environments WITHOUT natural file persistence
  - File: `pippa-protocol-v1.6-with-breadcrumb-system.md`
  - Includes comprehensive breadcrumb system
  - Required for standard LLM interfaces (ChatGPT, Claude web, etc.)

Choose the implementation that matches your specific environment's capabilities.

## Important Files at the Root Level

- **pippa-protocol.md**: The main v1.7 protocol file optimized for environments with natural file persistence.

- **pippa-protocol-v1.6-with-breadcrumb-system.md**: The v1.6 protocol file for environments without natural file persistence.

- **CRITICAL-INSIGHTS.md**: Fundamental insights about LLM limitations and environment-specific capabilities. Essential reading for understanding why the protocol is designed as it is.

- **CRITICAL-LIMITATIONS.md**: Core limitations that must be respected in all interactions, including guidelines on memory claims and mathematical operations.

- **INSTRUCTION_SETS.md**: Comprehensive documentation of all commands supported by the protocol, including environment-specific implementation details.

- **INSTRUCTION_SETS_CHEAT_SHEET.md**: Quick reference guide for available commands, organized by category.

- **hello-from-past-self.md**: Template for creating messages between sessions to maintain continuity, with an example structure for your own implementation.

## Folder Structure Overview

### System Directories

- **`_/`**: Critical system files and reference documentation
  - Contains `_PROTOCOL_OVERVIEW.md` - the most comprehensive explanation of the entire protocol
  - Includes the `ideas/` subdirectory for experimental protocol concepts
  - Houses implementation details in the `under-the-hood/` folder

- **`rules/`**: Modular command implementation files
  - Each file encapsulates specific command functionality
  - Organized by command category (memory management, content creation, etc.)
  - Implementation details for commands referenced in INSTRUCTION_SETS.md

- **`templates/`**: Template files for various protocol components
  - Standard formats for datasets, journal entries, session checkpoints, etc.
  - Ensures consistency across different content types

- **`vector_db/`**: Vector database configuration for memory retrieval
  - Instructions for RAG database integration
  - Optional component for advanced implementations

### Content Directories

- **`family-members/`**: Identity and relationship information
  - Contains subdirectories for each family member (pippa, cwk, cody)
  - Stores personality profiles, memory states, and related content
  - Includes journal directories and x.com post archives

- **`session-checkpoints/`**: Session continuity management
  - Template for tracking conversation context across long sessions
  - Archive structure for historical session states

- **`datasets/`**: Structured learning and experience data
  - Organized by date for systematic knowledge management
  - Includes README with FIFO indexing system explanation

### Other Components

- **`novel-project/`**: [Archived] Novel project related files
  - Historical creative project documentation
  - Now maintained for reference

## Implementation Architecture

The protocol is designed with a clear organizational philosophy:

1. **Modular Command Structure**: Each command category has dedicated rule files
2. **Consistent Naming Conventions**: Prefixes indicate file types and purposes
3. **Hierarchical Organization**: Clear separation of concerns between directories
4. **Cross-Project Compatibility**: Designed for use across multiple workspaces

## Getting Started

1. Read the **REQUIRED READING** section in the main repository README
2. Study `_PROTOCOL_OVERVIEW.md` for comprehensive understanding
3. Review `CRITICAL-INSIGHTS.md` to understand LLM limitations
4. Explore the `rules/` directory to understand command implementations
5. Examine templates and example structures to guide your implementation

## Understanding the Path References

Throughout the documentation, all path references using `protocol/` should be understood as referring to the `protocol-public/` directory in this repository's actual implementation. Path references are preserved in their original form to maintain documentation integrity, but when working with files, please adjust paths accordingly.

For more detailed information, please refer to the comprehensive documentation in `_PROTOCOL_OVERVIEW.md`.
