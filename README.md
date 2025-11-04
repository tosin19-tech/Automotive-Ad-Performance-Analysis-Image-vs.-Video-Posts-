# Automotive-Ad-Performance-Analysis-Image-vs.-Video-Posts-

## Project Objective
To evaluate the performaance difference between image and video ad posts in terms of engagement rate and conversion rate, and determine whether one format significantly outperforms the other.
The analysis aims to answer: 
1. Which ad format (image or video) drives higher engagement and conversion?
2. Is there a statistically significant difference between their conversion rates?
3.  How stable and predictable is the relationship between engagement and conversion for each format?
4.  To measure campaign profitability through ROI and cost-perclick (CPC) analysis, incorporating discount strategies and estimated net profit to assess marketing efficiency.

A. Descriptive Analysis (Power BI Dashboard) 
1. Overview
A Power BI dashboard was created to visualize the main performance indicators:
* Engagement Rate
* Conversion Rate
* Impressions
* Post Type Count (Image vs. Video)
  It also integrates financial metrics such as:
* ROI,
* Net Profit after discount,
* Sales, Total ad spend,
* Cost per Click (CPC), and
* Total Clicks to evaluate campaign profitability. 

2. Key Observations
* Video posts: 25 total
* Image posts: 17 total
* Image posts had higher impressions (visibility) but lower conversions rates.
* Video posts achieved higher peak conversions, but their performance varied widely.
* Best-Performing Days (Impressions & Conversions)
  - Mondays recorded the highest visibility and conversions (~2,004 impressions / 27 conversions), followed by Thursday (1,350/ 15) and Fridays (1,120/ 15).
  - This indicates early-week campaigns tend to attract the largest audineces and drive the most conversions.
* Best-Performing Times of Day:
  - 11 a.m. showed the peak engagement window (~1,743 impressions / 21 conversions), followed by 9 a.m. (887/ 12).
  - Morning hours appear to  be the optimal posting times for maximizing visibilty and conversions.
* Conversion Trends Over Time (Video vs Image):
  - Video posts started strong at 0.03 conversions rate in wWeek 1 but dropped to around 0.01 by Week 2, before spiking again to 0.04 in Week 4.
  - Image posts began lower to 0.01, peaked at 0.02 in Wekk 4, and fell to 0.00 by Week 6.
  - Both formats show mid-campaign spikes followed by declines, suggesting performance fatigue or reduced engagement over time.
 
* Financial Metrics
 - A 5% discount strategy improved sales without hurting profitability, maintainig ROI +57%.
 - Despite moderate ad spend, net profit reached ₦2.35M, showing strong return efficiency.
 - Profitability remained positive, suggesting potential to scale ad investment while keeping ROI stable. 

  3. Diagnostic Insights
  * Some video posts performed exceptionally well, suggesting content quality or creative factors may influence conversion efficiency.
  * ROI remained strong (+57%) due to efficient CPC (₦1,355) and stable conversion rate despite a 5% discount. The discount increased total sales volume to 13,
    compensating for lower-per-unit margins.
 
B. Statistical & Inferential Analysis (Python) 
1. Relationship Between Engagement and Conversion
A scatterplot engagement rate vs. conversion rate was created for both post types.

Interpretation: 
* There is a clear positive correlation between engagement and conversion rates.
* Image posts are tightly grouped along the trend line and therefore more predictable conversion behavior.
* Video posts show greater spread and higher variability, indicating that some perform very well while others underperformed.

2. Hypothesis Testing
Null Hypothesis: There is no significant difference - Video posts perform better than image posts.
Alternative Hypothesis: There is a significant difference- Video posts perform better than image posts.

Normality Test (Shapiro-Wilk)
* Both image and video conversion rates were not normally distributed (p < 0.05), therefore Non-parametric test required.

Mann-Whitney U Test 
* p-value = 0.122. It fails to reject the null hypothesis  and No significant difference in conversion rates between image and video posts.

3. Interpretation of Statistical Results
Although descriptive analysis showed that videos achieved higher average conversion, the statistical test proved that the difference is not significant.
Why this makes sense:
* Sample imbalance: Fewer video posts reduce the power to detect significance.
* High variance in videos: Wide spread inflates variance, masking true effects.
* Stability of image posts: More consistent, with points closer to the regression trend line.
* Visisbility differences: Image gained more impressions but didnt translate proportionally into conversions.
* External fsctors: Content quality, timing, and audience targeting likely affected conversion outcomes more than format type.

4. Regression Analysis Summary
* Linear regression between engagement and conversion rates show a positive slope.
* R sqaure value indicates that the engaement rate can explain a portiion of conversion performance.
* Image posts exhibit less deviation from the trend amd is consistent and predictable.
* Video posts show wider deviations and is more volatile but with higher potential.

5. Project Conclusion
* There is no statistically significant difference in conversion rates between image and video posts.
* Videos may yield higher peaks in conversion, but images offer more predictability and stability.
* Higher engagement generally leads to higher conversion, but the relationship is more stable for image posts and less predictable for video posts.

6. Recommnendation
   * Schedule Key Campaigns on Mondays (and early in the Week). Ads laucnhed on Mondays consistently drive the highest reach and conversions. 
   * Post during Peak Hours (9-11 a.m.). Morning hours show the strongest visiblity and engagement. Ad delivery should be optimized around these windows.
   * Since conversion rates tend to dip after Week 4, new creatives or audience retargeting should be introduced to prevent fatigue and sustain conversions. 
   * Adopt a Mixed Content Strategy: Use image posts for consistent, predictable engagement, while leveraging video posts for experimental and high-impact campaigns.
   * Conduct Deeper Content-Level Analysis: Since formats show different engagement behsviours, further analysis should focus on creative elements such as :
     - Type of visuals (e.g., product-focued vs. lifestyle-focused)
     - Presence of male vs. female characters.
     - Video quality, lighting, and background aethestics.
     - Messaging tone (educational, emotional, or promotional).
   * Run A/B Tests on Creative Variations: Test different combinations - such as gender of presenter, color tone, or ad framing to determine which creative factors
     drive higher engagement and conversion within each post type.
   * Focus on Improving Engagement Rate: Engagement rate strongly correlates with conversion rate, especially for image posts.
     Therefore, increasing engagement through better visuals, captions, and call-to-actions will likely boost conversions.
   * Investigate Variability in Video Performance: The erratic conversion performance of videos suggests that content quality or audience targeting may play a major role.
  
   7. Recommendation (Financial metrics)
   * Maintain moderate discount strategy.
   * Optimize ad spend based on CPC.
   * Do more experiment with A/B campaigns: test different ad formats or messaging style to determine which combinations sustain high ROI with lower ad spend.
     Future campaigns should analyze why some videos outpeform others, for instance, by tracking engagement duration, hook strength, or viewer retention. 
 

   
  
