import os
from snowflake.connector
connection_parameters = {
"account":"ifb03328.prod3.us-west-2.aws",
"user":"VINOTHA",
"password":"Thanik@123",
"role":"ACCOUNTADMIN",
"warehouse":"compute_wh",
"database":"ESG_SCORES_SP500_DEMO",
"schema":"SCORING"
  }
test_session = Session.builder.configs(connection_parameters).create()
 
