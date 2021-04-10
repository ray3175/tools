<template>
    <div>
        <div v-show="phoneAlertList.length" id="self-message-alert">
            <messageAlert v-for="(phone, index) in phoneAlertList" :key="index" :phone="phone">
                手机号&nbsp;<strong>{{ phone }}</strong>&nbsp;过滤成功！
            </messageAlert>
        </div>
        <div class="row self-top-row">
            <div class="col-6">
                <div class="input-group mb-3 shadow-lg rounded">
                    <div class="input-group-prepend">
                        <span class="input-group-text">项目名称</span>
                    </div>
                    <select v-model="item" class="custom-select">
                        <option v-for="(value, key, index) in itemObj" :value="value" selected>{{ key }}</option>
                    </select>
                </div>
            </div>
            <div class="col-6">
                <div class="input-group mb-3 shadow-lg rounded">
                    <div class="input-group-prepend">
                        <span class="input-group-text">获取数量</span>
                    </div>
                    <input v-model="multi" class="form-control" type="text">
                </div>
            </div>
            <div class="col-6">
                <div class="input-group mb-3 shadow-lg rounded">
                    <div class="input-group-prepend">
                        <span class="input-group-text">指定类型</span>
                    </div>
                    <select v-model="type" class="custom-select">
                        <option v-for="(obj, index) in typeList" :value="obj.value" selected>{{ obj.name }}</option>
                    </select>
                </div>
            </div>
            <div class="col-6">
                <div class="input-group mb-3 shadow-lg rounded">
                    <div class="input-group-prepend">
                        <span class="input-group-text">指定号码</span>
                    </div>
                    <input v-model="type" class="form-control" type="text">
                </div>
            </div>
            <div class="col-12">
                <div class="input-group mb-3 shadow-lg rounded">
                    <div class="input-group-prepend">
                        <span class="input-group-text self-tip" title='如果多个要过滤的号码，请使用"||"分隔。'>号码过滤</span>
                    </div>
                    <input v-model="filterPhonePrefix" class="form-control" type="text">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-2 self-button">
                <button @click="getPhoneNumber()" class="btn btn-outline-primary btn-lg shadow-lg rounded" type="button">获取号码</button>
            </div>
            <div class="col-md-2 self-button">
                <button @click="releaseAllPhoneNumber()" class="btn btn-outline-secondary btn-lg shadow-lg rounded" type="button">全部释放</button>
            </div>
            <div class="col-md-2 self-button">
                <button @click="getPhoneMessage()" class="btn btn-outline-success btn-lg shadow-lg rounded" type="button">获取短信</button>
            </div>
            <div class="col-md-2 self-button">
                <button @click="releasePhoneNumber()" class="btn btn-outline-warning btn-lg shadow-lg rounded" type="button">释放号码</button>
            </div>
            <div class="col-md-2 self-button">
                <button @click="removePhoneNumber()" class="btn btn-outline-danger btn-lg shadow-lg rounded" type="button">拉黑号码</button>
            </div>
            <div class="col-md-2 self-button">
                <button @click="activeAutoGetMessage()" :class="autoGetMessageTimer ? 'btn-success': 'btn-dark'" class="btn btn-lg shadow-lg rounded" type="button">{{ autoGetMessageTimer ? '停止' : '激活' }}自动获取</button>
            </div>
        </div>
        <div class="row">
            <div class="col-md-3">
                <phoneNumber ref="phoneNumber" :phone="phone" :phoneDict="phoneDict"></phoneNumber>
            </div>
            <div class="col-md-9">
                <phoneMessage ref="phoneMessage" :phone="phone"></phoneMessage>
            </div>
        </div>
    </div>
</template>

<script>
    import { CODE_PLATFORM_KEKE, CODE_PLATFORM_JINDOU, CODE_PLATFORM_MIYI } from "@/config/code-platform-info";
    import { shortMessageApi } from "./api";

    import messageAlert from "./message-alert";
    import phoneNumber from "./phone-number";
    import phoneMessage from "./phone-message";

    export default {
        name: "short-message",
        mixins: [shortMessageApi],
        components: { messageAlert, phoneNumber, phoneMessage },
        data() {
            return {
                name: null,
                token: null,
                multi: "1",
                item: null,
                itemObj: {},
                type: "0",
                filterPhonePrefix: "",
                typeList: [
                    {
                        name: "排除虚拟号码",
                        value: "0"
                    },
                    {
                        name: "不限",
                        value: "1"
                    },
                    {
                        name: "移动",
                        value: "2"
                    },
                    {
                        name: "联通",
                        value: "3"
                    },
                    {
                        name: "电信",
                        value: "4"
                    },
                    {
                        name: "虚拟号码",
                        value: "5"
                    }
                ],
                autoGetMessageTimer: null,
                phone: null,
                phoneDict: {},
                messageDict: {},
                phoneAlertList: []
            };
        },
        mounted() {
            if (this.$self.verificationCode) {
                this.name = this.$self.verificationCode.name;
                this.token = this.$self.verificationCode.token;
            }
            if (this.name && this.token) {
                [CODE_PLATFORM_KEKE, CODE_PLATFORM_JINDOU, CODE_PLATFORM_MIYI].forEach((value) => {
                    if (value.name === this.name ) {
                        this.itemObj = value.item;
                    }
                });
            } else {
                if (confirm("系统未检测到您的token，建议先选择接码平台并完成登录！")) {
                    this.$router.push({
                        path: "/verification-code"
                    });
                }
            }
        },
        methods: {
            releasePhone(phone) {
                this.phone = null;
                let tmpDict = JSON.parse(JSON.stringify(this.phoneDict));
                delete tmpDict[phone];
                this.phoneDict = tmpDict;
            },
            activeAutoGetMessage() {
                alert("接口暂未开放！");
                this.autoGetMessageTimer = ! this.autoGetMessageTimer;
            },
            activePhoneNumber(phone) {
                this.phone = phone;
                this.$refs.phoneMessage.setMessage(this.messageDict[phone]);
            }
        }
    }
</script>

<style scoped>
    #self-message-alert {
        left: 0;
        width: 100%;
        position: fixed;
        z-index: 999;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .self-top-row {
        margin-top: 20px;
        margin-bottom: -10px;
    }

    .self-button {
        margin-top: 20px;
    }

    .self-tip {
        cursor: help;
    }
</style>
