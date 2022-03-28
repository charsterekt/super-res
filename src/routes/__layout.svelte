<script>
    import Nav from "../components/Nav.svelte"
</script>


<Nav />
<div class="layout-container">
    <slot></slot>
</div>

<style>
    .layout-container {
        height: calc(100vh - 80px);
    }

    @media only screen and (max-width: 1300px) {
        .layout-container {
            height: calc(100vh + 500px);
        }
    }
</style>