from typing import List


def unique_device_names(num: int, device_names: List[str]):
    devices = []
    for name in device_names:
        if name not in devices:
            devices.append(name)
        else:
            name_suffix = sum(1 for prev_name in devices if prev_name.startswith(name))
            devices.append(f"{name}{name_suffix}")

    return list(devices)


print(unique_device_names(6, ["switch", "tv", "switch", "tv", "switch", "tv"]))
