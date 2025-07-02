# AI Health Assistant

A cross-platform AI-powered health assistant for elderly care with conversational AI, smart reminders, health monitoring, and emergency detection.

##  Project Structure
- **frontend/** — React Native mobile app or Kivy prototype.
- **backend/** — Python FastAPI/Flask API server, PostgreSQL ORM.
- **ai_ml_core/** — TensorFlow, OpenCV, MediaPipe, LangChain.
- **non_ai_core/** — Data processing with Pandas, NumPy, Matplotlib.
- **integration/** — OpenAPI docs, Postman tests, smart home APIs.

##  How to Run Backend

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run API server
uvicorn main:app --reload
```

---
