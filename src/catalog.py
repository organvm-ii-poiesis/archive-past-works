"""Catalog module for indexing and organizing archived creative works.

Provides a structured inventory of past works with categorization,
tagging, and full-text search capabilities across the archive.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class Medium(Enum):
    """Creative medium classifications."""

    VISUAL = "visual"
    AUDIO = "audio"
    TEXT = "text"
    PERFORMANCE = "performance"
    INTERACTIVE = "interactive"
    MIXED = "mixed"


@dataclass
class CatalogEntry:
    """A single work in the archive catalog."""

    work_id: str
    title: str
    medium: Medium
    created_date: datetime
    tags: list[str] = field(default_factory=list)
    description: str = ""
    collaborators: list[str] = field(default_factory=list)
    source_organ: str = "poiesis"

    def matches_query(self, query: str) -> bool:
        """Check if this entry matches a text search query.

        Searches across title, description, and tags (case-insensitive).

        Args:
            query: The search string to match against.

        Returns:
            True if the query matches any searchable field.
        """
        query_lower = query.lower()
        if query_lower in self.title.lower():
            return True
        if query_lower in self.description.lower():
            return True
        if any(query_lower in tag.lower() for tag in self.tags):
            return True
        return False

    def to_record(self) -> dict[str, Any]:
        """Serialize this entry to a flat dictionary for export."""
        return {
            "work_id": self.work_id,
            "title": self.title,
            "medium": self.medium.value,
            "created_date": self.created_date.isoformat(),
            "tags": self.tags,
            "description": self.description,
            "collaborators": self.collaborators,
            "source_organ": self.source_organ,
        }


class Catalog:
    """Central index of all archived creative works.

    Supports adding, searching, and filtering works by medium,
    date range, and free-text query.
    """

    def __init__(self) -> None:
        self._entries: dict[str, CatalogEntry] = {}

    def add_entry(self, entry: CatalogEntry) -> None:
        """Register a new work in the catalog.

        Args:
            entry: The catalog entry to add.

        Raises:
            ValueError: If a work with the same ID already exists.
        """
        if entry.work_id in self._entries:
            raise ValueError(f"Duplicate work_id: '{entry.work_id}'")
        self._entries[entry.work_id] = entry

    def search(self, query: str) -> list[CatalogEntry]:
        """Search all entries by free-text query.

        Args:
            query: Search string to match.

        Returns:
            List of matching entries, ordered by creation date (newest first).
        """
        matches = [e for e in self._entries.values() if e.matches_query(query)]
        return sorted(matches, key=lambda e: e.created_date, reverse=True)

    def filter_by_medium(self, medium: Medium) -> list[CatalogEntry]:
        """Return all entries of a specific creative medium.

        Args:
            medium: The medium to filter by.

        Returns:
            List of matching entries.
        """
        return [e for e in self._entries.values() if e.medium == medium]

    def get_entry(self, work_id: str) -> CatalogEntry:
        """Retrieve a single entry by its work ID.

        Raises:
            KeyError: If no entry with the given ID exists.
        """
        return self._entries[work_id]

    @property
    def total_works(self) -> int:
        """Return the total number of cataloged works."""
        return len(self._entries)
