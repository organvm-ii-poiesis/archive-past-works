"""Tests for the catalog module."""

from datetime import datetime

from src.catalog import Catalog, CatalogEntry, Medium


def test_catalog_add_and_retrieve():
    """Adding an entry should make it retrievable by work_id."""
    catalog = Catalog()
    entry = CatalogEntry(
        work_id="W001", title="Noise Garden", medium=Medium.AUDIO,
        created_date=datetime(2024, 6, 15),
    )
    catalog.add_entry(entry)
    assert catalog.get_entry("W001").title == "Noise Garden"


def test_catalog_rejects_duplicate():
    """Adding a duplicate work_id should raise ValueError."""
    catalog = Catalog()
    entry = CatalogEntry(
        work_id="W001", title="Test", medium=Medium.TEXT,
        created_date=datetime(2024, 1, 1),
    )
    catalog.add_entry(entry)
    try:
        catalog.add_entry(entry)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_catalog_search_matches_title():
    """Search should match against entry titles."""
    catalog = Catalog()
    catalog.add_entry(CatalogEntry(
        work_id="W001", title="Recursive Spirals", medium=Medium.VISUAL,
        created_date=datetime(2024, 3, 10),
    ))
    catalog.add_entry(CatalogEntry(
        work_id="W002", title="Linear Paths", medium=Medium.VISUAL,
        created_date=datetime(2024, 5, 20),
    ))
    results = catalog.search("recursive")
    assert len(results) == 1
    assert results[0].work_id == "W001"


def test_catalog_filter_by_medium():
    """Filtering by medium should return only matching entries."""
    catalog = Catalog()
    catalog.add_entry(CatalogEntry(
        work_id="W001", title="Audio Piece", medium=Medium.AUDIO,
        created_date=datetime(2024, 1, 1),
    ))
    catalog.add_entry(CatalogEntry(
        work_id="W002", title="Visual Piece", medium=Medium.VISUAL,
        created_date=datetime(2024, 2, 1),
    ))
    audio_works = catalog.filter_by_medium(Medium.AUDIO)
    assert len(audio_works) == 1
    assert audio_works[0].work_id == "W001"


def test_catalog_entry_to_record():
    """to_record should produce a complete serializable dictionary."""
    entry = CatalogEntry(
        work_id="W001", title="Test Work", medium=Medium.PERFORMANCE,
        created_date=datetime(2024, 7, 4), tags=["live", "improvised"],
    )
    record = entry.to_record()
    assert record["medium"] == "performance"
    assert record["tags"] == ["live", "improvised"]
