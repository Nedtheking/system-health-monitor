import psutil

#--------------------- RAM CHECK ---------------------

def check_ram(verbose=True):
    ram = psutil.virtual_memory()

    total_gb = ram.total / 1_000_000_000
    available_gb = ram.available / 1_000_000_000
    used_percent = ram.percent

    if verbose:
        print(f"Current RAM Usage: {used_percent}%")
        print(f"Total RAM: {total_gb:.1f} GB")
        print(f"Available RAM: {available_gb:.1f} GB")

    status = "ok" if used_percent < 85 else "warning"
    message = "✅ Your computer is running programs normally." if status == "ok" else (
        "Your computer is very busy running programs right now.\n"
        "When it’s too busy, it can slow down or freeze.\n"
        "Try closing unnecessary applications or restarting your computer."
    )

    return {
        "status": status,
        "message": message,
        "used_percent": used_percent,
        "total_gb": total_gb,
        "available_gb": available_gb
    }
