# Frontend Documentation

This part of the project involves the use of the Vue.js app in the frontend_app directory. This includes the Vue cli, axios, eslint-plugin, etc. The Vue app consists of the directories *node_modules*, *public* and *src*. The *src* directory is where most of your work will be. It contains the
assets, components, router and views 

- Assets
The *assets* diectory stores all static files like image files, css files and other similar files to be used for each webpage's appearance.

- Components
 This *components* directory is where the UI components(Basically formatted webpages) are stored with the extension `.vue`. Currently this just contains the HelloWorld.vue component.

- Router
The *router* directory contains the index.js file where urls are defined and mapped to the components

- Views
This is similar to components and contains webpage templates also with the extension `.vue`

The `main.js` file initiates the vue app

You will be required to document each component as they are added under *Components* above. Also document any other important feature added When you are done and ready to deploy to production, delete the former `dist` folder and run the command:

`npm run build`

This creates a new `dist` folder 


Note:
If you will be using VScode as a text editor you will need extensions
[Vue](Vue.volar) for the vue application
[Prettier](esbenp.prettier-vscode) to help with code formatting

**You're good to go!**