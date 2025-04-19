# 🎓 Manipal University Feedback Automation Script

This Python script automates the feedback form submission process on the Manipal University Jaipur student portal. It's useful when you want to skip the repetitive task of manually filling out feedback for each course, especially when it's mandatory. (Yes I used ChatGPT to write this documentation.)

---

## ⚙️ Features

- Automatically navigates to the feedback page.
- Selects "Yes" radio buttons for each question.
- Selects dropdown responses (where required).
- Submits the form for all available feedback entries.
- Waits for manual login before proceeding.

---

## 🛠 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (matching your browser version)
- `selenium` library

Install Selenium with:

```bash
pip install selenium
```

---

## 🧾 Usage

1. **Download ChromeDriver**  
   [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)  
   Place it somewhere convenient and update the `path` in the script.

2. **Run the script**  
   Open a terminal or command prompt and run:

```bash
python yup.py
```

3. **Manual Login Step**  
   The browser will open and load the MUJ login page.  
   ✅ Login manually.  
   ⏳ After logging in, return to the terminal and press `Enter`.

4. **Let the script work**  
   It will:
   - Open each feedback form
   - Select appropriate answers
   - Submit the form
   - Move to the next one

---

## 📂 File Structure

```
feedback_automation.py   # Main script
README.md                # This file
```

---

## 🧠 Notes

- This script assumes that each feedback form has up to 10 rows of questions.
- If dropdowns are optional or sometimes missing, the script handles that gracefully.
- For maximum reliability, ensure your internet connection is stable during execution.
- You may need to update ChromeDriver if your Chrome browser updates.

---

## 📌 Disclaimer

This script is for educational and personal use only ;).  
Use responsibly and respect your university’s digital policy (lol).  
Always ensure you’re complying with academic honesty and portal usage guidelines.

## 📧 Contact

Maintained by [Your Name]  
Feel free to reach out on GitHub or via email if you face issues or want to collaborate.