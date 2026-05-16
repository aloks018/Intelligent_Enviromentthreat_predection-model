# IEIRAS deployment guide

## Recommended free host

Use **Streamlit Community Cloud** for the primary deployment.

Why:

- built specifically for Streamlit
- free public hosting
- automatic app startup
- public `streamlit.app` URL
- easiest for beginners

## Fallback host

Use **Render** if you later want a second public deployment path.

## Required repository files

- `app.py`
- `requirements.txt`
- `.streamlit/config.toml`

Optional support files in this repo:

- `render.yaml`
- `Procfile`
- `Dockerfile`
- `.env.example`

## Environment variables

- `OPENAI_API_KEY`

This is only required if you want the AI assistant inside the map page to answer.

Without it, the rest of the website still works.

## Streamlit Community Cloud deploy

1. Push this project to GitHub.
2. Open `https://share.streamlit.io/`.
3. Click **Create app**.
4. Select your GitHub repository.
5. Set branch to `main`.
6. Set main file path to `app.py`.
7. Choose a custom subdomain if available.
8. In advanced settings, add `OPENAI_API_KEY` only if needed.
9. Deploy.

Your public link will look like:

`https://your-chosen-name.streamlit.app`

## Render deploy

1. Push this project to GitHub.
2. Open Render dashboard.
3. Create a new **Web Service** from GitHub.
4. Render should read `render.yaml`.
5. Confirm deploy.

Your public link will look like:

`https://ieiras-impact.onrender.com`

## Domain connection

For a fully custom domain like `ieiras.site` or `ieirasimpact.com`:

1. Buy a domain from a registrar such as Cloudflare Registrar or Namecheap.
2. For Streamlit Community Cloud, use the free `streamlit.app` subdomain.
3. For a paid custom domain later, connect it through Render or another host that supports custom domains.
