<template>
    <div>
        <div v-show="!isInputNow" class="error-show">
            <div v-show="isError" class="error-show-warning">抱歉，您错了！</div>
            <div>
                <button @click="erroneousJudgementButtonClick" v-show="isError" class="btn btn-outline-success error-show-button" type="button">误判，实为正确</button>
                <button @click="continueButtonClick" id="self-verify-area-button-success" class="btn btn-outline-primary error-show-button" type="button">{{ isEnd ? '完成' : '继续' }}</button>
            </div>
        </div>
        <div v-show="isInputNow" class="input-group">
            <input v-model="wordInputText" @keydown.enter="submitButtonClick" id="self-verify-area-input-text" class="form-control" type="text" placeholder="请输入中文。。。">
            <div class="input-group-append">
                <button @click="submitButtonClick" class="btn btn-outline-primary" type="button">提交</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "verify-area",
        data() {
            return {
                isInputNow: true,
                isError: false,

                wordInputText: ""
            };
        },
        computed: {
            isEnd() {
                return this.$parent.wordIndex+1 >= this.$parent.all;
            }
        },
        methods: {
            initVerifyArea() {
                this.wordInputText = "";
                this.isInputNow = true;
            },
            submitButtonClick() {
                this.$parent.verifyWord(this.wordInputText);
            },
            resultStatus(status) {
                this.isInputNow = false;
                this.isError = !status;
                if (!this.isEnd) {
                    setTimeout(() => {
                        $("#self-verify-area-button-success").focus();
                    }, 100);
                }
            },
            erroneousJudgementButtonClick() {
                this.$parent.erroneousJudgement();
                this.continueButtonClick();
            },
            continueButtonClick() {
                this.$parent.nextWord();
                setTimeout(() => {
                    $("#self-verify-area-input-text").focus();
                }, 100);
            }
        }
    }
</script>

<style scoped>
    .error-show {
        display: flex;
        flex-direction: column;
        text-align: center;
    }

    .error-show-warning {
        font-weight: bolder;
        color: orangered;
        margin-bottom: 20px;
    }

    .error-show-button {
        font-weight: bolder;
    }

    #self-verify-area-button-success {
        width: 138px;
    }

    @media (max-width: 800px) {
        #self-verify-area-button-success {
            margin-top: 10px;
        }
    }
</style>
