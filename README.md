# Exploratory Data Analysis

## 1. Daily Orders Trend (Grey and Blue Gloves)

###  Observation:
-  **Orders for blue gloves generally exceed those for grey gloves**, indicating a higher market demand for blue gloves.
-  **Significant spikes** in orders were observed for both glove types on specific days, possibly due to **special orders** or **seasonal trends**.

###  Actionable Insight:
-  **Adjust production focus** towards blue gloves to better meet market demand.
-  **Investigate peak days** to identify potential recurring patterns, such as **seasonal** or **event-driven demand**.
  
  ![Daily_Orders_Trend](https://github.com/user-attachments/assets/7a0de749-f70d-48d1-b891-fc8bf25e57be)


## 2. Daily Production Trend (Grey and Blue Gloves)

###  Observation:
-  **Grey glove** production appears more **stable**, close to the 8000-unit capacity most days.
-  **Blue glove** production **fluctuates more**, with occasional dips below 8000.

###  Actionable Insight:
-  **Production planning for blue gloves** needs optimization to avoid **underproduction** during high-demand periods.

![Daily_Production_Trend](https://github.com/user-attachments/assets/82eaa591-49c0-4a46-87ef-a53911d3912f)


## 3. Daily Delivery Trend (Grey and Blue Gloves)

###  Observation:
-  Orders for **blue gloves** often surpass those for grey gloves, indicating they are generally in **higher demand**.
-  **Both grey and blue gloves** show **fluctuating daily orders**, with blue gloves exhibiting more **pronounced spikes**.

###  Actionable Insight:
-  Prioritize **production and inventory management** for **blue gloves** to accommodate higher and more unpredictable demand.

![Daily_Delivered_Trend](https://github.com/user-attachments/assets/f5fe15fc-1b13-486a-ba6a-343940940cbf)


## 4. Dispatch Efficiency (Grey vs. Blue Gloves)

###  Observation:
-  **Dispatch efficiency for grey gloves often exceeds 100%**, indicating the firm is utilizing inventory to meet demand.
-  **Blue gloves** also show **high dispatch efficiency**, but with greater variability

###  Actionable Insight:
-  **Maintain a balance between inventory and dispatch** to avoid **stockouts** for blue gloves.
-  Analyze days with exceptionally **high dispatch efficiency** for potential operational bottlenecks.

![Dispatch Efficiency](https://github.com/user-attachments/assets/fd7a493f-5a9d-4a12-90be-e845f17c8697)


## 5. Production Efficiency Comparison

###  Strong Relationships:
-  

###  Actionable Insight:
-  Align **blue glove production** more closely with orders to reduce waste and inefficiencies.

![Production_Efficiency](https://github.com/user-attachments/assets/886bf54c-6dec-4be4-bdbe-a62e5e78e7f4)

## 6. Correlation Analysis

###  Strong Relationships:
-  High correlation between **Gloves Ordered** and **Gloves Produced** suggests production generally aligns with demand.
-  Strong correlation between **Gloves Produced** and **Gloves Delivered** indicates an efficient supply chain, but this may not be true on outlier days.

### Actionable Insight:
-   Investigate weak correlations (if any) to understand operational inefficiencies, such as underproduction or over-delivery.

![Correlation](https://github.com/user-attachments/assets/cd9c8c98-f90b-46d6-9050-1acbd8200b96)

## 7. Monthly Trends

### Orders:
-   **Grey gloves** show consistent demand, while **blue gloves** have periods of higher demand spikes.
-   Peaks in **blue glove** orders suggest seasonal or event-driven patterns.

### Dispatch Efficiency:
-   Efficiency improves over time, suggesting better alignment between production and dispatch.

### Actionable Insight:
-   Use monthly trends to prepare for demand surges and ensure adequate inventory.


![Monthly_Average_Orders](https://github.com/user-attachments/assets/541ff021-ba43-4dd9-a031-f6f47b1caf60)

![Monthly_Average_Dispatch_Efficiency](https://github.com/user-attachments/assets/eba50773-cb2b-4567-8854-b9740ff27ac4)

## 8. Outlier Detection for Dispatch Efficiency

### Grey Gloves:
-   Days with very high dispatch efficiency could be over-delivery or inventory clearing.

### Blue Gloves:
-   Fewer outliers, indicating more stable dispatch, but high values on certain days suggest possible operational anomalies.

### Actionable Insight:
-   Investigate outliers to improve consistency and operational efficiency.

![Dispatch_Efficiency_outliers](https://github.com/user-attachments/assets/75dfd7cf-d534-4da5-8a1c-90e2c80b30dd)

## 9. Outlier Detection for Production Efficiency

### Grey Gloves:
-   Days with very high production efficiency suggest overproduction, likely due to overestimating demand or attempting to catch up from previous underproduction.

### Blue Gloves:
-   Fewer outliers in production efficiency suggest a more stable and predictable production process.

### Actionable Insight:
-   Investigate the reasons behind overproduction on outlier days and evaluate whether it aligns with demand or leads to surplus stock.
-   Adjust forecasting models to better predict demand and prevent unnecessary overproduction.

![Production_Efficiency_Outliers](https://github.com/user-attachments/assets/4f6e8e85-7386-46c1-a160-222919e41d14)

## 10. Delivery Gap Analysis

### Positive Gaps (Ordered > Delivered):
-   Indicates unmet demand, highlighting missed revenue opportunities.

### Negative Gaps (Delivered > Ordered):
-   Suggests over-delivery, potentially leading to stock depletion or higher costs.

### Actionable Insight:
-   Minimize delivery gaps by better-aligning production and dispatch with actual orders.


![Delivery_Gap_Over_Time](https://github.com/user-attachments/assets/f7c8e411-e77a-43de-8ba0-87f5180df099)

## 11. Distribution of Dispatch Efficiency

###  Observation:
-  **Grey gloves** dispatch efficiency is more evenly distributed, with values clustering around the mid-range.
-  **Blue gloves** dispatch efficiency shows higher peaks, indicating periods of high efficiency.

###  Actionable Insight:
-  The higher variability for **blue gloves** might point to inconsistent dispatch processes, which could be addressed with better planning and coordination.

![Distribution_of_Dispatch_Efficiency](https://github.com/user-attachments/assets/8ffd7ff9-70ab-4eb4-bd45-0fcc0f7b8c32)

## 12. Distribution of Production Efficiency

###  Observation:
-  **Grey gloves** production efficiency is concentrated around higher values, indicating consistent production practices.
-  **Blue gloves** production efficiency has a wider spread, with more occurrences of lower efficiency.

###  Actionable Insight:
-   **Blue gloves** production processes may need optimization to reduce inefficiencies and align production closer to demand.

![Distribution_of_Production_Efficiency](https://github.com/user-attachments/assets/fcc7a774-4e6f-4621-9a27-84eaf911e5fd)

## 13. Comparison of Dispatch and Production Efficiencies

###  Observation:
-  **Grey gloves** show a stronger positive relationship between dispatch and production efficiency, suggesting a well-synchronized process.
-  **Blue gloves** scatter widely, indicating misalignment between production and dispatch.

###  Actionable Insight:
-   Focus on improving the synchronization of production and dispatch processes for blue gloves to achieve better overall efficiency.

![Dispatch_Efficiency_vs_Production_Efficiency](https://github.com/user-attachments/assets/44c96281-8047-470b-96ca-99d09de793f9)
