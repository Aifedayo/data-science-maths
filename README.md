# data-science-maths

Understanding the concept of mean and median usage:
- [x] Used for Descriptive analysis
- [x] Data cleaning (Filling NA Values)

Outlier is a datapoint that is very different from the rest of the data points

Percentile shows the part where the data lies:
- [x] 50th percentile means 50 percent of the data have values less than or equal to what is on the 50th percentile

| Name | Score |
| ---- |-------|
| Akeem | 50    |
| Zainab | 68    | 
| Abdullah | 76    |
|Abdurrahman | 77    |
| Abdurraheem | 85    |
| Abdulmalik | 87    |

In the above dataset:
- the 100th percentile is `Abdulmalik 87`
- the 0th percentile is `Akeem 50`
- the 50th percentile is between `Abdullah 76 and Abdurrahman 77`
- the 25th percentile is `Akeem 50 and Zainab 68` : by multiplying the total number of our datasets + 1 by 0.25

Interquartile Range (IQR) which is the value(s) between the 25th percentile and the 75th percentile 
If it between a min and max, it is called a Range

#### Uses of Percentile:
1. Removing outliers
2. General data analysis

#### Mode: 
means most frequently occurring value in a dataset