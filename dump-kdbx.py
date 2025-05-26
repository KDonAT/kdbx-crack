#!/usr/bin/env python3

import argparse
from pykeepass import PyKeePass
import sys

def main():
    parser = argparse.ArgumentParser(description="Dump KeePass entries, optionally extract passwords")
    parser.add_argument("-f", "--file", required=True, help="Path to the .kdbx file")
    parser.add_argument("-p", "--password", required=True, help="Master password")
    parser.add_argument("-pO", "--passwordOutput", action="store_true", help="Write all passwords to passwords.txt")
    args = parser.parse_args()

    try:
        kp = PyKeePass(args.file, password=args.password)
    except Exception as e:
        print(f"[-] Failed to open database: {e}")
        sys.exit(1)

    if not kp.entries:
        print("[-] No entries found in the database.")
        sys.exit(1)

    password_list = []

    for entry in kp.entries:
        print("="*60)
        print(f"Title:    {entry.title}")
        print(f"Username: {entry.username}")
        print(f"Password: {entry.password}")
        print(f"Notes:    {entry.notes}")
        print(f"Tags:     {', '.join(entry.tags) if entry.tags else 'None'}")
        print("="*60)
        if args.passwordOutput and entry.password:
            password_list.append(entry.password)

    if args.passwordOutput:
        with open("passwords.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(password_list))
        print(f"[+] Saved {len(password_list)} passwords to passwords.txt")

if __name__ == "__main__":
    main()
