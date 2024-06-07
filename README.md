<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>


To use this script:
1. Git pull the repository
2. Create a `.env` file in your local environment that looks like the following:
```
DDS_DOMAIN_NAME=<domain-name>
DDS_USERNAME=<user-with-admin-privilege>
DDS_API_KEY=<user-api-key>
```
3. Run the script using `python list_apps.py`. This will print the table of apps and their information, as well as output a the same table to an output file. You can disable this behaviour using the `disable_stdout` and `disable_file` flags.

The output table will dispaly the following headers:
```
Name                           | Owner                | Running              | Created              | Last GIT Push        | URL      
```
