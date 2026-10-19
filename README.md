# Landscape to Portrait Orientation Shift: A TimeGuessr Analysis (2012–2026)

> *Using 151 manually-cataloged TimeGuessr images, Exploratory Data Analysis in Tableau, and a chi-square test to empirically prove when the world switched from filming horizontally to filming vertically.*

![Timeguessr Logo](readme_png_refs/timguessrthumbnail.png)

## Project Overview
TimeGuessr is an online game where you look at historical photographs and try to pinpoint both the exact year and the geographic location on a map where each photo was taken.

I'm a huge fan of the game. Over the course of 3+ years of daily play, I built intuitions about countless trends and patterns in culture, fashion, technology and how those artifacts show up in everyday photographs.

This analysis focuses on one of those intuitions I shared with the TimeGuessr community as a tip:

> [!TIP]
> In the 2010s, the dominant phone orientation when taking a picture is horizontal (i.e, landscape mode). In the 2020s, this reverses and the dominant phone orientation when taking a picture is vertical (i.e., portrait mode).

When I shared this insight back in April 2026, it was just an intuition without proof. This project finally turns that intuition into **statistical proof**. By sampling 151 random Timeguessr photos from 78 different countries and territories over a 20-year timespan, then bounding-box annotating 1,525 people, I can now cite real data to back up my intuitions.

---

## Key Findings & Insights
* **The 2019/2020 Crossover:** The graph of the raw count and the proportional count show a clear crossover point around **2019–2020**, where vertical phone orientation officially overtook horizontal orientation.
* **Global Consistency:** This shift is culturally independent and observable in major metropolitan areas around the world: Asia, Africa, Europe, North America, South America, and Oceania.
* **Subject-Independent:** Phone orientation is largely independent of the subject of the photograph. The most common subject of many TimeGuessr photographs in both the 2010s and 2020s is a parade, festival, or procession, yet the correlation between year and orientation persist. In certain photographs, there is a clear disconnect between the phone orientation and the subject of the photograph (i.e., horizontal filming of a vertical activity or vertical filming of a horizontal activity).

![IMG_050](annotated/IMG_050.jpeg)
<br>
_IMG_050 (Jakarta, Indonesia) uniquely highlights subject-independence: Despite filming a vertical activity, the dominant phone orientation is horizontal, which strongly correlates with the year (2017) and not the subject of the photograph._

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
  * *Pre-2012 Photographs:* Prior to 2012, the dominant picture-taking device is not a phone but a digital camera. Although I found some valid TimeGuessr photographs from 2006 to 2012, there were too few photos, often with only one person and one phone representing the entire year. This created skewed outliers for those years, so the analysis was narrowed to post-2012, the year phones started to surpass digital cameras and became the dominant picture-taking device.

![IMG_134](annotated/IMG_134.webp)
<br>
_IMG_134 (Lhasa, Tibet, China) is the earliest dated photograph in the dataset._

3. **Data Analysis:**
   * *The Electoral College Problem:* Each year contains a wide range of photographs. Some have one or two phones while others have 30+. How do you balance giving each country and location equal weight to truly capture the global big picture trend while also being careful not to skew the data in favor of photographs with one or two people?

![IMG_037](annotated/IMG_037.jpeg)
<br>
_IMG_037 (Sanandaj, Iran) contains 41 horizontal and 8 vertical This single location could drown out the other 2017 photographs if we used a raw total count alone._


![IMG_037](readme_png_refs/Raw_Phone_Count.png)
<br>
_Raw phone count shows that horizontal count is consistently above vertical through the 2010s and the reverse is true during the 2020s. However, the total counts for each year are skewed by large crowds._

To correct the effect of large crowds, I normalized each photograph by assigning each a proportional calculation (e.g., 41 horizontal and 8 vertical calculates to a score of 0.84 for horizontal and 0.16 for vertical) and then averaging the photographs in each year.

![IMG_037](readme_png_refs/Proportional_Count.png)
<br>
_Proportional count graph._

However, this creates the classic Electoral College problem where a picture with 2 people carries as much weight as a picture with 40. Unlike the tricky problem of representational politics, this problem had a simple solution: find the central value least affected by either outlier, i.e., the median.

![IMG_037](readme_png_refs/Proportional_Count.png)
<br>
_Proportional count graph with median instead of the mean._

---

## Results

---

## Files

* **`Phone Orientation Dataset - Photos.csv`**: Contains the cleaned 151 photograph dataset with years, locations, latitude, longitude, counts, photo description, and source.
* **`annotate_photos.py`**: Interactive OpenCV annotation tool used to manually process image assets.
* **`annotated/`**: High-resolution previews and bounding-box markups of all 151 photographs.
* **`readme_png_refs/`**: Tableau results map and graphs.

