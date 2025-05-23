# 🔐 kdbx-crack

Brute-force tool for cracking KeePass `.kdbx` password databases using a wordlist.  
Compatible with `.kdbx` version 4. Tested on Kali Linux.

---

## ✅ Features

- Supports large wordlists like `rockyou.txt`
- Uses `pykeepass` for parsing
- Stops immediately when a valid password is found
- Simple and reliable CLI usage

---

## 🔧 Installation

```bash
git clone https://github.com/KDonAT/kdbx-crack.git
cd kdbx-crack
pip install -r requirements.txt
```

### (Optional: use a virtual environment)

```bash
python3 -m venv .kdbx
source .kdbx/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python3 kdbx-crack.py <file.kdbx> -w /path/to/wordlist.txt
```

### Example:

```bash
python3 kdbx-crack.py recovery.kdbx -w /usr/share/wordlists/rockyou.txt
```

---

## 💡 Tip

To avoid polluting your system environment, use a virtual environment:
```bash
python3 -m venv .kdbx
source .kdbx/bin/activate
pip install -r requirements.txt
```

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational, ethical, and authorized use only**.

- Do **not** use this tool on systems or files you do not own or have **explicit permission** to test
- Use only in legal, controlled environments such as penetration tests with written consent or isolated labs
- Misuse may be illegal under local, national, or international law

> The author is **not responsible** for any misuse or damage. By using this tool, you agree to comply with all applicable laws and ethical guidelines.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
