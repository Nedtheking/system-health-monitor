from disk_check import check_disks
from cpu_check import check_cpu
from ram_check import check_ram

def quick_scan():
    print ("\n===⚡ QUICK SYSTEM SCAN ⚡===\n")

    issues = []

    #DISK
    disks = check_disks()
    for disk in disks:
        if disk["status"] != "ok":
            issues.append(f"{disk['mountpoint']}: Storage is almost full. ")

    
    #CPU
    cpu = check_cpu()
    if cpu["status"] != "ok":
        issues.append("Your computer’s brain is working very hard.")

    
    #RAM
    ram = check_ram()
    if ram["status"] != "ok":
        issues.append("Your computer is very busy running programs.")

    
    #OUTPUT 
    if issues:
        print("⚠️ Problems found:\n")
        for issue in issues:
            print(f"• {issue}")
        print("\nEverything else looks fine.")
    else:
        print("✅ Your computer looks healthy.")
        print("No common problems were found.")

if __name__ == "__main__":
    quick_scan()