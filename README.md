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
