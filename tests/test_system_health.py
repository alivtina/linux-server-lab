import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "python" / "system-health"))

from system import check_usage


@pytest.mark.parametrize(
    "percent, threshold, expected",
    [
        (50, 80, "OK"),
        (90, 80, "WARNING"),
        (80, 80, "OK"),
    ],
)
def test_check_usage(percent, threshold, expected):
    result = check_usage(percent, threshold)
    assert result == expected
