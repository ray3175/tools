<template>
    <nav class="navbar navbar-expand-lg navbar-light self-navbar">
        <router-link class="navbar-brand" to="/english/root">首页</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarEnglishNavDropdown" aria-controls="navbarEnglishNavDropdown" aria-expanded="false" aria-label="navbar触发器">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarEnglishNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item nav-link dropdown">
                    <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarEnglishNavDropdownFirst" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">单词</a>
                    <div class="dropdown-menu" aria-labelledby="navbarEnglishNavDropdownFirst">
                        <router-link class="dropdown-item" to="/english/word-overview">概览</router-link>
                    </div>
                </li>
                <li class="nav-item nav-link dropdown">
                    <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarEnglishNavDropdownSecond" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">其他</a>
                    <div class="dropdown-menu" aria-labelledby="navbarEnglishNavDropdownSecond">
                        <router-link class="dropdown-item" to="/">返回</router-link>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    export default {
        name: "nav-bar"
    }
</script>

<style scoped>
    .self-navbar {
        background-color: burlywood;
    }
</style>