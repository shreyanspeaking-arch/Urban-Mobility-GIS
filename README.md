<div align="center">

# 🗂️ Input gpkg files

**A branch of [Urban Mobility GIS](https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS), a collection of Python programs that map and measure the wards of Indian cities.**

![Format](https://img.shields.io/badge/format-GeoPackage-2ea44f) ![Cities](https://img.shields.io/badge/cities-8-purple) ![CRS](https://img.shields.io/badge/CRS-EPSG%3A4326-lightgrey)

</div>

Ward-boundary files for 8 Indian cities. Every program in this repository reads one of these files: each holds the name or number of every ward and the ward's shape, stored in latitude and longitude (`EPSG:4326`).

## 📂 Files in this branch

| City | File | Wards | Ward column to enter |
|---|---|:-:|---|
| Ahmedabad | [`ahmedabad_wards.gpkg`](./ahmedabad_wards.gpkg) | 48 | `Name` |
| Bengaluru | [`bengaluru_wards_2022.gpkg`](./bengaluru_wards_2022.gpkg) | 243 | `KGISWardName` or `KGISWardNo` |
| Chennai | [`chennai_wards.gpkg`](./chennai_wards.gpkg) | 201 | `Ward_No` |
| Delhi | [`delhi_wards.gpkg`](./delhi_wards.gpkg) | 290 | `Ward_Name` or `Ward_No` |
| Hyderabad | [`hyderabad_wards.gpkg`](./hyderabad_wards.gpkg) | 145 | `name` |
| Jaipur | [`jaipur_wards.gpkg`](./jaipur_wards.gpkg) | 77 | `WARD_NO` |
| Kolkata | [`kolkata_wards_141.gpkg`](./kolkata_wards_141.gpkg) | 141 | `WARD` |
| Mumbai | [`mumbai_electoral_wards_2017.gpkg`](./mumbai_electoral_wards_2017.gpkg) | 227 | `WARD` |

When a program asks for the column that contains the spatial geometry of the ward shapes, enter `geometry` (geopandas gives the shape column that name when it reads the file).

## ⚙️ Getting started

Download a single file into the folder of the program you want to run:

```bash
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS/raw/Input-gpkg-files/kolkata_wards_141.gpkg
```

or clone the whole branch:

```bash
git clone -b Input-gpkg-files --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS.git
```

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-GIS">Back to all topics</a></sub></div>
