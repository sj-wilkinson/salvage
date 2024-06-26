import os, alminer, pandas

environ = os.environ
NAME = str(environ['NAME'])
ID = str(environ['ID'])
#out_dir = str(environ['tmp_dir'])
out_dir = f'/arc/projects/salvage/ALMA_data/{ID}/'

# loading ALMiner query object from the crossmatch between SDSS and the ALMA archive
f = '/arc/projects/salvage/ALMAxmatch/ALminer_output/SDSS-ALMA-search-Feb12-total.pkl'
myquery = pandas.read_pickle(f)

print('... Downloading with ALMiner.')
alminer.download_data(myquery[myquery['ALMA_source_name']==NAME], fitsonly=False, dryrun=False, location=out_dir, print_urls=False, archive_mirror='NRAO')

print('Python script complete.')










#myquery = alminer.conesearch(ra=RA, dec=DEC, point=False, search_radius=0.00001) #several targets at RA and DEC
#myquery = alminer.target(NAME) #alma target name not in SIMBAD
#myquery = alminer.keysearch({'target_name': NAME})

#print('... Conducting ALMiner search.')
#myquery = alminer.conesearch(ra=RA, dec=DEC, point=True)