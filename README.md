# 🔐 Password Generator

A lightweight, GUI-based random password generator written in Python. Create strong passwords with customizable options for length, uppercase letters, digits, and symbols—all with clipboard integration and instant feedback.

---

## ⚙️ Features

- ✅ Adjustable password length (4–64 characters)
- 🔡 Toggle options for:
  - Uppercase letters
  - Numbers
  - Special characters (`!@#$%^&*()-_=+`)
- 📋 Auto-copy to clipboard after generation
- 🧪 Clipboard confirmation popup
- 🖥️ Simple, clean `tkinter`-based GUI

---

## 📦 Requirements

- Python 3.11 
- [`pyperclip`](https://pypi.org/project/pyperclip/) (auto-installed if missing)

---

## 🚀 How to Run

```bash
python password_generator.py
```

The app will launch a small window with configuration options and a "Generate Password" button.

---

## 🖼️ Screenshot (Conceptual)

```
+-------------------------------------------+
|       Password Generator                  |
|-------------------------------------------|
| [✓] Include Uppercase     [✓] Numbers     |
| [✓] Include Symbols                      |
|                                           |
| Password Length: [ 16 ]                   |
|                                           |
| [ Generate Password ]                     |
|                                           |
| [ Lh$2pd7#qZRt0mv1 ]                      |
+-------------------------------------------+
```

---

## ✨ How It Works

1. You select your desired character types and password length.
2. Click “Generate Password.”
3. A random password is displayed and **automatically copied** to your clipboard.
4. A popup confirms that the password has been copied.

---

## 🔒 Security Notes

- Passwords are generated using Python's `random.choice` from a secure character pool.
- No passwords are logged or stored.
- This app is suitable for **local/offline** use—avoid using it inside shared terminals or remote sessions where clipboard interception is possible.

---

## 📋 Tech Stack

| Component     | Used For         |
|---------------|------------------|
| `tkinter`     | GUI window       |
| `pyperclip`   | Clipboard access |
| `string`      | Character pools  |
| `random`      | Password creation logic |
