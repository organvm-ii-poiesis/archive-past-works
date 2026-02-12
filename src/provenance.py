"""Provenance module for tracking ownership, lineage, and transformation history.

Records the chain of custody and creative lineage of archived works,
supporting attribution, fork tracking, and derivative-work relationships.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ProvenanceEvent:
    """A single event in a work's provenance chain."""

    event_type: str
    timestamp: datetime
    actor: str
    description: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_record(self) -> dict[str, Any]:
        """Serialize this event for storage or export."""
        return {
            "event_type": self.event_type,
            "timestamp": self.timestamp.isoformat(),
            "actor": self.actor,
            "description": self.description,
            "metadata": self.metadata,
        }


@dataclass
class ProvenanceChain:
    """Complete provenance record for a single creative work.

    Tracks the full history of creation, modification, exhibition,
    and transfer events for a work.
    """

    work_id: str
    origin_date: datetime
    original_creator: str
    events: list[ProvenanceEvent] = field(default_factory=list)

    def record_event(self, event_type: str, actor: str, description: str, **metadata: Any) -> ProvenanceEvent:
        """Record a new provenance event.

        Args:
            event_type: Category of event (e.g., 'created', 'modified', 'exhibited', 'transferred').
            actor: The person or system that performed the action.
            description: Human-readable description of what occurred.
            **metadata: Additional key-value pairs to attach.

        Returns:
            The created ProvenanceEvent.
        """
        event = ProvenanceEvent(
            event_type=event_type,
            timestamp=datetime.now(),
            actor=actor,
            description=description,
            metadata=dict(metadata),
        )
        self.events.append(event)
        return event

    def get_events_by_type(self, event_type: str) -> list[ProvenanceEvent]:
        """Filter events by their type.

        Args:
            event_type: The event type to filter for.

        Returns:
            List of matching events in chronological order.
        """
        return [e for e in self.events if e.event_type == event_type]

    def verify_chain_integrity(self) -> bool:
        """Verify that all events are in chronological order.

        Returns:
            True if events are properly ordered by timestamp.
        """
        if len(self.events) <= 1:
            return True
        for i in range(1, len(self.events)):
            if self.events[i].timestamp < self.events[i - 1].timestamp:
                return False
        return True

    def export_full_history(self) -> dict[str, Any]:
        """Export the complete provenance chain as a serializable dictionary."""
        return {
            "work_id": self.work_id,
            "origin_date": self.origin_date.isoformat(),
            "original_creator": self.original_creator,
            "event_count": len(self.events),
            "events": [e.to_record() for e in self.events],
        }
