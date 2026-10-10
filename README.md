<div align="center">

# 📐 Ward Area Map

**A branch of [Urban Mobility GIS](https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS), a collection of Python programs that map and measure the wards of Indian cities.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

The area of a ward is a basic measure of urban form: comparing ward sizes across a city shows where administrative units are packed tightly, usually in the dense core, and where they spread out towards the edges.

## 📂 Programs in this branch

| # | Program | What it does |
|:-:|---|---|
| 1 | [**Ward Area Map**](#1-ward-area-map) | Area of each ward in km², saved to Excel and shown on a map |

## ⚙️ Getting started

```bash
git clone -b Ward-Area-Map --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS.git
cd Urban-Mobility-GIS
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas pandas matplotlib openpyxl
python ward_area.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows a map. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS/tree/Input-gpkg-files) branch.

---

## 1. Ward Area Map

📄 **File:** [`ward_area.py`](./ward_area.py)

Computes the area of every ward in a city from a ward-boundary file, saves the list of wards and their areas to Excel, and draws a choropleth map of the wards shaded by area.

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS/tree/Input-gpkg-files) branch. If the file has no `WARD` column, the program lists its columns and asks which one holds the ward name or number; it does the same for the geometry column.
2. The ward shapes are projected to UTM zone 45N (`EPSG:32645`) so that they can be measured in metres, and the area of each ward is computed and converted to km².
3. The user enters a name for the output file (without `.xlsx`). The program saves the columns `WARD` and `Area (in km2)` to that Excel file, then projects the wards back to latitude and longitude and draws a map of the wards shaded by area.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`kolkata.xlsx`](./kolkata.xlsx)<br>[`kolkata.png`](./kolkata.png) |

**🗺️ Sample map**

<p align="center">
  <img src="./kolkata.png" alt="Kolkata wards shaded by area" width="720">
</p>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS">Back to all topics</a></sub></div>
