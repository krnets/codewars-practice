def interpret_as_int32(stream):
    merged_stream = b"".join(stream)
    n = len(merged_stream) // 4 * 4
    return [
        int.from_bytes(merged_stream[i : i + 4], byteorder="big", signed=True)
        for i in range(0, n, 4)
    ]
