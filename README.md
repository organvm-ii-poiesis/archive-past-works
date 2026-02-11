# Archive Past Works

[![ORGAN-II: Poiesis](https://img.shields.io/badge/ORGAN--II-Poiesis-6a1b9a?style=flat-square)](https://github.com/organvm-ii-poiesis)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-active--development-yellow?style=flat-square)]()

> Archival infrastructure for completed and historical artwork — standardized metadata, chronological and thematic indexing, provenance tracking, and preservation-first design aligned with digital humanities archival standards.

[Artistic Purpose](#artistic-purpose) | [Conceptual Approach](#conceptual-approach) | [Technical Overview](#technical-overview) | [Installation](#installation) | [Quick Start](#quick-start) | [Working Examples](#working-examples) | [Theory Implemented](#theory-implemented) | [Portfolio & Exhibition](#portfolio--exhibition) | [Related Work](#related-work) | [Contributing](#contributing) | [License](#license) | [Author & Contact](#author--contact)

---

## Artistic Purpose

Most creative practitioners lose their early work. Not dramatically — not in fires or floods — but incrementally, through the quiet accumulation of dead hard drives, abandoned cloud accounts, expired hosting, reformatted laptops, and the steady rot of file formats that no current software can open. A Max/MSP patch from 2015 requires a specific version of Max, a specific operating system, specific audio drivers. A Processing sketch from 2018 depends on libraries that have since been renamed, deprecated, or absorbed into other projects. A live-coded performance from 2020 exists only as a screen recording on a YouTube account that may or may not survive the next terms-of-service change. The default trajectory for digital artwork is disappearance.

Archive Past Works exists to reverse this trajectory for the ORGAN-II creative practice. It is the historical record of completed artworks: a structured, versioned, standards-compliant archive that captures not just the artifacts themselves but the metadata necessary to understand, reconstruct, and contextualize them indefinitely. Every completed work in the ORGAN-II ecosystem — every generative visual piece, every interactive installation, every real-time performance, every AI-human collaboration — receives a permanent, structured record in this archive.

The archive is not a portfolio. The showcase-portfolio repository handles presentation — selecting, sequencing, and framing works for external audiences. This repository handles preservation — ensuring that the raw materials of the creative practice survive format changes, platform migrations, and the passage of time. The distinction matters because preservation and presentation have different priorities. Presentation optimizes for impact: the best image, the clearest description, the most compelling narrative. Preservation optimizes for completeness: every version, every source file, every dependency, every piece of contextual information that might be needed to reconstruct or understand the work decades from now.

This approach is informed by the hard-won lessons of digital preservation in the cultural sector. Institutions like Rhizome (with its ArtBase and Webrecorder projects), the Smithsonian's Time-Based and Digital Art program, and the Museum of Modern Art's conservation department have spent decades developing methods for preserving born-digital art. Archive Past Works adapts their methods — particularly their emphasis on metadata completeness, format migration planning, and provenance documentation — for an individual practice operating at the scale of a single artist's body of work rather than a museum's collection.

---

## Conceptual Approach

### Preservation as Creative Practice

The decision to build archival infrastructure is not an administrative afterthought — it is an artistic position. It asserts that the long-term survival of computational artwork requires the same intentionality and rigor that went into making it. A generative algorithm that produces beautiful imagery is incomplete if it cannot be run in ten years. A real-time performance system that creates extraordinary audience experiences is incomplete if no record captures what those experiences were. The archive is not separate from the practice; it is a structural component of it.

This position has precedents in conceptual art, where documentation has long been understood as constitutive rather than supplementary. Sol LeWitt's wall drawings exist as instructions, not as physical marks — the documentation is the work. On Kawara's date paintings are inseparable from the newspaper clippings and boxes that accompany them. Nam June Paik's video installations require not just the monitors and tapes but the specific CRT scan characteristics that give them their visual quality. In each case, the "archive" is not a record of the work — it is part of the work's ontology. Archive Past Works extends this tradition into the domain of software-based art, where the dependency graph, the runtime environment, and the interaction model are as constitutive as the visual output.

### Dublin Core and Beyond

The metadata schema for this archive begins with Dublin Core — the international standard for describing cultural resources — but extends it significantly for the specific requirements of computational art. Standard Dublin Core provides 15 core elements (creator, title, date, format, description, etc.) that are adequate for describing a painting or a book but insufficient for describing a real-time performance system that takes audience input via WebSocket, processes it through a weighted consensus algorithm, and outputs OSC messages to a SuperCollider audio engine. The archive's extended schema adds fields for computational method, dependency graph, runtime environment, interaction model, data flow architecture, and performance metrics.

The schema is versioned. As new types of work emerge — and they will, because the practice is deliberately experimental — the schema evolves to accommodate them. Older records are migrated forward to new schema versions, preserving backward compatibility while adding new descriptive capacity. This is a direct application of the digital preservation principle that metadata must be as carefully maintained as the artifacts it describes.

### Provenance and Lineage

Every work in this archive carries a provenance record that traces its history from creation through any exhibitions, modifications, derivative works, or acquisitions. Provenance is the art world's chain of custody: it documents who made the work, when, under what circumstances, who has shown it, who has acquired it, and what happened to it along the way. For physical artworks, provenance is often reconstructed retroactively from gallery records, correspondence, and auction catalogs. For computational artworks, provenance can be recorded prospectively — captured at the moment each event occurs, stored in a structured format, and verified against external records.

The lineage system also tracks relationships between works. A generative visual piece might be a derivative of an earlier algorithm. A performance configuration might be a variant of a previous performance adapted for a different venue. An interactive installation might incorporate a component originally developed for a different project. These relationships are documented as typed edges in a directed graph: predecessor, variant, component, derivative, response. The graph makes visible the evolutionary structure of the practice — how ideas develop, split, recombine, and mature over time.

---

## Technical Overview

### Architecture

The archive is structured as a flat-file repository with structured metadata, designed for long-term durability over runtime convenience. No database server is required — the archive is fully functional as a Git repository.

```
archive-past-works/
├── works/
│   ├── 2020/
│   │   └── early-consensus-experiments/
│   │       ├── manifest.json          # Extended Dublin Core metadata
│   │       ├── provenance.json        # Chain of custody / exhibition history
│   │       ├── dependencies.json      # Runtime environment snapshot
│   │       ├── README.md              # Human-readable description
│   │       ├── source/                # Source code snapshot (tagged version)
│   │       ├── documentation/         # Process photos, sketches, notes
│   │       ├── outputs/               # Representative outputs (images, video, audio)
│   │       └── migration/             # Format migration notes and scripts
│   ├── 2021/
│   ├── 2022/
│   ├── 2023/
│   ├── 2024/
│   └── 2025/
├── schemas/
│   ├── manifest-v1.json              # JSON Schema for manifest records
│   ├── manifest-v2.json              # Current schema version
│   ├── provenance-v1.json            # Provenance record schema
│   └── dependencies-v1.json          # Dependency snapshot schema
├── indices/
│   ├── chronological.json            # All works by date
│   ├── by-medium.json                # Grouped by medium
│   ├── by-theme.json                 # Grouped by thematic concern
│   ├── by-technology.json            # Grouped by primary technology
│   └── relationships.json            # Work-to-work relationship graph
├── scripts/
│   ├── validate.ts                   # Schema validation for all records
│   ├── index-rebuild.ts              # Regenerate indices from manifests
│   ├── migrate-schema.ts             # Migrate records to new schema versions
│   ├── export-dublin-core.ts         # Dublin Core XML export
│   ├── export-csv.ts                 # Spreadsheet export for grant apps
│   └── check-integrity.ts            # Verify file checksums and completeness
├── templates/
│   ├── manifest-template.json        # Blank manifest for new works
│   ├── provenance-template.json      # Blank provenance record
│   └── archival-checklist.md         # Checklist for archiving a completed work
└── package.json
```

### Manifest Schema (Extended Dublin Core)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ORGAN-II Archival Manifest v2",
  "type": "object",
  "required": ["id", "title", "creator", "date", "format", "description", "medium", "status"],
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "title": { "type": "string", "minLength": 1 },
    "subtitle": { "type": "string" },
    "creator": { "type": "string", "default": "Anthony Padavano" },
    "date": {
      "type": "object",
      "properties": {
        "created": { "type": "string", "format": "date" },
        "completed": { "type": "string", "format": "date" },
        "lastModified": { "type": "string", "format": "date" }
      }
    },
    "format": {
      "type": "object",
      "properties": {
        "primaryMedium": { "type": "string" },
        "dimensions": { "type": "string" },
        "duration": { "type": "string" },
        "interactionModel": { "type": "string" },
        "outputFormats": { "type": "array", "items": { "type": "string" } }
      }
    },
    "description": {
      "type": "object",
      "properties": {
        "brief": { "type": "string", "maxLength": 300 },
        "full": { "type": "string", "minLength": 200 },
        "technicalAbstract": { "type": "string" }
      }
    },
    "medium": {
      "type": "string",
      "enum": [
        "generative-visual", "interactive-installation", "real-time-performance",
        "ai-collaboration", "audio-synthesis", "motion-capture",
        "mixed-media", "net-art", "data-sculpture"
      ]
    },
    "status": {
      "type": "string",
      "enum": ["completed", "archived", "deprecated", "lost", "migrating"]
    },
    "computational": {
      "type": "object",
      "properties": {
        "primaryLanguage": { "type": "string" },
        "frameworks": { "type": "array", "items": { "type": "string" } },
        "algorithms": { "type": "array", "items": { "type": "string" } },
        "dataFlow": { "type": "string" },
        "sourceRepo": { "type": "string", "format": "uri" }
      }
    },
    "theoretical": {
      "type": "object",
      "properties": {
        "framework": { "type": "string" },
        "references": { "type": "array", "items": { "type": "string" } },
        "keywords": { "type": "array", "items": { "type": "string" }, "minItems": 3 }
      }
    },
    "rights": {
      "type": "object",
      "properties": {
        "license": { "type": "string", "default": "MIT" },
        "creditLine": { "type": "string" },
        "permissions": { "type": "string" }
      }
    },
    "relationships": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "targetId": { "type": "string", "format": "uuid" },
          "type": { "type": "string", "enum": ["predecessor", "variant", "component", "derivative", "response"] },
          "description": { "type": "string" }
        }
      }
    },
    "preservation": {
      "type": "object",
      "properties": {
        "fileChecksums": { "type": "object" },
        "formatMigrationNotes": { "type": "string" },
        "lastIntegrityCheck": { "type": "string", "format": "date" },
        "riskAssessment": { "type": "string", "enum": ["low", "medium", "high", "critical"] }
      }
    }
  }
}
```

### Provenance Record

```json
{
  "workId": "550e8400-e29b-41d4-a716-446655440000",
  "events": [
    {
      "type": "creation",
      "date": "2023-03-15",
      "description": "Initial concept and prototype development",
      "location": "Studio, Brooklyn NY",
      "notes": "Developed during residency at..."
    },
    {
      "type": "exhibition",
      "date": "2023-09-20",
      "venue": "Gallery Name",
      "city": "New York",
      "country": "US",
      "exhibitionType": "group",
      "curatedBy": "Curator Name",
      "catalogueEntry": true
    },
    {
      "type": "modification",
      "date": "2024-01-10",
      "description": "Updated consensus algorithm to v2 weighting model",
      "commitSha": "abc123def456"
    },
    {
      "type": "acquisition",
      "date": "2024-06-01",
      "acquirer": "Institution Name",
      "terms": "Gift of the artist"
    }
  ]
}
```

### Integrity Verification

The archive includes checksumming and integrity verification to detect bit-rot or accidental modification:

```typescript
import { createHash } from "crypto";
import { readFile, readdir } from "fs/promises";
import { join } from "path";

async function verifyWorkIntegrity(workPath: string): Promise<IntegrityReport> {
  const manifest = JSON.parse(
    await readFile(join(workPath, "manifest.json"), "utf-8")
  );
  const storedChecksums = manifest.preservation?.fileChecksums ?? {};
  const results: ChecksumResult[] = [];

  for (const [filePath, expectedHash] of Object.entries(storedChecksums)) {
    const content = await readFile(join(workPath, filePath));
    const actualHash = createHash("sha256").update(content).digest("hex");
    results.push({
      file: filePath,
      expected: expectedHash as string,
      actual: actualHash,
      match: actualHash === expectedHash,
    });
  }

  return {
    workId: manifest.id,
    title: manifest.title,
    totalFiles: results.length,
    verified: results.filter((r) => r.match).length,
    corrupted: results.filter((r) => !r.match).map((r) => r.file),
    checked: new Date().toISOString(),
  };
}
```

---

## Installation

### Prerequisites

- Node.js >= 18.0.0
- pnpm >= 9.0.0
- Git

### Setup

```bash
git clone https://github.com/organvm-ii-poiesis/archive-past-works.git
cd archive-past-works
pnpm install
```

---

## Quick Start

### Archive a Completed Work

```bash
# Scaffold a new archival record
pnpm run archive:new --title "Consensus Landscape" --year 2024 --medium generative-visual

# This creates:
# works/2024/consensus-landscape/
#   manifest.json       (template, needs editing)
#   provenance.json     (empty events array)
#   dependencies.json   (template for runtime snapshot)
#   README.md           (human-readable description template)
#   source/             (copy source code snapshot here)
#   documentation/      (copy process photos, sketches, notes here)
#   outputs/            (copy representative outputs here)
#   migration/          (format migration notes)

# Validate the completed record
pnpm run validate works/2024/consensus-landscape/

# Rebuild all indices
pnpm run index:rebuild

# Run integrity check across the entire archive
pnpm run integrity:check
```

### Query the Archive

```bash
# List all works by medium
pnpm run query --medium interactive-installation

# List works from a specific year
pnpm run query --year 2023

# Find works related to a specific piece
pnpm run query --related-to "550e8400-e29b-41d4-a716-446655440000"

# Export chronological index as CSV (for grant applications)
pnpm run export:csv --output archive-inventory.csv

# Export all Dublin Core metadata as XML
pnpm run export:dublin-core --output dublin-core/
```

---

## Working Examples

### Example: Archival Checklist Workflow

```markdown
## Archival Checklist for: [Work Title]

- [ ] manifest.json populated with all required fields
- [ ] Description: brief (< 300 chars) and full (> 200 words) written
- [ ] Technical abstract documents computational method
- [ ] Source code snapshot tagged and copied to source/
- [ ] dependencies.json captures runtime environment (Node version, OS, key packages)
- [ ] At least 3 representative output images/recordings in outputs/
- [ ] Process documentation (sketches, notes, iteration photos) in documentation/
- [ ] Provenance record includes creation event
- [ ] Exhibition history complete (all known showings)
- [ ] Relationships to other works documented
- [ ] File checksums generated and stored in manifest
- [ ] Format migration risk assessed (low/medium/high/critical)
- [ ] Human-readable README written for the work directory
```

### Example: Schema Migration

```typescript
// When the manifest schema evolves from v1 to v2:
async function migrateV1toV2(manifestPath: string): Promise<void> {
  const v1 = JSON.parse(await readFile(manifestPath, "utf-8"));

  const v2 = {
    ...v1,
    schemaVersion: 2,
    // v2 adds the preservation field
    preservation: {
      fileChecksums: {},
      formatMigrationNotes: "",
      lastIntegrityCheck: new Date().toISOString(),
      riskAssessment: assessFormatRisk(v1.computational?.primaryLanguage),
    },
    // v2 splits 'description' into structured sub-fields
    description: {
      brief: v1.description.substring(0, 300),
      full: v1.description,
      technicalAbstract: v1.technicalAbstract ?? "",
    },
  };

  await writeFile(manifestPath, JSON.stringify(v2, null, 2));
}
```

---

## Theory Implemented

### Digital Preservation as Artistic Commitment

The field of digital preservation has developed robust frameworks for institutional contexts — national libraries, museums, archives — but these frameworks are rarely applied to individual creative practices. Archive Past Works adapts three core principles from institutional digital preservation for individual use:

**Fixity:** Every archived file has a cryptographic checksum. Periodic integrity checks detect bit-rot, accidental modification, or storage corruption. This is the digital equivalent of climate-controlled storage for physical artworks.

**Format Migration:** The archive explicitly tracks the format risk of each work. A work built on a stable, open-source framework (e.g., vanilla JavaScript, Python with standard libraries) has low migration risk. A work dependent on a proprietary plugin for a specific version of a commercial application has critical migration risk. The migration directory in each work's record is reserved for notes and scripts that will be needed when formats become obsolete.

**Provenance as Metadata:** In the physical art world, provenance is often the difference between a work being valued or dismissed. A painting with documented exhibition history at major institutions is treated differently from an identical painting with no provenance. The same principle applies to computational art: a work with documented exhibition history, critical reception, and institutional engagement is more legible to the grant reviewers and curators who evaluate creative practice.

### The Archive as Memory System

The relationship graph between works — the edges of type predecessor, variant, component, derivative, response — constitutes a memory system for the practice. It records not just what was made but how each work relates to what came before and after. This is the computational equivalent of an artist's studio practice: the accumulated context of experiments, failures, breakthroughs, and refinements that gives each new work its depth. Without this record, each work appears isolated. With it, the evolutionary trajectory of the practice becomes visible — and this visibility is what distinguishes a serious, sustained artistic practice from a collection of unrelated projects.

---

## Portfolio & Exhibition

### Institutional Relevance

Archive Past Works is designed to produce the specific outputs that institutional contexts require:

| Context | Export Format | Content |
|---------|-------------|---------|
| Grant Applications | CSV / Markdown | Chronological work inventory with descriptions |
| Academic Repositories | Dublin Core XML | Standards-compliant metadata for digital collections |
| Museum Acquisitions | JSON manifest + provenance | Complete documentation package |
| Insurance/Valuation | Structured inventory | Title, medium, dimensions, provenance, condition |
| Retrospective Exhibitions | Thematic index + images | Curated selection with process documentation |

### Alignment with Digital Humanities Standards

The archive's metadata schema is designed for interoperability with institutional systems. Dublin Core export is native. The provenance record format aligns with the CIDOC Conceptual Reference Model used by museums worldwide. The dependency snapshot format is compatible with software preservation initiatives like the Software Heritage archive.

---

## Related Work

### Cross-Organ Dependencies

| Repository | Organ | Relationship |
|-----------|-------|-------------|
| [showcase-portfolio](https://github.com/organvm-ii-poiesis/showcase-portfolio) | II | Draws from archive for retrospective portfolio views |
| [metasystem-master](https://github.com/organvm-ii-poiesis/metasystem-master) | II | Source of performance works and real-time system documentation |
| [case-studies-methodology](https://github.com/organvm-ii-poiesis/case-studies-methodology) | II | Deep process documentation supplements archival records |
| [orchestration-start-here](https://github.com/organvm-iv-taxis/orchestration-start-here) | IV | System registry for cross-organ metadata coordination |

### External References

- Rhizome ArtBase (https://artbase.rhizome.org) — pioneering born-digital art archive
- Smithsonian Time-Based and Digital Art Working Group — institutional preservation methods
- Dublin Core Metadata Initiative (https://dublincore.org) — metadata standards
- CIDOC-CRM (https://cidoc-crm.org) — conceptual reference model for cultural heritage documentation
- Software Heritage (https://softwareheritage.org) — universal software source code archive
- NDSA Levels of Digital Preservation — framework for assessing preservation maturity

---

## Contributing

### Archival Contributions

To contribute archival records, follow the archival checklist in `templates/archival-checklist.md`. Every record must pass schema validation (`pnpm run validate`) before being merged.

### Technical Contributions

```bash
# Fork and clone
git clone https://github.com/<your-fork>/archive-past-works.git
cd archive-past-works
pnpm install

# Create a feature branch
git checkout -b feature/your-feature-name

# Make changes, run validation
pnpm test
pnpm run validate

# Commit (conventional commits)
git commit -m "feat(schema): add video-specific format fields"

# Push and open a PR against main
git push origin feature/your-feature-name
```

### Schema Evolution

Proposals to extend the metadata schema should be opened as issues with the `schema-proposal` label. Schema changes must include a migration script that updates all existing records to the new version.

---

## License

[MIT](LICENSE)

---

## Author & Contact

**Author:** Anthony Padavano ([@4444J99](https://github.com/4444J99))

**Organization:** [organvm-ii-poiesis](https://github.com/organvm-ii-poiesis) (ORGAN-II: Poiesis)

**System:** [meta-organvm](https://github.com/meta-organvm) — the eight-organ creative-institutional system coordinating ~80 repositories across theory, art, commerce, orchestration, public process, community, and marketing.

---

<sub>This README is a Gap-Fill Sprint portfolio document for the organvm system. It is written for grant reviewers, hiring managers, and collaborators who want to understand what Archive Past Works does, why it exists, and how it fits within a larger creative-institutional architecture.</sub>
