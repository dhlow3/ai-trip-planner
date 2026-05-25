# AI Trip Planner

A web app that generates personalised outdoor trip itineraries using the OpenAI API. Enter a destination, activity, season, and experience level — get back a full itinerary, packing list, and safety tips.

Built with FastAPI (Python) on the backend and plain HTML/CSS/JS on the frontend.

---

## Project Structure

```
app/
├── main.py          # App entry point, routes static files
├── config.py        # Loads environment variables
├── models/          # Request/response shapes (Pydantic)
├── routes/          # API endpoints
├── services/        # OpenAI integration
└── static/          # Frontend (index.html)
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key — get one at platform.openai.com |

Copy `.env.example` to `.env` and fill in your key:

```bash
cp .env.example .env
```

---

## Running Locally

**Prerequisites:** Python 3.12 or 3.13

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key to `.env` (see above).

4. Start the server:

```bash
uvicorn app.main:app --reload
```

5. Open `http://localhost:8000` in your browser.

---

## API Endpoints

| Method | URL | Description |
|---|---|---|
| `GET` | `/` | Serves the frontend |
| `POST` | `/trips/generate-trip` | Generates a trip plan |
| `GET` | `/health` | Health check |

---

## Deploying to Render

This repo includes a `render.yaml` that pre-configures everything.

1. Push this repo to GitHub.
2. Go to [render.com](https://render.com) → New → Web Service → connect your repo.
3. Render will auto-detect `render.yaml` — no manual setup needed.
4. In the **Environment** tab, add your `OPENAI_API_KEY`.
5. Click **Deploy**.

Your app will be live at `https://<your-app>.onrender.com`.

> **Note:** The free tier on Render spins down after inactivity. The first request after a sleep may take ~30 seconds.
