
 DepSentinel
------------

**DepSentinel** is a Python-based tool with a Streamlit UI that scans your project's `requirements.txt` file, checks for vulnerable dependencies using PyPI, and notifies developers through an interactive dashboard or email alerts.

Built to support **DevSecOps pipelines**, this tool helps teams identify outdated Python packages early, reducing security and stability risks.

* * *

### 🔍 Key Features

*   ✅ Parses `requirements.txt` for pinned dependencies
    
*   🔁 Checks against the latest package versions on [PyPI](https://pypi.org)
    
*   📊 Displays outdated packages in a user-friendly **Streamlit dashboard**
    
*   📬 Sends **email notifications** if updates are available
    
*   ⚙️ Easily integratable into CI/CD tools like GitHub Actions
    

* * *

### 🧑‍💻 Built With

*   `Python 3.10+`
    
*   `Streamlit` – for the web UI
    
*   `Requests` – for PyPI version checks
    
*   `Packaging` – for safe version comparison
    
*   `SMTP` – for sending email alerts
    
*   `dotenv` – for secure config management
    

* * *

### 🚀 Quick Start

 1. Clone the repository:
```bash
git clone https://github.com/addharshini/DepSentinel.git
cd DepSentinel
```
2. Install dependencies
`pip install -r requirements.txt` 

3.  Run the Streamlit app
`python -m streamlit run streamlit_app.py` 

* * *

### 📬 Email Alert Setup

Create a `.env` file in the root directory with your email config:

`EMAIL_FROM=your_email@gmail.com
EMAIL_PASSWORD=your_password` 

Then click "📬 Send Email Notification" in the dashboard when outdated dependencies are found.

> 💡 Use Gmail App Passwords if 2FA is enabled.

* * *

### 🖼️ UI Preview
<img width="1778" height="402" alt="Screenshot 2025-07-16 121600" src="https://github.com/user-attachments/assets/f2be6854-7176-4f1d-a055-d120c511c28b" />

_Outdated dependencies shown in a real-time table._

* * *

### 🧪 Example `requirements.txt`


`flask==2.2.5
requests==2.28.1
pandas==1.5.3` 

* * *


### 📄 License

MIT License © 2025 Divya Dharshini

* * *

### 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first.

* * *
