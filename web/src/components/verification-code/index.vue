<template>
    <div>
        <div class="header">
            <nav-bar></nav-bar>
        </div>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script>
    import navBar from './nav-bar';

    export default {
        name: "verification-code",
        components: {
            "nav-bar": navBar
        },
        mounted () {
            this.$self.verificationCode = {};
        }
    }
</script>

<style scoped>
</style>
