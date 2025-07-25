from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from your frontend

def convert(time: str) -> str:
    """
    Converts:
      • 12‑hour input ending in 'am'/'pm' → military 'HHMM hrs'
      • military input ending in 'hrs'    → 12‑hour 'H:MM am/pm'
    """
    s = time.replace(" ", "").lower()

    # 1) 12‑hour to military
    if s.endswith("am") or s.endswith("pm"):
        period = s[-2:]
        core   = s[:-2]
        if ":" not in core:
            raise ValueError("Expected ':' in 12‑hour time")
        h_str, m_str = core.split(":", 1)
        if not (h_str.isdigit() and m_str.isdigit()):
            raise ValueError("Invalid hour or minute")
        h, m = int(h_str), int(m_str)
        if not (1 <= h <= 12 and 0 <= m < 60):
            raise ValueError("Hour must be 1–12, minute 0–59")
        if period == "am":
            h = 0 if h == 12 else h
        else:
            h = h if h == 12 else h + 12
        return f"{h:02d}{m:02d} hrs"

    # 2) Military to 12‑hour
    elif s.endswith("hrs"):
        core = s[:-3]
        if not core.isdigit() or not (3 <= len(core) <= 4):
            raise ValueError("Expected 3–4 digit military time before 'hrs'")
        core = core.zfill(4)
        h, m = int(core[:2]), int(core[2:])
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError("Hour must be 00–23, minute 00–59")
        suffix = "am" if h < 12 else "pm"
        h12 = h if 1 <= h <= 12 else (h - 12 if h > 12 else 12)
        return f"{h12}:{m:02d} {suffix}"

    # invalid format
    raise ValueError("Time must end with 'am', 'pm', or 'hrs'")


# Serve the frontend at the root URL
@app.route("/")
def index():
    return render_template("convert.html")

@app.route("/api/convert", methods=["POST"])
def api_convert():
    data = request.get_json(force=True)
    time_str = data.get("time", "")
    try:
        result = convert(time_str)
        return jsonify({"success": True, "converted": result})
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400



