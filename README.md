<div align="center">

# 💱 Live Currency Converter
### 🌍 Real-Time Exchange Rates for 160+ Countries | ⚡ Built with Python

**A fast, simple tool that converts money between 160+ countries using live market rates!**

</div>

---

## 🤔 What Does This Project Do? (For Everyone!)

Ever wondered how much **100 USD** is in **Pakistani Rupees (PKR)** or **Indian Rupees (INR)** right now?  
Instead of searching on Google every single time, this tool connects directly to a live financial server on the internet, grabs today's exact exchange rate, and calculates your converted amount in less than a second!

### ✨ Why Use This?
- 🌍 **Live Market Rates:** Always fetches fresh, real-time rates (no outdated numbers!).
- 💱 **160+ Currencies Supported:** Works with almost every country in the world.
- 🔑 **No Sign-Up or API Key Needed:** Works instantly out of the box.
- 🧠 **Beginner & User Friendly:** Clean, fast, and super easy to use.

---

## 💻 How It Looks When You Run It

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

## 🧑‍💻 How to Run This (Even If You Are Non-Tech!)

You don't need to be a programmer to use this tool. Just follow these **3 simple steps**:

### Step 1: Install Python (One-Time Setup)
1. Go to [python.org/downloads](https://python.org) and download **Python**.
2. Open the installer and **IMPORTANT:** Check the box that says **"Add Python to PATH"** at the bottom, then click **Install Now**.

### Step 2: Download This Project
* **Easy Way (No Coding):** Click the green **`<> Code`** button at the top of this page -> click **`Download ZIP`** -> extract the folder on your PC.
* **Developer Way (Git):**
  ```bash
  git clone https://github.com
  cd Currency-Converter
  ```

### Step 3: Run the Converter
1. Open the extracted folder, click the top address bar, type **`cmd`**, and press **Enter**.
2. Type these two commands one by one:
   ```bash
   pip install requests
   python main.py
   ```
3. Type your currency code (like `PKR`), target currency (like `USD`), and amount—done! 🎉

---

## 🌐 20 Popular Currency Codes You Can Use

Type any of these **3-letter codes** when the program asks `Convert from` or `Convert to`:

| Country / Region | Currency Code | Country / Region | Currency Code |
| :--- | :---: | :--- | :---: |
| 🇵🇰 **Pakistan** | `PKR` | 🇨🇦 **Canada** | `CAD` |
| 🇮🇳 **India** | `INR` | 🇦🇺 **Australia** | `AUD` |
| 🇺🇸 **USA** | `USD` | 🇹🇷 **Turkey** | `TRY` |
| 🇬🇧 **UK** | `GBP` | 🇧🇩 **Bangladesh** | `BDT` |
| 🇪🇺 **Europe** | `EUR` | 🇱🇰 **Sri Lanka** | `LKR` |
| 🇦🇪 **UAE** | `AED` | 🇲🇾 **Malaysia** | `MYR` |
| 🇸🇦 **Saudi Arabia** | `SAR` | 🇸🇬 **Singapore** | `SGD` |
| 🇯🇵 **Japan** | `JPY` | 🇰🇷 **South Korea** | `KRW` |
| 🇨🇳 **China** | `CNY` | 🇨🇭 **Switzerland** | `CHF` |
| 🇿🇦 **South Africa** | `ZAR` | 🇳🇵 **Nepal** | `NPR` |

> 💡 **Tip:** Over **140+ more currency codes** (like `QAR`, `OMR`, `KWD`, `RUB`) also work automatically!

---

## ⚙️ How It Works Behind the Scenes
1. Takes your input (`from_currency`, `to_currency`, and `amount`).
2. Sends a live request to [ExchangeRate-API](https://exchangerate-api.com).
3. Reads the **JSON** data returned by the server.
4. Multiplies your amount by today's exact rate and displays the result.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com"><b>Sufyan-m</b></a></p>
</div>
