from disk_check import check_disks
from cpu_check import check_cpu
from ram_check import check_ram

def full_report():
    print("\n=== FULL SYSTEM REPORT ===\n")

    # -------------------- DISK CHECK --------------------
    print("--- Disk Check ---")
    disks_info = check_disks()  # returns a list of all disks
    for disk in disks_info:
        print(f"{disk['mountpoint']}:")
        print(f"  Total: {disk['total_gb']} GB")
        print(f"  Used: {disk['used_gb']} GB")
        print(f"  Free: {disk['free_gb']} GB")
        print(f"  Usage: {disk['percent']}%")
    # Collect disk issues
    disk_issues = [f"{disk['device']}: {disk['message']}" for disk in disks_info if disk['status'] != 'ok']

    # -------------------- CPU CHECK --------------------
    print("\n--- CPU Check ---")
    cpu_result = check_cpu()
    cpu_issues = []
    if cpu_result['status'] != 'ok':
        cpu_issues.append(f"CPU: {cpu_result['message']}")

    # -------------------- RAM CHECK --------------------
    print("\n--- RAM Check ---")
    ram_result = check_ram()
    ram_issues = []
    if ram_result['status'] != 'ok':
        ram_issues.append(f"RAM: {ram_result['message']}")

    # -------------------- OVERALL SYSTEM HEALTH --------------------
    print("\n--- OVERALL SYSTEM HEALTH ---")
    issues = disk_issues + cpu_issues + ram_issues
    if issues:
        print(f"⚠️ Issues Detected ({len(issues)}):")
        for i, issue in enumerate(issues, start=1):
            print(f"{i}. {issue}")
    else:
        print("✅ Everything looks good on your system!")

# Run full report
if __name__ == "__main__":
    full_report()
