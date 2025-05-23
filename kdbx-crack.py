#!/usr/bin/env python3

import argparse
from pykeepass import PyKeePass
from tqdm import tqdm
import sys

def main():
    parser = argparse.ArgumentParser(description="KeePass KDBX dictionary cracker")
    parser.add_argument("kdbx_file", help="Path to .kdbx file")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to password wordlist")
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r", encoding="latin-1", errors="ignore") as wordlist:
            for password in tqdm(wordlist, desc="Trying passwords"):
                password = password.strip()
                try:
                    PyKeePass(args.kdbx_file, password=password)
                    print(f"\n[+] Password found: {password}")
                    return
                except Exception:
                    continue
    except FileNotFoundError:
        print("[-] Wordlist or KDBX file not found.")
        sys.exit(1)

    print("\n[-] Password not found in wordlist.")

if __name__ == "__main__":
    main()
