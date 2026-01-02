# QUICK START GUIDE

## ✅ What Has Been Created

### 1. Certificate ID System
- **Format**: MLDL-JNTUGV-XXX (where XXX is 001-100, randomly assigned)
- **Total Certificates**: 37 unique IDs
- **ID Mapping**: See `id.csv` file

### 2. Files Created
```
/certificates/
├── verify.html          ✅ Certificate verification page (PDF viewer)
├── data.json           ✅ Database with all 37 certificates
├── id.csv              ✅ Name-to-ID mapping
├── data.csv            (Original CSV data)
├── update-data.ps1     (PowerShell script used for conversion)
├── README.md           ✅ Detailed setup instructions
└── assets/
    └── PLACEHOLDER.txt  (Placeholder - replace with actual PDFs)
```

## 🎯 Next Steps (What YOU Need to Do)

### Step 1: Add JNTU Logo
Place your college logo in:
```
assets/jntu-logo.png
```
Recommended: 120px width, transparent background

### Step 2: Generate PDF Certificates
Create 37 PDF certificates and place them in the `assets/` folder.

Each PDF must be named according to `id.csv`. For example:
- `assets/MLDL-JNTUGV-015.pdf` → for Dr K Dayana
- `assets/MLDL-JNTUGV-025.pdf` → for SRADHANJALI PATTANAIK
- `assets/MLDL-JNTUGV-014.pdf` → for DASARI PROMOD KUMAR
- ... and so on (37 total)

**Each PDF certificate should include:**
- Candidate name
- Designation & Department
- College name
- Course: "40 Hours Certification Course on Machine Learning & Deep Learning"
- Duration: "06-10-2025 to 27-10-2025"
- Grade obtained
- **QR Code** with URL: `https://yourusername.github.io/certificates/verify.html?id=MLDL-JNTUGV-XXX`
- **Certificate ID printed below QR code** (e.g., MLDL-JNTUGV-015)

### Step 3: Test Locally
1. Open `verify.html` in your browser
2. Enter any ID from `id.csv` (example: `MLDL-JNTUGV-015`)
3. Click "Verify Certificate"
4. The PDF should display and be downloadable

### Step 4: Deploy to GitHub Pages
1. Push all files to GitHub repository
2. Enable GitHub Pages
3. Share verification links with participants

## 📋 Sample Certificate IDs (First 10)

| Name | Certificate ID |
|------|---------------|
| Dr K Dayana | MLDL-JNTUGV-015 |
| SRADHANJALI PATTANAIK | MLDL-JNTUGV-025 |
| DASARI PROMOD KUMAR | MLDL-JNTUGV-014 |
| MEESALA SRINUVASU RAO NAIDU | MLDL-JNTUGV-048 |
| VELUMURU SRIKANTH | MLDL-JNTUGV-024 |
| PALLANTLA YESWANTH | MLDL-JNTUGV-073 |
| Jayasree Pinajala | MLDL-JNTUGV-034 |
| Sathiraju Tejaswi | MLDL-JNTUGV-086 |
| Jami Kavitha | MLDL-JNTUGV-009 |
| BHASKARA RAO SANAPALA | MLDL-JNTUGV-067 |

**See `id.csv` for complete list of all 37 IDs**

## 🔗 How QR Codes Work

When a user scans the QR code on their certificate:
1. Browser opens: `https://yourusername.github.io/certificates/verify.html?id=MLDL-JNTUGV-015`
2. Page automatically loads their certificate
3. They can view the PDF and download it
4. **No manual typing required!**

## ⚠️ Important Notes

- Certificate IDs are **case-sensitive** (use uppercase)
- All 37 PDF files must be in the `assets/` folder
- File names must match exactly (e.g., `MLDL-JNTUGV-015.pdf`)
- Each QR code must encode the correct URL with the person's ID
- Print the Certificate ID below the QR code on each certificate

## 🧪 Testing Examples

Test these IDs after adding PDFs:
- `MLDL-JNTUGV-015` (Dr K Dayana)
- `MLDL-JNTUGV-025` (SRADHANJALI PATTANAIK)
- `MLDL-JNTUGV-073` (PALLANTLA YESWANTH)

Invalid ID test:
- `MLDL-JNTUGV-999` (should show error message)

## 📞 Support

For questions, check:
1. `README.md` - Detailed instructions
2. `id.csv` - Complete ID list
3. `data.json` - Certificate database

---

**Status**: ✅ System ready - Just add logo + PDF certificates!
