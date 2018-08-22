from limnopapers import *

if(len(sys.argv) == 2):
    data = get_papers(day = sys.argv[1], to_csv=True)        
else:
    data = get_papers(day = str(datetime.date.today()), to_csv=True)        

toots = data['title'] + ". " + data['dc_source']  + ". " + data['prism_url']
for toot in toots:
    print(toot)    
