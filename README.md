# Aviation Time Converter

A simple web application for converting between 12-hour (am/pm) and military (24-hour) time formats, built with Flask and a modern HTML frontend.

## Features
- Convert 12-hour time (e.g., `7:30 pm`) to military time (e.g., `1930 hrs`).
- Convert military time (e.g., `0000 hrs`) to 12-hour time (e.g., `12:00 am`).
- User-friendly web interface styled with Tailwind CSS.
- REST API for programmatic access.

## Project Structure
- `convert.py` — Flask backend with the conversion logic and API endpoint.
- `convert.html` — Frontend web page for user interaction.
- `requirements.txt` — Python dependencies.

## Setup
1. **Clone the repository** and navigate to the project folder.
2. **Create and activate a virtual environment:**
   - On Windows (Git Bash):
     ```bash
     python -m venv env
     source env/Scripts/activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask server:**
   ```bash
   python convert.py
   ```
5. **Open `convert.html` in your browser** to use the web interface.

## API Usage
- **Endpoint:** `POST /api/convert`
- **Request JSON:** `{ "time": "7:30 pm" }`
- **Response JSON:** `{ "success": true, "converted": "1930 hrs" }`

## Example
```bash
curl -X POST http://127.0.0.1:5000/api/convert \
     -H "Content-Type: application/json" \
     -d '{"time": "7:30 pm"}'
```

## License
MIT
