from quick_scan import quick_scan
from full_report import full_report
from modular_scan import modular_scan

# If modular_scan.py exists
try:
    from modular_scan import modular_scan
except ImportError:
    modular_scan = None

def main():
    while True:
        print("\n=== System Health Assistant ===\n")
        print("Choose a mode:")
        print("1) Quick Scan (only problems)")
        print("2) Full Report (all details)")
        print("3) Modular Checks (pick what to check)")
        print("0) Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            quick_scan()

        elif choice == "2":
            full_report()

        elif choice == "3":
            modular_scan()

        elif choice == "0":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()