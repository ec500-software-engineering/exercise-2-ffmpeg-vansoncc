import Ex2


def test1():
    input = "test.mp4"
    output_720 = "test720.mp4"
    output_480 = "test480.mp4"

    orig_meta = Ex2.ffprobe(input)
    meta_480 = Ex2.ffprobe(output_480)
    meta_720 = Ex2.ffprobe(output_720)
    in_duration = (float)(orig_meta['format']['duration'].split('.')[0])
    out_480_duaration = (float)(meta_480['format']['duration'].split('.')[0])
    out_720_duaration = (float)(meta_720['format']['duration'].split('.')[0])

    assert in_duration == out_480_duaration
    assert in_duration == out_720_duaration
    # print("Passed Test")


