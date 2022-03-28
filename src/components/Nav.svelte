<div class="navbar">
    <a href="/">
        <span class="logo">Swellte</span>
    </a>
    <nav class="nav-links">
        <a class="link" href="/">Home</a>
        <a class="link" href="/about">About</a>
    </nav>
</div>
<!-- <div class="blend"></div> -->

<style>
    .navbar {
        background-color: #082032;
        height: 80px;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .nav-links {
        position: absolute;
        right: 40px;
    }

    .logo {
        color: #FF4C29;
        font-size: 3rem;
        margin-left: 30px;
        font-weight: bold;
    }

    .link {
        color: #FF4C29;
        font-size: 1.5rem;
        margin-left: 40px;
    }

    .link:hover {
        border-bottom: 2px solid #FF4C29;
        line-height: 2rem;
    }

    /* .blend {
        background-color: #2C394B;
        width: 100%;
        height: 20px;
    } */

    /* MEDIA QUERIES */

    @media only screen and (max-width: 900px) {
        .link {
            font-size: 1.2rem;
            margin-left: 20px;
        }

        .logo {
            font-size: 2rem;
        }
    }
</style>