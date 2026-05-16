# Render deploy notes

This project is ready to deploy to Render as a Python web service.

## Start command

Render will start the app with:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

## Required files

- `requirements.txt`
- `render.yaml`
- `.streamlit/config.toml`

## Optional environment variables

- `OPENAI_API_KEY`

Without `OPENAI_API_KEY`, the map page still loads, but the AI assistant section will not answer.

## Deploy flow

1. Push this project to GitHub.
2. Create a new Render Web Service from the repository.
3. Render will detect `render.yaml`.
4. After the first deploy, open the generated Render URL.
5. Add your custom domain in Render dashboard.
6. Update DNS records at your domain registrar.
