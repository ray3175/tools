<template>
    <div class="recite-setting">
        <div class="custom-control custom-radio recite-setting-word-type-line">
            <input v-model="reciteSetting.wordType" id="word-type-all" class="custom-control-input" type="radio" name="word-type" value="all">
            <label class="custom-control-label" for="word-type-all">全部</label>
        </div>
        <div class="custom-control custom-radio recite-setting-word-type-line">
            <input v-model="reciteSetting.wordType" id="word-type-new" class="custom-control-input" type="radio" name="word-type" value="new">
            <label class="custom-control-label" for="word-type-new">新词</label>
        </div>
        <div class="custom-control custom-radio recite-setting-word-type-line">
            <input v-model="reciteSetting.wordType" id="word-type-error" class="custom-control-input" type="radio" name="word-type" value="error">
            <label class="custom-control-label" for="word-type-error">错误词汇</label>
        </div>
        <div class="custom-control custom-radio recite-setting-word-type-line">
            <input v-model="reciteSetting.wordType" id="word-type-error-repeat" class="custom-control-input" type="radio" name="word-type" value="error-repeat">
            <label class="custom-control-label" for="word-type-error-repeat">重复错误词汇</label>
        </div>
        <div class="custom-control custom-radio recite-setting-word-type-line">
            <input v-model="reciteSetting.wordType" id="word-type-error-repeat-in-30-day" class="custom-control-input" type="radio" name="word-type" value="error-repeat-in-30-day">
            <label class="custom-control-label" for="word-type-error-repeat-in-30-day">30天错误词汇</label>
        </div>
        <div class="custom-control custom-radio recite-setting-word-type-line">
            <input v-model="reciteSetting.wordType" id="word-type-error-repeat-in-7-day" class="custom-control-input" type="radio" name="word-type" value="error-repeat-in-7-day">
            <label class="custom-control-label" for="word-type-error-repeat-in-7-day">7天错误词汇</label>
        </div>
        <div class="input-group setting-recite-word-number-line">
            <div class="input-group-prepend">
                <span class="input-group-text setting-recite-word-number">设置背诵词汇量</span>
            </div>
            <input v-model="reciteSetting.wordNumber" class="form-control" type="text">
        </div>
        <div class="input-group word-mode-random-line">
            <div class="custom-control custom-switch">
                <input v-model="reciteSetting.wordRandomMode" id="word-mode-random" class="custom-control-input" type="checkbox" value="random" disabled>
                <label class="custom-control-label" for="word-mode-random">随机模式</label>
            </div>
        </div>
        <div class="col-4-sm recite-setting-goto-word-recite-button-line">
            <button @click="gotoWordRecite" class="btn btn-lg btn-outline-success" type="button">开始背诵</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "recite-setting",
        data() {
            return {
                reciteSetting: {
                    wordType: "all",
                    wordNumber: "50",
                    wordRandomMode: true
                }
            };
        },
        methods: {
            gotoWordRecite() {
                this.$router.push({
                    name: "english word-recite",
                    params: {
                        id: this.$route.params.id,
                        name: this.$route.params.name,
                        wordType: this.reciteSetting.wordType,
                        wordNumber: this.reciteSetting.wordNumber,
                        wordRandomMode: this.reciteSetting.wordRandomMode
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .recite-setting {
        background: #f6e3c4;
        padding: 10px 10px 10px 10px;
        border-radius: 5px;
    }

    .recite-setting-word-type-line {
        margin-bottom: 5px;
    }

    .setting-recite-word-number {
        font-size: small;
    }

    .setting-recite-word-number-line {
        margin-top: 10px;
        margin-bottom: 15px;
        padding-right: 30px;
    }

    .word-mode-random-line {
        margin-bottom: 20px;
    }

    .recite-setting-goto-word-recite-button-line {
        margin-bottom: 5px;
    }
</style>
