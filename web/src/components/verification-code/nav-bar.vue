<template>
    <nav class="navbar navbar-expand-lg navbar-light self-navbar">
        <router-link class="navbar-brand" to="/verification-code/root">首页</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarVerificationCodeNavDropdown" aria-controls="navbarVerificationCodeNavDropdown" aria-expanded="false" aria-label="navbar触发器">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarVerificationCodeNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item nav-link" :class="$route.name === 'verification-code short-message' ? 'active' : null">
                    <router-link class="nav-link" to="/verification-code/short-message">短信管理</router-link>
                </li>
                <li class="nav-item nav-link" :class="$route.name === 'verification-code history' ? 'active' : null">
                    <router-link class="nav-link" to="/verification-code/history">历史记录</router-link>
                </li>
                <li class="nav-item nav-link dropdown">
                    <a class="nav-link dropdown-toggle" href="javascript:void(0)" id="navbarVerificationCodeNavDropdownFirst" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">其他</a>
                    <div class="dropdown-menu" aria-labelledby="navbarVerificationCodeNavDropdownFirst">
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
        background-color: blueviolet;
    }
</style>