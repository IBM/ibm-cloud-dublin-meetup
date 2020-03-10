Demo Steps:

1. Create new project (namespace). eg `opendatahub-meetup`
2. Go to Install OpenDataHub Operator into new project:
![image](https://media.github.ibm.com/user/7080/files/9723b980-5ed4-11ea-8605-8eb79065889a)
3. Configs for installation: <https://github.ibm.com/fd4b-demo/IBM-Cloud-Meetup-2020-03-10/blob/master/OpenDataHub-ibmcloud-meetup-dublin.yaml>
4. Check deployment status: ![image](https://media.github.ibm.com/user/7080/files/d0a9f400-5ed7-11ea-9415-1b420dfe4f93)
5. Find route to jupyterhub: ![image](https://media.github.ibm.com/user/7080/files/064edd00-5ed8-11ea-9d88-cb3e2f9db7bf)
6. Check status of deployments from project dashboard (pods): ![image](https://media.github.ibm.com/user/7080/files/588ffe00-5ed8-11ea-80f0-32f8de85847c)
7. Check status of persistent volume claims: ![image](https://media.github.ibm.com/user/7080/files/8d03ba00-5ed8-11ea-8a10-e7bccdbbe648)
8. If everything ready, try to access the jupyter route, first time will ask for permissions: ![image](https://media.github.ibm.com/user/7080/files/cccaa180-5ed8-11ea-875a-d32bc6dcb473)
9. Choose Spawner Options for JupyterHub env: ![image](https://media.github.ibm.com/user/7080/files/f97eb900-5ed8-11ea-93ac-3c7f61bcf85b)
10. It may show some errors like: ![image](https://media.github.ibm.com/user/7080/files/5aa68c80-5ed9-11ea-8df9-fe1b85fd3e18)
11. Reopen it up again, status will get properly updated: ![image](https://media.github.ibm.com/user/7080/files/8e81b200-5ed9-11ea-8013-0cca5c86ce1b)
12. Now environment should be accessible: https://jupyterhub-opendatahub-meetup.ibmcloud-meetup-dublin-464a84d5f4e75649fcf20b8d41ef69aa-0000.eu-gb.containers.appdomain.cloud/user/iam%23gallomas@ie.ibm.com/tree screenshot: ![image](https://media.github.ibm.com/user/7080/files/63985d80-5edb-11ea-8e20-8be430435f22)
13. Create a sample notebook, or use some public available sample like https://github.com/ibm-et/jupyter-samples/blob/master/scikit-learn/sklearn_cookbook.ipynb and import it
14. To import the sample notebook, clone the github repo then do "Upload" notebook: ![image](https://media.github.ibm.com/user/7080/files/5466df00-5ede-11ea-89bb-c30fbf7759a2)
