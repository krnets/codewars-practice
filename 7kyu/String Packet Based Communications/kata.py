# def communication_module(packet):
#     parts = [packet[i : i + 4] for i in range(0, len(packet), 4)]
#     header, instruction, data1, data2, footer = parts

#     match instruction:
#         case "B7A2": res = max(0, int(data1) - int(data2))
#         case "0F12": res = min(9999, int(data1) + int(data2))
#         case "C3D9": res = min(9999, int(data1) * int(data2))
#     return f"{header}FFFF{res:04}0000{footer}"

from textwrap import wrap

def communication_module(packet):
    header, instruction, data1, data2, footer = wrap(packet, 4)

    match instruction:
        case "B7A2": res = max(0,    int(data1) - int(data2))
        case "0F12": res = min(9999, int(data1) + int(data2))
        case "C3D9": res = min(9999, int(data1) * int(data2))
    return f"{header}FFFF{res:04}0000{footer}"
