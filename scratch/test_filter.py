import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Influence of land use and hydrologic variability on seasonal dissolved organic carbon and nitrate export: insights from a multi-year regional analysis for the northeastern USA"], 'summary': ["Land use/land cover (LULC) change has significant impacts on nutrient loading to aquatic systems and has been linked to deteriorating water quality globally. While many relationships between LULC and nutrient loading have been identified, characterization of the interaction between LULC, climate (specifically variable hydrologic forcing) and solute export across seasonal and interannual time scales is needed to understand the processes that determine nutrient loading and responses to change. Recent advances in high-frequency water quality sensors provide opportunities to assess these interannual relationships with sufficiently high temporal resolution to capture the unpredictable, short-term storm events that likely drive important export mechanisms for dissolved organic carbon (DOC) and nitrate (NO3−–N). We deployed a network of in situ sensors in forested, agricultural, and urban watersheds across the northeastern United States. Using 2 years of high-frequency sensor data, we provide a regional assessment of how LULC and hydrologic variability affected the timing and magnitude of dissolved organic carbon and nitrate export, and the status of watershed fluxes as either supply or transport controlled. Analysis of annual export dynamics revealed systematic differences in the timing and magnitude of DOC and NO3−–N delivery among different LULC classes, with distinct regional similarities in the timing of DOC and NO3−–N fluxes from forested and urban watersheds. Conversely, export dynamics at agricultural sites appeared to be highly site-specific, likely driven by local agricultural practices and regulations. Furthermore, the magnitude of solute fluxes across watersheds responded strongly to interannual variability in rainfall, suggesting a high degree of hydrologic control over nutrient loading across the region. Thus, there is strong potential for climate-driven changes in regional hydrologic cycles to drive variation in the magnitude of downstream nutrient fluxes, particularly in watersheds where solute supply and/or transport has been modified."]}
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
