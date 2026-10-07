# Site Log IP Geolocation

Recovered 2020 utility for extracting unique visitor IP addresses from a web-server access log and enriching them with IP geolocation metadata.

The script was originally written to get more useful geographic context from site logs than the raw IP addresses alone provided. It filters obvious bot/scanner/request noise, extracts unique IPs, looks them up through the ipgeolocation.io API, and writes the returned metadata to CSV.

## Files

- `site_log_ip_geolocation.py` — cleaned recovered script.
- `.env.example` — API-key placeholder.

## Usage

Set the API key first:

```bash
export IPGEOLOCATION_API_KEY=your_key_here
```

The recovered script currently expects the historical access-log filename `shanelessa.com-Dec-2020` in the working directory. Change that argument in `init()` to analyze another log.

## Recovery notes

The original source contained an API key directly in the file; it has been removed from this archive. The bot/scanner filter also used `any(word not in line ...)`, which made the condition effectively true for almost every line. The cleaned version uses `not any(word in line ...)`, matching the apparent intent of the original code.

No original access logs or generated visitor-geolocation CSVs are included.