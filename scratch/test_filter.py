import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Listening to air–water gas exchange in running waters"], 'summary': ["Air–water gas exchange velocities (k) are critical components of many biogeochemical and ecological process studies in aquatic systems. However, their high spatiotemporal variability is difficult to capture with traditional methods, especially in turbulent flow. Here, we investigate the potential of sound spectral analysis to infer k in running waters, based on the rationale that both turbulence and entrained bubbles drive gas exchange and cause a characteristic sound. We explored the relationship between k and sound spectral properties using laboratory experiments and field observations under a wide range of turbulence and bubble conditions. We estimated k using flux chamber measurements of CO2 exchange and recorded sound above and below the water surface by microphones and hydrophones, respectively. We found a strong influence of turbulence and bubbles on sound pressure levels (SPLs) at octave bands of 31.5 Hz and 1000 Hz, respectively. The difference in SPLs at these bands and background noise bands showed a linear correlation with k both in the laboratory (R2 = 0.93–0.99) and in the field (median R2 = 0.42–0.90). Underwater sound indices outperformed aerial sound indices in general, and indices based on hydraulic parameters in particular, in turbulent and bubbly surface flow. The results highlight the unique potential of acoustic techniques to predict k, isolate mechanisms, and improve the spatiotemporal coverage of k estimates in bubbly flow."]}
df = pd.DataFrame(data = d)
test = lp.filter_limno(df)

print(list(test['filter_against']))



keywords = pd.read_csv(pkg_resources.resource_filename('limnopapers',
                                                       'keywords.csv'))
filter_for = keywords['filter_for'].tolist()
filter_for = [x for x in filter_for if str(x) != 'nan']
filter_against = keywords['filter_against'].tolist()



test = pd.read_csv(pkg_resources.resource_filename('limnopapers',
                                                   'keywords.csv'))
for item in test['filter_against'].tolist():
    print(type(item))

filter_for = test['filter_for'].tolist()
filter_for = [x for x in filter_for if str(x) != 'nan']
