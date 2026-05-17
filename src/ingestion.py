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

    try:
        data = res.json()
    except:
        return []

    ids = data.get("esearchresult", {}).get("idlist", [])

    papers = []

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
            continue

        result = summary_data.get("result", {}).get(pmid, {})

        title = result.get("title", "")
        authors = result.get("authors", [])
        journal = result.get("fulljournalname", "")
        pubdate = result.get("pubdate", "")

        papers.append({
            "pmid": pmid,
            "title": title,
            "abstract": title,
            "authors": authors,
            "journal": journal,
            "year": pubdate,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        })

    return papers
