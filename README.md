# Revit Parameter Checker

This Python script is designed to be used within Dynamo for Autodesk Revit.  
It helps identify model elements that are missing critical parameter values, which is useful for quality control workflows in BIM projects.

---

## 🔍 Features

- Takes a list of elements and checks if specified parameters are empty.
- Highlights elements in the Revit model for easy identification.
- Supports single parameter names or name-pairs (source → target).

---

## 💻 How It Works

1. Input:
   - IN[0]: List of Revit elements to check
   - IN[1]: List of parameter names or pairs (e.g. `[["Klasa_Betonu"], ["Kod_pakietu_dokumentacji"]]`)

2. Processing:
   - Iterates through the elements.
   - Checks each specified parameter for an empty string or None.
   - Adds elements with empty parameters to a result list.

3. Output:
   - List of elements with at least one empty parameter (OUT)

---

## Use Cases

- BIM quality assurance
- Preparation before issuing documentation
- Ensuring model completeness before export

---

## Technologies Used

- Autodesk Revit API
- Python for Dynamo
- RevitServices

---

## File

- `DetectEmptyParameters.py` — main script to be used in a Python node inside Dynamo

---

## Author

**Albert Kłoczewiak**  
GitHub: [@albertk-labs](https://github.com/albertk-labs)  
Email: akkloczewiak@gmail.com
