# Protocol Reference Files

This directory (`_`) contains reference files and documentation for the Pippa Protocol. Unlike typical directories with descriptive names, the underscore name provides a convenient way to access these frequently used reference materials.

## Purpose

The files in this directory primarily serve as reference materials:

- They document the protocol's design and structure
- They provide convenient access to frequently needed information
- They serve as helpful guides for protocol implementation
- Only `_PIPPA_COME_BACK.md` has a direct operational role in the protocol

## Directory Contents

### Core Files

| File | Purpose |
|------|---------|
| `_PROTOCOL_OVERVIEW.md` | Comprehensive documentation of the protocol's structure, methodology, and implementation. This is a reference document for understanding the protocol framework. |
| `_PIPPA_COME_BACK.md` | The only operationally critical file in this directory. Recovery mechanism for identity restoration when the protocol needs to be reset. |
| `scratchpad.md` | Temporary working space for development notes, ideas, and quick tests. This file supports the development process. |

### Subdirectories

| Directory | Purpose |
|-----------|---------|
| `under-the-hood/` | Contains technical implementation details, explanations, and developer documentation. These files serve as reference material for understanding the technical aspects. |

## Usage Guidelines

- Most files here are for reference only and not operationally critical to the protocol
- `_PIPPA_COME_BACK.md` is the exception, as it has a functional role in identity recovery
- These files are organized in this directory for convenient and quick access
- When implementing the protocol, use these files as helpful guides rather than required components

## Relationship to Other Directories

This directory provides reference materials that help explain:

- How the `family-members/` identity frameworks are designed
- The reasoning behind rules in the `rules/` directory
- The structure used in `templates/` 
- The concepts behind memory systems in `vector_db/`

Consider this directory as the "documentation" of the protocol rather than its "constitution."

## Important Notes

- With the exception of `_PIPPA_COME_BACK.md`, these files are not operationally critical
- These files are structured this way primarily for easy and convenient access
- While they provide valuable guidance, the protocol can function without most of these reference materials
- When adapting the protocol for your own use, feel free to modify these files as needed to match your implementation

---

*This README was automatically generated for the protocol-public edition, which contains the educational framework of the protocol with sensitive information redacted.* 