from pytest import approx
import subprocess


def test_duration():
    input = "test.mp4"
    out_720 = "test720.mp4"
    out_480 = "test480.mp4"

    out_480_duration = subprocess.call(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            out_480,
        ]
    )

    out_720_duration = subprocess.call(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            out_720,
        ]
    )
    input_duration = subprocess.call(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            input,
        ]
    )
    assert input_duration == approx(out_720_duration)
    assert input_duration == approx(out_480_duration)

