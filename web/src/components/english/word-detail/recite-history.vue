<template>
    <div :id="timeShow ? 'recite-history-' + timeShow : 'recite-history'" class="accordion">
        <div v-for="(obj, index) in value" class="card">
            <div :id="'heading-' + obj.timeShow" class="card-header">
                <h2 class="mb-0">
                    <button @click="getValue(obj)" class="btn btn-link collapsed self-recite-history-button" type="button" data-toggle="collapse" :data-target="'#collapse-' + obj.timeShow" aria-expanded="false" :aria-controls="'collapse-' + obj.timeShow">{{ obj.timeShow }}</button>
                </h2>
            </div>
            <div :id="'collapse-' + obj.timeShow" class="collapse" :aria-labelledby="'heading-' + obj.timeShow" :data-parent="timeShow ? '#recite-history-' + timeShow : '#recite-history'">
                <div class="card-body">
                    <recite-history v-if="stack < 2" :timeShow="obj.timeShow" :stack="stack + 1" :value="obj.value" :categoryId="categoryId"></recite-history>
                    <info v-else :value="obj.info" :historyTime="obj.timeShow"></info>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { getWordDetailReciteHistory } from "@/api/english";

    import info from "./info";

    export default {
        name: "recite-history",
        props: {
            timeShow: {
                type: String,
                default: null
            },
            stack: {
                type: Number,
                default: 0
            },
            value: {
                type: Array,
                default: () => []
            },
            categoryId: {
                type: Number
            }
        },
        components: { info },
        data() {
            return {
                hasGetTimeShowList: []
            };
        },
        methods: {
            initValue(data) {
                let tmp = [];
                for (let i in data) {
                    tmp.push({
                        timeShow: data[i],
                        value: [],
                        info: {}
                    });
                }
                return tmp;
            },
            getValue(obj) {
                if (!(this.hasGetTimeShowList.includes(obj.timeShow))) {
                    getWordDetailReciteHistory(this.categoryId, this.stack + 1, obj.timeShow, (rsp) => {
                        if (rsp.data.code === 200) {
                            if (this.stack < 2) {
                                obj.value = this.initValue(rsp.data.data);
                            } else {
                                let data = rsp.data.data;
                                data.errorRepeat = data.error_repeat;
                                data.errorRepeatIn30Day = data.error_repeat_in_30_day;
                                data.errorRepeatIn7Day = data.error_repeat_in_7_day;
                                obj.info = data;
                            }
                            this.hasGetTimeShowList.push(obj.timeShow);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            }
        }
    }
</script>

<style scoped>
    .self-recite-history-button {
        font-weight: bolder;
    }
</style>
