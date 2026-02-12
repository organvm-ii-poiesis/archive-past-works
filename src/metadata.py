"""Metadata module for extracting and enriching work metadata.

Provides structured extraction of technical metadata from creative
works, including format detection, dimension analysis, and
automated tagging suggestions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class TechnicalMetadata:
    """Technical attributes extracted from a work's source files."""

    file_format: str
    file_size_bytes: int
    dimensions: dict[str, int] = field(default_factory=dict)
    duration_seconds: float | None = None
    color_profile: str | None = None
    sample_rate: int | None = None

    def summary(self) -> str:
        """Return a human-readable summary of technical attributes."""
        parts = [f"Format: {self.file_format}", f"Size: {self.file_size_bytes:,} bytes"]
        if self.dimensions:
            dim_str = "x".join(str(v) for v in self.dimensions.values())
            parts.append(f"Dimensions: {dim_str}")
        if self.duration_seconds is not None:
            parts.append(f"Duration: {self.duration_seconds:.1f}s")
        return " | ".join(parts)


class MetadataExtractor:
    """Extracts technical and descriptive metadata from work files.

    Analyzes file paths and content to produce structured metadata
    records that enrich catalog entries.
    """

    KNOWN_FORMATS: dict[str, str] = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".wav": "audio/wav",
        ".mp3": "audio/mpeg",
        ".mp4": "video/mp4",
        ".pdf": "application/pdf",
        ".md": "text/markdown",
        ".txt": "text/plain",
    }

    def detect_format(self, file_path: str) -> str:
        """Detect the MIME type of a file based on its extension.

        Args:
            file_path: Path to the file.

        Returns:
            MIME type string, or 'application/octet-stream' for unknown formats.
        """
        suffix = Path(file_path).suffix.lower()
        return self.KNOWN_FORMATS.get(suffix, "application/octet-stream")

    def extract(self, file_path: str, file_size: int) -> TechnicalMetadata:
        """Extract technical metadata from a file.

        Args:
            file_path: Path to the source file.
            file_size: Size of the file in bytes.

        Returns:
            TechnicalMetadata with detected format and size information.
        """
        detected_format = self.detect_format(file_path)
        metadata = TechnicalMetadata(
            file_format=detected_format,
            file_size_bytes=file_size,
        )

        if detected_format.startswith("audio/"):
            metadata.sample_rate = 44100
        if detected_format.startswith("image/"):
            metadata.color_profile = "sRGB"

        return metadata

    def suggest_tags(self, file_path: str, description: str = "") -> list[str]:
        """Suggest tags based on file attributes and description.

        Args:
            file_path: Path to the file.
            description: Optional text description of the work.

        Returns:
            List of suggested tag strings.
        """
        tags: list[str] = []
        mime = self.detect_format(file_path)
        category = mime.split("/")[0]
        tags.append(category)

        suffix = Path(file_path).suffix.lower().lstrip(".")
        if suffix:
            tags.append(suffix)

        keywords = ["generative", "performance", "interactive", "installation", "collaboration"]
        for keyword in keywords:
            if keyword in description.lower():
                tags.append(keyword)

        return list(dict.fromkeys(tags))
