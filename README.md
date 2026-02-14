# 🔎 Typesense Multi-Search Scraper

A beginner-friendly, educational project demonstrating how to:  

- Inspect browser DevTools to understand API requests  
- Break down a `multi_search` cURL request  
- Implement pagination for API responses  
- Secure API keys using environment variables  
- Export structured results to CSV  

This repository is **generic** and **educational**. It contains no sensitive information or proprietary data.

---

## 📚 What You Will Learn

By following this guide, you will learn:  

- How to inspect network requests in DevTools  
- How to understand exported cURL commands  
- How search APIs structure responses  
- How pagination works internally  
- How to securely store API keys  
- How to build a clean, reusable API client in Python  
- How to export results to CSV for analysis

---

## 🧭 Inspecting API Requests in DevTools

1. Open your browser and right-click → **Inspect**  
2. Go to the **Network** tab  
3. Filter by **Fetch/XHR**  
4. Perform a search on the website  
5. Click the request that resembles the search endpoint  
6. Right-click → **Copy → Copy as cURL**  

This allows you to see exactly how the website is communicating with the backend. The cURL will include headers, API keys, and request payloads.  

Example cURL (simplified):

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
```

---

## 🔍 Understanding the Multi-Search API

The `multi_search` endpoint allows querying multiple collections at once. Key fields:  

- `"collection"`: The dataset to query  
- `"q"`: Search term (use `"*"` for all items)  
- `"query_by"`: Comma-separated fields to search within  
- `"page"`: Page number for pagination  
- `"per_page"`: Number of results per page  

The API returns JSON including:  

- `results`: Array of items per collection  
- `facet_counts`: Counts and facets for filtering and stats  
- `metadata`: Optional info like `total_count`  

---

## 💻 Python Scraper Overview

The scraper included in this repository demonstrates:  

1. **Loading your API key securely** using environment variables (`.env`)  
2. **Making POST requests** to the multi_search endpoint  
3. **Handling pagination** to fetch all exercises  
4. **Parsing JSON responses** and extracting relevant fields  
5. **Exporting results to CSV** for analysis  

You can find the Python scraper file here: [📄 scraper.py](./scraper.py)

---

## 🔁 Handling Pagination

- The API supports `"page"` and `"per_page"` parameters  
- Use a loop to iterate through pages until all items are retrieved  
- Inspect `metadata` in the response to calculate total pages dynamically  

---

## 📦 Exporting Results to CSV

- The scraper converts JSON responses into a structured format  
- You can export the data using `pandas` for analysis, filtering, or reporting  
- The CSV includes all relevant fields returned by the API  

---

## 🛡️ Security Best Practices

- Keep your API keys in a `.env` file  
- Never commit `.env` or sensitive keys to GitHub  
- Use environment variables when deploying or sharing code  

---

## 🚀 Tips for Beginners

- Start by copying cURL from DevTools to understand the request  
- Inspect the JSON response structure before writing code  
- Test API requests in small batches before scraping everything  
- Comment your code and separate functions for reusability  
- Use `try-except` blocks to handle API errors gracefully  

---

## 📖 References

- [Typesense Documentation](https://typesense.org/docs/)  
- [Python Requests Library](https://docs.python-requests.org/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [Python Dotenv](https://pypi.org/project/python-dotenv/)  

---

## 📝 License

This repository is **educational**. Feel free to use it for learning and personal projects. Do **not** upload API keys or sensitive information.

