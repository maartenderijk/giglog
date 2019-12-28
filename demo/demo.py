''' Demo site generator'''
# Relative imports python
import sys
sys.path.append(".") 

from time import sleep
from sitegenerator import SiteGenerator
from datetime import datetime
import json

# Setup datestring
now = datetime.now()
datestr = now.strftime(r"%Y%m%d%H%M%S")

# Generate a small markup file to use in the main template. Tags with {% date %} and {% time %} are replaced
snapshot_page = SiteGenerator()
snapshot_page.template_folder = "./demo/templates"
snapshot_page.base_template = "base_snapshot.html"
snapshot_page.output_file = ".demo/templates/snapshot_" + datestr + ".html"
snapshot_page.replacements = {
    "date": now.strftime(r"%d-%m-%Y"),
    "time": now.strftime(r"%H:%M:%S"),
}
snapshot_page.render()


# Update main template with new templates
indexpage = SiteGenerator(output_file="./demo/new_index.html")
indexpage.render()
