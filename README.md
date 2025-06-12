# What Makes a Game Successful on Steam? Insights from 1000 Games

</br>

## Project Overview

This is a **personal data analysis project** where I explored **what makes players stay or leave** across **1,000 games on the Steam platform**.

Using **real-world data**, I analyzed **game lifecycles**, **genre patterns**, **player reviews**, and the impact of **Early Access** and **content features**. My goal was to identify **behavioral trends** and **success factors** that can help **game studios** and **product teams** optimize **retention** and **player engagement**.

This project combines **exploratory analysis** with **real product thinking** — and is designed as a **practical case** for **business-oriented game analytics**.

</br>

## Tools & Dataset
- **Data collection:** Python (SteamSpy public data)
- **Data cleaning & transformation:** Google Sheets
- **Visualization:** Power BI
- **Dataset:** [SteamSpy public data](https://steamspy.com/api.php), [SteamCharts API scraping](https://steamcharts.com/)

---

</br>

## Section 1 – Game Lifecycle & Market Segmentation

### Business Question
**What types of games sustain player interest over time — and what patterns lead to early drop-off?**  
Understanding lifecycle curves helps studios plan for content updates, predict revenue cycles, and prioritize support efforts.
#

### Market Landscape: Genre Distribution
Before diving into retention behavior, it's critical to understand the genre composition of the Steam market.  
This distribution sets the context for comparing lifecycle trajectories and engagement levels across game types.

![Game Lifecycle Dashboard](plots/distribution_by_genre.jpg)

### Key Findings

- **Action** dominates the market with **668 titles**, indicating high player interest but also intense competition.
- **Adventure (376)** and **Indie (364)** games represent substantial market share, offering opportunities with slightly less saturation.
- **RPG (253)** and **Strategy (209)** maintain a strong presence, often associated with higher engagement and longer playtime.
- **Niche genres** like **MMO, Sports, and Racing** cater to specialized audiences and may offer higher retention in smaller but loyal player bases.


 <br/><br/>
### Distribution of Games by Price

![Game Lifecycle Dashboard](plots/distribution_by_price.jpg)

### Key Findings

- **Mid-range pricing ($10–$29.99)** dominates the market, representing **39.3%** of all titles — indicating a strong standard pricing band for paid games.
- **Budget games ($0.01–$9.99)** account for **24.6%**, highlighting a large segment of low-cost indie or casual games.
- **Free-to-play (F2P)** titles make up a significant **19.2%**, reflecting the popularity of alternative monetization models.
- **Premium-priced games ($30+)** represent **16.9%**, suggesting a smaller but potentially high-margin niche for AAA-style experiences.
  
 <br/><br/>
### Game Ownership by Genre: Average vs. Total Market Share

To understand player distribution across genres, I compare **average ownership per game** with **total market volume**.  
This dual perspective highlights both **individual game success** and **genre-level saturation**, uncovering key differences in competitive dynamics.


**Average Owners per Game by Genre:**
![Game Lifecycle Dashboard](plots/average_owners_by_genre.jpg)

**Sum of Owners by Genre:**
![Game Lifecycle Dashboard](plots/sum_of_owners_by_genre.jpg)


### Key Findings

#### Individual Game Performance
- **Massively Multiplayer (MMO)** games lead with nearly **8M average owners per title**, far exceeding other genres.
- **Action** and **Adventure** follow, but with lower per-game averages due to genre saturation.
- **Sports** and **Casual** genres show unexpectedly strong individual performance despite smaller market share.

#### Total Market Volume
- **Action** dominates in total owners: over **4.5 billion combined**, driven by volume.
- **Adventure** and **Indie** also show high total reach due to large title counts.
- **MMOs**, while strong per title, represent a smaller slice of overall ownership.

#### Market Structure & Strategic Insight

- Some genres have **only a few games**, but each of them has **a lot of players** (like **MMO** and **Sports**).
- Other genres have **many games**, but each game gets **fewer players on average** (like **Action**, **Adventure**, and **Indie**).

This means studios should think differently depending on the genre:

- **MMO games** need long-term support and ways to keep players coming back.
- **Action games** need strong marketing, regular updates, and active communities to stand out in a crowded space.

 <br/><br/>
### Player Satisfaction Analysis: Positive Review Rates by Genre

This chart shows the average % of positive reviews for each genre. It helps us understand how happy players are with different types of games.

![Game Lifecycle Dashboard](plots/average_per_of_reviews.jpg)

### Key Findings

#### Top-Rated Genres
- **Indie games** have the highest player satisfaction — **87.43%** of reviews are positive.
- **Simulation** and **Casual** games also perform well, with over **85%** positive reviews.
- **Strategy, Adventure, and Racing** games stay in the **80%+** range, showing strong overall approval.

#### Lower-Rated Genres
- **Sports games** receive fewer positive reviews (**77.36%**).
- **MMO (Massively Multiplayer)** games rank the lowest, with only **73.31%** of reviews being positive.

#### Review Patterns
- There is a **clear drop** in satisfaction from Indie to MMO games.
- **Competitive and online genres** tend to have lower scores — possibly due to technical issues, high expectations, or balancing problems.


 <br/><br/>
### Player Engagement Patterns: Average vs. Median Playtime by Genre
This chart shows how long players spend in games, using two metrics:
- **Average playtime** = total minutes played divided by number of players  
- **Median playtime** = the middle value, showing what a "typical" player does

Looking at both helps understand how many players really stay active — and how a small group of heavy users can change the numbers.

![Game Lifecycle Dashboard](plots/average_median_playtime.jpg)


### Key Findings

#### Playtime Distribution
- In every genre, **average playtime is much higher than median**.
- This means a few very active players play a lot, while **most players spend less time**.
- The **median playtime shows a more realistic view** of what regular players actually do.

#### Genre-Based Engagement
- **Sports games** have the **highest average playtime** (6.6K minutes), but median is only 3.2K.
- **MMO games** show the biggest gap: average = 3.9K vs. median = 0.5K.
- **Action games** are more balanced: average = 2.2K, median = 0.6K.
- **Indie and Casual games** have the **lowest playtime** in both average and median.

#### Player Behavior Insights
- A clear **“whale effect”** is present — a few very loyal players boost the numbers.
- **Most players play only a little**, no matter the genre.
- **Competitive genres** (like MMO and Sports) have wider gaps between casual and hardcore players.
#

### Business Summary – Section 1: Market & Lifecycle Insights

#### Key Patterns
- **Action games** flood the market, but fight for attention.
- **MMOs** show massive success per title, but with fewer releases.
- **Simulation and Indie** games lead in player satisfaction (85–87%+).
- Playtime data shows a strong **“whale effect”** — most players engage briefly, while a few skew the averages.

#### Takeaways for Game Teams
- **Genre choice defines your strategy**: High-volume genres need standout content and marketing; niche genres benefit from deeper retention design.
- **Don’t trust the average** — median playtime is more realistic for measuring real engagement.
- **Player expectations differ**: Competitive games need support and balance; slower-paced genres need polish and long-term hooks.

---

## Section 2 – Behavioral Patterns: Lifecycle Case Studies

### Business Question

**How do different types of games retain players over time — and what engagement patterns can guide post-launch decisions?**  
Understanding lifecycle curves helps studios plan updates, allocate marketing budgets, and set realistic expectations for player retention.

### Methodology

I selected 4 games with different behavioral profiles:
- **The Sims 4** – a classic example of long-term, stable player retention
- **Hogwarts Legacy** – a highly hyped single-player release with a sharp post-launch drop
- **No Man's Sky** – a rare case of revival through continuous updates after a weak start
- **Stardew Valley** – a slow-burning indie success with organic, sustained growth

Each game is shown with a line chart of monthly player counts (SteamCharts), annotated with major releases or updates where relevant.

#

### Hogwarts Legacy – Hype Spike & Sharp Decline

![Game Lifecycle Dashboard](plots/hogwards.jpg)

*Pattern:* Massive launch spike → rapid drop-off → flat long tail

*What we see:*  
Hogwarts Legacy launched in February 2023 with extremely high engagement (over 500K peak players).  
However, within 2 months, player activity dropped by ~90% and remained consistently low in the following year.

*Possible explanation:*  
This was a highly anticipated, single-player game with limited replay value and no major content updates post-launch. Once players completed the main story, few reasons remained to return.

> **Takeaway:**    
Even massive hype can’t guarantee long-term retention — without post-launch content or community hooks, player interest fades quickly.

### No Man’s Sky – Revival Through Updates

![Game Lifecycle Dashboard](plots/no_mans_sky.jpg)


*Pattern:* Initial collapse → slow comeback → long-term growth through updates

*What we see:*  
After a disappointing launch in 2016, player numbers fell sharply in 2017.  
However, from 2018 onward, we see a steady rise in both average and peak players — driven by a continuous stream of major updates and improvements.

*Possible explanation:*  
The developers committed to rebuilding the game post-launch with free expansions, feature reworks, and strong communication — eventually rebuilding player trust and engagement.

> **Takeaway:**  
A weak launch doesn’t mean failure — long-term player retention is possible through consistent updates and community care.

### The Sims 4 – Long-Term Growth & Steady Engagement

![Game Lifecycle Dashboard](plots/sims.jpg)

*Pattern:* Consistent year-over-year growth with strong retention

*What we see:*  
Since 2020, The Sims 4 has shown stable growth in both average and peak players.  
Engagement increases each year, with no major dips — a rare example of a long-running title gaining momentum over time.

*Possible explanation:*  
Frequent content packs, seasonal events, strong community support, and modding culture keep players coming back. The game's open-ended nature supports long-term play.

> **Takeaway:**  
Steady growth is possible when games are built for longevity — with regular updates and systems that support ongoing engagement.

### Stardew Valley – Organic Growth & Community-Driven Longevity

![Game Lifecycle Dashboard](plots/valley.jpg)

*Pattern:* Gradual long-term growth → major resurgence post-2023

*What we see:*  
After a modest launch in 2015, Stardew Valley steadily gained players over time.  
A massive spike in 2023–2024 suggests renewed interest — possibly due to major updates, platform expansions, or social buzz.

*Possible explanation:*  
The game’s relaxing gameplay, strong word of mouth, active modding scene, and continued developer support built a loyal player base.  
Viral moments and re-releases helped reintroduce the game to new audiences.

> **Takeaway:**  
Games don’t need explosive launches to succeed — slow, steady growth powered by community and ongoing updates can lead to long-term success.










