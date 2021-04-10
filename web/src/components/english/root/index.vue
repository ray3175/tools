<template>
    <div class="self-echart">
        <div class="self-echart-view">
            <word-recite-echart :timeType="timeType"></word-recite-echart>
        </div>
        <div class="self-echart-date-button">
            <div class="btn-group dropright">
                <button id="self-time-type-show" class="btn btn-lg btn-warning" type="button">{{ timeType === 'year' ? '年' : timeType === 'month'? '月' : '日' }}</button>
                <button class="btn btn-lg btn-warning dropdown-toggle dropdown-toggle-split" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <span class="sr-only"></span>
                </button>
                <div class="dropdown-menu">
                    <a @click="timeTypeUpdate('year')" class="dropdown-item" href="javascript:void(0);">年</a>
                    <a @click="timeTypeUpdate('month')" class="dropdown-item" href="javascript:void(0);">月</a>
                    <a @click="timeTypeUpdate('day')" class="dropdown-item" href="javascript:void(0);">日</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import wordReciteEchart from "./word-recite-echart";

    export default {
        name: "root",
        components: {
            "word-recite-echart": wordReciteEchart
        },
        data() {
            return {
                timeType: "day"
            };
        },
        methods: {
            timeTypeUpdate(type) {
                this.timeType = type;
            }
        }
    }
</script>

<style scoped>
    .self-echart {
        text-align: center;
    }

    .self-echart-view {
        position: relative;
        margin-top: 30px;
    }

    .self-echart-date-button {
        margin-top: 20px;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
    }

    #self-time-type-show {
        width: 100px;
    }
</style>
