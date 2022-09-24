# CrisprCoders
A Django web app with authentication server and resources server. The resources server is protected with the authentication server. It means that the authenticated user can only access the resources.

**#Requirements**
1. Python == 3.7.9
2. Django == 3.2.14

**#Authentication Server**
--> The logic of authentication is developed inside the authapp.

**#Resources Server**
--> The resources are served from the resources app. It contains a simple class based view that return the reponse with static data that is further used by web application for rendering the CV.

**#Installing and Running this App**
1. Download the zip file and unzip it.
