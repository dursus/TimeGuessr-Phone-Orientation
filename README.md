# Landscape to Portrait Orientation Shift: A TimeGuessr Analysis (2012–2026)

> *Using 151 manually cataloged TimeGuessr images and a chi-square test to empirically prove when the world switched from filming horizontally to filming vertically.*

![Timeguessr Logo](readme_png_refs/timguessrthumbnail.png)

## Project Overview
TimeGuessr is an online game where you look at historical photographs and try to pinpoint both the exact year and the geographic location on a map where each photo was taken.

I'm a huge fan of the game. Over the course of 3+ years of daily play, I built intuitions about countless trends and patterns in culture, fashion, technology and how those artifacts show up in everyday photographs.

This analysis focuses on one of those intuitions I shared with the TimeGuessr community as a tip:

> [!TIP]
> In the 2010s, the dominant phone orientation when taking a picture is horizontal (i.e, landscape mode). In the 2020s, this reverses and the dominant phone orientation when taking a picture is vertical (i.e., portrait mode).

When I shared this insight back in April 2026, it was just an intuition without proof. This project finally turns that observation into a **statistically-validated data story**. By sampling 151 random Timeguessr photos from 78 different countries and territories over a 20-year timespan, then bounding-box annotating 1,525 people, I can now cite real data to back up my intuitions.

---

## Key Findings & Insights
* **The 2019/2020 Crossover:** The graph of the raw count and the proportional count show a clear crossover point around **2019–2020**, where vertical phone orientation officially overtook horizontal orientation.
* **Global Consistency:** This shift is culturally independent and observable in major metropolitan areas around the world: Asia, Africa, Europe, North America, South America, and Oceania.
* **Subject-Independent:** Phone orientation is largely independent of the subject of the photograph. The most common subject of many TimeGuessr photographs in both the 2010s and 2020s is a parade, festival, or procession, yet the correlation between year and orientation persist. In certain photographs, there is a clear disconnect between the phone orientation and the subject of the photograph (i.e., horizontal filming of a vertical activity or vertical filming of a horizontal activity).

![IMG_050](annotated/IMG_050.jpeg)
<br>
_IMG_050 (Jakarta, Indonesia) uniquely highlights subject-independence: Despite filming a vertical activity, the dominant phone orientation, horizontal filming, strongly correlates with the year (2017) and not the subject of the photograph._

---

## Methodology

1. **Data Collection:**

Custom dataset built in Google Sheets. 151 images were sourced from the 'random mode' in Timeguessr as well as past daily games archived and catalogued by TimeGuessr players on YouTube and Twitch.

   * Built a custom **Python/OpenCV script** (`annotate_photos.py`) to manually catalog and draw color-coded bounding boxes on devices:
     * 🔵 **Blue:** Horizontal / Landscape
     * 🟠 **Coral:** Vertical / Portrait
     * ⚪ **White:** Ambiguous / Traditional Digital Cameras
* Criteria for marking 🔵 Blue or 🟠 Coral:
     * **The device must be visible and must be a phone.** If the image was too blurry, or hands obscured the device, or I could not tell if it was a phone or digital camera, it was marked with a white bounding-box.
     * **The person must be in the act of taking a picture.** There are clear indicators someone is taking a picture: the phone is raised over the head, or there's a two-handed grip framing the phone, or the phone lens is angled towards a clear subject. If it was unclear whether a person was taking a picture or simply looking at their phone screen, it was marked with a white bounding-box.
     * **The phone must be oriented in a clear direction.** If a person's phone was angled at 45° or in the middle of orienting motion, then it was not counted and marked with a white bounding-box.
2. **Data Cleaning:**
  * *Pre-2012 Photographs:* Prior to 2012, the dominant picture-taking device is not a phone but a digital camera. Although I found some valid TimeGuessr photographs from 2006 to 2012, there were too few photos, often with only one person and one phone representing the entire year. This created skewed outliers for those years, so the analysis was narrowed to post-2012, the year phones surpassed digital cameras and became the dominant picture-taking device.
![IMG_134](annotated/IMG_134.webp)
<br>
_IMG_134 (Lhasa, Tibet, China) is the earliest dated photograph in the dataset._   
   * *The Electoral College Problem:* Raw averages were easily skewed by single-person photos (100% horizontal) versus massive stadium crowds.
   * *The Solution:* Switched from arithmetic means to the **median of proportions per year** to establish a robust central tendency completely immune to outlier distortion.
3. **Data Analysis:**
   * **Tableau:** Built an interactive dashboard featuring a global symbol map synced with normalized yearly trend lines and custom visual image tooltips.

---

## Results

---

## Files

* **`Phone Orientation Dataset - Photos.csv`**: Contains the cleaned 151 photograph dataset with years, locations, latitude, longitude, counts, photo description, and source.
* **`annotate_photos.py`**: Interactive OpenCV annotation tool used to manually process image assets.
* **`annotated/`**: High-resolution previews and bounding-box markups of all 151 photographs.
* **`readme_png_refs/`**: Tableau results map and graphs.

