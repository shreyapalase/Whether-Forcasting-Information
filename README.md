# 🌦️ Weather Forecasting App

A simple and interactive **Weather Forecasting Application** built using **Python**, **OpenWeatherMap API**, **ipywidgets**, and **Matplotlib**. This project allows users to check real-time weather conditions for a single city and compare temperatures across multiple cities using graphical visualization.

---

#  Project Overview

This Weather Forecasting App fetches live weather data from the OpenWeatherMap API and presents it in a user-friendly interface.

The application provides:

* Real-time weather information
* Temperature monitoring
* Humidity tracking
* Wind speed details
* Weather condition descriptions
* Multi-city temperature comparison
* Graphical data visualization

This project demonstrates practical usage of:

* API Integration
* Data Visualization
* GUI Development
* Python Programming
* Error Handling
* User Interaction

---

#  Features

## Single City Weather Forecast

Users can:

* Enter a city name
* View current temperature
* Check humidity level
* View wind speed
* Read weather descriptions

Example Output:

```text
 WEATHER REPORT
------------------
City: Mumbai
Temperature: 30°C
Weather: scattered clouds
Humidity: 75%
Wind: 3.2 m/s
```

---

## Multi-City Comparison

Users can compare weather conditions among multiple cities.

Example Input:

```text
Mumbai, Delhi, Pune
```

Output:

```text
Mumbai : 30°C
Delhi : 35°C
Pune : 28°C
```

The application also generates a bar chart for visual comparison.

---

#  Technologies Used

| Technology         | Purpose                    |
| ------------------ | -------------------------- |
| Python             | Core Programming Language  |
| Requests           | API Communication          |
| OpenWeatherMap API | Weather Data Provider      |
| ipywidgets         | Interactive GUI Components |
| Matplotlib         | Data Visualization         |
| Jupyter Notebook   | Development Environment    |

---

#  Project Structure

```text
Weather-Forecasting-App/
│
├── weather_forecasting_app.ipynb
├── README.md
└── requirements.txt
```

---

#  Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/weather-forecasting-app.git
```

```bash
cd weather-forecasting-app
```

---

## Step 2: Install Required Libraries

```bash
pip install requests
pip install matplotlib
pip install ipywidgets
```

Or install all at once:

```bash
pip install -r requirements.txt
```

---

# 📄 requirements.txt

Create a file named:

```text
requirements.txt
```

Add:

```text
requests
matplotlib
ipywidgets
```

---

#  OpenWeatherMap API Setup

1. Create an account on OpenWeatherMap.
2. Generate your free API Key.
3. Replace the API key in the code:

```python
API_KEY = "YOUR_API_KEY"
```

---

# ▶️ How to Run

## Using Jupyter Notebook

Launch Jupyter:

```bash
jupyter notebook
```

Open:

```text
weather_forecasting_app.ipynb
```

Run all cells.

---

#  Workflow

```text
User Input
     ↓
City Name
     ↓
OpenWeatherMap API
     ↓
Weather Data Retrieved
     ↓
Display Results
     ↓
Visualization (Matplotlib)
```

---

# 🔍 Code Components

## Weather Data Retrieval

Responsible for:

* API Request
* JSON Processing
* Data Extraction

Function:

```python
get_weather(city)
```

---

## Single City Forecast

Function:

```python
show_single()
```

Features:

* Weather report generation
* Error handling for invalid cities

---

## Multi-City Comparison

Function:

```python
show_multi()
```

Features:

* Multiple city support
* Temperature comparison
* Bar chart visualization

---

#  Skills Demonstrated

This project showcases:

### Programming Skills

* Python Development
* Function Design
* Data Structures

### Data Handling

* API Integration
* JSON Parsing
* Error Management

### Visualization

* Matplotlib Charts
* Data Presentation

### User Interface

* Interactive Widgets
* User Input Handling

---

#  Important Notes

## API Rate Limits

The free OpenWeatherMap plan has request limits. Excessive requests may temporarily block access.

---

## Internet Connection Required

Since weather information is fetched from an online API, an active internet connection is required.

---

## API Key Security

Never upload your actual API key to public repositories.

Instead use:

```python
API_KEY = "YOUR_API_KEY"
```

or environment variables.

---

#  Future Improvements

Possible enhancements:

* 5-Day Weather Forecast
* Weather Icons
* Dark Mode UI
* Temperature Trend Analysis
* CSV Export Feature
* Geolocation Support
* Search History

---

# Learning Outcomes

Through this project, I gained experience in:

* REST API Integration
* Python GUI Development
* Data Visualization
* Real-Time Data Processing
* Software Debugging
* User-Centered Design

---

#  Why This Project Matters

Weather forecasting applications are widely used in:

* Travel Planning
* Agriculture
* Logistics
* Event Management
* Disaster Preparedness

This project demonstrates the ability to work with real-world APIs and build practical software solutions.

---

#  Contribution

Contributions, suggestions, and improvements are welcome.

Steps:

1. Fork Repository
2. Create New Branch
3. Commit Changes
4. Push Branch
5. Create Pull Request

---

#  License

This project is intended for educational and portfolio purposes.



---

#  Developer Information

**Project Developer:** Ms.Shreya Sunil Palase

**GitHub:** https://github.com/shreyapalase 



---

# Acknowledgements

* OpenWeatherMap API
* Python Community
* Matplotlib Documentation
* Jupyter Notebook Team

---

If you found this project useful, consider giving it a  on GitHub.

Thank you for visiting this project repository!
