import requests

def fetch_papers(query, limit=5):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": limit
    }

    res = requests.get(url, params=params)

    print("STATUS:", res.status_code)

    # Parse JSON safely
    try:
        data = res.json()
    except:
        print("Not JSON response")
        print(res.text[:300])
        return []

    # Validate response
    if "esearchresult" not in data:
        print("Invalid response:", data)
        return []

    ids = data["esearchresult"].get("idlist", [])
    print("IDS:", ids)

    if not ids:
        print("No IDs found")
        return []

    papers = []

    # Move loop INSIDE function
    for pmid in ids:
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        
        summary_params = {
            "db": "pubmed",
            "id": pmid,
            "retmode": "json"
        }

        summary_res = requests.get(summary_url, params=summary_params)

        try:
            summary_data = summary_res.json()
        except:
            print(f" Failed to parse summary for {pmid}")
            continue

        result = summary_data.get("result", {}).get(pmid, {})

        title = result.get("title", "")

        if not title:
            continue

        papers.append({
            "title": title,
            "abstract": title,  # fallback
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        })

    print(" Papers fetched:", len(papers))

    return papers   