"""Tests for the metadata module."""

from src.metadata import MetadataExtractor, TechnicalMetadata


def test_detect_format_known():
    """Known file extensions should return their MIME type."""
    extractor = MetadataExtractor()
    assert extractor.detect_format("work.png") == "image/png"
    assert extractor.detect_format("song.mp3") == "audio/mpeg"


def test_detect_format_unknown():
    """Unknown extensions should return application/octet-stream."""
    extractor = MetadataExtractor()
    assert extractor.detect_format("data.xyz") == "application/octet-stream"


def test_extract_audio_sets_sample_rate():
    """Extracting metadata from audio files should set sample_rate."""
    extractor = MetadataExtractor()
    meta = extractor.extract("piece.wav", 1024000)
    assert meta.sample_rate == 44100
    assert meta.file_format == "audio/wav"


def test_extract_image_sets_color_profile():
    """Extracting metadata from image files should set color_profile."""
    extractor = MetadataExtractor()
    meta = extractor.extract("photo.jpg", 500000)
    assert meta.color_profile == "sRGB"


def test_suggest_tags_includes_medium():
    """Tag suggestions should include the file's media category."""
    extractor = MetadataExtractor()
    tags = extractor.suggest_tags("visual.png")
    assert "image" in tags


def test_suggest_tags_includes_keywords():
    """Tag suggestions should detect keywords from the description."""
    extractor = MetadataExtractor()
    tags = extractor.suggest_tags("work.mp4", "A generative performance piece")
    assert "generative" in tags
    assert "performance" in tags


def test_technical_metadata_summary():
    """Summary should format key attributes into a readable string."""
    meta = TechnicalMetadata(
        file_format="audio/wav", file_size_bytes=2048000,
        duration_seconds=45.3,
    )
    summary = meta.summary()
    assert "audio/wav" in summary
    assert "2,048,000" in summary
    assert "45.3" in summary
