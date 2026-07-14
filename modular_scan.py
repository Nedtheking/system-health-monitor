from disk_check import check_disks
from cpu_check import check_cpu
from ram_check import check_ram

def modular_scan():
    print("\n=== MODULAR SYSTEM CHECK ===\n")
    print("What do you want to check?")
    print("1) Disk")
    print("2) CPU")
    print("3) RAM")
    print("4) ALL")

    choice = input("\nEnter numbers separated by commas (e.g. 1,3): ")
    options = [x.strip() for x in choice.split(",")]

    issues = []

    # ----- DISK -----
    if "1" in options or "4" in options:
        print("\n--- Disk Check ---")
        disks = check_disks()
        for disk in disks:
            print(f"{disk['mountpoint']}: {disk['percent']}% used")
            if disk["status"] != "ok":
                issues.append(f"{disk['mountpoint']} is almost full.")

    # ----- CPU -----
    if "2" in options or "4" in options:
        print("\n--- CPU Check ---")
        cpu = check_cpu()
        print(f"CPU usage: {cpu['percent']}%")
        if cpu["status"] != "ok":
            issues.append("Your computer’s brain is working very hard.")

    # ----- RAM -----
    if "3" in options or "4" in options:
        print("\n--- RAM Check ---")
        ram = check_ram()
        print(f"RAM usage: {ram['used_percent']}%")
        if ram["status"] != "ok":
            issues.append("Your computer is very busy running programs.")

    # ----- SUMMARY -----
    if issues:
        print("\n⚠️ Issues found:")
        for issue in issues:
            print(f"• {issue}")
    else:
        print("\n✅ No problems found in selected checks.")