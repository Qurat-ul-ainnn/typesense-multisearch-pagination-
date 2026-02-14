# 🔎 Typesense Multi-Search Scraper

A beginner-friendly, educational Python project demonstrating how to:

- Inspect browser DevTools to understand API requests  
- Break down a `multi_search` cURL request  
- Implement pagination for API responses  
- Secure API keys using environment variables  
- Export structured results to CSV  

This repository is **generic** and **educational**. It contains no sensitive information or proprietary data.

---

## 📚 What You Will Learn

- How to inspect network requests in DevTools  
- How to understand exported cURL commands  
- How search APIs structure responses  
- How pagination works internally  
- How to securely store API keys  
- How to build a clean, reusable API client in Python  

---

## 🧭 Inspecting API Requests in DevTools

1. Open your browser and right-click → **Inspect**  
2. Go to the **Network** tab  
3. Filter by **Fetch/XHR**  
4. Perform a search on the website  
5. Click the request that resembles the search endpoint  
6. Right-click → **Copy → Copy as cURL**

Example cURL:

```bash
curl 'https://search-us.physitrack.com/multi_search' \
  -H 'content-type: text/plain' \
  -H 'x-typesense-api-key: YOUR_API_KEY' \
  --data-raw '{
    "searches":[
      {
        "collection":"exercises_production_us",
        "q":"*",
        "query_by":"name_en,alias_en,instructions_en,regions_en,name_en_us",
        "page":1,
        "per_page":20
      }
    ]
  }'
