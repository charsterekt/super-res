<div class="about-container">
	<div class="software-section">
		<h1 class="header">POWERED BY</h1>
		<div class="cards">
			<div class="img-card iCard-style3">
				<div class="card-content">
					<div class="card-image">
						<span class="card-title">Flask</span>
						<img src="assets/flask.png" alt="flask" class="flask" />
					</div>

					<div class="card-text">
						<p>A simple Flask microservice that handles image processing and requests.</p>
					</div>
				</div>

				<div class="card-link">
					<a href="https://flask.palletsprojects.com/en/2.0.x/" title="Read Full">
						<span>Go To Link</span>
					</a>
				</div>
			</div>

			<div class="img-card iCard-style3">
				<div class="card-content">
					<div class="card-image">
						<span class="card-title">Svelte</span>
						<img src="assets/svelte.png" alt="svelte" />
					</div>

					<div class="card-text">
						<p>
							Smooth and performant reactive frontend framework that handles a lot of work on the
							client side.
						</p>
					</div>
				</div>

				<div class="card-link">
					<a href="https://svelte.dev/" title="Read Full">
						<span>Go To Link</span>
					</a>
				</div>
			</div>

			<div class="img-card iCard-style3">
				<div class="card-content">
					<div class="card-image">
						<span class="card-title">ESRGAN</span>
						<img src="assets/github.png" alt="esrgan" />
					</div>

					<div class="card-text">
						<p>Strong GAN model responsible for image upscaling. Original credits to Xinntao</p>
					</div>
				</div>

				<div class="card-link">
					<a href="https://github.com/xinntao/ESRGAN" title="Read Full">
						<span>Go To Link</span>
					</a>
				</div>
			</div>
		</div>
	</div>

	<div class="info-section">
		<h1 class="header">ABOUT</h1>
        <p class="para">
            <span class="first-word">ESRGAN</span>&nbsp;is a Generative Adversarial Neural network that
            upscales images by 4 times in each dimension, while attempting to preserve the image's
            quality in a process commonly known as super resolution. The model in use in this web app is
            a pre trained model from xinntao's github.
        </p>

        <p class="para">
            <span class="first-word">Svelte</span>&nbsp;is a reactive front-end framework that is sleek,
            easy to use, and highly performant. Sveltekit is a fullstack framework built around it that
            makes building web apps easier.
        </p>

        <p class="para">
            <span class="first-word">Flask</span>&nbsp;is a Python framework for writing REST APIs that
            was used to create a simple microservice to interact with the model within Python. It is a
            small and lightweight framework.
        </p>

        <p class="para">
            <span class="first-word">Limitations</span>&nbsp;with the project are the lack of ability to
            choose a resolution to upscale to, as it is currently a 4x multiplier. The model also runs on
            CPU due to hosting budgets which means results take a long time to process and return, which leads
            to long wait times. The load times for the site might be bloated since the backend is hosted on 
            a free server and may have to wake up from sleep to process the request while the frontend spins 
            up immediately.
        </p>
	</div>
</div>

<style>

	.about-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		background-color: #2c394b;
		border-radius: 20px;
		padding: 40px;
		margin: 40px;
		width: 80vw;
		margin: 40px auto 20px auto;
	}

	.header {
		text-align: center;
		font-size: 3rem;
		color: #fff;
	}

	.software-section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.info-section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin-top: 40px;
	}

	.cards {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		grid-gap: 50px;
	}

	.para {
		color: #fff;
		font-size: 1.1rem;
		max-width: 60vw;
	}

	.first-word {
		font-weight: bold;
		font-size: 1.3rem;
		color: #ff4c29;
	}

	.img-card {
		width: 300px;
		position: relative;
		border-radius: 5px;
		text-align: left;

		-webkit-box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.3);
		-moz-box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.3);
		-o-box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.3);
		box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.3);
	}

	.img-card .card-image {
		position: relative;
		margin: auto;
		overflow: hidden;
		border-radius: 5px 5px 0px 0px;
		height: 400px;
	}

	.img-card .card-image img {
		width: 100%;
		border-radius: 5px 5px 0px 0px;

		-webkit-transition: all 0.8s;
		-moz-transition: all 0.8s;
		-o-transition: all 0.8s;
		transition: all 0.8s;
	}

	.img-card .card-image:hover img {
		-webkit-transform: scale(1.1);
		-moz-transform: scale(1.1);
		-o-transform: scale(1.1);
		transform: scale(1.1);
	}

	.img-card .card-text {
		padding: 0 15px 15px;
		line-height: 1.5;
	}

	.img-card .card-link {
		padding: 20px 15px 30px;
		width: -webkit-fill-available;
	}

	.img-card .card-link a {
		text-decoration: none;
		position: relative;
		padding: 10px 0;
	}

	.img-card .card-link a:after {
		top: 30px;
		content: '';
		display: block;
		height: 2px;
		left: 50%;
		position: absolute;
		width: 0;

		-webkit-transition: width 0.3s ease 0s, left 0.3s ease 0s;
		-moz-transition: width 0.3s ease 0s, left 0.3s ease 0s;
		-o-transition: width 0.3s ease 0s, left 0.3s ease 0s;
		transition: width 0.3s ease 0s, left 0.3s ease 0s;
	}

	.img-card .card-link a:hover:after {
		width: 100%;
		left: 0;
	}

	.img-card.iCard-style3 {
		text-align: center;
	}

	.img-card.iCard-style3 .card-title {
		top: 75%;
		font-size: 30px;
		color: #fff;
		background: #082032;
		position: absolute;
		width: 100%;
		font-family: 'Roboto', sans-serif;
		z-index: 1;
	}

	.img-card.iCard-style3 .card-text {
		color: #fff;
	}

	.img-card.iCard-style3 .card-link a {
		color: #fff;
	}

	.img-card.iCard-style3 .card-link a:after {
		background: #585858;
	}

    /* MEDIA QUERIES */
	
    @media only screen and (max-width: 1300px) {
        .cards {
            grid-template-columns: 1fr 1fr;
        }
    }

    @media only screen and (max-width: 900px) {
        .cards {
            grid-template-columns: 1fr;
        }

        .img-card {
            width: 250px;
        }
    }

</style>
