```markdown
# MUTUAL FUND DATA COLLECTION TOOL

Interactive tool for collecting historical NAV data for Indian mutual funds from MFAPI.

## FEATURES

- Browse all available mutual fund schemes on MFAPI
- Search schemes by keywords
- Collect NAV data for specific schemes by scheme code
- Interactive menu-driven interface

## SETUP

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure you have the SchemeBrowser module in the same directory

## USAGE

Run the main script:
```bash
python Data-Collector.py
```

### MENU OPTIONS

**Option 1: Get List of All Schemes**
- Fetches and displays all available mutual fund schemes from MFAPI
- Saves complete list to `data/raw/Schemes-List.csv`
- Useful for browsing available schemes

**Option 2: Browse Schemes Interactively**
- Search schemes by keyword

**Option 3: Get Data of Specific Schemes**
- Enter scheme codes (comma-separated)
- Validates scheme codes against MFAPI database
- Downloads complete NAV history for selected schemes
- Saves individual CSV files for each scheme

**Option 4: Exit**
- Safely exit the application

## EXAMPLE WORKFLOW

1. Run the program: `python Data-Collector.py`
2. Select Option 1 to see all available schemes
3. Note down scheme codes you want to collect
4. Select Option 3 and enter scheme codes
5. Data will be saved in `data/raw/` directory

## INPUT FORMAT

When collecting specific schemes (Option 3):
```
Enter scheme codes: 120503, 118989, 119597
```

## OUTPUT FILES

Collected data is saved in the following structure:
```
data/
└── raw/
    ├── Schemes-List.csv         # Complete list of schemes
    ├── scheme_120503.csv        # Individual scheme data
    ├── scheme_118989.csv
    └── scheme_119597.csv
```

## DATA FORMAT

Each scheme CSV file contains:
- `date`: NAV date (DD-MM-YYYY format)
- `nav`: Net Asset Value
- `scheme_code`: Scheme identifier
- `scheme_name`: Full scheme name
- `fund_house`: Asset Management Company

## ERROR HANDLING

- Invalid scheme codes will be rejected with error message
- Network failures trigger automatic retry with exponential backoff
- API rate limits respected with 1-2 second delays between requests
- All errors logged to console for debugging
```
