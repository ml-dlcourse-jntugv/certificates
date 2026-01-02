# Certificate Verification System - Setup Guide

## Folder Structure
```
/certificates/
├── verify.html          (Main verification page)
├── data.json           (Certificate database)
├── id.csv              (Name to ID mapping)
├── data.csv            (Original data)
├── update-data.ps1     (Update script)
└── assets/
    ├── jntu-logo.png
    ├── MLDL-JNTUGV-001.pdf
    ├── MLDL-JNTUGV-002.pdf
    └── ... (all certificate PDFs)
```

## Certificate ID Format

All certificates use the format: **MLDL-JNTUGV-XXX**

Where XXX is a unique random number between 001-100.

## Required Files in /assets/ Folder

### 1. JNTU Logo
- File: `jntu-logo.png`
- Recommended size: 120px width (transparent background)
- Place at: `assets/jntu-logo.png`

### 2. Certificate PDFs
You need to create/place PDF certificates for all 37 participants.

The PDF filenames must match the IDs in `id.csv`:

| Name | Certificate ID | Required File |
|------|---------------|---------------|
| Dr K Dayana | MLDL-JNTUGV-015 | assets/MLDL-JNTUGV-015.pdf |
| SRADHANJALI PATTANAIK | MLDL-JNTUGV-025 | assets/MLDL-JNTUGV-025.pdf |
| DASARI PROMOD KUMAR | MLDL-JNTUGV-014 | assets/MLDL-JNTUGV-014.pdf |
| MEESALA SRINUVASU RAO NAIDU | MLDL-JNTUGV-048 | assets/MLDL-JNTUGV-048.pdf |
| VELUMURU SRIKANTH | MLDL-JNTUGV-024 | assets/MLDL-JNTUGV-024.pdf |
| PALLANTLA YESWANTH | MLDL-JNTUGV-073 | assets/MLDL-JNTUGV-073.pdf |
| Jayasree Pinajala | MLDL-JNTUGV-034 | assets/MLDL-JNTUGV-034.pdf |
| Sathiraju Tejaswi | MLDL-JNTUGV-086 | assets/MLDL-JNTUGV-086.pdf |
| Jami Kavitha | MLDL-JNTUGV-009 | assets/MLDL-JNTUGV-009.pdf |
| BHASKARA RAO SANAPALA | MLDL-JNTUGV-067 | assets/MLDL-JNTUGV-067.pdf |
| Yanda Nagamani | MLDL-JNTUGV-060 | assets/MLDL-JNTUGV-060.pdf |
| Doddi Ravali | MLDL-JNTUGV-061 | assets/MLDL-JNTUGV-061.pdf |
| REDDI SWAPNA | MLDL-JNTUGV-047 | assets/MLDL-JNTUGV-047.pdf |
| B. Usha Rani | MLDL-JNTUGV-066 | assets/MLDL-JNTUGV-066.pdf |
| Kulukuru Anil | MLDL-JNTUGV-092 | assets/MLDL-JNTUGV-092.pdf |
| Dr. Teki Vamsee Krishna | MLDL-JNTUGV-030 | assets/MLDL-JNTUGV-030.pdf |
| Kommanapalli Madhavi | MLDL-JNTUGV-097 | assets/MLDL-JNTUGV-097.pdf |
| GOSU NAVEEN | MLDL-JNTUGV-038 | assets/MLDL-JNTUGV-038.pdf |
| D HIMA BINDU | MLDL-JNTUGV-022 | assets/MLDL-JNTUGV-022.pdf |
| Medisetti Prishikilla | MLDL-JNTUGV-036 | assets/MLDL-JNTUGV-036.pdf |
| BHUPATHIRAO LAKINANA | MLDL-JNTUGV-079 | assets/MLDL-JNTUGV-079.pdf |
| MAKKA JAYAKRISHNA | MLDL-JNTUGV-075 | assets/MLDL-JNTUGV-075.pdf |
| S S R M RAJU PAIDI | MLDL-JNTUGV-091 | assets/MLDL-JNTUGV-091.pdf |
| NageswaraRao Bodepudi | MLDL-JNTUGV-028 | assets/MLDL-JNTUGV-028.pdf |
| Allada Vineela | MLDL-JNTUGV-057 | assets/MLDL-JNTUGV-057.pdf |
| ANURADHA TUTIKA | MLDL-JNTUGV-002 | assets/MLDL-JNTUGV-002.pdf |
| Aravinda Kasukurthi | MLDL-JNTUGV-041 | assets/MLDL-JNTUGV-041.pdf |
| K.SWATHI | MLDL-JNTUGV-062 | assets/MLDL-JNTUGV-062.pdf |
| Mrs Kavitha Chekuri | MLDL-JNTUGV-004 | assets/MLDL-JNTUGV-004.pdf |
| Reventh Raj Dasari | MLDL-JNTUGV-085 | assets/MLDL-JNTUGV-085.pdf |
| POTNURI GAYATRI | MLDL-JNTUGV-006 | assets/MLDL-JNTUGV-006.pdf |
| N. Sushma Rani | MLDL-JNTUGV-054 | assets/MLDL-JNTUGV-054.pdf |
| Usha Rani Bhupathi | MLDL-JNTUGV-084 | assets/MLDL-JNTUGV-084.pdf |
| ALLADA DHANUNJAYA PRASAD | MLDL-JNTUGV-064 | assets/MLDL-JNTUGV-064.pdf |
| SIRRA SIREESA | MLDL-JNTUGV-049 | assets/MLDL-JNTUGV-049.pdf |
| VADABOYINA APPALARAJU | MLDL-JNTUGV-077 | assets/MLDL-JNTUGV-077.pdf |
| VALLABHANENI PRANAV | MLDL-JNTUGV-053 | assets/MLDL-JNTUGV-053.pdf |

## How to Generate QR Codes

Each certificate should have a QR code that links to:
```
https://<your-username>.github.io/certificates/verify.html?id=MLDL-JNTUGV-XXX
```

Example for ID MLDL-JNTUGV-015:
```
https://yourusername.github.io/certificates/verify.html?id=MLDL-JNTUGV-015
```

**Important:** Print the Certificate ID (e.g., MLDL-JNTUGV-015) below the QR code on each certificate.

## How It Works

1. **QR Code Scan**: When someone scans the QR code, they are taken to `verify.html?id=MLDL-JNTUGV-XXX`
2. **Auto-Load**: The certificate automatically loads and displays
3. **Manual Entry**: Users can also manually type the Certificate ID
4. **View & Download**: Users can view the PDF and download it

## Testing Locally

1. Place all PDF files in the `assets/` folder
2. Place the logo: `assets/jntu-logo.png`
3. Open `verify.html` in a browser
4. Test with any ID from `id.csv` (e.g., MLDL-JNTUGV-015)

## Deploying to GitHub Pages

1. Create a repository named `certificates`
2. Upload all files maintaining the folder structure
3. Enable GitHub Pages in repository settings
4. Access at: `https://yourusername.github.io/certificates/verify.html`

## Notes

- Certificate IDs are **case-sensitive**
- All IDs are unique and randomly assigned
- PDF files must be named exactly as specified
- The system works entirely client-side (no backend needed)
