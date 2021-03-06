import wget

print "Downloading drug exposures..."
for i in range(0,55):
    url = 'http://stash.osgconnect.net/+rvanguri/AEOLUS_all_reports_'+str(i)+'.npy'
    print wget.download(url)

for i in range(0,55):
    url = 'http://stash.osgconnect.net/+rvanguri/AEOLUS_all_reports_IN_'+str(i)+'.npy'
    print wget.download(url)

print "Downloading outcomes..."
url = 'http://stash.osgconnect.net/+rvanguri/AEOLUS_all_reports_alloutcomes.mtx'
print wget.download(url)

print "Downloading outcomes..."
url = 'http://stash.osgconnect.net/+rvanguri/AEOLUS_all_reports_IN_alloutcomes.mtx'
print wget.download(url)

print "Downloading report ids..."
url = 'http://stash.osgconnect.net/+rvanguri/all_reportids.npy'
print wget.download(url)

print "Downloading IN report ids..."
url = 'http://stash.osgconnect.net/+rvanguri/all_reportids_IN.npy'
print wget.download(url)

print "Downloading age vector..."
url = 'http://stash.osgconnect.net/+rvanguri/all_ages.npy'
print wget.download(url)

print "Downloading year vector..."
url = 'http://stash.osgconnect.net/+rvanguri/all_years.npy'
print wget.download(url)

