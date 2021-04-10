<template>
    <div class="user-info shadow-lg rounded">
        <div class="row">
            <div class="col">
                <div class="header">
                    <b>{{ platformName }}</b>
                </div>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-5 col-form-label" for="user-info-user-name">用户名</label>
            <div class="col-7">
                <input v-model="userName" id="user-info-user-name" class="form-control-plaintext" type="text" readonly>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-5 col-form-label" for="user-info-user-money">余额</label>
            <div class="col-7">
                <input v-model="userMoney" id="user-info-user-money" class="form-control-plaintext" type="text" readonly>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-5 col-form-label" for="user-info-user-token">Token</label>
            <div class="col-7">
                <input v-model="userToken" id="user-info-user-token" class="form-control-plaintext" type="text" readonly>
            </div>
        </div>
        <div class="form-group row self-button">
            <button @click="switchToLogin()" class="btn btn-primary btn-lg shadow-lg rounded self-login-button-middle" type="button">重新登录</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "user-info",
        props: ["platformName", "userName", "userMoney", "userToken",],
        methods: {
            switchToLogin() {
                this.$parent.switchLoginShow();
            }
        }
    }
</script>

<style scoped>
    .user-info {
        position: relative;
        width: 380px;
        margin: 0 auto;
        border: 1px solid blueviolet;
        border-radius: 10px;
        padding: 40px;
    }

    .user-info .header {
        font-size: 36px;
        margin-bottom: 20px;
    }

    .user-info .row {
        margin-top: 20px;
    }

    .user-info .self-button {
        margin-bottom: 25px;
    }

    .user-info .self-login-button-middle {
        margin-top: 20px;
        margin-left: 33%;
    }
</style>
