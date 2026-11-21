<div align="center">

<!-- Animated Typing Header -->
<img src="https://demolab.com💱+Live+Currency+Converter;🌍+160%2B+Global+Currencies+Supported;⚡+Powered+by+Python+%26+REST+API" alt="Typing SVG" />

<br/>

<!-- Tech Badges -->
![Python](https://shields.io)
![REST API](https://shields.io)
![Status](https://shields.io)
![Made By](https://shields.io)

<p>
  <b>A fast, lightweight command-line tool that converts money between 160+ countries using real-time exchange rates!</b>
</p>

</div>

---

## 🤔 What Does This Project Do? (For Everyone!)

Ever wondered how much **100 USD** is in **Pakistani Rupees (PKR)** or **Indian Rupees (INR)** right now?  
Instead of opening Google every time, this tool connects directly to a live financial server on the internet, grabs today's exact exchange rate, and calculates your converted amount in less than a second!

### ✨ Key Features
- 🌍 **Real-Time Rates:** Fetches live market exchange rates (no outdated numbers!).
- 💱 **160+ Currencies:** Supports `USD`, `PKR`, `INR`, `EUR`, `GBP`, `AED`, `SAR`, `JPY`, and many more.
- ⚡ **Zero API Key Needed:** Works straight out of the box without complicated sign-ups.
- 🧠 **Clean & Simple:** Built with pure Python logic and beginner-friendly code.

---

## 💻 How It Looks in Action

```text
Convert from  : PKR
Convert to    : INR
Enter amount  : 100
Converted amount: 33.76 INR
```

```text
Convert from  : USD
Convert to    : EUR
Enter amount  : 100
Converted amount: 91.07 EUR
```

---

## 🚀 How to Run This on Your PC (Step-by-Step)

Even if you are new to coding, you can run this in **3 easy steps**:

### 1️⃣ Install Python
Make sure you have **Python** installed on your computer. You can download it from [python.org](https://python.org).

### 2️⃣ Download This Project & Install Required Tool
Open your terminal or command prompt and run:

```bash
git clone https://github.com
cd YOUR_REPO_NAME
pip install requests
```

### 3️⃣ Start Converting!
Run the script with:

```bash
python main.py
```

---

## 🌐 Popular Currency Codes You Can Try

| Country / Region | Currency Name | Code to Type |
| :--- | :--- | :---: |
| 🇵🇰 Pakistan | Pakistani Rupee | `PKR` |
| 🇮🇳 India | Indian Rupee | `INR` |
| 🇺🇸 United States | US Dollar | `USD` |
| 🇪🇺 European Union | Euro | `EUR` |
| 🇬🇧 United Kingdom | British Pound | `GBP` |
| 🇦🇪 UAE | UAE Dirham | `AED` |
| 🇸🇦 Saudi Arabia | Saudi Riyal | `SAR` |
| 🇯🇵 Japan | Japanese Yen | `JPY` |

---

## 🛠️ How It Works Behind the Scenes
1. Takes user input (`from_currency`, `to_currency`, and `amount`).
2. Sends a live HTTP `GET` request to [ExchangeRate-API](https://exchangerate-api.com).
3. Parses the incoming **JSON** response into a Python dictionary.
4. Multiplies the entered amount by the live rate and prints a clean, 2-decimal result.

---

<div align="center">
  <img src="https://vercel.app" width="100%"/>
  <p>Built with ❤️ and curiosity by <a href="https://github.com"><b>Sufyan-m</b></a></p>
</div>
