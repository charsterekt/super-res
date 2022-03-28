<script>
	import Dropzone from 'svelte-file-dropzone'

	let files = {
		accepted: [],
		rejected: []
	}

	async function handleFilesSelect(e) {
		const { acceptedFiles, fileRejections } = e.detail
		files.accepted = [...files.accepted, ...acceptedFiles]
		files.rejected = [...files.rejected, ...fileRejections]

		if (files.accepted.length != 0) {
			console.log(files.accepted)
			var preview = document.getElementById('image-preview')
			var hidden_preview = document.getElementById('preview-dims')
			preview.setAttribute('src', URL.createObjectURL(files.accepted[0]))
			hidden_preview.setAttribute('src', URL.createObjectURL(files.accepted[0]))
		}

		if (files.accepted.length > 1) {
			files.accepted.shift()
			var preview = document.getElementById('image-preview')
			preview.setAttribute('src', URL.createObjectURL(files.accepted[0]))
		}

		if (files.rejected.length > 0) {
			// console.log(files.rejected)
			// alert("Only .jpeg, .jpg, and .png files upto 1.5Mb are allowed")
			var modal = document.getElementById('modal')
			modal.style.display = 'flex'
			files.rejected.pop()
		}
	}

	$: src = ''
	$: og = '0 x 0'
	$: enhanced = '0 x 0'


	async function getImage() {
		console.log('Getting response')
		var loader = document.getElementById('enhance-loader')
		var enhanced_imagebox = document.getElementById('imagebox')
		var upload_div = document.getElementById('upload-container')
		enhanced_imagebox.setAttribute('src', 'assets/download-icon.png')
		loader.style.display = 'block'
		enhanced_imagebox.style.display = 'none'
		upload_div.style.pointerEvents = 'none'
		upload_div.style.opacity = '0.6'

		var data = new FormData()
		data.append('image', files.accepted[0])
		console.log(data)
		fetch('https://swellte.herokuapp.com/image', {
			method: 'POST',
			body: data
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data)
				var bytestring = data['status']
				var image = bytestring.split("'")[1]
				var hidden_returned_preview = document.getElementById('returned-dims')
				enhanced_imagebox.setAttribute('src', 'data:image/png;base64,' + image)
				hidden_returned_preview.setAttribute('src', 'data:image/png;base64,' + image)
				files.accepted.pop()
				src = 'data: image/png;base64,' + image
				loader.style.display = 'none'
				enhanced_imagebox.style.display = 'block'
				upload_div.style.pointerEvents = 'all'
				upload_div.style.opacity = '1'
			})
			.catch((error) => {
				console.log(error)
				return []
			})
	}

	function setOgSize() {
		const preview = document.getElementById('preview-dims')
		og = `${preview.clientWidth} x ${preview.clientHeight}`
		console.log(og)
	}

	function setEnhancedSize() {
		const preview = document.getElementById('returned-dims')
		enhanced = `${preview.clientWidth} x ${preview.clientHeight}`
		console.log(enhanced)
	}

	function toggleModal() {
		const modal = document.getElementById('modal')
		modal.style.display = 'none'
	}

	const containerClasses = `
		drop-area
	`

	const containerStyles = `
		opacity: 0;
		height: 50vh;
		position: relative;
		margin-top: -20px;
	`
</script>

<div class="dropbox-wrapper">
	<div class="modal" id="modal">
		<p class="modal-text">Only .jpeg, .jpg, and .png files of up to 1.5Mb are allowed.</p>
		<button class="modal-toggle" on:click={toggleModal}>Dismiss</button>
	</div>
	<div class="dropbox">
		<!-- <div class="upload-container-container"> -->
		<div class="upload-container" id="upload-container">
			<p class="instructional">Drag and drop an image here or click to select a file</p>
			<div class="upload-area">
				<Dropzone
					accept="image/*"
					multiple={false}
					maxSize={1572864}
					disableDefaultStyles={true}
					{containerClasses}
					{containerStyles}
					on:drop={handleFilesSelect}
				/>
				<!-- max size 1.5Mib (mebibyte) = 1572864 bytes -->
				<div class="image-preview-container">
					<img
						src="assets/upload-icon.png"
						class="image-preview"
						id="image-preview"
						alt="preview"
						on:load={setOgSize}
					/>
				</div>
			</div>
			<div class="controls">
				<p class="img-size" id="original-size">Size: {og}</p>
				<button class="button" on:click={getImage}>Enhance</button>
			</div>
		</div>
		<!-- </div> -->
		<!-- <div class="results-container-container"> -->
		<div class="results-container">
			<p class="instructional">Click download to receive the file at full resolution</p>
			<div class="enhanced-preview">
				<img
					id="imagebox"
					class="enhanced-image"
					src="assets/download-icon.png"
					alt="returned"
					on:load={setEnhancedSize}
				/>
				<img
					id="enhance-loader"
					class="enhanced-image enhance-loader"
					src="assets/enhance-loader.gif"
					alt="returned"
				/>
			</div>
			<div class="controls">
				<p class="img-size" id="returned-size">Size: {enhanced}</p>
				<button class="button">
					<a href={src} download rel="noopener noreferrer" target="_blank" class="button-link"
						>Download</a
					>
				</button>
			</div>
		</div>
		<!-- </div> -->
	</div>
	<div class="hidden-stuff">
		<img class="hidden-dims" id="preview-dims" src="" alt="dims" />
		<img class="hidden-dims" id="returned-dims" src="" alt="dims" />
	</div>
</div>

<style>
	.dropbox {
		display: flex;
		background-color: #2c394b;
		border-radius: 20px;
		padding: 40px;
		padding-top: 60px;
		justify-content: space-evenly;
		align-items: center;
		width: 80vw;
		position: absolute;
	}

	.dropbox-wrapper {
		display: flex;
		flex-direction: column;
		justify-content: center;
    	align-items: center;
		overflow-x: hidden;
	}

	.upload-container {
		position: relative;
	}

	.upload-area {
		height: 50vh;
		width: 30vw;
		border-radius: 20px;
		transition: border 0.24s ease-in-out;

		background: transparent;
		border: 4px solid #082032;

		position: relative;
	}

	.upload-area:hover {
		border: 4px #ff4c29 solid;
		cursor: pointer;
	}

	.image-preview-container {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	/* .image-preview-container > img {
		width: 200px;
		height: 200px;
	} */

	/* .results-container {
		width: 45%;
	} */

	/* .upload-container-container {
		display: grid;
		justify-content: center;
		align-items: center;
	} */

	/* .results-container-container {
		display: grid;
		justify-content: center;
		align-items: center;
	} */

	/* .image-preview-container {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 500px;
		width: 500px;
		position: absolute;
		z-index: -1;
	} */

	.enhanced-preview {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 50vh;
		width: 30vw;
		border-radius: 20px;
		border: 4px solid #082032;
	}

	.enhanced-image {
		max-height: 90%;
		max-width: 90%;
	}

	.image-preview {
		max-height: 90%;
		max-width: 90%;
	}

	.button {
		height: 50px;
		border-radius: 20px;
		background: #082032;
		border: none;
		outline: none;
		font-size: 1.3rem;
		color: #ff4c29;
		cursor: pointer;
		transition: background 0.24s ease-in-out;
		display: grid;
		align-items: center;
		justify-content: center;
	}

	.button:hover {
		background: #334756;
	}

	.img-size {
		display: grid;
		justify-content: center;
		background: #334756;
		border-radius: 20px;
		height: 50px;
		align-items: center;
		color: white;
		font-size: 1.3rem;
		text-align: center;
	}

	.button-link {
		color: #ff4c29;
	}

	.controls {
		margin-top: 20px;
		display: grid;
		grid-template-columns: 1fr 1fr;
		justify-content: center;
		align-items: center;
		grid-gap: 100px;
	}

	.instructional {
		color: white;
		font-size: 1.1rem;
		align-items: center;
		justify-content: center;
		display: flex;
		text-align: center;
	}

	.hidden-dims {
		z-index: -100;
		opacity: 0;
	}

	.hidden-stuff {
		/* position: absolute; */
		pointer-events: none;
	}

	.enhance-loader {
		display: none;
	}

	.modal {
		height: 20vh;
		width: 40vw;
		background: rgba(161, 161, 161, 0.3);
		backdrop-filter: blur(10px);
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 30px;
		border-radius: 20px;
		border: 2px #ff4c29 solid;
		position: absolute;
		z-index: 100;
		top: calc(50% - 40vh);
		transition: fade 0.24s ease-in-out;
		display: none;
	}

	.modal-text {
		text-align: center;
		margin-bottom: 20px;
		color: white;
		font-size: 1.3rem;
	}

	.modal-toggle {
		height: 50px;
		width: 150px;
		border-radius: 20px;
		background: white;
		border: none;
		outline: none;
		font-size: 1.3rem;
		color: black;
		cursor: pointer;
		transition: background 0.24s ease-in-out;
		display: grid;
		align-items: center;
		justify-content: center;
		margin: 0 auto;
	}

	.modal-toggle:hover {
		background: black;
		color: white;
	}

	/* MEDIA QUERIES */

    @media only screen and (max-width: 1300px) {
        .dropbox {
			display: grid;
			grid-template-columns: 1fr;
		}

		.upload-area {
			width: 100%;
		}

		.enhanced-preview {
			width: 100%;
		}
    }

    @media only screen and (max-width: 900px) {
		.instructional {
			font-size: 1rem;
		}

		.button {
			font-size: 1rem;
		}

		.img-size {
			font-size: 0.8rem;
		}

		.controls {
			grid-gap: 50px;
		}

		.modal {
			width: 60vw;
		}

		.modal-text {
			font-size: 1.1rem;
		}
	}

    @media only screen and (max-width: 500px) {
		.controls {
			grid-gap: 20px;
		}

		.modal {
			width: 80vw;
			height: 25vh;
		}
	}
</style>
