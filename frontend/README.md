# Frontend Documentation

This part of the project involves the use of the Vue.js app in the frontend_app directory. This includes the Vue cli, axios, eslint-plugin, etc. The Vue app consists of the directories *node_modules*, *public* and *src*. The *src* directory is where most of your work will be. It contains the
assets, components, router and views 

- Assets
The *assets* diectory stores all static files like image files, css files and other similar files to be used for each webpage's appearance.

- Components
 This *components* directory is where the UI components(Basically formatted webpages) are stored with the extension `.vue`. Currently this just contains the HelloWorld.vue component.



The `main.js` file initiates the vue app and the `App.vue` handles the url routing and mapping.  

### Consuming backend data

Any data to be consumed will be served via a deployed version of the backend on a live server. In absence of the live server data, you will be required to set up and run the backend on your local machine and use the uri `http://127.0.0.1:5000`. Find explanation on how to set up in the [backend readme](../backend/README.md). 


### Setting up

To get started, have npm installed on your local machine, visit this [guide](https://phoenixnap.com/kb/install-node-js-npm-on-windows) for help if needed. Clone this repository by navigating to your chosen directory for the project in your git bash terminal and running the following command:

`git clone https://github.com/JhimmieC137/conference-wesite.git`


### Running the app

To run the Vue app, navigate to the frontend_app directory in your terminal, run the command:

`npm run serve`

On first setup you should see the the page show in the image below
![firstpage](https://user-images.githubusercontent.com/71768696/210447383-c7517612-df9f-4607-b3e1-f10e9be003d1.png)





### Documentation

You will also be required to document each component as they are added under *Components* above. Also document any other important feature added.

### Deploying the app

When you are done and ready to deploy to production, delete the former `dist` folder and run the command:

`npm run build`

This creates a new `dist` folder 



**Note:**
If you will be using VScode as a text editor you will need extensions
[Vue](Vue.volar) for the vue application
[Prettier](esbenp.prettier-vscode) to help with code formatting

**You're good to go!**
