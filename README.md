## Base atmos page parser

### Installation:

virtualenv -p python3 **env**

cd **env**

source bin/activate

git clone https://github.com/alexstone23/atmos_parser

cd atmos_parser/

pip install -r requirements.txt

cd atmos_parser/

**single page parsing**

scrapy crawl single_linker -o single.csv -t csv

**single page extended parsing**

scrapy crawl single_linker_extended -o single_extended.csv -t csv

**parsing people's page**

scrapy crawl people_parser -o people_page.csv -t csv

**env deactivation**

deactivate





