''' Demo site generator'''
from time import sleep
from sitegenerator import sitegenerator
from datetime import datetime
import json

# Setup datestring
now = datetime.now()
datestr = now.strftime(r"%Y%m%d%H%M%S")

snapshot_page = sitegenerator.SiteGenerator()
snapshot_page.base_template = "base_snapshot.html"
snapshot_page.output_file = "./templates/snapshot_" + datestr + ".html"
snapshot_page.replacements = {
    "date": now.strftime(r"%d-%m-%Y"),
    "time": now.strftime(r"%H:%M:%S"),
}
snapshot_page.render()


# Update main template with new templates
indexpage = sitegenerator.SiteGenerator(output_file="./docs/new_index.html")
indexpage.render()
