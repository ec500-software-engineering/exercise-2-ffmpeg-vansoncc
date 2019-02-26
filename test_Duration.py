from pytest import approx
import subprocess


def test_duration():
    input_video = "./test.mp4"
    out_720 = "./test720.mp4"
    out_480 = "./test480.mp4"

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
    print(out_480_duration)

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
    print(out_720_duration)
    input_duration = subprocess.call(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            input_video,
        ]
    )
    print(input_duration)
    assert input_duration == approx(out_720_duration)
    assert input_duration == approx(out_480_duration)
