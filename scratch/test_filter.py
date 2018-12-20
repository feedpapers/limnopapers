import limnopapers as lp
import pandas as pd
# help(lp.filter_limno)

d = {'title': ["Integrating fast and slow processes is essential for simulating human–freshwater interactions"], 'summary': ["Integrated modeling is a critical tool to evaluate the behavior of coupled human–freshwater systems. However, models that do not consider both fast and slow processes may not accurately reflect the feedbacks that define complex systems. We evaluated current coupled human–freshwater system modeling approaches in the literature with a focus on categorizing feedback loops as including economic and/or socio-cultural processes and identifying the simulation of fast and slow processes in human and biophysical systems. Fast human and fast biophysical processes are well represented in the literature, but very few studies incorporate slow human and slow biophysical system processes. Challenges in simulating coupled human–freshwater systems can be overcome by quantifying various monetary and non-monetary ecosystem values and by using data aggregation techniques. Studies that incorporate both fast and slow processes have the potential to improve complex system understanding and inform more sustainable decision-making that targets effective leverage points for system change."]}
dt = pd.DataFrame(data = d)

test = lp.filter_limno(dt)
test['filter_against']
