from limnopapers import *

if(len(sys.argv) == 2):
    data = get_papers(day = sys.argv[1], limno = False, to_csv=True)        
else:
    data = get_papers(day = str(datetime.date.today()), limno = False, to_csv=True)        

print("All papers: ")
toots = data['title'] + ". " + data['dc_source']  + ". " + data['prism_url']
for toot in toots:
    print(toot)

print("Filtered: ")
filtered = filter_limno(data)
toots = filtered['title'] + ". " + filtered['dc_source']  + ". " + filtered['prism_url']
for toot in toots:
    print(toot)
