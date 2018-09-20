import pandas as pd

title = ["How Well Does the Mechanistic Water Quality Model CE‐QUAL‐W2 Represent Biogeochemical Responses to Climatic and Hydrologic Forcing?", 
"junk"]
summary = ["Mechanistic water quality models are applied globally for water quality management in rivers and lakes. However, it is unclear how well these models represent the response of lakes to changes in climate and hydrologic conditions. To address this question, we conducted a series of climate and hydrologic sensitivity analyses using a parameterized water quality model, CE‐QUAL‐W2, for the Spokane River and Lake Spokane system. Two experimental tests with climate and flow forcing showed that the model predictions were rather insensitive to climatic‐driven hydrologic changes and a wide range of hydrologic conditions (1st to 99th percentile flows) for two different wastewater treatment plant discharge scenarios. The model realistically represented some aspects of Lake Spokane's observed responses to climatic and hydrologic variability, for example, the water residence time and some water quality trends. However, the model overestimated the reservoir total phosphorus (TPR) concentration by ~37% and the chlorophyll a (Chl a) concentration by ~31% and underestimated the minimum volume‐weighted hypolimnetic dissolved oxygen (DOMIN) concentration by ~26% for a wide range of flows compared to the observed data. In contrast to the model's water quality insensitivity, the modeled temperature was more sensitive to flow than was actually observed in Lake Spokane. This study provides guidance for improving the response of one of the most important mechanistic water quality models to climatic and hydrologic forcing and should help modelers and decision‐makers to develop a rigorous assessment of climate and flow sensitivity to improve the margin of safety when setting total maximum daily load targets.", 
"junk"]

df = pd.DataFrame({'title': title, 'summary': summary})

filter_for = ['lake', "reservoir", "inland waters"]
has_limno_title = df['title'].str.contains('|'.join(filter_for),
                                           case = False)
has_limno_summary = df['summary'].str.contains('|'.join(filter_for),
                                               case = False)

filter_against = ['ocean', 'iran', 'fault', 'wetland', 'correction',
                  'hydroelectric', '^mining$', 'Great Lakes']
has_junk_summary = ~df['summary'].str.contains('|'.join(filter_against),
                                               case = False)
has_junk_title = ~df['title'].str.contains('|'.join(filter_against),
                                           case = False)

is_limno = pd.DataFrame([has_limno_title, has_limno_summary, has_junk_summary, 
has_junk_title]).transpose().sum(axis = 1) > 2

df[is_limno]
