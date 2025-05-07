# Azure SLA Calculator

A simple yet powerful Streamlit-based web application that calculates the combined SLA (Service Level Agreement) percentage for selected Azure services.

## 🔧 Features

- Select Azure services from a dropdown menu
- The application fetches official SLA percentages from the `azure_sla_reference.txt` file
- View the combined SLA and estimated monthly downtime (in minutes)
- Easy-to-use interface powered by Streamlit

## 📋 Requirements

- Python 3.11 or higher
- Streamlit

## 🔗 Live-demo
[open in browser](https://sla-app-8a9dugwnczgp4kdxr7nljg.streamlit.app/)

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd sla-calc
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Create a requirements.txt file:
   ```bash
   echo "streamlit>=1.30.0" > requirements.txt
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Run the Streamlit application:
   ```bash
   streamlit run sla_app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Select the Azure services you're using from the dropdown menu

4. The application will automatically calculate the combined SLA percentage and estimated monthly downtime

## 💡 How It Works

The application uses the following formula to calculate the combined SLA:

```
Combined SLA = SLA_Service1 × SLA_Service2 × ... × SLA_ServiceN
```

For example, if you select:
- App Service (99.9%)
- SQL Database (99.99%)

The combined SLA would be: 0.999 × 0.9999 = 0.9989001 (99.89001%)

The estimated monthly downtime is calculated as:
```
Downtime (minutes) = (1 - Combined SLA) × 30 days × 24 hours × 60 minutes
```

## 🔄 CI/CD

This project includes a GitHub Actions workflow that:
- Runs on push to main and pull requests
- Sets up Python 3.11
- Installs dependencies
- Performs a headless check of the Streamlit application

## 📝 Data Source

The SLA percentages are stored in `azure_sla_reference.txt` in a simple format:
```
Service Name: SLA value
```

For example:
```
App Service: 0.999
SQL Database: 0.9999
```

You can update this file with the latest SLA values from the [Azure SLA documentation](https://azure.microsoft.com/en-us/support/legal/sla/).

## 📄 License

[MIT License](LICENSE)
