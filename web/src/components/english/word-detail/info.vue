<template>
    <table class="table table-bordered table-warning table-hover table-sm">
        <tbody>
            <tr>
                <th>总数</th>
                <th><b @click="gotoWordRecite('all')" class="self-click-area">{{ value.all }}</b></th>
            </tr>
            <tr>
                <th>正确数</th>
                <th><b @click="gotoWordRecite('right')" class="self-click-area">{{ value.all - value.error }}</b></th>
            </tr>
            <tr>
                <th>错误数</th>
                <th><b @click="gotoWordRecite('error')" class="self-click-area">{{ value.error }}</b></th>
            </tr>
            <tr>
                <th>重复错误数</th>
                <th><b @click="gotoWordRecite('error-repeat')" class="self-click-area">{{ value.errorRepeat }}</b></th>
            </tr>
            <tr>
                <th>30天错误数</th>
                <th><b @click="gotoWordRecite('error-repeat-in-30-day')" class="self-click-area">{{ value.errorRepeatIn30Day }}</b></th>
            </tr>
            <tr>
                <th>7天错误数</th>
                <th><b @click="gotoWordRecite('error-repeat-in-7-day')" class="self-click-area">{{ value.errorRepeatIn7Day }}</b></th>
            </tr>
        </tbody>
    </table>
</template>

<script>
    export default {
        name: "info",
        props: {
            historyTime: {
                type: String,
                default: ""
            },
            value: {
                type: Object,
                default: {}
            }
        },
        methods: {
            gotoWordRecite(type="all") {
                this.$router.push({
                    name: "english word-recite",
                    query: {
                        id: this.$route.params.id,
                        wordType: type,
                        historyTime: this.historyTime
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .self-click-area {
        transition: all .3s;
        cursor: pointer;
    }

    .self-click-area:hover {
        color: lightyellow;
    }
</style>
