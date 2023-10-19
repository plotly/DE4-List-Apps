from dds import client as dds_client
from gql import gql
from datetime import datetime
import sys, os
#Get all apps
FILENAME='output.txt'
disable_stdout = False
disable_file = True

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

#Need to do this by page
apps_name_query = gql(
    """
    query Apps($page: Int!, $allApps: Boolean!) {
        apps(page: $page, allApps: $allApps) {
            apps {
                name
                urlOnServer
                status {
                    running
                }
                owner {
                    username
                }
                analytics {
                    timestamps {
                        created
                        updated
                        visited
                    }
                }
            }
            nextPage
        }
    }
    """
)
getAllApps = True
all_apps = {"apps":[]}
page = 1 
next_page = True
if disable_stdout:
    blockPrint()
print("Pulling app data")
while next_page:
    
    print(f"Pulling data from page: {page}")
    page_apps = dds_client.execute(apps_name_query, {"page": page, "allApps": getAllApps})["apps"]
    all_apps['apps'] += page_apps['apps']
    
    if page_apps['nextPage']:
        page = page_apps['nextPage']
    else:
        next_page = False

print('Done')
if disable_stdout:
    enablePrint()

#Display as a table

if not disable_stdout:
    print ("{:<30} | {:<20} | {:<20} | {:<20} | {:<20} | {:<30}".format('Name','Owner','Running', 'Created', 'Last GIT Push', 'URL'))
    print ("-"*200)
    for app in all_apps['apps']:
        running = "Running" if app['status']['running'] == 1 else "Stopped"
        created = datetime.strptime(app['analytics']['timestamps']['created'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d @ %H:%M") if app['analytics']['timestamps']['created'] else 'None'
        updated = datetime.strptime(app['analytics']['timestamps']['updated'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d @ %H:%M") if app['analytics']['timestamps']['updated'] else 'None'
        print ("{:<30} | {:<20} | {:<20} | {:<20} | {:<20} | {:<30}".format(app['name'], app['owner']['username'], running, created, updated, app['urlOnServer']))

if not disable_file:
    with open(FILENAME, 'w') as file:
        file.write("{:<30} | {:<20} | {:<20} | {:<20} | {:<20} | {:<30}\n".format('Name','Owner','Running', 'Created', 'Last GIT Push', 'URL'))
        file.write("-"*200)
        file.write("\n")
        for app in all_apps['apps']:
            running = "Running" if app['status']['running'] == 1 else "Stopped"
            created = datetime.strptime(app['analytics']['timestamps']['created'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d @ %H:%M") if app['analytics']['timestamps']['created'] else 'None'
            updated = datetime.strptime(app['analytics']['timestamps']['updated'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d @ %H:%M") if app['analytics']['timestamps']['updated'] else 'None'
            file.write("{:<30} | {:<20} | {:<20} | {:<20} | {:<20} | {:<30}\n".format(app['name'], app['owner']['username'], running, created, updated, app['urlOnServer']))