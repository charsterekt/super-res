<h1>Super Resolution</h1>
<hr>

An image enhancement web app built around the ESRGAN model by <a href="https://github.com/xinntao/ESRGAN">xinntao</a>. The model is a PyTorch CPU model and thus while it can in theory handle images of any size, I have limited file size to 1.5mb to prevent memory overflows and excessively long loading times. The frontend is built in Svelte and is responsive for most device sizes. The frontend is deployed on Vercel. It makes requests to a simple Flask microservice that lives on a Heroku instance. Because of this, there might be a long wait time when someone wakes the app from sleep as free-tier Heroku apps sleep after 30 mins of inactivity. The app resizes images by 4 times in each dimension while trying to maintain the fidelity.
<br><br>
The deployed app can be found <a href="https://swellte.vercel.app">here.</a>
