import psutil

#--------------------- CPU CHECK ---------------------

def check_cpu(verbose=True):
    cpu_usage = psutil.cpu_percent(interval=1)

    if verbose:
        print(f"Current CPU Usage: {cpu_usage}%")

    status = "ok" if cpu_usage < 85 else "warning"
    message = "✅ Your computer’s workload is normal." if status == "ok" else (
        "Your computer is overworking very hard right now.\n"
        "This can cause slowness, lag, or freezing.\n"
        "Try closing unnecessary applications or restarting your computer."
    )

    return {
        "status": status,
        "message": message,
        "cpu_percent": cpu_usage
    }
