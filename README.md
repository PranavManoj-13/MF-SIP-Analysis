# Quick Start Guide: Mutual Funds Data Collection

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Demo/Collection Tool
```bash
python DataCollector.py
```

Then select **Option 3** for full collection.

## What You'll Get

After running the collection:

### Directory Structure
```
data/raw/
├── all_schemes.csv              # Complete list of ~1000+ schemes
├── collection_summary.csv       # Summary of collected schemes
├── all_nav_data.csv             # Combined NAV data (all schemes)
├── scheme_120503.csv            # Individual scheme files
├── scheme_118989.csv
└── ...
```

### Data Format

Each scheme file contains:
- **date**: NAV date (DD-MM-YYYY)
- **nav**: Net Asset Value
- **scheme_code**: Unique scheme identifier
- **scheme_name**: Full scheme name
- **fund_house**: AMC name
- **scheme_type**: Open/Closed ended
- **scheme_category**: Category classification

## Alternative: Manual Collection

### Option A: Browse and Select Schemes
```bash
python scheme_browser.py
```

### Option B: Enhanced Collection with Custom Categories
```bash
python enhanced_collector.py
```

Edit the script to customize categories and number of schemes.

### Option C: Basic Collection
```bash
python mf_data_collector.py
```

Collects predefined popular schemes.

## For Your Project

**Recommended approach:**
1. Run `demo_collection.py`
2. Choose Option 3 (Full Collection)
3. Wait 5-10 minutes for collection to complete
4. Check `data/raw/collection_summary.csv` for overview
5. Proceed to Phase 2: Database Design

## Expected Collection

- **Schemes**: 15-20 across 5 categories
- **Records**: ~25,000 total NAV records
- **Time Period**: 5+ years of historical data
- **File Size**: ~2-3 MB total

## Troubleshooting

**API Rate Limit Issues?**
- Increase delay between requests in code
- Run collection in smaller batches

**Missing Schemes?**
- Check scheme codes in all_schemes.csv
- Use scheme_browser.py to find alternatives

**Data Quality Issues?**
- Review validation output in collection summary
- Document issues for Phase 2 (Data Cleaning)

## Next Phase

After collection:
✓ Phase 1 (Data) - COMPLETE
→ Phase 2 (OLTP) - Design database schema
→ Phase 3 (Data Warehouse) - Star/Snowflake schema
→ Phase 4 (OLAP) - Analysis queries
→ Phase 5 (SIP Simulation) - Calculate optimal frequencies

---

**Questions?** Check DATA_COLLECTION_GUIDE.md for detailed documentation.
