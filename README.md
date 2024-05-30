# Gemini Pro Vercel

## Run in local environment
1. Setup your local environment for running Python app
2. Download the Repo
3. Add a `.env` file inside the folder and add `GOOGLE_API_KEY=replace_me_with_gemini_Key`
4. install dependencys
```
pip install Flask
pip install python-dotenv
pip install requests
```
5. For running the server use `flask run`

## Deploy to Vercel

1. Create vercel account `https://vercel.com`
2. install vercel CLI `npm i -g vercel` (you have to install Node.js first)
3. For simple deploy use `vercel` and for production use `vercel --prod`