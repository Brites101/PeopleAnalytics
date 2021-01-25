#just renamed variables
# 
#  dump_data.py
# initialize PYDATASET_HOME, and
# dump pydataset/resources.tar.gz into $HOME/.pydataset/

import tarfile
from os import path as os_path
from os import mkdir as os_mkdir
from os.path import join as path_join

def __setup_db():

    homedir = os_path.expanduser('~')
    PEOPLEANALYTICSDATASET_HOME = path_join(homedir, '.peopleanalyticsdataset/')

    if not os_path.exists(PEOPLEANALYTICSDATASET_HOME):
        # create $HOME/.peopleanalyticsdataset/
        os_mkdir(PEOPLEANALYTICSDATASET_HOME)
        print('initiated datasets repo at: {}'.format(PEOPLEANALYTICSDATASET_HOME))

        # copy the resources.tar.gz from the module files.

        # # There should be a better way ? read from a URL ?
        import peopleanalyticsdataset
        filename = path_join(peopleanalyticsdataset.__path__[0], 'resources.tar.gz')
        tar = tarfile.open(filename, mode='r|gz')

        # # reading 'resources.tar.gz' from a URL
        # try:
        #     from urllib.request import urlopen # py3
        # except ImportError:
        #     from urllib import urlopen # py2
        # import tarfile
        #
        # targz_url = 'https://example.com/resources.tar.gz'
        # httpstrem = urlopen(targz_url)
        # tar = tarfile.open(fileobj=httpstrem, mode="r|gz")

        # extract 'resources.tar.gz' into PYDATASET_HOME
        # print('extracting resources.tar.gz ... from {}'.format(targz_url))
        tar.extractall(path=PEOPLEANALYTICSDATASET_HOME)
        # print('done.')
        tar.close()
