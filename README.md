# Weather Analysis and AI Advisory Bot

A Python-based application that integrates real-time weather data with Large Language Models (LLM) to provide localized weather reports and automated lifestyle recommendations.

## Project Overview

This project demonstrates the integration of multiple APIs to create a functional service. It fetches meteorological data for a specific location and processes this information through an AI engine to generate context-aware advice for users.

## Technical Stack

* **Language:** Python 3.x
* **Weather Data:** OpenWeatherMap API
* **AI Engine:** Google Gemini AI (Generative AI SDK)
* **Network Operations:** Requests library
* **Version Control:** Git

## System Architecture

1.  **Data Acquisition:** The system sends a request to the OpenWeatherMap API to retrieve current temperature and weather conditions.
2.  **Processing:** The raw JSON data is parsed to extract relevant metrics (Celsius, weather description).
3.  **Intelligence Layer:** The extracted data is passed to the Gemini-1.5-flash model via a structured prompt.
4.  **Output:** The model generates a localized recommendation based on the severity of the weather conditions.

## Installation and Setup

### Prerequisites
* Python 3.10 or higher
* Valid API keys for OpenWeatherMap and Google AI Studio

### Configuration
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/project-name.git](https://github.com/yourusername/project-name.git)
