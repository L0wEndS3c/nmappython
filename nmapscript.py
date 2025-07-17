#!/usr/bin/env python3
#Author L0wEndS3c
#NMAP python script prompting for Scan Type, Target, Scripts, and Port
#06/25/2025

import subprocess
import sys
import shlex
from pyfiglet import Figlet

def print_banner():
    f = Figlet(font='slant')  # Try also 'big', 'standard', 'doom', etc.
    print(f.renderText("NMAP by L0wEndS3c"))

def main():
    try:
        print_banner()

        print("Available scan flags (combine multiple, space-separated):")
        print("  -sS  (TCP SYN scan)")
        print("  -sT  (TCP connect scan)")
        print("  -sU  (UDP scan)")
        print("  -sV  (Service/version detection)")
        print("  -O   (OS detection)")
        print("  -A   (Aggressive scan)\n")

        scan_flags = input("Enter your desired scan flags: ").strip()
        if not scan_flags:
            print("No scan flags provided. Exiting.")
            sys.exit(1)

        target = input("Enter the IP address or hostname to scan: ").strip()
        if not target:
            print("No target provided. Exiting.")
            sys.exit(1)

        port_input = input("Enter specific ports (e.g., 22,80,443 or 1-1000), or press Enter to skip: ").strip()

        use_script = input("Would you like to use an Nmap script? (y/n): ").strip().lower()
        script_name = ""
        if use_script == "y":
            print("\nExamples: default, vuln, ssl-heartbleed, http-title, etc.")
            script_name = input("Enter the script name or category to use (e.g., default, vuln): ").strip()
            if not script_name:
                print("No script name provided. Skipping script usage.")
                script_name = ""

        # Build the command
        cmd = ["nmap"] + shlex.split(scan_flags)

        if port_input:
            cmd += ["-p", port_input]
        if script_name:
            cmd += ["--script", script_name]

        cmd.append(target)

        print(f"\n[+] Running scan: {' '.join(cmd)}\n")

        result = subprocess.run(cmd, capture_output=True, text=True)

        print("=== Scan Results ===")
        print(result.stdout)

        if result.stderr:
            print("=== Errors ===")
            print(result.stderr)

    except KeyboardInterrupt:
        print("\n[!] Scan cancelled by user.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
