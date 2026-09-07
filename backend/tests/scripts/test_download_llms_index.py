from pathlib import Path
from urllib.error import URLError

import pytest

from scripts import download_llms_index


class FakeResponse:
    def __init__(self, body: bytes) -> None:
        self.body = body

    def read(self) -> bytes:
        return self.body

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *args: object) -> None:
        return None


def test_download_writes_the_index_and_creates_parent_directories(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        download_llms_index,
        "urlopen",
        lambda request, timeout: FakeResponse(b"# Cato Networks\n"),
    )
    destination = tmp_path / "nested" / "llms.txt"

    result = download_llms_index.download_llms_index(destination)

    assert result == destination.resolve()
    assert destination.read_bytes() == b"# Cato Networks\n"


def test_download_rejects_an_empty_index(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        download_llms_index,
        "urlopen",
        lambda request, timeout: FakeResponse(b" \n "),
    )
    destination = tmp_path / "llms.txt"

    with pytest.raises(download_llms_index.DownloadError, match="empty"):
        download_llms_index.download_llms_index(destination)

    assert not destination.exists()


def test_download_wraps_network_failures(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def raise_network_error(request: object, timeout: float) -> FakeResponse:
        raise URLError("network unavailable")

    monkeypatch.setattr(download_llms_index, "urlopen", raise_network_error)

    with pytest.raises(download_llms_index.DownloadError, match="Could not download"):
        download_llms_index.download_llms_index(tmp_path / "llms.txt")
