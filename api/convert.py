from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def convert(time: str) -> str:
    s = time.replace(" ", "").lower()

    if s.endswith("am") or s.endswith("pm"):
        period, core = s[-2:], s[:-2]
        if ":" not in core:
            raise ValueError("Expected ':' in 12-hour time")
        h_str, m_str = core.split(":", 1)
        if not (h_str.isdigit() and m_str.isdigit()):
            raise ValueError("Invalid hour or minute")
        h, m = int(h_str), int(m_str)
        if not (1 <= h <= 12 and 0 <= m < 60):
            raise ValueError("Hour must be 1–12, minute 0–59")
        h = 0 if (period == "am" and h == 12) else (h if (period == "pm" and h == 12) else (h + 12 if period == "pm" else h))
        return f"{h:02d}{m:02d} hrs"

    elif s.endswith("hrs"):
        core = s[:-3]
        if not core.isdigit() or not (3 <= len(core) <= 4):
            raise ValueError("Expected 3–4 digit military time before 'hrs'")
        core = core.zfill(4)
        h, m = int(core[:2]), int(core[2:])
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError("Hour must be 00–23, minute 00–59")
        suffix = "am" if h < 12 else "pm"
        h12 = h if 1 <= h <= 12 else (12 if h == 0 else h - 12)
        return f"{h12}:{m:02d} {suffix}"

    raise ValueError("Time must end with 'am', 'pm', or 'hrs'")


@app.route("/api/convert", methods=["POST"])
def api_convert():
    try:
        data = request.get_json()
        time_str = data.get("time", "")
        result = convert(time_str)
        return jsonify(success=True, converted=result)
    except ValueError as e:
        return jsonify(success=False, error=str(e)), 400
    except Exception as e:
        return jsonify(success=False, error="Internal server error"), 500
