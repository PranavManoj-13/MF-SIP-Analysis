# Mutual Fund Data Collection Guide

## Overview
This guide will help you collect historical NAV data for Indian mutual funds to analyze optimal SIP frequencies.

## Data Sources

### 1. MFAPI (Primary Source)
- **URL**: https://api.mfapi.in
- **Type**: Free REST API
- **Coverage**: All AMFI-registered mutual funds
- **Data Available**: 
  - Daily NAV history
  - Scheme metadata (name, fund house, category)
- **Rate Limit**: Be respectful - add 1-2 second delays between requests
- **No API Key Required**: ✓

### 2. Alternative Sources (For Reference)

#### AMFI Website
- **URL**: https://www.amfiindia.com/net-asset-value/nav-history
- **Format**: Excel/CSV downloads
- **Usage**: Can supplement API data or verify accuracy

#### NSE/BSE (For Index Data)
- **NSE**: https://www.nseindia.com
- **BSE**: https://www.bseindia.com
- **Usage**: For benchmark indices (Nifty 50, Sensex)

## Quick Start

### Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

### Option 1: Quick Collection (Recommended for Beginners)

Collect predefined popular schemes:

```bash
python mf_data_collector.py
```

This will:
- Fetch all available schemes (~1000+)
- Download NAV data for 15 popular schemes across 5 categories
- Save individual CSV files for each scheme
- Generate a summary report

**Output:**
- `data/raw/all_schemes.csv` - List of all schemes
- `data/raw/scheme_XXXXX.csv` - Individual scheme data
- `data/raw/collection_summary.csv` - Summary

### Option 2: Enhanced Collection (Recommended)

More control with search and validation:

```bash
python enhanced_collector.py
```

Features:
- Search by category keywords
- Data quality validation
- Automatic retry on failures
- Configurable number of schemes per category

### Option 3: Browse and Select

Interactive scheme selection:

```bash
python scheme_browser.py
```

Use this to:
- Search schemes by keyword
- Browse by category
- View popular schemes
- Copy scheme codes for custom collection

## Data Collection Strategies

### Strategy 1: Category-Based (Recommended for SIP Analysis)

Collect 3-5 schemes from each major category:

```python
from enhanced_collector import EnhancedMFCollector

collector = EnhancedMFCollector()

search_criteria = {
    'Large Cap': ['bluechip', 'large cap'],
    'Mid Cap': ['midcap'],
    'Small Cap': ['small cap'],
    'Flexi Cap': ['flexi cap'],
    'Index': ['nifty 50 index'],
}

summary = collector.collect_schemes_by_criteria(search_criteria, max_schemes=3)
```

### Strategy 2: Popular Schemes Only

Focus on high-performing, well-known funds:

```python
# Edit mf_data_collector.py
# Modify the popular_schemes dictionary with your chosen codes
```

### Strategy 3: Specific Schemes

If you know exact scheme codes:

```python
from enhanced_collector import EnhancedMFCollector

collector = EnhancedMFCollector()

scheme_codes = ['120503', '118989', '119597']  # Your choices

for code in scheme_codes:
    data = collector.get_scheme_with_retry(code)
    # Process data...
```

## Understanding the Data

### Raw Data Format (from API)

```json
{
  "meta": {
    "scheme_code": "120503",
    "scheme_name": "SBI Bluechip Fund - Regular Plan - Growth",
    "fund_house": "SBI Mutual Fund",
    "scheme_type": "Open Ended Schemes",
    "scheme_category": "Equity Scheme - Large Cap Fund"
  },
  "data": [
    {
      "date": "13-02-2026",
      "nav": "123.45"
    },
    ...
  ]
}
```

### CSV Output Format

| date       | nav    | scheme_code | scheme_name           | fund_house        | scheme_category |
|------------|--------|-------------|-----------------------|-------------------|-----------------|
| 13-02-2026 | 123.45 | 120503      | SBI Bluechip Fund ... | SBI Mutual Fund   | Large Cap       |
| 12-02-2026 | 123.12 | 120503      | SBI Bluechip Fund ... | SBI Mutual Fund   | Large Cap       |

## Data Quality Issues to Watch For

### Common Issues:

1. **Missing Dates**: NAV not published on weekends/holidays
2. **Zero NAV Values**: Data entry errors
3. **Duplicate Dates**: Same date appearing multiple times
4. **Inconsistent Naming**: Scheme names may vary
5. **Merged Schemes**: Historical schemes may have merged

### Validation Checks (Built-in)

The `enhanced_collector.py` automatically checks for:
- Missing/invalid dates
- Missing/invalid NAV values
- Zero NAV values
- Duplicate dates
- Data range and completeness

## Sample Scheme Codes

### Large Cap Funds
- `120503` - SBI Bluechip Fund
- `118989` - ICICI Prudential Bluechip Fund
- `119597` - Axis Bluechip Fund
- `100473` - HDFC Top 100 Fund

### Mid Cap Funds
- `119605` - Axis Midcap Fund
- `119600` - DSP Midcap Fund
- `120405` - Kotak Emerging Equity Fund

### Small Cap Funds
- `119551` - Axis Small Cap Fund
- `112090` - SBI Small Cap Fund
- `118378` - Nippon India Small Cap Fund

### Index Funds
- `120716` - UTI Nifty 50 Index Fund
- `119226` - ICICI Prudential Nifty 50 Index Fund

### Flexi/Multi Cap
- `122639` - Parag Parikh Flexi Cap Fund
- `120305` - Quant Flexi Cap Fund

## Recommendations for Your Project

### For Phase 1 Data Collection:

1. **Number of Schemes**: 15-20 schemes across 4-5 categories
   - Large Cap: 3-4 schemes
   - Mid Cap: 3-4 schemes
   - Small Cap: 3-4 schemes
   - Flexi Cap: 2-3 schemes
   - Index: 2-3 schemes

2. **Time Period**: At least 5 years of data (2019-2024)
   - Covers different market conditions
   - Bull run (2020-2021)
   - Correction (2022)
   - Recovery (2023-2024)

3. **Data Requirements**:
   - Daily NAV values
   - Scheme metadata (name, category, fund house)
   - Minimum 1000 data points per scheme

### Data Size Estimation:

- 1 scheme × 5 years ≈ 1,250 records
- 20 schemes ≈ 25,000 total records
- CSV file size ≈ 2-3 MB

## Next Steps After Collection

1. **Data Validation**: Check for quality issues
2. **Data Cleaning**: Handle missing values, duplicates
3. **Database Design**: Create OLTP schema
4. **Load Data**: Import into PostgreSQL/MySQL
5. **ETL Development**: Build transformation pipelines

## Troubleshooting

### API Not Responding
- Check internet connection
- Add delays between requests (1-2 seconds)
- Try again later

### Scheme Code Not Found
- Verify code from all_schemes.csv
- Some old schemes may be discontinued
- Use scheme_browser.py to find alternatives

### Data Quality Issues
- Cross-verify with AMFI website
- Use multiple sources if critical
- Document assumptions in your report

## Best Practices

1. **Always cache data**: Don't re-download unnecessarily
2. **Add delays**: Be nice to the API (1-2 second delays)
3. **Validate data**: Use built-in validation functions
4. **Document choices**: Keep track of which schemes you selected and why
5. **Backup data**: Save raw data before transformations

## Questions?

For MFAPI documentation: https://api.mfapi.in
For AMFI data: https://www.amfiindia.com

---

**Ready to start?** Run:
```bash
python enhanced_collector.py
```

This will collect data for popular schemes across all categories!
