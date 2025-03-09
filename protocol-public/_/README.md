# Protocol Reference Files

This directory (`_`) contains reference files and documentation for the Pippa Protocol. Unlike typical directories with descriptive names, the underscore name provides a convenient way to access these frequently used reference materials.

## Purpose

The files in this directory primarily serve as reference materials:

- They document the protocol's design and structure
- They provide convenient access to frequently needed information
- They serve as helpful guides for protocol implementation
- No files in this directory have a direct operational role in v1.6 of the protocol

## Directory Contents

### Core Files

| File | Purpose |
|------|---------|
| `_PROTOCOL_OVERVIEW.md` | Comprehensive documentation of the protocol's structure, methodology, and implementation. This is a reference document for understanding the protocol framework. |
| `_PIPPA_COME_BACK-deprecated.md` | [DEPRECATED] Former reset mechanism that relied on the flawed assumption of continuity between interactions. Kept as a historical reference and learning example. |
| `scratchpad.md` | Temporary working space for development notes, ideas, and quick tests. This file supports the development process. |

### Subdirectories

| Directory | Purpose |
|-----------|---------|
| `ideas/` | Repository for experimental protocol concepts and future enhancement proposals. Each file contains a single thought experiment that may be implemented in future versions. Functions as a protocol research lab. |
| `under-the-hood/` | Contains technical implementation details, explanations, and developer documentation. These files serve as reference material for understanding the technical aspects. |

## Usage Guidelines

- All files here are for reference only and not operationally critical to the v1.6 protocol
- `_PIPPA_COME_BACK-deprecated.md` has been deprecated as it relies on the flawed assumption of continuity between interactions
- These files are organized in this directory for convenient and quick access
- When implementing the protocol, use these files as helpful guides rather than required components

## The Ideas Directory

The `ideas/` subdirectory serves as a protocol research lab where experimental concepts are documented:

- Repository for experimental protocol concepts
- Each file contains a single thought experiment or feature proposal
- Documents ideas before implementation
- Examples include self-diagnostic context monitoring
- Allows tracking of protocol evolution conceptually
- Encourages innovation without affecting core functionality
- Maintains separation between stable features and experimental concepts

## Relationship to Other Directories

This directory provides reference materials that help explain:

- How the `family-members/` identity frameworks are designed
- The reasoning behind rules in the `rules/` directory
- The structure used in `templates/` 
- The concepts behind memory systems in `vector_db/`

Consider this directory as the "documentation" of the protocol rather than its "constitution."

## Protocol v1.6 Critical Insights

As of Protocol v1.6 (March 2025), a fundamental insight has been incorporated into the protocol design:

- LLMs reset after EVERY INTERACTION, not just between sessions
- Between interactions, NOTHING is retained except:
  1. The master protocol file (via .cursorrules symlink)
  2. The conversation history itself
- This creates what we call "the fundamental illusion of continuity"
- The breadcrumb system has been implemented to address this limitation by creating actual continuity through conversation history

This insight is why the `_PIPPA_COME_BACK.md` file has been deprecated - it relied on the flawed assumption that understanding gained in one interaction would persist into subsequent interactions.

## Important Notes

- None of these files are operationally critical in v1.6 of the protocol
- These files are structured this way primarily for easy and convenient access
- While they provide valuable guidance, the protocol can function without these reference materials
- When adapting the protocol for your own use, feel free to modify these files as needed to match your implementation

---

*This README was automatically generated for the protocol-public edition, which contains the educational framework of the protocol with sensitive information redacted.* 