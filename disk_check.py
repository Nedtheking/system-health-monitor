import psutil

#--------------------- DISK CHECK ---------------------


def check_disks():
    """
    Returns a list of dictionaries for each disk with:
    device, mountpoint, total, used, free, percent, status, message
    """
    disks_info = []

    partitions = psutil.disk_partitions(all=False)  # only real drives
    main_drive = []
    internal_drives = []
    external_drives = []

    for part in partitions:
        usage = psutil.disk_usage(part.mountpoint)
        status = "ok" if usage.percent < 85 else "warning"
        message = (
            "✅ Storage is healthy." if status == "ok"
            else "⚠️ Almost out of storage!\n"
                "When storage is too full, computers become slow and freeze more often.\n"
                "This is like trying to stuff more clothes into an already full closet."
        )




        disk_dict = {
            "device": part.device,
            "mountpoint": part.mountpoint,
            "total_gb": round(usage.total / 1_000_000_000, 1),
            "used_gb": round(usage.used / 1_000_000_000, 1),
            "free_gb": round(usage.free / 1_000_000_000, 1),
            "percent": usage.percent,
            "status": status,
            "message": message,
            "opts_type": part.opts  # internal vs external
        }

        # Determine type
        if part.device.startswith("C:"):
            main_drive.append(disk_dict)
        elif 'removable' in part.opts:
            external_drives.append(disk_dict)
        else:
            internal_drives.append(disk_dict)

    # Order: main, internal, external
    disks_info.extend(main_drive)
    disks_info.extend(internal_drives)
    disks_info.extend(external_drives)

    return disks_info
