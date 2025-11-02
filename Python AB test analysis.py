#!/usr/bin/env python
# coding: utf-8

# #### Import Libraries (Data Loading & Inspection)

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

import warnings 

warnings.filterwarnings("ignore")


# #### Load datset

# In[2]:


df = pd.read_csv("AB TEST VIDEO IMAGE STIMULATED.csv")


# ## Data Cleaning and Transformation

# #### Observe the columns and first few rows of the tables

# In[3]:


df.head()


# #### Data types of each columns

# In[4]:


df.dtypes


# #### Check for duplicates with respect to Post ID

# In[5]:


df.duplicated(subset= 'Post ID').sum()

-The result shows there are 2 duplicate entries. 
# #### Drop duplicate entries

# In[6]:


df = df.drop_duplicates(subset = 'Post ID')


# #### Convert Post Date column to DateTime Format

# In[7]:


df['Post Date'] = pd.to_datetime(df['Post Date'])


# ## Basic Explorative Analysis

# In[8]:


df.describe()

-- INTERPRETATION
-Mean(0.013) > Median(0.0045) - Right skeweness (+vely skewed)
This means that most conversion rates are low, but there are a few very high conversion rates pulling the Mean upward. 
-STD (0.021) & CV (1.59)
CV measures relative variability: how spread out the data is compared to the mean. A CV > 1.0 indicates high variability,
meaning conversion rates differ widely across posts.
So the conversion performance is not consistent, meaning that some posts convert well, whole others barely convert. 
- The maximum(0.09) is far higher than Q3 (0.019), confirming a few outliers with strong performance.

# In[9]:


median_conversions = df['Conversion Rates'].median()
median_conversions

Statistically, the mean> median, meaning the data in review could be right skewed. 
To confirm this, we use a histogram and a Box plot
# #### Comparing Conversion rates of  VIDEO and IMAGE performance

# In[10]:


plt.figure(figsize=(8,5))
sns.histplot(data=df,x ='Conversion Rates', hue = 'Post Type', multiple = 'dodge', bins =7, edgecolor = 'k', kde= True)
plt.title('Distributiom of Conversion Rate for Image vs Video Posts')
plt.xlabel('Conversion Rates')
plt.ylabel('Count')
plt.show()

-- INTERPRETATION
The histogram shows that both image and video posts have right-skewed conversion distributions, meaning most of both posts achieved low conversions.
However, video posts show a longer right tail, extending up to 0.08 compared to only 0.02 for image posts. 
This indicates that while most video posts perform modestly, a few achieve exceptionally high conversion rates, suggesting higher performance 
potential.
# In[11]:


df.columns


# #### Check if the categorical variable have appropriate number of levels

# In[12]:


df_cat= df[['Post Day', 'Post Type']]
df_cat.nunique()


# #### Check if the categorical variable have appropriate levels

# In[13]:


for i in df_cat.columns:
    print(i.upper(), ":", df_cat[i].unique())


# In[14]:


df_cat=df[['Post Day', 'Post Type', 'Conversion Rates', 'Time of Post (hours)']]


# #### Univariate Analysis

# In[15]:


variable = 'Conversion Rates'

plt.figure(figsize=(8,6))
# Histogram
plt.subplot(1,2,1)
sns.histplot(x= variable, data=df)
plt.title(f'Histogram-{variable}')

# Box plot
plt.subplot(1,2,2)
sns.boxplot(y= variable, data=df)
plt.title(f'Boxplot-{variable}')
plt.tight_layout()
plt.show()

-- INTERPRETATION
- The histogram and Box plot show right-skewed distribution: most  conversions are low (0-0.03) with a few high outliers (0.05-0.09). 
This indicates that the data may not be normally distributed, so i will check normality before choosing the appropriate statistical
test for image vs. video posts.
Since the conversion data is right-skewed and may violate normality assumptions, i will perform a p-value test to determine whether
a t-test or a non-parametric test is appropriate.
--THE LOGIC FOR THE NEXT STEP--
--Check the data distribution (Conversion Rate) using a violin, histogram or boxplot if the data is symmetric or skewed.  
Use it to identify outliers as well (values far from Q1/Q3 or above/below whiskers).
--Decide the next step based on distribution.
* If symmetric and roughly normal, you can likely use a t-test directly. 
* If right- or left-skewed/ not normal, you consider one of these:
* Outlier treatment:remove extreme values (e.g., >75th percentile) or cap them. 
* Data transformation: Log, square root, etc., to reduce skeweness.
* Non-oarametric test: skip transformations and use Mann-Whitney U test instead of t-test. 

--P-VALUE CHECK BEFORE HYPOTHESIS TESTING--
* The p-value tells you whether you can assume normality:
- p>0.05, data is roughly normal and t test is okay.
- p<= 0.05, data not normal and non-paramwtric test preferred. 
# In[16]:


variable = 'Post Type'
plt.figure(figsize=(6,4))

# Count Plot 
plt.subplot (1,2,1)
sns.countplot(x=variable, data=df_cat)
plt.title(f'Count Plot- {variable}')
plt.xticks(rotation=45)

# Pie Chart
plt.subplot (1,2,2)
counts = df_cat[variable].value_counts()
plt.pie(counts, labels= counts.index, autopct= '%0.2f%%')
plt.title(f'Pie Chart -{variable}') 

# Adjust Layout
plt.tight_layout()


# Show the plots
plt.show()
        


           

-The result shows that the dataset contains more video posts than image posts, indicating that the audience were exposed to more Video ads than Image ads overall during the period analyzed. 
-So we have more videos than images, so before concluding that videos performed better, we must compare conversion rates rather than raw counts.
# In[17]:


variable = 'Post Day'
plt.figure(figsize=(6,4))

# Count Plot
plt.subplot(1,2,1)
sns.countplot(x=variable, data= df_cat, order= df_cat['Post Day'].value_counts().index)
plt.title(f'Count Plot- {variable}')
plt.xticks(rotation = 90)

# Pie Chart
plt.subplot(1,2,2)
counts=df_cat[variable].value_counts()
plt.pie(counts, labels=counts.index, autopct= '%0.2f%%')
plt.title(f'Pie Chart - {variable}')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

--INTERPRETATION 
-The count plot reveals that audience engagement peaks on Mondays, with posts being viewed over 12 times on average. 
This indicates tha Mondays are the most active days for audience exposure to ads or posts. 
The Pie chart supports this finding, approx. 30.95% of all impressions occur on Mondays, making it the dominant day of audience visibility. 
This result can guide optimal psoting or ad scheduling strategy. 
# In[ ]:





# In[18]:


variable = 'Time of Post (hours)' # Note that, 1 means 1pm, 2 means 2pm, 10 means 10am, etc.
plt.figure(figsize=(6,4))

# Count Plot
plt.subplot(1,2,1)
sns.countplot(x=variable, data= df_cat, order= df_cat['Time of Post (hours)'].value_counts().index)
plt.title(f'Count Plot- {variable}')
plt.xticks(rotation = 90)

# Pie Chart
plt.subplot(1,2,2)
counts=df_cat[variable].value_counts()
plt.pie(counts, labels=counts.index, autopct= '%0.2f%%')
plt.title(f'Pie Chart - {variable}')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

--INTERPRETATION
-The count plot and Pie chart reveal that audience visibilty varies significantly based on the time of post or ad displayed.
The highest visibilty occured around 9 am, accounting for approximately 19.05% of the total impressions. This suggests that audience
engagement is strongest during the early hours of the day. 
# In[ ]:





# In[19]:


variable = 'Impressions'
plt.figure(figsize=(6,4))

# Histogram
plt.subplot(1,2,1)
sns.histplot(x=variable, data = df)
plt.title(f'Histogram - {variable}')

# Pie Chart
plt.subplot(1,2,2)
sns.boxplot(y=variable, data=df)
plt.title(f'Boxplot- {variable}')

 # Adjust layout
plt.tight_layout()
# Show plots


# REASON FRO PLOTTING THE HISTOGAM AND BOXPLOT
# They were plotted to examine the distribution and spread of exposure levels across all posts. 
# The histogram helps to identify whether the data is right-skewed distribution or left skewed.  A right skewed means most posts have low impressiosn.
# while a few post have very high exposure, suggesting an unequal visibility across content. 

# The box plot complements this by showing the median number of impressions, interquartile range, and possible outliers. 

-- INTERPRETATION
- The box plot for Impressions shows that 50% of all posts received between 20 to 190 impressions, while a median of around 100.
This means that half of our posts generally fall within this range, representing moderate audience exposure. (This depends on our target impression).
The lower whisker(~20) and upper whisker (~350) indicates the spread of impressions is fairly wide, however no outlier where observed. 
The histogram is right skewed, meaningmost posts had low impressions while only a few achieved high impressions. 

# ### Bivariate Analysis
-- We want to check how Post type (video vs image) relate to whether users converted or not, or how conversion rate differ
by post type using a Violin Plot
# In[20]:


sns.violinplot(x='Post Type', y='Conversion Rates', data= df, palette = 'muted')

-- INTERPRETATION 
The violin plot comparing rates across post types shows that video posts achieved higher and more varied conversion rates than Image posts. 
Video posts have a wider spread and a longer right tail indicating that while most videos converted around 1%, a few performed exceptionally well 
up to 12%. 
In contrast, the image posts are more tighly distributed around very low conversion rates (mostly below 1%), suggesting fewer high-performing images. 
Overall, the visual evidence supports the idea that videos tend to drive higher conversions. 
# #### Comparing Post Day and Conversion Rates

# In[21]:


plt.figure(figsize=(12,4))
sns.boxplot(x='Post Day', y='Conversion Rates', data=df, order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.show()

--INTEPRETATION
1. Monday shows the widest spread in conversion rates with multiple outliers reaching up to 0.08-0.09 (outliers), much higher than other days.
However, the median is around 0.00, meaning that most posts on Monday still performed poorly overall. So, few posts were highly successful, but most were not. 
2. Tuesday's distribution is tighly compressed around 0.00, indicating very low and consistent conversion rates. The single outlier (~0.02) 
one or two posts performed better than usual, but overall conversions were minimal. 
3. Wednesday shows a slighly higher and more stable conversion pattern with box extending roughly from 0.015 to 0.04 and median near 0.02.
This means that 50% of Wednesday's posts achied conversion rates between 1.5% and 4%, showing more consistency and higher central performance
than Monday and Tuesday. 

--Takeaway
-Monday has the potential for high conversions(outliers), but very inconsistent, maybe due to variable content quality or timing. 
-Wednesday shows steady and moderate conversions,making it potentially the most reliable posting day. 
# In[22]:


plt.figure(figsize=(12,6))
sns.boxplot(x='Time of Post (hours)', y= 'Conversion Rates', data=df)
plt.show()

-- Summary
-9AM- Conversions were relatively high and consistent, with 50% of the values(IQR) between 0.00 and ~0.022. The upper whisker extends 
to ~0.054, suggesting occasional spikes in conversion performance.  
This indicates that morning posts around 9am tend to perform relaible well, with occasional strong results. 
10AM- The conversion rate range was narrower (up to ~0.02), showing lower variability and moderate perofrmance overall. It is stable but few conversions.
11AM- This time had visible outlier(~0.09), which represents one unusual high conversion event. Its promising but not consistent. 
12PM - 2PM - The box plots for these hours are concentrated between 0.00 and ~0.025, with upper whiskers reaching 0.06. This indicates steady and moderately strong conversion activities. 

9AM, 1PM and 2PM are the more consistent hours with conversion rates
# In[23]:


# SCATTER PLOT OF ENGAGEMENT RATE AND CONVERSION RATE


plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Engagement Rate',y='Conversion Rates', hue = 'Post Type', alpha=0.7)
sns.regplot(data=df, x='Engagement Rate',y='Conversion Rates', scatter= False, color='black', 
            line_kws={'linewidth':1})
plt.title('Relationship Between Engagement Rate and Conversion Rate')
plt.xlabel('Engagement Rate')
plt.ylabel('Conversion Rate')
plt.show()

-- SCATTER PLOT INTERPRETATION OF ENGAGEMENT RATE VS CONVERSION RATE
* The scatter plot shows a clear positive correlation between engagement rate and conversion rate. 
This means that posts with higher engagement rates tend to drive more conversions. 
* The points for image posts are more tightly grouped along the trend line, indicating that images deliver more consistent conversion outcomes. 
* In contrast however, video posts display a wider spread of values-some perform exceptionally well, while others underperformed. 
* Video posts showed greater variability. 
* Overall, higher engagement generally tend to lead to higher conversion rates , but the effect is more stable for images and more unpredictable 
for videos. 

# ## Inferential / Statistical Testing
-- Null Hypothesis: There is no significant difference in conversion rates between image and video posts.
-- Alternative Hypothesis: There is a significant difference in conversion rates between image and video posts, Meaning that
video performs better than image. 

# In[ ]:




Since the conversion data is right-skewed and may violate normality assumptions, i will perform a p-value test to determine whether
a t-test or a non-parametric test is appropriate.
--THE LOGIC FOR THE NEXT STEP--
--Check the data distribution (Conversion Rate) using a violin, histogram or boxplot if the data is symmetric or skewed.  
Use it to identify outliers as well (values far from Q1/Q3 or above/below whiskers).
--Decide the next step based on distribution.
* If symmetric and roughly normal, you can likely use a t-test directly. 
* If right- or left-skewed/ not normal, you consider one of these:
* Outlier treatment:remove extreme values (e.g., >75th percentile) or cap them. 
* Data transformation: Log, square root, etc., to reduce skeweness.
* Non-oarametric test: skip transformations and use Mann-Whitney U test instead of t-test. 

--P-VALUE CHECK BEFORE HYPOTHESIS TESTING--
* The p-value tells you whether you can assume normality:
- p>0.05, data is roughly normal and t test is okay.
- p<= 0.05, data not normal and non-paramwtric test preferred. --Shapiro-Wilk normality test for each group since the goal is to compare conversion rates betwen image and video posts.
This will tell us whether the conversion rates in each group are approximately normal, and from there we will decide which hypothesis
test to run (t-test or Mann-Whitney U )
# ### Shapiro-Wilk normality test

# In[24]:


import scipy.stats as stats
# Separate conversion rates by post type
image_conversion = df[df['Post Type'] == 'Image']['Conversion Rates'].dropna() 
video_conversion= df[df['Post Type']=='Video']['Conversion Rates'].dropna()

# Shapiro-Wilk normality test for image posts
stat_image, p_image = stats.shapiro(image_conversion)
print(f"Image posts: Shapiro-Wilk stat={stat_image:.3f}, p-value={p_image:.3f}")
if p_image>0.05:
    print("Image conversion rates are approximately normal") 
else: 
    print("Image conversion rates are not normal")

# Shapiro-Wilk normality test for Video posts
stat_video, p_video = stats.shapiro(video_conversion)
print(f"Video posts: Shapiro-Wilk stat={stat_video:.3f}, p-value={p_video:.3f}")
if p_video>0.05:
    print("Video conversion rates are approximately normal") 
else: 
    print("Video conversion rates are not normal")

    

    

--INTERPRETATION--
Both image abd video conversion rates are not normally distributed (Shapiro-Wilk p<=0.05).
Therefore, we will use Mann-Whitney U test (Non-parametric test) to compare conversion
# ### Run a Mann-Whitney U test (Normality Check)
# ##### Purpose: Compare conversion rates between image and video posts since the data is not normally distributed.
# ##### If p-value < 0.05, then reject the Null Hypothesis: meaning there is a significant difference, supporting that video postsperform better. 
# ##### If p-value >= 0.05, fail to reject the Null Hypothesis and no significant difference between image and video posts.

# In[25]:


import scipy.stats as stats
# Separate conversion rates by post type
image_conversion = df[df['Post Type'] == 'Image']['Conversion Rates'].dropna() 
video_conversion= df[df['Post Type']=='Video']['Conversion Rates'].dropna()

# Mann-Whitney U test
stat, p_value = stats.mannwhitneyu(image_conversion, video_conversion, alternative='two-sided')

# Print results
print(f"Mann-Whitney U Test Statistic:{stat:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in the conversion rates between image an video posts.")
else:
    print("Fail to reject the null hypothesis: No significant difference in conversion rates between image and video posts.")


# #### PROJECT CONCLUSION: Image vs. Video Post Conversion Rates
--Our analysis shows that there is no statistically significant difference in conversion rates between image and video posts.
This indicates that, overall, neither format outperforms the other in driving conversions
# In[ ]:





# #### Export cleaned data to desk top

# In[26]:


df.to_csv('C:/Users/RUTH/Python files/data.csv', index = False)


# In[ ]:





# In[28]:


get_ipython().system('jupyter nbconvert --to script "Python Analysis AB test analysis.ipynb"')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




